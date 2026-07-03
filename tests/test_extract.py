import unittest
import requests
from src.extract import fetch_api_data
from config.settings import get_config
from unittest.mock import patch, MagicMock


class TestFetchApiData(unittest.TestCase):

    def setUp(self):
        self.config = get_config()

    @patch("src.extract.requests.get")
    def test_successful_api_call_returns_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.response_code = 200
        mock_response.json.return_value = [{"id": 1, "name": "Homer Simpson"}]
        mock_get.return_value = mock_response

        result = fetch_api_data(self.config["url"])

        self.assertEqual(result, [{"id": 1, "name": "Homer Simpson"}])
        mock_get.assert_called_once_with(self.config["url"])

    @patch("src.extract.requests.get")
    def test_http_error_returns_none(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Not Found"
        )
        mock_get.return_value = mock_response

        result = fetch_api_data(self.config["url"])

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
