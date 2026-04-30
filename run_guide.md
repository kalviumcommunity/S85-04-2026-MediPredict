# MediPredict Run Guide (Beginner Friendly)

## Quick Setup
1. Open terminal.
2. Go to project folder:
   ```bash
   cd S85-04-2026-MediPredict
   ```
3. Create virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate virtual environment:
   Mac/Linux:
   ```bash
   source venv/bin/activate
   ```
   Windows:
   ```bash
   venv\Scripts\activate
   ```
5. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
6. Generate and clean data:
   ```bash
   python src/data_preprocessing.py
   ```
7. Train models:
   ```bash
   python src/model_training.py
   ```
8. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Anaconda + Jupyter Steps
1. Open Anaconda Navigator.
2. Launch Jupyter Notebook.
3. Open `notebooks/MediPredict_EDA_Modeling.ipynb`.
4. Run cells one by one.
