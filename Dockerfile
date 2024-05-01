FROM python:3.11.9-slim

COPY pyproject.toml ./
RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

RUN mkdir -p /workspace/app
WORKDIR /workspace/app

EXPOSE 8888