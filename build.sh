#!/bin/bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=config.settings
python manage.py migrate --noinput --settings=config.settings || true
python manage.py loaddata --settings=config.settings --ignorenonexistent portfolio/fixtures/initial_data.json || true

if [ -d "staticfiles" ]; then
  mkdir -p public
  cp -r staticfiles public/static
fi
