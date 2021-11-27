FROM python:3.9-slim-buster

ENV POETRY_VERSION=1.0.0

# System dependencies
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory
WORKDIR /usr/src

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root

# Copy source code
COPY . .

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
