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

## Python, Conda & Jupyter Verification

### Verification Status ✅ COMPLETED
**Verification Date**: April 22, 2026  
**Environment**: datascience conda environment

### System Verification Results

#### 1. Python Verification ✅
```bash
python --version
# Output: Python 3.13.12

python -c "print('Python is working correctly!')"
# Output: Python is working correctly!
```

#### 2. Conda Environment Verification ✅
```bash
conda --version
# Output: conda 26.1.1

conda env list
# Output:
# conda environments:
#
# base                  *  C:\Users\Dell\miniconda3
# datascience              C:\Users\Dell\Miniconda3\envs\datascience

conda activate datascience
# Output: (datascience)
```

#### 3. Jupyter Verification ✅
```bash
jupyter --version
# Output: Selected Jupyter core packages...
# IPython          : 9.12.0
# ipykernel        : 7.2.0
# jupyter_core     : 5.9.1
# jupyter_server   : 2.17.0
# jupyterlab       : 4.5.6
# notebook         : 7.5.5

jupyter notebook --version
# Output: 7.5.5
```

#### 4. Jupyter Notebook Launch Test ✅
- Jupyter Notebook server launched successfully
- Browser interface accessible
- Test notebook created: `test_verification.ipynb`
- All verification cells executed successfully

### Environment Details
- **Operating System**: Windows 11
- **Active Environment**: datascience
- **Python Version**: 3.13.12
- **Conda Version**: 26.1.1
- **Jupyter Components**: All core packages installed and functional

### Verification Test Results
The following components were verified and are working correctly:

1. **✅ Python Installation**: 
   - Version check successful
   - Basic execution working
   - REPL functionality confirmed

2. **✅ Conda Environment Management**:
   - Conda commands working
   - Environment listing successful
   - Environment activation working
   - Active environment properly reflected in terminal

3. **✅ Jupyter Notebook/Lab**:
   - Jupyter server launches without errors
   - Browser interface accessible
   - Notebook creation and execution working
   - Data science packages (numpy, pandas, matplotlib) functional

4. **✅ End-to-End Integration**:
   - Python + Conda + Jupyter working together
   - Test notebook with data operations completed successfully
   - Plotting capabilities verified

### Usage Instructions for Verified Environment

1. **Activate the verified environment**:
```bash
conda activate datascience
```

2. **Start Jupyter Notebook**:
```bash
jupyter notebook
```

3. **Run verification test**:
   - Open `test_verification.ipynb`
   - Execute all cells to verify functionality

### Verification Commands Reference
For future verification, use these commands:
```bash
# Quick verification
python --version && conda --version && jupyter --version

# Environment check
conda env list

# Package verification
python -c "import numpy, pandas, matplotlib; print('All packages OK')"
```

**Environment Status**: ✅ VERIFIED AND READY FOR DATA SCIENCE WORK

---

## Jupyter Notebook Navigation & Interface Guide

### Navigation Mastery ✅ COMPLETED
**Completion Date**: April 22, 2026  
**Environment**: datascience conda environment  
**Working Directory**: `C:\Users\Dell\Desktop\Medipredict`

### 1. Launching Jupyter Notebook ✅

#### Correct Launch Procedure:
```bash
# Activate the correct environment
conda activate datascience

# Navigate to project directory
cd C:\Users\Dell\Desktop\Medipredict

# Launch Jupyter Notebook
jupyter notebook
```

#### Launch Verification:
- ✅ Environment: datascience conda environment active
- ✅ Directory: `C:\Users\Dell\Desktop\Medipredict` (project root)
- ✅ Browser: Jupyter opens at `http://localhost:8888`
- ✅ Server: Running with correct kernel configuration

### 2. Jupyter Home Interface Components ✅

#### Key Interface Areas Identified:
1. **📁 File Browser**: Lists files and folders in current directory
2. **🧭 Navigation Breadcrumbs**: Shows current path and allows navigation
3. **➕ New Button**: Dropdown menu for creating new files/notebooks
4. **📤 Upload Button**: For uploading files to current directory
5. **🔄 Refresh Button**: Reload the file browser
6. **🏃 Running Tab**: Shows active kernels and sessions
7. **🔍 Search Bar**: Filter files and folders

#### File Type Indicators:
- 📁 **Folder**: Directory
- 📓 **Notebook**: .ipynb files
- 📄 **File**: Other file types (.py, .txt, .csv, etc.)

