FROM python:3.9

ENV PYTHONBUFFERED 1
MAINTAINER Brian Martin Icochea Lopez

COPY ./requirements.txt requirements.txt
COPY ./wait-for-selenium-container.sh wait-for-selenium-container.sh

RUN apt-get update 
RUN apt-get install -y jq

RUN pip install -r requirements.txt

COPY . .
