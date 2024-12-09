#!/bin/sh
poetry run python3 /app/manage.py collectstatic --noinput
poetry run gunicorn app.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/app
