import os
from dotenv import load_dotenv


def get_config():
    load_dotenv()
    return {
        "aws_access_key": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "bucket_name": os.getenv("AWS_BUCKET_NAME"),
        "bucket_region": os.getenv("AWS_REGION"),
        "s3_raw_prefix": os.getenv("AWS_RAW_PREFIX"),
        "s3_processed_prefix": os.getenv("AWS_PROCESSED_PREFIX"),
        "url": f"{os.getenv('BASE_URL')}{os.getenv('END_POINT')}",
        "log_file": os.getenv("LOG_FILE_PATH"),
        "processed_csv_file_path": os.getenv("PROCESSED_CSV_FILE_PATH"),
        "raw_json_file_path": os.getenv("RAW_JSON_FILE_PATH"),
    }