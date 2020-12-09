FROM dosel/zalenium
WORKDIR /test
COPY requirements.txt requirements.txt
USER root
RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["behave"]
