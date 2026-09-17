import logging

import requests

logger = logging.getLogger(__name__)


def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        logger.info(f"Request Successful!: {response.status_code}")

        return response.json()

    except requests.exceptions.HTTPError as e:
        logger.warning(f"HTTP ERROR: {e}")

    except requests.exceptions.RequestException as e:
        logger.warning(f"Request Failed! {e}")

    return None
