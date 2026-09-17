import io
import json
import logging
from datetime import datetime

import boto3
import psycopg2

from config.settings import get_config

logger = logging.getLogger(__name__)


def get_redshift_host():
    client = boto3.client("redshift-serverless")
    response = client.get_workgroup(workgroupName="data-platform-workgroup")
    return response["workgroup"]["endpoint"]["address"]


def get_redshift_credentials():
    secrets_client = boto3.client("secretsmanager")
    secret = secrets_client.get_secret_value(
        SecretId="data-platform-redshift-credentials"
    )
    return json.loads(secret["SecretString"])


def load_to_redshift(transformed_data):
    config = get_config()

    if transformed_data is None or transformed_data.empty:
        logger.warning("No data to load into Redshift!")
        return

    filename = f"processed-data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    processed_key = f"{config['s3_processed_prefix']}{filename}.csv"

    s3 = boto3.client("s3")
    buffer = io.StringIO()
    transformed_data.to_csv(buffer, index=False)
    s3.put_object(
        Bucket=config["bucket_name"], Key=processed_key, Body=buffer.getvalue()
    )
    logger.info(
        f"Processed file written to s3://{config['bucket_name']}/{processed_key}"
    )

    creds = get_redshift_credentials()
    host = get_redshift_host()

    conn = psycopg2.connect(
        host=host,
        dbname=creds["database"],
        user=creds["username"],
        password=creds["password"],
        port=creds["port"],
    )

    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE staging.characters;")
    cur.execute(f"""
        COPY staging.characters (id, name, normalized_name, gender, gender_is_inferred)
        FROM 's3://{config['bucket_name']}/{processed_key}'
        IAM_ROLE '{config['redshift_iam_role']}'
        CSV
        IGNOREHEADER 1;
    """)
    conn.commit()
    cur.close()
    conn.close()
    logger.info("Data successfully loaded into Redshift")
