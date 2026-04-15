# MediPredict — Project Overview and Part A Documentation

## 1) Project Intent & High-Level Flow

- **Problem / question:** The repository aims to support data-driven decisions about post-discharge patient care by identifying which discharges are most likely to experience an unplanned 30‑day readmission and therefore would benefit from targeted interventions. The practical goal is to convert clinical and administrative records into operationally useful risk signals that clinicians or care managers can act on.

- **High-level workflow followed here:**
  1. Problem framing — define the decision, the target population, and the action (who receives intervention).

2.  Data assembly & validation — gather admissions, prior utilization, medications, labs, and contextual data; validate provenance, timestamps, and linkage keys.
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

If you'd like, I will: 1) add the suggested `DESIGN.md` draft, 2) create a small sample `data/sample_schema.csv` sketch, or 3) open a PR with this README update. Which should I do next?
