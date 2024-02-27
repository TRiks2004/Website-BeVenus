FROM python:3.11-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt install -y python-dev

RUN pip install --upgrade pip
RUN pip install poetry

ADD gunicorn/gunicorn.conf.py ./gunicorn/

ADD pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

ARG HOST_PORT
EXPOSE $HOST_PORT

COPY . .

CMD ["gunicorn", "-c", "./gunicorn/gunicorn.conf.py", "main:app"]