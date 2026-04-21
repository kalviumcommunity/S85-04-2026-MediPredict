# Installation Proof — Environment Verification

Date: 2026-04-21

This document contains artifacts and instructions to verify the development environment for MediPredict (Python, Conda, and Jupyter).

Files added

- `proof/verification.ipynb` — notebook that prints Python/Platform/Conda info and a test message.
- `proof/run_proof.ps1` — PowerShell script to capture version outputs and execute the notebook.

How to generate the proofs (PowerShell)

```powershell
# from repo root
.\proof\run_proof.ps1
```

Manual commands (equivalent)

```powershell
python --version | Out-File proof/python_version.txt -Encoding utf8
conda --version | Out-File proof/conda_version.txt -Encoding utf8
conda info --envs | Out-File proof/conda_envs.txt -Encoding utf8
jupyter --version | Out-File proof/jupyter_version.txt -Encoding utf8
jupyter nbconvert --to notebook --execute proof/verification.ipynb --output executed_verification.ipynb --output-dir proof
```

Proof artifacts (after running the script)

- `proof/python_version.txt`
- `proof/conda_version.txt`
- `proof/conda_envs.txt`
- `proof/jupyter_version.txt`
- `proof/executed_verification.ipynb`

What to include in the PR

- Add the `proof/*` files (executed notebook and the text outputs) and update this document.
- Paste the contents of `proof/python_version.txt` and `proof/conda_version.txt` into the PR description and confirm which `conda` env you activated.

Example git commands (create branch, commit, push)

```powershell
git checkout -b proof/environment-verification
git add proof/*
git add INSTALLATION_PROOF.md
git commit -m "docs(proof): add environment verification notebook and run script"
git push -u origin proof/environment-verification
# then open a PR on GitHub or use `gh pr create` with a PR body that lists the outputs
```

Notes:

- If `jupyter` is not found on your PATH, run via Python: `python -m jupyter lab` or `python -m notebook`.
- If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
```
