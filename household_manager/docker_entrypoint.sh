#!/bin/bash
export DJANGO_SETTINGS_MODULE=household_manager.settings

python manage.py makemigrations 
python manage.py migrate 
python manage.py createsuperuser --no-input
# python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
# gunicorn household_manager.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000