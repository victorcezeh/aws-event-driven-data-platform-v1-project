import logging
import unittest

from src.transform import transform_data

logger = logging.getLogger(__name__)


class TestTransformDataTypes(unittest.TestCase):

    def setUp(self):
        self.valid_data = [
            {
                "id": 1,
                "name": "Homer Simpson",
                "normalized_name": "homer simpson",
                "gender": "m",
            },
            {
                "id": 2,
                "name": "Marge Simpson",
                "normalized_name": "marge simpson",
                "gender": "f",
            },
            {
                "id": 3,
                "name": "Bart Simpson",
                "normalized_name": "bart simpson",
                "gender": "m",
            },
        ]

        try:
            self.result = transform_data(self.valid_data)
        except Exception as e:
            logger.exception(f"Error running transform_data: {e}")
            raise

    def test_id_is_int64(self):
        self.assertEqual(self.result["id"].dtype, "int64")

    def test_name_is_string(self):
        self.assertEqual(self.result["name"].dtype, "string")

    def test_normalized_name_is_string(self):
        self.assertEqual(self.result["normalized_name"].dtype, "string")

    def test_gender_is_string(self):
        self.assertEqual(self.result["gender"].dtype, "string")

    def test_gender_is_inferred_is_boolean(self):
        self.assertEqual(self.result["gender_is_inferred"].dtype, "bool")

    def test_output_columns_match_schema(self):
        expected_columns = [
            "id",
            "name",
            "normalized_name",
            "gender",
            "gender_is_inferred",
        ]
        self.assertListEqual(list(self.result.columns), expected_columns)


if __name__ == "__main__":
    unittest.main()
