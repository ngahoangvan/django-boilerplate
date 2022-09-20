FROM python:3.8-alpine

# Install OS package
RUN apk add build-base
RUN apk add --no-cache jpeg-dev zlib-dev

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1


WORKDIR /app/
COPY ./requirements requirements
RUN python3 -m pip install -r requirements/all.txt --no-cache-dir
RUN addgroup -S django && adduser -S django -G django
COPY src/ .
RUN chown -R django /app

COPY ./bin/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh
RUN exec "$0"
