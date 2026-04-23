# MediPredict Project Structure Guide

## Overview

This document outlines the standardized folder structure for the MediPredict Data Science project. A well-organized project ensures reproducibility, collaboration, and maintainability throughout the development lifecycle.

## Project Directory Structure

```
MediPredict/
├── README.md                    # Project overview and setup instructions
├── .gitignore                   # Git ignore patterns
├── environment.yml              # Conda environment specification
│
├── data/                        # Data files (read-only after creation)
│   ├── raw/                    # Original, immutable data files
│   ├── processed/               # Cleaned and processed data
│   ├── external/               # Data from external sources
│   └── sample.csv              # Sample data for testing
│
├── notebooks/                   # Jupyter notebooks for analysis
│   ├── eda/                    # Exploratory Data Analysis
│   ├── modeling/               # Model development and training
│   ├── visualization/          # Data visualization and plots
│   └── reports/                # Final analysis reports
│
├── scripts/                     # Reusable Python scripts
│   ├── data_processing/        # Data cleaning and preprocessing
│   ├── modeling/               # Model training and evaluation
│   └── utilities/              # Helper functions and utilities
│
├── models/                      # Trained model artifacts
│   ├── trained_models/         # Serialized model files
│   ├── model_metadata/         # Model information and configs
│   └── model_evaluation/       # Performance metrics and results
│
├── outputs/                     # Generated outputs and results
│   ├── figures/                # Plots, charts, and visualizations
│   ├── reports/                # Generated reports and summaries
│   └── logs/                   # Execution logs and debugging info
│
├── docs/                        # Project documentation
│   ├── PROJECT_STRUCTURE.md    # This file
│   ├── DATA_DICTIONARY.md      # Data field descriptions
│   └── API_DOCUMENTATION.md    # API and service documentation
│
├── backend/                     # Backend application code
├── frontend/                    # Frontend application code
└── proof/                       # Verification and proof files
```

## Folder Descriptions

### 📁 data/
**Purpose**: Store all data files with clear separation of data states

- **raw/**: Original, immutable data files. Never modify files in this folder.
- **processed/**: Cleaned, transformed, and processed data ready for analysis.
- **external/**: Data from third-party sources or APIs.

**Rules**:
- Never modify raw data files
- Always document data sources and transformations
- Use descriptive file names with dates when appropriate

### 📁 notebooks/
**Purpose**: Jupyter notebooks for interactive analysis and exploration

- **eda/**: Exploratory Data Analysis notebooks
- **modeling/**: Model development, training, and evaluation
- **visualization/**: Data visualization and plotting notebooks
- **reports/**: Final analysis reports and presentations

**Rules**:
- Keep notebooks focused on specific tasks
- Use clear, descriptive names
- Document assumptions and methodology
- Clean up and restart before final submission

### 📁 scripts/
**Purpose**: Reusable Python scripts for automated tasks

- **data_processing/**: Data cleaning, transformation, and preprocessing
- **modeling/**: Model training, evaluation, and deployment scripts
- **utilities/**: Helper functions and common utilities

**Rules**:
- Scripts should be self-contained and reproducible
- Include proper error handling and logging
- Use clear function and variable names
- Document input/output specifications

### 📁 models/
**Purpose**: Store trained model artifacts and metadata

- **trained_models/**: Serialized model files (.pkl, .joblib, .h5, etc.)
- **model_metadata/**: Model information, configurations, and parameters
- **model_evaluation/**: Performance metrics, confusion matrices, etc.

**Rules**:
- Include model versioning and timestamps
- Document model architecture and hyperparameters
- Store evaluation metrics alongside models
- Use consistent naming conventions

### 📁 outputs/
**Purpose**: Generated outputs, figures, and reports

- **figures/**: Plots, charts, and visualizations
- **reports/**: Generated analysis reports and summaries
- **logs/**: Execution logs and debugging information

**Rules**:
- Use descriptive file names with dates
- Include figure legends and descriptions
- Separate temporary outputs from final results
- Clean up old outputs regularly

### 📁 docs/
**Purpose**: Project documentation and guides

- **PROJECT_STRUCTURE.md**: This structure guide
- **DATA_DICTIONARY.md**: Data field descriptions and meanings
- **API_DOCUMENTATION.md**: API endpoints and service documentation

**Rules**:
- Keep documentation up-to-date
- Use clear, concise language
- Include examples where helpful
- Review and update regularly

## File Naming Conventions

### Data Files
- Raw data: `dataset_name_YYYY-MM-DD.csv`
- Processed data: `dataset_name_processed_YYYY-MM-DD.csv`
- External data: `source_dataset_YYYY-MM-DD.csv`

### Notebooks
- EDA: `eda_feature_description_YYYY-MM-DD.ipynb`
- Modeling: `model_modelname_version_YYYY-MM-DD.ipynb`
- Visualization: `viz_plot_type_YYYY-MM-DD.ipynb`

### Scripts
- Data processing: `process_data_description.py`
- Modeling: `train_model_name.py`
- Utilities: `util_function_name.py`

### Models
- Trained models: `model_name_version_YYYY-MM-DD.pkl`
- Metadata: `model_name_version_metadata.json`

## Collaboration Guidelines

### Before Starting Work
1. Review existing project structure
2. Check for existing similar files
3. Follow established naming conventions
4. Update relevant documentation

### During Development
1. Keep work in appropriate folders
2. Use descriptive commit messages
3. Update documentation as needed
4. Test file paths and references

### Before Submission
1. Clean up temporary files
2. Restart notebooks and clear outputs
3. Verify all file paths work correctly
4. Update documentation with changes

## Common Pitfalls to Avoid

### ❌ Don't Do This
- Mix data files with code files
- Modify raw data files directly
- Use vague file names like "analysis.ipynb"
- Store outputs in the same folder as inputs
- Create deeply nested folder structures
- Ignore documentation updates

### ✅ Do This Instead
- Keep data, code, and outputs separate
- Always work on copies of raw data
- Use descriptive, dated file names
- Store results in dedicated output folders
- Maintain a clean, shallow structure
- Keep documentation current

## Reproducibility Checklist

Before sharing or submitting work, ensure:

- [ ] All data files are in correct folders
- [ ] Notebook file paths are relative and correct
- [ ] Scripts can run independently
- [ ] Models are properly versioned
- [ ] Documentation is up-to-date
- [ ] No hardcoded absolute paths
- [ ] Environment requirements documented

## Getting Started

1. Clone the repository
2. Set up the conda environment: `conda env create -f environment.yml`
3. Activate environment: `conda activate datascience`
4. Review this structure guide
5. Check existing data in `data/` folder
6. Start with notebooks in `notebooks/eda/` for new analysis

This structure ensures your work remains organized, reproducible, and collaboration-ready throughout the Data Science sprint.
