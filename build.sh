#!/bin/bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=config.settings
python manage.py migrate --settings=config.settings
