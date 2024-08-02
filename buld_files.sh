#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python3.9 manage.py makemigrations

# Migrate
echo "Applying migrations..."
python3.9 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

# Additional commands can be added here if needed