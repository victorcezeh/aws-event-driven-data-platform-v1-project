import logging
from config import log_file

def logging_configuration():

    if not log_file:
        print("ERROR: LOG_FILE_PATH is not set or is none!")
        return logging.getLogger()

    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s",
            handlers=[
                logging.FileHandler(filename=log_file, mode="a"),
                logging.StreamHandler(),
            ],
        )

        logger = logging.getLogger()
        logging.getLogger("urllib3").setLevel(logging.WARNING)

        logger.info("Logging setup complete!")
        return logger

    except PermissionError:
        logging.warning(f"Permission denied: Cannot write to {log_file}.")
        return logging.getLogger()

    except FileNotFoundError:
        logging.warning(f"File path not found: {log_file}")
        return logging.getLogger()

    except Exception as e:
        logging.warning(f"ERROR: Logging setup failed: {e}")
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
        logging.warning("Falling back to basic configuration.")
        return logging.getLogger()