#!/usr/bin/env bash
# Generates INSTALLATION_PROOF.md capturing python/conda info on Unix-like systems
set -euo pipefail
proofFile="INSTALLATION_PROOF.md"
echo "# Installation proof" > "$proofFile"
echo "Generated: $(date --iso-8601=seconds)" >> "$proofFile"
echo "" >> "$proofFile"

echo "## System" >> "$proofFile"
uname -a >> "$proofFile" 2>&1 || true
echo "" >> "$proofFile"

echo "## Python" >> "$proofFile"
python --version >> "$proofFile" 2>&1 || true
python -c 'import sys; print("Executable:", sys.executable)' >> "$proofFile" 2>&1 || true
which python >> "$proofFile" 2>&1 || true
echo "" >> "$proofFile"

echo "## Conda" >> "$proofFile"
conda --version >> "$proofFile" 2>&1 || true
conda info --envs >> "$proofFile" 2>&1 || true
which conda >> "$proofFile" 2>&1 || true
echo "" >> "$proofFile"

echo "## pip list" >> "$proofFile"
python -m pip --version >> "$proofFile" 2>&1 || true
python -m pip list --format=columns >> "$proofFile" 2>&1 || true
echo "" >> "$proofFile"
echo "## Notes" >> "$proofFile"
echo "Add manual notes here." >> "$proofFile"

echo "Generated $proofFile"
