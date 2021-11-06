FROM python:3.8.3

RUN adduser api

WORKDIR /home/gvsearch

RUN apt-get update -y && \
    apt-get install -y \
        cmake \
        git \
        gcc \
        g++ \
        libc-dev \
        tar \
        gfortran \
        ca-certificates \
        tcl \
        tk \
        dpkg-dev  \
        libzbar0
RUN apt-get install -y git libffi-dev 
RUN apt-get install -y python3-dev python2 musl-dev
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app/ app/
COPY gvsearch.py ./

ENV FLASK_APP gvsearch.py

RUN chown -R api:api ./
USER api

EXPOSE 8080
CMD venv/bin/gunicorn --bind 0.0.0.0:8080 --access-logfile - --error-logfile - gvsearch:app