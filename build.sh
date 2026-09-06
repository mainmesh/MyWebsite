#!/bin/bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=config.settings
echo "Running migrations..."
python manage.py migrate --settings=config.settings
echo "Loading initial data..."
python manage.py loaddata --settings=config.settings --ignorenonexistent portfolio/fixtures/initial_data.json || true

echo "Static files collected:"
ls -la staticfiles/
