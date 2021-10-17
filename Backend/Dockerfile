FROM alpine:latest
MAINTAINER Brian Martin Icochea Lopez

ENV PYTHONBUFFERED 1

# Installing python3 on alpine linux
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Creating folder inside the root folder and make our Work Directory
RUN mkdir Backend
WORKDIR /Backend

# Copy the requirements from our project inside the container and install them
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the whole project folders and files inside the container
COPY . .

# When the image has been build, this command will be run when running the container of the image.
CMD ["pytest", "Tests/", "--tb", "line"]