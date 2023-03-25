FROM python:3.10-slim

WORKDIR /app


RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./

CMD gunicorn app:app