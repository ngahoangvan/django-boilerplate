FROM python:3.10-alpine

# Install OS package
RUN apk add build-base
RUN apk add --no-cache jpeg-dev zlib-dev

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install poetry setuptools --no-cache-dir

WORKDIR /app/
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install --no-root --no-interaction

COPY src/ .
RUN addgroup -S django && adduser -S django -G django
RUN chown -R django /app

COPY ./bin/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

RUN exec "$0"
