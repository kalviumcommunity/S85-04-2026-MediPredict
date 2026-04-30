"""Train ML models for bed, oxygen, and ICU requirement prediction."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

try:
    from src.utils import ensure_directory, project_root
except ModuleNotFoundError:
    from utils import ensure_directory, project_root


FEATURE_COLUMNS = [
    "total_patients",
    "emergency_patients",
    "admitted_patients",
    "icu_patients",
    "oxygen_patients",
    "discharged_patients",
    "available_beds",
    "available_oxygen_cylinders",
    "available_icu_beds",
    "avg_patient_age",
    "high_risk_patients",
]

TARGET_COLUMN_MAP = {
    "beds": "next_day_bed_requirement",
    "oxygen": "next_day_oxygen_requirement",
    "icu": "next_day_icu_requirement",
}

MODEL_OUTPUT_FILES = {
    "beds": "bed_model.pkl",
    "oxygen": "oxygen_model.pkl",
    "icu": "icu_model.pkl",
}


def add_target_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Create next-day requirement targets using shifted values."""
    model_df = df.copy().sort_values("date").reset_index(drop=True)
    model_df[TARGET_COLUMN_MAP["beds"]] = model_df["admitted_patients"].shift(-1)
    model_df[TARGET_COLUMN_MAP["oxygen"]] = model_df["oxygen_patients"].shift(-1)
    model_df[TARGET_COLUMN_MAP["icu"]] = model_df["icu_patients"].shift(-1)
    model_df = model_df.dropna().reset_index(drop=True)
    return model_df


def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Return MAE, RMSE, and R2 values."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return {
        "mae": round(float(mae), 3),
        "rmse": round(float(rmse), 3),
        "r2": round(float(r2), 3),
    }


def train_for_target(df: pd.DataFrame, target_col: str) -> tuple:
    """Train and compare LinearRegression and RandomForestRegressor."""
    X = df[FEATURE_COLUMNS]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    linear_preds = linear_model.predict(X_test)
    linear_metrics = evaluate_model(y_test, linear_preds)

    rf_model = RandomForestRegressor(n_estimators=200, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)
    rf_metrics = evaluate_model(y_test, rf_preds)

    if rf_metrics["rmse"] < linear_metrics["rmse"]:
        selected_name = "RandomForestRegressor"
        selected_model = rf_model
    else:
        selected_name = "LinearRegression"
        selected_model = linear_model

    metrics = {
        "LinearRegression": linear_metrics,
        "RandomForestRegressor": rf_metrics,
        "selected_model": selected_name,
    }

    return selected_model, metrics


def main() -> None:
    root = project_root()
    data_path = root / "data" / "processed" / "cleaned_hospital_data.csv"
    models_dir = root / "models"
    reports_dir = root / "outputs" / "reports"

    ensure_directory(models_dir)
    ensure_directory(reports_dir)

    if not data_path.exists():
        raise FileNotFoundError(
            "Cleaned data not found. Please run src/data_preprocessing.py first."
        )

    df = pd.read_csv(data_path)
    df["date"] = pd.to_datetime(df["date"])
    model_df = add_target_columns(df)

    all_results = {}

    for target_key, target_col in TARGET_COLUMN_MAP.items():
        model, metrics = train_for_target(model_df, target_col)
        model_file = models_dir / MODEL_OUTPUT_FILES[target_key]
        joblib.dump(model, model_file)
        all_results[target_key] = metrics

    metrics_path = reports_dir / "model_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    print("Model training complete.")
    for target_key, metrics in all_results.items():
        print(f"\nTarget: {target_key}")
        print(json.dumps(metrics, indent=2))
    print(f"\nSaved metrics report at: {metrics_path}")


if __name__ == "__main__":
    main()
