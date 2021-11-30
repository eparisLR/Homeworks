FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

RUN apt update

ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD ./app ./app