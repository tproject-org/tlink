#!/bin/sh

chmod +x ./manage.py

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username=admin --email=admin@example.com
./manage.py runserver