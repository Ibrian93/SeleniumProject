FROM python

ENV PYTHONBUFFERED 1
MAINTAINER Brian Martin Icochea Lopez

RUN mkdir Backend
WORKDIR /Backend

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "Tests/", "--tb", "line"]