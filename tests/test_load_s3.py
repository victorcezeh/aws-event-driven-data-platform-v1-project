import unittest
from unittest.mock import MagicMock, patch

from src.load_s3 import load_to_s3


class TestLoadToS3(unittest.TestCase):

    @patch("src.load_s3.boto3.client")
    def test_load_to_s3_put_object_call(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3

        api_data = [{"id": 1, "name": "Homer"}]
        config = {
            "bucket_name": "data-platform-event-driven-project",
            "s3_raw_prefix": "raw/",
        }

        load_to_s3(api_data, config)

        mock_s3.put_object.assert_called_once()


if __name__ == "__main__":
    unittest.main()
