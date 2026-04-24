# Data Organization PR — Proof and Video Instructions

This file accompanies the PR that demonstrates data organization for the milestone. It contains a checklist, PR body template, and a short video script you can follow.

Checklist for the PR
- [ ] `data/raw/` contains raw data only (no edits). See `data/raw/sample.csv`.
- [ ] `data/processed/` exists for derived datasets (placeholder added).
- [ ] `data/output/` exists for plots/reports (placeholder added).
- [ ] `data/README.md` explains structure and naming conventions.

PR title suggestion
```
chore(data): add data organization (raw/processed/output) and proof
```

PR body template
```
This PR demonstrates proper data lifecycle organization for the project.

What I changed:
- Added `data/raw/sample.csv` (original raw file preserved).
- Added placeholders: `data/processed/.gitkeep` and `data/output/.gitkeep`.
- Added `data/README.md` describing naming conventions and rules.
- Added this proof file with video instructions.

Why:
- Keeps raw data immutable and separate from derived data and outputs.

Video walkthrough (attach `walkthrough.mp4` to PR or add link):
- ~2 minutes showing the repository tree and explaining naming conventions.

Checklist:
- [ ] Attach executed video file or link
- [ ] Confirm no raw files were modified
```

Short ~2-minute video script (suggested timings)
- 0:00–0:15 — Quick intro: name, repo, purpose of the change
- 0:15–0:45 — Show `data/` tree and explain `raw/`, `processed/`, `output/`
- 0:45–1:30 — Explain naming conventions and give an example using `sample.csv`
- 1:30–1:50 — State that raw data is preserved and where to find derived artifacts
- 1:50–2:00 — Closing and where to find this PR/proof files

Recording tips (Windows example using `ffmpeg`, optional)
```
ffmpeg -f gdigrab -framerate 30 -i desktop -t 00:02:00 -vcodec libx264 -preset ultrafast -pix_fmt yuv420p walkthrough.mp4
```

If `ffmpeg` is not available, use your preferred screen recorder (Xbox Game Bar, Loom, Zoom, etc.). Keep it short and show the `data/` folder clearly.
