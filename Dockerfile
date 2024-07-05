# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip \
  && pip install poetry

# Copy the project files to the container
COPY ./pyproject.toml poetry.lock* /app/


# Install project dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of the application
COPY . /app

# Command to run the application using Uvicorn
CMD ["uvicorn", "src.app.entrypoint.api.main:app", "--host", "0.0.0.0", "--port", "80"]
