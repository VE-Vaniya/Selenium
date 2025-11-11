Write-Host "Creating virtual environment..."
python -m venv venv

if (!(Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "Virtual environment creation failed."
    exit 1
}

Write-Host "Activating virtual environment..."
& "venv\Scripts\Activate.ps1"

Write-Host "Installing dependencies from requirements.txt..."
pip install -r "requirements.txt"

Write-Host "`nEnvironment setup complete!"
