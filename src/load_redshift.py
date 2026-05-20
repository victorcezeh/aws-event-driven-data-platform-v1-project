import io
import json
import logging
import os
import boto3
import psycopg2
from config.settings import get_config

logger = logging.getLogger(__name__)


def load_to_redshift(transformed_data):

    config = get_config()

    if transformed_data is None or transformed_data.empty:
        logger.warning("No data to write to Redshift")
        return

    processed_key = "processed/characters.csv"

    # Write cleaned DataFrame to S3 processed prefix
    s3 = boto3.client("s3")
    buffer = io.StringIO()
    transformed_data.to_csv(buffer, index=False)
    s3.put_object(
        Bucket=config["bucket_name"], Key=processed_key, Body=buffer.getvalue()
    )
    logger.info(f"Cleaned file written to s3://{config['bucket_name']}/{processed_key}")

    # Fetch Redshift credentials from Secrets Manager
    secrets_client = boto3.client("secretsmanager")
    secret = secrets_client.get_secret_value(SecretId=os.environ["REDSHIFT_SECRET_NAME"])
    creds = json.loads(secret["SecretString"])

    # COPY from S3 into Redshift
    conn = psycopg2.connect(
        host=creds["RS_HOST"],
        dbname=creds["RS_DB"],
        user=creds["RS_USER"],
        password=creds["RS_PASSWORD"],
        port=5439,
    )
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE staging.characters;")
    cur.execute(f"""
        COPY staging.characters (id, name, normalized_name, gender, gender_is_inferred)
        FROM 's3://{config["bucket_name"]}/{processed_key}'
        IAM_ROLE '{os.environ["REDSHIFT_IAM_ROLE"]}'
        CSV
        IGNOREHEADER 1;
    """)
    conn.commit()
    cur.close()
    conn.close()
    logger.info("Data successfully loaded into Redshift")

# REDSHIFT_SECRET_NAME = pointer to the secret
# REDSHIFT_IAM_ROLE = the ARN