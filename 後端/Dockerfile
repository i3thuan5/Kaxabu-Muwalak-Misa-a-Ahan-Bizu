FROM python:3.7-stretch

MAINTAINER Ithuan

WORKDIR /opt/kaxabu/
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE kaxabu.settings_tsiunnsuann

EXPOSE 8000
CMD gunicorn kaxabu.wsgi --log-level debug -b 0.0.0.0:8000
