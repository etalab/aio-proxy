FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.pip

EXPOSE 8080

CMD [ "make", "run" ] 
