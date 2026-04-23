# MediPredict Data Dictionary

## Overview

This document describes the data fields, formats, and meanings used in the MediPredict project. This dictionary ensures consistent understanding and interpretation of data across all team members and analyses.

## Sample Dataset Structure

### Patient Data Schema

| Field Name | Data Type | Description | Example | Notes |
|------------|------------|-------------|---------|-------|
| patient_id | Integer | Unique patient identifier | 12345 | Primary key, immutable |
| admission_date | Date | Date of hospital admission | 2024-01-15 | Format: YYYY-MM-DD |
| discharge_date | Date | Date of hospital discharge | 2024-01-20 | NULL if still admitted |
| age | Integer | Patient age in years | 65 | Range: 0-120 |
| gender | String | Patient gender | 'M' or 'F' | Values: 'M', 'F', 'Other' |
| diagnosis | String | Primary diagnosis code | 'J12.9' | ICD-10 codes |
| severity | Integer | Condition severity score | 3 | Range: 1-5, higher = more severe |
| bed_type | String | Type of bed required | 'ICU' | Values: 'General', 'ICU', 'Emergency' |
| oxygen_required | Boolean | Oxygen therapy required | True | True/False |
| oxygen_flow_rate | Float | Oxygen flow rate (L/min) | 2.5 | NULL if not required |
| length_of_stay | Integer | Length of hospital stay (days) | 5 | Calculated field |
| readmission_30d | Boolean | Readmission within 30 days | False | True/False |
| mortality_30d | Boolean | Death within 30 days | False | True/False |

### Resource Utilization Schema

| Field Name | Data Type | Description | Example | Notes |
|------------|------------|-------------|---------|-------|
| date | Date | Date of resource measurement | 2024-01-15 | Daily measurements |
| total_beds | Integer | Total hospital beds available | 200 | Capacity metric |
| occupied_beds | Integer | Currently occupied beds | 180 | Utilization metric |
| icu_beds | Integer | Total ICU beds available | 20 | ICU capacity |
| occupied_icu | Integer | Currently occupied ICU beds | 18 | ICU utilization |
| oxygen_tanks | Integer | Oxygen tanks available | 50 | Resource metric |
| oxygen_in_use | Integer | Oxygen tanks currently in use | 35 | Resource utilization |
| staff_nurses | Integer | Nursing staff on duty | 45 | Staffing metric |
| staff_doctors | Integer | Medical doctors on duty | 15 | Staffing metric |
| emergency_wait_time | Float | Emergency department wait time (hours) | 2.5 | Service metric |

## Data Sources

### Internal Hospital Systems
- **EHR (Electronic Health Records)**: Patient admissions, diagnoses, treatments
- **Hospital Management System**: Bed management, resource allocation
- **Pharmacy System**: Medication orders and inventory
- **Laboratory System**: Test results and diagnostics

### External Data Sources
- **Public Health Data**: Regional disease trends and statistics
- **Weather Data**: Environmental factors affecting health
- **Demographic Data**: Population statistics for the service area

## Data Quality Standards

### Completeness
- **Required Fields**: patient_id, admission_date, age, gender, diagnosis
- **Optional Fields**: discharge_date, oxygen_flow_rate, readmission_30d
- **Missing Data Threshold**: <5% for required fields, <20% for optional fields

### Accuracy
- **Age Range**: 0-120 years
- **Date Validation**: Admission date ≤ discharge date
- **Logical Consistency**: Oxygen required → oxygen_flow_rate not NULL

### Consistency
- **Coding Standards**: ICD-10 for diagnoses, standard units for measurements
- **Naming Conventions**: Snake_case for all field names
- **Data Types**: Consistent data types across all datasets

## Data Processing Rules

### Data Cleaning
1. **Remove Duplicates**: Based on patient_id and admission_date
2. **Handle Missing Values**: 
   - Required fields: Remove records
   - Optional fields: Impute with appropriate defaults
3. **Validate Ranges**: Check for outliers and impossible values
4. **Standardize Formats**: Ensure consistent date and text formats

### Feature Engineering
1. **Derived Fields**: Calculate length_of_stay from dates
2. **Categorical Encoding**: Convert gender, bed_type to numeric codes
3. **Normalization**: Scale numerical fields as appropriate
4. **Time Series**: Create lag features for resource utilization

## Data Privacy and Security

### Sensitive Information
- **PHI (Protected Health Information)**: All patient identifiers
- **Access Control**: Role-based access to patient data
- **Data Masking**: Remove direct identifiers in analysis datasets

### Compliance Requirements
- **HIPAA**: Health Insurance Portability and Accountability Act
- **Data Retention**: Store data for required retention period
- **Audit Trail**: Log all data access and modifications

## Usage Guidelines

### Analysis Best Practices
1. **Use Processed Data**: Always work with data from `data/processed/` folder
2. **Document Transformations**: Record all data cleaning steps
3. **Validate Results**: Cross-check summary statistics
4. **Version Control**: Track data schema changes

### Reporting Standards
1. **Include Metadata**: Always report data sources and date ranges
2. **Define Metrics**: Clearly define all calculated metrics
3. **Limitations**: Document data limitations and assumptions
4. **Reproducibility**: Provide code for all data transformations

## Data Lineage

### Raw Data → Processed Data
1. **Extraction**: Pull from source systems
2. **Cleaning**: Remove errors and inconsistencies
3. **Transformation**: Apply business rules and calculations
4. **Validation**: Verify data quality and completeness
5. **Storage**: Save to processed data folder

### Processed Data → Analysis
1. **Feature Selection**: Choose relevant variables
2. **Aggregation**: Summarize as needed for analysis
3. **Visualization**: Create plots and summary tables
4. **Modeling**: Use for predictive model training

## Contact and Support

### Data Steward
- **Name**: Data Management Team
- **Email**: data-team@hospital.org
- **Responsibility**: Data quality and documentation

### Technical Support
- **Name**: IT Help Desk
- **Email**: helpdesk@hospital.org
- **Responsibility**: System access and technical issues

This data dictionary should be updated whenever:
- New data fields are added
- Data sources change
- Business rules are modified
- Quality standards are updated

Last Updated: 2024-04-23
Version: 1.0
