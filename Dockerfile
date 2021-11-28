FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.0.0

# system dependencies
RUN pip install "poetry==$POETRY_VERSION"

# set working directory
WORKDIR /usr/src

# copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root

# copy source code
COPY . .
