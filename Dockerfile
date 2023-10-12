# pull official base image
FROM python:3.12.0-slim-bullseye AS app

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_ALLOWED_HOSTS='["*"]' \
    APP_DATABASES__default__ENGINE="django.db.backends.postgresql" \
    APP_DATABASES__default__NAME="app" \
    APP_DATABASES__default__USER="app" \
    APP_DATABASES__default__HOST="postgres" \
    DJANGO_SETTINGS_MODULE="core.settings"

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN python manage.py collectstatic --noinput

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]