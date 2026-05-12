import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Fetch credentials and other config
aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_access_key_id = os.getenv("AWS_SECRET_ACCESS_KEY_ID")
bucket_name = os.getenv("AWS_BUCKET_NAME")
bucket_region = os.getenv("AWS_REGION")
base_url = os.getenv("BASE_URL")
end_point = os.getenv("END_POINT")
url = f"{os.getenv('BASE_URL')}{os.getenv('END_POINT')}"
key = os.getenv("KEY")

# Log file path
log_file = os.getenv("LOG_FILE_PATH")
csv_file_path = os.getenv("CSV_FILE_PATH")
json_file_path = os.getenv("JSON_FILE_PATH")