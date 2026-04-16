#!/usr/bin/env pwsh
# Generates INSTALLATION_PROOF.md capturing python/conda info on Windows/PowerShell
$proofFile = "INSTALLATION_PROOF.md"
$timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
"# Installation proof" | Out-File $proofFile -Encoding UTF8
"Generated: $timestamp" | Out-File -Append $proofFile
"" | Out-File -Append $proofFile

"## System" | Out-File -Append $proofFile
try {
    $os = Get-CimInstance Win32_OperatingSystem | Select-Object -First 1
    ("OS: {0} ({1})" -f $os.Caption, $os.Version) | Out-File -Append $proofFile
} catch {
    "OS info not available: $_" | Out-File -Append $proofFile
}

"" | Out-File -Append $proofFile
"## Python" | Out-File -Append $proofFile
try {
    & python --version 2>&1 | Out-File -Append $proofFile
    & python -c "import sys; print('Executable: ' + sys.executable)" 2>&1 | Out-File -Append $proofFile
    & python -c "import sys; print('Version: ' + sys.version)" 2>&1 | Out-File -Append $proofFile
    & where.exe python 2>&1 | Out-File -Append $proofFile
} catch {
    "Python command failed or not found: $_" | Out-File -Append $proofFile
}

"" | Out-File -Append $proofFile
"## Conda" | Out-File -Append $proofFile
try {
    & conda --version 2>&1 | Out-File -Append $proofFile
    & conda info --envs 2>&1 | Out-File -Append $proofFile
    & where.exe conda 2>&1 | Out-File -Append $proofFile
} catch {
    "Conda command failed or not found: $_" | Out-File -Append $proofFile
}

"" | Out-File -Append $proofFile
"## Pip / Installed Python packages (sample)" | Out-File -Append $proofFile
try {
    & python -m pip --version 2>&1 | Out-File -Append $proofFile
    & python -m pip list --format=columns 2>&1 | Out-File -Append $proofFile
} catch {
    "pip info unavailable: $_" | Out-File -Append $proofFile
}

"" | Out-File -Append $proofFile
"## Notes" | Out-File -Append $proofFile
"Add manual notes or observations here." | Out-File -Append $proofFile

Write-Host "Generated $proofFile" -ForegroundColor Green
