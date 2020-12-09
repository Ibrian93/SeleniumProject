FROM dosel/zalenium
WORKDIR /test
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["behave"]
