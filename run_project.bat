@echo off
echo Student Attendance Predictor - Setup and Run
echo ===========================================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully!
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

REM Run the main program
echo.
echo Starting Student Attendance Predictor...
echo.
python main.py

echo.
echo Program finished. Press any key to exit...
pause >nul
