# Run from the repository root with PowerShell: .\proof\run_proof.ps1
# This script collects version outputs and executes the verification notebook.
Set-StrictMode -Version Latest
$out = $PSScriptRoot
# Ensure output directory exists
if (-not (Test-Path $out)) { New-Item -ItemType Directory -Path $out | Out-Null }
# Capture versions and env info
python --version 2>&1 | Out-File -FilePath (Join-Path $out 'python_version.txt') -Encoding utf8
conda --version 2>&1 | Out-File -FilePath (Join-Path $out 'conda_version.txt') -Encoding utf8
conda info --envs 2>&1 | Out-File -FilePath (Join-Path $out 'conda_envs.txt') -Encoding utf8
jupyter --version 2>&1 | Out-File -FilePath (Join-Path $out 'jupyter_version.txt') -Encoding utf8
# Execute the notebook and write an executed copy into the proof folder
jupyter nbconvert --to notebook --execute (Join-Path $out 'verification.ipynb') --output 'executed_verification.ipynb' --output-dir $out
Write-Host "Proof files written to $out"
