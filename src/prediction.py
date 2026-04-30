"""Prediction helper functions for Streamlit app."""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd

try:
    from src.model_training import FEATURE_COLUMNS
except ModuleNotFoundError:
    from model_training import FEATURE_COLUMNS


MODEL_FILES = {
    "beds": "bed_model.pkl",
    "oxygen": "oxygen_model.pkl",
    "icu": "icu_model.pkl",
}


def load_models(models_dir: Path) -> dict:
    """Load all required models from disk."""
    models = {}
    for key, filename in MODEL_FILES.items():
        model_path = models_dir / filename
        if not model_path.exists():
            raise FileNotFoundError(
                f"Missing model file: {filename}. Run python src/model_training.py first."
            )
        models[key] = joblib.load(model_path)
    return models


def create_input_dataframe(user_inputs: dict) -> pd.DataFrame:
    """Convert user input dictionary to model-ready DataFrame."""
    return pd.DataFrame([user_inputs], columns=FEATURE_COLUMNS)


def predict_requirements(models: dict, input_df: pd.DataFrame) -> dict:
    """Generate predictions for bed, oxygen, and ICU requirements."""
    bed_pred = float(models["beds"].predict(input_df)[0])
    oxygen_pred = float(models["oxygen"].predict(input_df)[0])
    icu_pred = float(models["icu"].predict(input_df)[0])

    return {
        "predicted_beds": max(0, round(bed_pred)),
        "predicted_oxygen": max(0, round(oxygen_pred)),
        "predicted_icu": max(0, round(icu_pred)),
    }
