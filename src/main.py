import json
from config import url, json_file_path, csv_file_path
from config.logging_config import logging_configuration
from api_fetcher import fetch_api_data
from transformer import transform_data
from s3_writer import write_to_s3

def main():

    logger = logging_configuration()
    logger.info("Project begins!")

    # Extract
    data = fetch_api_data(url)

    # Transform
    df = transform_data(data)

    # Load raw data to S3, not transformed data
    write_to_s3(data)

    # Local inspection using pandas
    if df is not None:
        with open(json_file_path, "w") as f:
            json.dump(data, f, indent=2)

        df.to_csv(csv_file_path, index=False)

        logger.info("Local files saved")

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()