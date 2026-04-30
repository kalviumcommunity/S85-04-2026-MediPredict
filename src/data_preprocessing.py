"""Generate realistic sample hospital data and create a cleaned dataset."""

from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from src.utils import ensure_directory, project_root
except ModuleNotFoundError:
    from utils import ensure_directory, project_root


SEASONS = ["Normal", "Flu", "Heatwave", "Monsoon", "Viral Outbreak"]


def generate_sample_data(days: int = 120, random_seed: int = 42) -> pd.DataFrame:
    """Create a realistic sample hospital dataset."""
    rng = np.random.default_rng(random_seed)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days, freq="D")

    rows = []
    for i, date in enumerate(dates):
        # Seasonal shift every ~24 days to simulate changing conditions.
        season = SEASONS[(i // 24) % len(SEASONS)]

        seasonal_boost = {
            "Normal": 0,
            "Flu": 18,
            "Heatwave": 10,
            "Monsoon": 14,
            "Viral Outbreak": 30,
        }[season]

        total_patients = int(np.clip(rng.normal(120 + seasonal_boost, 15), 75, 230))
        emergency_patients = int(np.clip(total_patients * rng.uniform(0.15, 0.32), 10, total_patients))
        admitted_patients = int(np.clip(total_patients * rng.uniform(0.35, 0.6), 25, total_patients))
        icu_patients = int(np.clip(admitted_patients * rng.uniform(0.1, 0.22), 4, admitted_patients))
        oxygen_patients = int(np.clip(admitted_patients * rng.uniform(0.28, 0.5), 8, admitted_patients))
        discharged_patients = int(np.clip(total_patients * rng.uniform(0.22, 0.48), 15, total_patients))
        avg_patient_age = float(np.clip(rng.normal(48, 9), 18, 86))
        high_risk_patients = int(np.clip(total_patients * rng.uniform(0.1, 0.26), 5, total_patients))

        # Availability values change with operational capacity.
        available_beds = int(np.clip(rng.normal(95, 12), 60, 140))
        available_oxygen_cylinders = int(np.clip(rng.normal(85, 14), 45, 130))
        available_icu_beds = int(np.clip(rng.normal(24, 5), 10, 38))

        rows.append(
            {
                "date": date,
                "total_patients": total_patients,
                "emergency_patients": emergency_patients,
                "admitted_patients": admitted_patients,
                "icu_patients": icu_patients,
                "oxygen_patients": oxygen_patients,
                "discharged_patients": discharged_patients,
                "available_beds": available_beds,
                "available_oxygen_cylinders": available_oxygen_cylinders,
                "available_icu_beds": available_icu_beds,
                "avg_patient_age": round(avg_patient_age, 1),
                "high_risk_patients": high_risk_patients,
                "season_or_condition": season,
            }
        )

    df = pd.DataFrame(rows)

    # Introduce a few missing values intentionally for cleaning demonstration.
    df.loc[5, "avg_patient_age"] = np.nan
    df.loc[16, "available_oxygen_cylinders"] = np.nan

    # Add one duplicate row intentionally for duplicate handling demonstration.
    df = pd.concat([df, df.iloc[[30]]], ignore_index=True)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the dataset by handling missing values and duplicates."""
    cleaned_df = df.copy()
    cleaned_df["date"] = pd.to_datetime(cleaned_df["date"])

    # Fill missing numeric values with median values.
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if cleaned_df[col].isna().sum() > 0:
            cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())

    # Remove duplicates.
    cleaned_df = cleaned_df.drop_duplicates().reset_index(drop=True)

    # Ensure integer-like fields remain integers.
    integer_cols = [
        "total_patients",
        "emergency_patients",
        "admitted_patients",
        "icu_patients",
        "oxygen_patients",
        "discharged_patients",
        "available_beds",
        "available_oxygen_cylinders",
        "available_icu_beds",
        "high_risk_patients",
    ]
    cleaned_df[integer_cols] = cleaned_df[integer_cols].round().astype(int)

    return cleaned_df


def main() -> None:
    root = project_root()
    raw_dir = root / "data" / "raw"
    processed_dir = root / "data" / "processed"
    ensure_directory(raw_dir)
    ensure_directory(processed_dir)

    raw_path = raw_dir / "hospital_data.csv"
    processed_path = processed_dir / "cleaned_hospital_data.csv"

    raw_df = generate_sample_data(days=120)
    raw_df.to_csv(raw_path, index=False)

    cleaned_df = clean_data(raw_df)
    cleaned_df.to_csv(processed_path, index=False)

    print(f"Raw dataset created: {raw_path}")
    print(f"Cleaned dataset created: {processed_path}")
    print(f"Rows (raw): {len(raw_df)}")
    print(f"Rows (cleaned): {len(cleaned_df)}")


if __name__ == "__main__":
    main()
