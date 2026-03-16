#!/bin/bash

echo "=========================================="
echo "Mobile Mechanic Setup Script"
echo "=========================================="

# Check Python
echo "Checking Python..."
python --version || { echo "Python not found"; exit 1; }

# Create venv
echo "Creating virtual environment..."
python -m venv backend_venv

# Activate venv
echo "Activating virtual environment..."
source backend_venv/bin/activate || . backend_venv\Scripts\activate

# Install dependencies
echo "Installing Python packages..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py migrate

# Install frontend dependencies
echo "Installing Node packages..."
cd frontend
npm install
cd ..

echo "=========================================="
echo "✓ Setup complete!"
echo "=========================================="
echo ""
echo "To start the application:"
echo "1. Backend:  python manage.py runserver 8000"
echo "2. Frontend: cd frontend && npm start"
echo ""
echo "Then open: http://localhost:3000"
echo "=========================================="
