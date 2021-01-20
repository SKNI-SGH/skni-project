FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get auto-remove

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY backend/ .


CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8080

EXPOSE 8080
