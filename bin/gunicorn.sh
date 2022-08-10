#!/bin/sh
python3 /app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn app.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/app
