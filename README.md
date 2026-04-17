# MediPredict

A data-driven healthcare forecasting system for small hospitals to predict resource needs like beds, oxygen, and ICU capacity.

## Project Structure

- `data/`: Sample dataset (CSV)
- `backend/`: Node.js + Express API with MongoDB
- `frontend/`: React dashboard

## Setup

### Backend
1. Install MongoDB locally or use cloud (e.g., MongoDB Atlas).
2. Update `backend/.env` with your MONGO_URI.
3. Run `cd backend && npm install && npm start`

### Frontend
1. Run `cd frontend && npm install && npm start`

## APIs
- POST /api/data: Store data
- GET /api/data: Fetch data
- GET /api/predict: Get 7-day predictions

## Deployment

### Backend (Render)
1. Push backend to GitHub.
2. Sign up for Render, create a new Web Service.
3. Connect GitHub repo, set build command: `npm install`, start: `node server.js`.
4. Add environment variables (MONGO_URI).
5. Deploy.

### Frontend (Vercel)
1. Push frontend to GitHub.
2. Sign up for Vercel, import project.
3. Set build settings: build command `npm run build`, output dir `build`.
4. Deploy. Update API calls to production URL.

## Features
- Data upload form
- Charts for trends and predictions
- Alerts for high demand
3.  Exploratory analysis — characterize cohorts, inspect distributions and missingness, and surface candidate predictors and failure modes.
4.  Modeling & evaluation — build predictive models, select thresholds aligned with capacity, and evaluate calibration and subgroup performance.
5.  Operationalization & monitoring — package scores, create tooling for prioritization, and monitor model performance and outcomes post-deployment.

- **How the repository structure reflects stages of the lifecycle:** The repository separates exploratory artifacts (iterative notebooks, ad‑hoc plots) from reproducible steps (data processing scripts, model training code) and from delivery artifacts (saved model artifacts, reports). That separation supports an iterative flow: exploration informs pipeline design, which is then hardened into scripts and evaluated against the initial question.

## 2) Repository Structure & File Roles

- **Major folders and the type of work they contain:**
  - `data/` — stores raw and (when present) processed datasets; this is where evidence enters the project and must be handled with care (access controls, provenance notes).
  - `notebooks/` — exploratory analyses, visualization, and hypothesis testing. Notebooks are the workspace for discovery and quick iteration.
  - `scripts/` or `src/` — reproducible data-processing and modeling pipelines; scripts should be idempotent, parameterized, and suitable for automation.
  - `models/` — serialized model artifacts, training metadata, and version notes for reproducibility.
  - `outputs/` or `reports/` — human-facing artifacts: charts, CSV exports, and evaluation reports used to communicate findings and decisions.
  - `docs/` — design notes, evaluation criteria, and operational guidance (if present).

- **How exploratory work differs from finalized analysis:** Exploratory work (in `notebooks/`) is iterative, partially documented, and optimized for learning: rapid plots, temporary joins, and ad‑hoc slicing. Finalized analysis appears in `scripts/` or `src/` as repeatable, parameterized code with clear inputs/outputs, and accompanied by tests or checks. Finalized work should reproduce notebook findings with deterministic steps and explicit data contracts.

- **Where a new contributor should be cautious:**
  - Modifying raw data files or overwriting files in `data/` without versioning or provenance notes can corrupt experiments.
  - Changing production pipeline scripts or model weights without tests and a rollback plan — these are operational risks.
  - Committing sensitive PHI/PII into the repository; any patient‑level data must remain external and access‑controlled.

## 3) Assumptions, Gaps, and Open Questions

- **Assumptions apparent in the repo:**
  - The data contain reliable patient identifiers to link admissions and outcomes across sources.
  - Timestamp quality is sufficient to define index discharges and outcomes without leakage (events labeled correctly relative to prediction time).
  - The historical cohort is representative of future operational conditions (no major policy or population shifts).

- **Missing documentation or unclear steps:**
  - A clear data dictionary and small sample dataset are not present; contributors must infer column semantics from code and notebooks.
  - Reproducible run instructions (how to execute the full pipeline end-to-end) and environment setup (dependencies, Python version) are incomplete or missing.
  - Evaluation acceptance criteria (what minimum calibration, recall, or fairness thresholds are required before deployment) are not specified.

- **One practical improvement to make the repository easier to understand or extend:**
  Add a single `DESIGN.md` that contains: a) an explicit decision statement and operational objective, b) a concise data dictionary (example rows and field meanings), c) a minimal runbook to reproduce the pipeline (`scripts/run_pipeline.sh` or `make` target), and d) evaluation acceptance thresholds. This file bridges exploratory notebooks and production scripts, reduces onboarding friction, and clarifies assumptions for reviewers.

---

## Python & Anaconda Setup Documentation

### System Information
- **Operating System**: Windows 11
- **Python Version**: 3.12.4 (pre-installed)
- **Anaconda Version**: Miniconda3 with conda 26.1.1
- **Setup Date**: April 17, 2026

### Installation Steps

#### 1. Python Verification
Python was already installed on the system. Verified installation:
```bash
python --version
# Output: Python 3.12.4
```

#### 2. Anaconda Installation
Since full Anaconda download links were not accessible, Miniconda was installed instead:

1. Downloaded Miniconda installer:
```bash
curl -o miniconda-installer.exe https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
```

2. Ran the installer:
```bash
Start-Process -FilePath "C:\Users\Dell\Downloads\miniconda-installer.exe" -Wait
```

3. Verified installation location: `C:\Users\Dell\Miniconda3`

#### 3. Conda Configuration
1. Accepted Terms of Service for all channels:
```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```

2. Initialized conda for PowerShell:
```bash
conda init powershell
```

3. Added conda to PATH for current session:
```bash
$env:PATH += ";C:\Users\Dell\Miniconda3\Scripts;C:\Users\Dell\Miniconda3\condabin"
```

4. Verified conda installation:
```bash
conda --version
# Output: conda 26.1.1
```

#### 4. Data Science Environment Setup
Created dedicated conda environment for Data Science work:

1. Created environment:
```bash
conda create -n datascience python=3.12 -y
```

2. Activated environment:
```bash
& "C:\Users\Dell\Miniconda3\Scripts\activate.bat" datascience
```

3. Installed essential data science packages:
```bash
pip install numpy pandas matplotlib seaborn jupyter
```

#### 5. Environment Validation
Tested the installation by importing key packages:
```python
python -c "import numpy as np; import pandas as pd; import matplotlib.pyplot as plt; print('All data science packages imported successfully!')"
# Output: All data science packages imported successfully!
```

### Environment Details
- **Environment Name**: datascience
- **Python Version**: 3.12.13
- **Key Packages Installed**:
  - numpy 2.4.4
  - pandas 3.0.2
  - matplotlib 3.10.8
  - seaborn 0.13.2
  - jupyter 1.1.1

### Usage Instructions
To use the Data Science environment:

1. Open PowerShell
2. Activate the environment:
```bash
conda activate datascience
```
3. Start Jupyter Notebook:
```bash
jupyter notebook
```

### Verification Commands
For future verification, use these commands:
```bash
# Check Python version
python --version

# Check conda version
conda --version

# List environments
conda env list

# Check installed packages
pip list
```

This setup provides a complete Data Science development environment ready for the MediPredict project and future data analysis tasks.

---

If you'd like, I will: 1) add the suggested `DESIGN.md` draft, 2) create a small sample `data/sample_schema.csv` sketch, or 3) open a PR with this README update. Which should I do next?
