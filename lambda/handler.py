from config.logging_config import logging_configuration
from src.load_redshift import load_to_redshift
from src.s3_event_reader import get_s3_object_from_event
from src.transform import transform_data

logger = logging_configuration()


def process_handler(event, context):
    if "Records" not in event:
        logger.error("Invalid event format")
        return

    raw_data = get_s3_object_from_event(event)
    transformed = transform_data(raw_data)
    load_to_redshift(transformed)


# Next Steps:
# No error handling → wrap steps in try/except
# No return value or status → useful for observability
# Weak event validation ("Records" check is minimal)
# No idempotency or retry awareness (important for S3/Lambda)
# No type hints (optional)
