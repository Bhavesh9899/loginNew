#!/bin/bash

# Install required system dependencies
apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev

# Proceed with the usual pip install
pip install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt



echo "make migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "collect static files..."
python manage.py collectstatic --noinput --clear