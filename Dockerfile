FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .build-deps build-base postgresql-dev\
    && pip install -r /requirements.txt \
    && apk del .build-deps

# Setup directory structure

COPY ./src/ /app
WORKDIR /app
