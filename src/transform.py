import logging
import pandas as pd

logger = logging.getLogger(__name__)


def transform_data(api_data):
    if not api_data:
        logger.warning("No data to transform!")
        return None

    df = pd.DataFrame(api_data)

    # Schema validation
    required_columns = ["id", "name", "normalized_name", "gender"]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        logger.error(f"Missing required columns: {missing}")
        return None

    # Normalize text fields early
    df["name"] = df["name"].str.strip()
    df["normalized_name"] = df["normalized_name"].str.strip().str.lower()

    # Normalize + map gender
    df["gender"] = (
        df["gender"].str.lower().str.strip().map({"m": "male", "f": "female"})
    )

    # Fix known bad row
    mask = df["id"] == 22
    df.loc[mask, ["name", "normalized_name", "gender"]] = [
        "Martin Prince, Sr.",
        "martin prince sr",
        None,
    ]

    # Audit + fill
    df["gender_is_inferred"] = df["gender"].isna()
    df["gender"] = df["gender"].fillna("unknown")

    # Type enforcement
    df["id"] = df["id"].astype(int)

    # Drop duplicates using the primary key
    df = df.drop_duplicates(subset=["id"])

    logger.info(f"Data transformed successfully | rows={len(df)}")

    return df[["id", "name", "normalized_name", "gender", "gender_is_inferred"]]
