#!/bin/sh

python3 manage.py db init
python3 manage.py db migrate --message init
python3 manage.py db upgrade
python3 manage.py run