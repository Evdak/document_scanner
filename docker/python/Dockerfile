FROM python:3.11

COPY ./document_scanner /srv/www/document_scanner
COPY requirements.txt /srv/www/document_scanner
WORKDIR /srv/www/document_scanner

RUN pip install --no-cache-dir --upgrade -r requirements.txt