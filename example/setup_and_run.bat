@echo off
SET "VENV_DIR=venv"

REM Create virtual environment if it doesn't exist
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
)

REM Activate virtual environment
call "%VENV_DIR%\Scripts\activate.bat"

REM Install dependencies
echo Installing dependencies...
pip install -r "requirements.txt"

REM Run the main Python script
echo Running the main script...
python "main.py"

REM Deactivate the virtual environment after running
deactivate

REM Keep terminal open using cmd /K
cmd /K
