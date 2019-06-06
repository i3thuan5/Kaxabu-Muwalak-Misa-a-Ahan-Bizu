FROM python:3.7-stretch

MAINTAINER Ithuan

WORKDIR /opt/kaxabu/
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
RUN echo 'DEBUG = False' >> kaxabu/settings.py

EXPOSE 8000
CMD gunicorn kaxabu.wsgi --log-level debug -b 0.0.0.0:8000
