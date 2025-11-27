@echo off
pytest -v -n 3 --maxfail=1 --disable-warnings
pause