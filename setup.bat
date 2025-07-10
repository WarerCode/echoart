@echo off
echo === Loading echoart util from GitHub ===

REM Check Git
git --version >nul 2>&1
if errorlevel 1 (
    echo Git not found. Please install Git and try again.
    pause
    exit /b
)

REM Clone repo
git clone https://github.com/WarerCode/echoart.git
if errorlevel 1 (
    echo Failed to clone repository.
    pause
    exit /b
)

cd echoart || (
    echo Failed to enter echoart directory.
    pause
    exit /b
)

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python and try again.
    pause
    exit /b
)

REM Install requirements
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    pause
    exit /b
)

REM Run script
echo Running echoart...
call echoart.bat --input assets/tree.png

pause
