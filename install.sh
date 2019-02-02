#!/usr/bin/env bash
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
echo "yes" | python manage.py collectstatic
python manage.py createsuperuser