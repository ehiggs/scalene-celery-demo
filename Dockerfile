FROM python:3.9.5-slim

RUN apt-get update && apt-get -y --no-install-recommends install build-essential


WORKDIR /app
COPY requirements.txt /app
RUN pip install scalene
RUN pip install -r requirements.txt

COPY . /app
