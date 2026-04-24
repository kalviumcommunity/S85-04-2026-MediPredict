# Data directory layout and rules

This repository follows a strict data hygiene policy to keep raw data immutable and ensure traceability between stages.

- `data/raw/` — Immutable raw/source data. Never modify files here in-place; add new files if new raw snapshots arrive.
- `data/processed/` — Derived or cleaned datasets produced from raw data. Use clear, versioned filenames (e.g., `20260424_clean_v1.csv`).
- `data/output/` — Outputs such as plots, reports, model artifacts, and exported results.

Naming conventions and rules:
- Preserve original raw filenames. Treat files in `data/raw` as single-source-of-truth.
- Include date and version information in processed filenames (ISO-style date `YYYY-MM-DD` or `YYYYMMDD`).
- Do not commit large binary data to the repo; use Git LFS or external storage when necessary.

Example:

- `data/raw/hospital_counts_20260425.csv`
- `data/processed/hospital_counts_20260425_clean_v1.csv`
- `data/output/hospital_counts_20260425_report.pdf`
