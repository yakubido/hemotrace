FROM python:3.13-slim

LABEL author="chulimt@gmail.com"

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m app
USER app

COPY /application .
COPY .flaskenv_EXAMPLE .flaskenv
COPY config.py .
COPY hemotrace.py .
