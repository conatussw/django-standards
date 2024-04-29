FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
COPY requirements-dev.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements-dev.txt

COPY . /code/
