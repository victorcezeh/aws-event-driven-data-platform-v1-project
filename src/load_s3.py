import json
import logging
import boto3
from datetime import datetime
from config.settings import get_config

config = get_config()
logger = logging.getLogger(__name__)


def load_to_s3(api_data, config):
    try:
        logger.info("Beginning API data loading to S3...")

        filename = f"api-s3-data_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        key = f"{config['s3_raw_prefix']}{filename}.json"

        s3 = boto3.client("s3")

        s3.put_object(
            Bucket=config["bucket_name"],
            Key=key,
            Body=json.dumps(api_data).encode("UTF-8"),
        )

        logger.info(f"API data loaded successfully into S3: {key}")

    except Exception as e:
        logger.error(f"API data failed to load into S3: {e}")