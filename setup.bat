@echo off
echo.
echo ==========================================
echo Mobile Mechanic Setup Script
echo ==========================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1 || (echo Python not found && exit /b 1)

REM Create venv
echo Creating virtual environment...
python -m venv backend_venv

REM Activate venv
echo Activating virtual environment...
call backend_venv\Scripts\activate.bat

REM Install dependencies
echo Installing Python packages...
pip install -r requirements.txt

REM Run migrations
echo Running database migrations...
python manage.py migrate

REM Install frontend dependencies
echo Installing Node packages...
cd frontend
call npm install
cd ..

echo.
echo ==========================================
echo Setup complete!
echo ==========================================
echo.
echo To start the application:
echo 1. Backend:  python manage.py runserver 8000
echo 2. Frontend: cd frontend ^&^& npm start
echo.
echo Then open: http://localhost:3000
echo ==========================================
echo.
pause
