# MediPredict — Part A: README Documentation (PR Submission)

## Part A: README Documentation

### 1) Explaining the Lifecycle — Question → Data → Insight

- **Start with a clear question:** A good question is a specific decision we want to make, stated in terms of population, action, and timeframe. For example: "Which discharged patients should receive a targeted care-management visit to prevent a 30-day readmission?" Starting with a clear question focuses the whole project: it determines what counts as a positive case (the label), what features matter, and which evaluation metrics map to the decision (e.g., recall vs. precision depending on intervention cost). Without a clear question you risk building models that measure the wrong thing, collecting irrelevant data, or producing insights that can't be acted on.

- **Data as evidence — inspect it before analysis:** Data are measurements collected under practical constraints; they are not perfect truth. Understanding data means verifying provenance (where the records came from), schema (what each field actually records), time alignment (when events happened relative to the question), and quality (missing values, duplicates, inconsistent codes). Early exploration—sampling records, plotting distributions, checking missingness and time spans—turns raw tables into usable evidence and prevents errors like label leakage, mis-specified cohorts, or hidden biases.

- **Insights emerge from exploration, not from tools alone:** Tools (models, libraries, dashboards) are helpful, but insight requires thoughtful probing: segmenting the population, visualizing relationships, comparing subgroups, and validating patterns with domain knowledge. Real insight connects patterns in the data back to the original question and to decisions people can take. For instance, a model score is not an insight by itself; discovering that high readmission risk is concentrated among patients with recent medication changes and poor outpatient follow-up is an insight that suggests specific interventions.

- **How the steps connect:** The question defines the label, the relevant features, and the evaluation criteria. Understanding the data reveals whether you can answer that question with the available evidence and whether adjustments (more data, different cohort, re-defined time windows) are needed. Exploration converts data into understanding and surfaces the actionable patterns that answer the question. That understanding can refine the question, making the process iterative rather than linear.

### 2) Applying the Lifecycle to a Project Context — Example: 30-day Readmission Risk

- **The question:** "Which patients discharged from the hospital are at highest risk of unplanned readmission within 30 days, such that assigning a post-discharge case manager would likely reduce that risk?" The operational decision: allocate a limited number of case-manager visits each week to the highest-value patients.

- **The data needed (what and where it might come from):**
  - Index hospital admissions table (admission/discharge timestamps, service, discharge disposition) from the hospital EHR.
  - Demographics and comorbidities (age, sex, chronic conditions) from the EHR problem list and past encounters.
  - In-hospital measurements and labs during the index admission (last values, trends).
  - Medication lists at discharge and prior pharmacy fill records (if available).
  - Prior utilization: emergency department visits and admissions in the last 6–12 months from claims or EHR history.
  - Social determinants proxies (ZIP-code level socioeconomic data or documented social needs) from administrative data or external datasets.
  - Outcome label: a readmission event within 30 days after discharge (derived by linking admissions by patient identifier).

  Each row represents an index discharge; features are aggregated from the pre-defined time windows. Sources include the hospital data warehouse, pharmacy/claims feeds, and public SDOH datasets. Key early tasks are patient-linkage, defining the index cohort, and resolving different coding systems (ICD versions, medication codes).

- **The insight that is useful for decision-making:**
  - A ranked list of patients with calibrated risk scores (to decide who receives a case-manager visit).
  - Driver-level explanations and cohort summaries: which risk factors (e.g., recent prior admissions, specific lab abnormalities, medication gaps, lack of scheduled follow-up) are most responsible for elevated risk in the high-risk cohort. These suggest targeted interventions (medication reconciliation, scheduling outpatient follow-up, home health referrals).
  - A capacity-aware threshold: the risk cutoff chosen to match available case-manager capacity, plus an estimate of expected readmissions avoided and cost trade-offs.

- **Why this follows the lifecycle:** the question sets the label and action; the data chosen must contain evidence that maps to the question (timing, measurements that reflect clinical state and social risk); and exploration (cohort checks, subgroup analyses, feature importance, and calibration testing) produces the concrete, actionable insights needed to deploy the intervention responsibly.

---

If you'd like, I can: 1) add a short dataset sketch and column examples for this project, 2) create a separate DESIGN.md with evaluation criteria and acceptance thresholds, or 3) open a PR with this README change applied. Which would you prefer next?
