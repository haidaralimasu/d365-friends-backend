FROM python:3.12.5-slim as backend

WORKDIR /home/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt-get install -y python3-dev
RUN apt-get install -y libpq-dev gcc

RUN export PATH=/usr/lib/postgresql/16/bin/:$PATH

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .