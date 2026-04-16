PR: Local environment installation proof

This branch contains artifacts to help you prove Python + Conda are installed locally and that your environment is ready for DS/ML work.

Files added:

- `scripts/generate_installation_proof.ps1` — PowerShell script (Windows)
- `scripts/generate_installation_proof.sh` — Bash script (Unix/WSL)
- `environment.yml` — Minimal DS/ML environment (Python 3.11 + common libs)

Steps to produce proof locally (Windows PowerShell):

1. Create a branch for your PR:

```powershell
git checkout -b pr/install-proof
```

2. Run the verifier (PowerShell):

```powershell
.
\scripts\generate_installation_proof.ps1
```

Or on WSL / macOS / Git Bash:

```bash
bash scripts/generate_installation_proof.sh
```

3. Confirm `INSTALLATION_PROOF.md` was created and contains the outputs for `python --version` and `conda --version`.

4. Commit and push the proof:

```bash
git add environment.yml INSTALLATION_PROOF.md
git commit -m "chore: add environment.yml and installation proof"
git push -u origin pr/install-proof
```

5. Open a Pull Request on GitHub using the branch `pr/install-proof`. Use this PR description template:

```
Title: Proof of local Python + Conda installation

This PR proves that Python and Conda are installed on my local machine and that the repo has a reproducible environment for DS/ML work.

What I ran locally:
- `python --version`
- `conda --version`
- `scripts/generate_installation_proof.ps1` (or `scripts/generate_installation_proof.sh`)

Attached: `INSTALLATION_PROOF.md`

I will attach a short video walkthrough (30–120s) showing the terminal running the commands and the generated `INSTALLATION_PROOF.md`.
```

Video walkthrough checklist (short):

- Show `python --version` in terminal
- Show `conda --version` in terminal
- Run the verification script
- Open `INSTALLATION_PROOF.md` and show the captured output

Notes

- If `conda` is not found, install Anaconda or Miniconda (https://www.anaconda.com/products/distribution).
- If you prefer not to commit `INSTALLATION_PROOF.md`, paste its contents into the PR description instead.
