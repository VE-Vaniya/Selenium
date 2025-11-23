@echo off
REM Creating a Python virtual environment
python -m venv venv

REM Activating the virtual environment
call venv\Scripts\activate

REM Installing dependencies from requirements.txt
pip install -r requirements.txt

echo.
echo Environment setup complete!