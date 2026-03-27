#!/bin/bash

echo "Starting Kiaalap Dashboard..."
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting Dash application..."
echo "The application will be available at http://localhost:8050"
echo ""

python app.py
