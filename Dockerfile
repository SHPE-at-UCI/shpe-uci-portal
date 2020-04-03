from alpine:latest

RUN apk update && apk upgrade && apk add bash

RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
