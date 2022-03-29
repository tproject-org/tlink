#!/bin/sh

git clone https://github.com/tproject-org/tlink
cd tlink
virtualenv -p python3 tlink-venv
source tlink-venv/bin/activate
pip install -r requirements.txt

chmod +x ./manage.py

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username=admin --email=admin@example.com
./manage.py runserver