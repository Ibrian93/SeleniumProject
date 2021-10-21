FROM python:3.9

ENV PYTHONBUFFERED 1
MAINTAINER Brian Martin Icochea Lopez


RUN apt-get update 
RUN apt-get install -y jq

RUN mkdir Frontend
WORKDIR /Frontend

COPY Models/ Models
COPY features/ features
COPY Pages/ Pages
COPY Utils/ Utils
COPY __init__.py .
COPY behave.ini .
COPY requirements.txt .
COPY wait-for-selenium-container.sh .

RUN pip install -r requirements.txt


