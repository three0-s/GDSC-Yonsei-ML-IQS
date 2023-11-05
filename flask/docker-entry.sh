#!/bin/sh

python3 manage.py db init
python3 manage.py db migrate --message init
python3 manage.py db upgrade
uwsgi uwsgi.ini
# gunicorn --workers 3 --bind 0.0.0.0:8888 -m 007 "manage:run()"
# python3 manage.py run