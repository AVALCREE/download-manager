@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Installing Python...
    :: Define the URL for the Python installer
    set "PYTHON_INSTALLER_URL=https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
    set "PYTHON_INSTALLER=python_installer.exe"

    :: Download the Python installer
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_INSTALLER_URL% -OutFile %PYTHON_INSTALLER%"

    :: Install Python silently
    start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1

    :: Check if installation was successful
    python --version >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo Python installation failed. Please install Python manually.
        exit /b 1
    )
)

:: Navigate to the directory containing the Python script
cd /d "%~dp0"

:: Run the Python script
python main.py

:: Pause to keep the window open
pause
