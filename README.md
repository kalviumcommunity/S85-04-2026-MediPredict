# MediPredict

## Problem Statement
Small hospitals generate large amounts of patient data but rarely analyze it to predict resource needs like beds, oxygen, or critical care. This project shows how data-driven forecasting can improve healthcare preparedness.

## Team Size
3 members

## Objective
Build a beginner-friendly Data Science + Streamlit project to forecast hospital resource needs.

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Jupyter Notebook
- CSV files

## Folder Structure
```text
MediPredict/
│
├── data/
│   ├── raw/
│   │   └── hospital_data.csv
│   └── processed/
│       └── cleaned_hospital_data.csv
│
├── notebooks/
│   └── MediPredict_EDA_Modeling.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── prediction.py
│   └── utils.py
│
├── models/
│   ├── bed_model.pkl
│   ├── oxygen_model.pkl
│   └── icu_model.pkl
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── app.py
├── requirements.txt
├── README.md
└── run_guide.md
```

## Dataset Description
The dataset is realistic sample hospital data with 120 days of records. It includes:
- `date`
- `total_patients`
- `emergency_patients`
- `admitted_patients`
- `icu_patients`
- `oxygen_patients`
- `discharged_patients`
- `available_beds`
- `available_oxygen_cylinders`
- `available_icu_beds`
- `avg_patient_age`
- `high_risk_patients`
- `season_or_condition`

## Features
1. Data loading and cleaning
2. Missing value and duplicate checks
3. Summary statistics
4. EDA charts (trend, distribution, scatter, boxplot)
5. ML training for next-day:
   - bed requirement
   - oxygen requirement
   - ICU requirement
6. Model comparison:
   - Linear Regression
   - Random Forest Regressor
7. Metrics:
   - MAE
   - RMSE
   - R2 Score
8. Streamlit prediction app with preparedness status and recommendations

## ML Models Used
- Linear Regression
- Random Forest Regressor

## How To Run Project
1. `python -m venv venv`
2. Activate environment
3. `pip install -r requirements.txt`
4. `python src/data_preprocessing.py`
5. `python src/model_training.py`
6. `streamlit run app.py`

## Screenshots
- Add app home screen screenshot here
- Add predictions screenshot here
- Add charts screenshot here

## Insights
- Seasonal conditions can increase patient load.
- Emergency and admitted patient trends strongly influence oxygen and ICU demand.
- Simple ML models can provide useful first-level planning support.

## Assumptions
- Sample data follows realistic but synthetic patterns.
- Next-day demand can be estimated from current hospital metrics.
- Resource planning decisions are taken daily.

## Limitations
- Synthetic data is not a replacement for real hospital data.
- Model performance may vary with real-world anomalies.
- No advanced time-series modeling is used in this beginner project.

## Future Scope
- Add real hospital data integration
- Use advanced forecasting models
- Add alert notifications
- Add downloadable PDF reports

## Team Member Work Division
### Member 1
- Data collection/sample dataset creation
- Data cleaning
- Pandas/NumPy preprocessing

### Member 2
- EDA visualizations
- Model training
- Model evaluation

### Member 3
- Streamlit app
- README
- Final integration and testing
