@echo off
cd /d "%~dp0"
start "CareerBridge" cmd /k ".venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000"
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8000/ar/
