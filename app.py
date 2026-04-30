"""Streamlit application for MediPredict."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from src.model_training import FEATURE_COLUMNS
from src.prediction import create_input_dataframe, load_models, predict_requirements


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "cleaned_hospital_data.csv"
MODELS_DIR = PROJECT_ROOT / "models"


st.set_page_config(page_title="MediPredict", layout="wide")
st.title("MediPredict")
st.subheader("Hospital Resource Forecasting System")


def get_preparedness_status(pred_beds: int, pred_oxygen: int, pred_icu: int, available_beds: int, available_oxygen: int, available_icu: int) -> str:
    """Determine preparedness level based on predicted demand vs available resources."""
    high_risk = (
        pred_beds > available_beds
        or pred_oxygen > available_oxygen
        or pred_icu > available_icu
    )

    close_to_limit = (
        (available_beds > 0 and pred_beds >= 0.8 * available_beds)
        or (available_oxygen > 0 and pred_oxygen >= 0.8 * available_oxygen)
        or (available_icu > 0 and pred_icu >= 0.8 * available_icu)
    )

    if high_risk:
        return "High Risk"
    if close_to_limit:
        return "Moderate Risk"
    return "Safe"


def get_recommendations(status: str, pred_beds: int, pred_oxygen: int, pred_icu: int, available_beds: int, available_oxygen: int, available_icu: int) -> list[str]:
    """Generate actionable recommendations."""
    recommendations = []

    if pred_beds > available_beds:
        recommendations.append("Arrange extra beds")
    if pred_oxygen > available_oxygen:
        recommendations.append("Refill oxygen cylinders")
    if pred_icu > available_icu:
        recommendations.append("Prepare ICU staff")

    if status == "Moderate Risk" and not recommendations:
        recommendations.extend([
            "Arrange extra beds",
            "Refill oxygen cylinders",
            "Prepare ICU staff",
        ])

    if status == "Safe" and not recommendations:
        recommendations.append("Current resources are sufficient")

    return recommendations


# Sidebar inputs
st.sidebar.header("Enter Hospital Metrics")
user_inputs = {
    "total_patients": st.sidebar.number_input("Total Patients", min_value=0, value=130, step=1),
    "emergency_patients": st.sidebar.number_input("Emergency Patients", min_value=0, value=30, step=1),
    "admitted_patients": st.sidebar.number_input("Admitted Patients", min_value=0, value=65, step=1),
    "icu_patients": st.sidebar.number_input("ICU Patients", min_value=0, value=12, step=1),
    "oxygen_patients": st.sidebar.number_input("Oxygen Patients", min_value=0, value=28, step=1),
    "discharged_patients": st.sidebar.number_input("Discharged Patients", min_value=0, value=40, step=1),
    "available_beds": st.sidebar.number_input("Available Beds", min_value=0, value=90, step=1),
    "available_oxygen_cylinders": st.sidebar.number_input("Available Oxygen Cylinders", min_value=0, value=80, step=1),
    "available_icu_beds": st.sidebar.number_input("Available ICU Beds", min_value=0, value=22, step=1),
    "avg_patient_age": st.sidebar.number_input("Average Patient Age", min_value=0.0, value=50.0, step=0.1),
    "high_risk_patients": st.sidebar.number_input("High Risk Patients", min_value=0, value=20, step=1),
}

# Ensure input ordering matches model training features
ordered_inputs = {key: user_inputs[key] for key in FEATURE_COLUMNS}

with st.container(border=True):
    st.markdown("### Prediction Results")

    try:
        models = load_models(MODELS_DIR)
        input_df = create_input_dataframe(ordered_inputs)
        predictions = predict_requirements(models, input_df)

        status = get_preparedness_status(
            predictions["predicted_beds"],
            predictions["predicted_oxygen"],
            predictions["predicted_icu"],
            user_inputs["available_beds"],
            user_inputs["available_oxygen_cylinders"],
            user_inputs["available_icu_beds"],
        )

        recommendations = get_recommendations(
            status,
            predictions["predicted_beds"],
            predictions["predicted_oxygen"],
            predictions["predicted_icu"],
            user_inputs["available_beds"],
            user_inputs["available_oxygen_cylinders"],
            user_inputs["available_icu_beds"],
        )

        c1, c2, c3 = st.columns(3)
        with c1:
            st.info(f"Bed Prediction: **{predictions['predicted_beds']}**")
        with c2:
            st.info(f"Oxygen Prediction: **{predictions['predicted_oxygen']}**")
        with c3:
            st.info(f"ICU Prediction: **{predictions['predicted_icu']}**")

        st.success(f"Preparedness Status: **{status}**")

        st.markdown("### Recommendations")
        for rec in recommendations:
            st.write(f"- {rec}")

    except FileNotFoundError as e:
        st.error(str(e))


st.markdown("---")
st.markdown("## Dataset Preview")

if DATA_PATH.exists():
    df = pd.read_csv(DATA_PATH)
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("## Charts")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        ax1.plot(pd.to_datetime(df["date"]), df["total_patients"], color="tab:blue")
        ax1.set_title("Total Patients Trend")
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Total Patients")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    with chart_col2:
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(pd.to_datetime(df["date"]), df["oxygen_patients"], color="tab:green")
        ax2.set_title("Oxygen Demand Trend")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Oxygen Patients")
        plt.xticks(rotation=45)
        st.pyplot(fig2)
else:
    st.warning("Dataset not found. Please run python src/data_preprocessing.py first.")