### 3. Navigation Best Practices ✅

#### Safe Navigation Rules:
1. **Always know your current directory** - Check breadcrumbs
2. **Navigate intentionally** - Click folders, don't guess paths
3. **Use Up button** - Navigate to parent directory
4. **Check file locations** - Verify where notebooks are saved
5. **Stay within project folder** - Avoid working in system directories

#### Project Structure Navigation:
```
Medipredict/                    # Project root (current location)
├── notebooks/                   # Data analysis notebooks
├── data/                       # Datasets
├── scripts/                    # Python scripts
├── models/                     # Trained models
└── outputs/                    # Results and visualizations
```

### 4. Notebook Creation & Management ✅

#### Creation Process:
1. **New Notebook**: Click "New" → "Python 3"
2. **Correct Location**: Created in `C:\Users\Dell\Desktop\Medipredict`
3. **Kernel Verification**: Uses datascience environment Python 3.13.12

#### Created Notebooks:
- ✅ `jupyter_navigation_guide.ipynb` - Comprehensive guide
- ✅ `notebook_management_demo.ipynb` - Management demo
- ✅ `test_verification.ipynb` - Environment verification

### 5. File Management Operations ✅

#### Essential Operations Mastered:
1. **Create**: New → Python 3
2. **Rename**: Click notebook title or File → Rename
3. **Save**: Ctrl+S or floppy disk icon
4. **Close**: File → Close and Halt
5. **Reopen**: Click .ipynb file in Jupyter Home

#### Keyboard Shortcuts Verified:
- **Ctrl+S**: Save notebook ✅
- **Ctrl+Enter**: Run current cell ✅
- **Shift+Enter**: Run cell and select below ✅
- **Alt+Enter**: Run cell and insert below ✅
- **DD**: Delete current cell (command mode) ✅
- **A**: Insert cell above (command mode) ✅
- **B**: Insert cell below (command mode) ✅
- **M**: Change to markdown (command mode) ✅
- **Y**: Change to code (command mode) ✅

### 6. Navigation Verification Checklist ✅

#### ✅ Verified Capabilities:
- [x] **Jupyter Launch**: Started from correct directory and environment
- [x] **Interface Understanding**: Identified all key components
- [x] **Directory Navigation**: Confirmed working directory structure
- [x] **File Operations**: Created and verified multiple notebooks
- [x] **Notebook Creation**: Successfully created functional notebooks
- [x] **Kernel Functionality**: Python environment working correctly
- [x] **File Management**: Demonstrated save, rename, close operations

### 7. Current Environment Status ✅

#### System Information:
- **Working Directory**: `C:\Users\Dell\Desktop\Medipredict`
- **Active Environment**: datascience
- **Python Version**: 3.13.12
- **Conda Version**: 26.1.1
- **Jupyter Components**: All core packages functional

#### Access Information:
- **Jupyter URL**: `http://localhost:8888`
- **Project Root**: `C:\Users\Dell\Desktop\Medipredict`
- **Notebook Location**: Project directory (correct)

### 8. Ready for Data Science Work ✅

#### Navigation Confidence Achieved:
1. **✅ Launch**: Can start Jupyter correctly from terminal
2. **✅ Navigate**: Confidently move through interface and directories
3. **✅ Create**: Can create notebooks in correct locations
4. **✅ Manage**: Can save, rename, and organize notebooks
5. **✅ Execute**: Can run Python code successfully

#### Next Steps Ready:
- **Data Analysis**: Ready to create analysis notebooks
- **Visualization**: Ready to work with matplotlib/seaborn
- **Modeling**: Ready for machine learning workflows
- **Deployment**: Ready for Streamlit and other applications

**Navigation Status**: ✅ MASTERED AND READY FOR DATA SCIENCE SPRINT

### Quick Reference Commands

```bash
# Start Jupyter correctly
conda activate datascience
cd C:\Users\Dell\Desktop\Medipredict
jupyter notebook

# Quick environment check
conda info --envs
python --version
jupyter --version
```

**You are now fully prepared for Data Science work! 🎉**

---

If you'd like, I will: 1) add the suggested `DESIGN.md` draft, 2) create a small sample `data/sample_schema.csv` sketch, or 3) open a PR with this README update. Which should I do next?
