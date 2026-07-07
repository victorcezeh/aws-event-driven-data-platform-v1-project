import os
import json
from config.settings import get_config
from config.logging_config import logging_configuration
from src.extract import fetch_api_data
from src.transform import transform_data
from src.load_s3 import load_to_s3


def main():

    config = get_config()
    logger = logging_configuration()
    logger.info("Project begins!")

    # Extract
    data = fetch_api_data(config["url"])

    # Transform
    df = transform_data(data)

    # Load the raw api data into S3, not transformed data
    load_to_s3(data, config)

    # A local inspection of processed data using pandas
    if df is not None:
        os.makedirs(os.path.dirname(config["raw_json_file_path"]), exist_ok=True)
        os.makedirs(os.path.dirname(config["processed_csv_file_path"]), exist_ok=True)
        
        with open(config["raw_json_file_path"], "w") as f:
            json.dump(data, f, indent=2)

        df.to_csv(config["processed_csv_file_path"], index=False)

        logger.info("Local files saved")

    logger.info("Pipeline completed successfully!")


if __name__ == "__main__":
    main()
