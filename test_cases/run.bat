@echo off
REM Run all pytest test cases using the multi-browser fixture

REM Activate venv if needed (uncomment if you use a virtual environment)
REM call ..\..\venv\Scripts\activate.bat

pytest -v -n 3 --maxfail=1 --disable-warnings

pause
