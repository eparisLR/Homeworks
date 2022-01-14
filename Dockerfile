FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

COPY ./app /app/app
COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --disable-pip-version-check --upgrade -r /tmp/requirements.txt

CMD ["/start-reload.sh"]