# Use an official Python runtime as a parent image
FROM python:3.10-slim

# The "1000" is a default value. If you encounter conflicts, please refer to
# https://github.com/loggi/url-shortener/pull/149#discussion_r1452674399 for more context.
ARG LOCAL_USER_ID=1000

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

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$PATH"

# User privileges (optional for security)
# Create a new user named 'appuser' with no home directory and no system group
RUN adduser --disabled-password --gecos '' --uid $LOCAL_USER_ID appuser

# Install Poetry
RUN pip install --upgrade pip \
  && pip install poetry

# Copy the project files to the container
COPY ./pyproject.toml poetry.lock* /app/


# Copy the rest of the application
COPY . /app
COPY entrypoint.sh ./

# Install project dependencies
RUN poetry config virtualenvs.create false &&\
  poetry install --no-interaction --no-ansi && \
  chmod +x entrypoint.sh && \
  chown -R appuser:appuser /app 

# Switch to the 'appuser' user
USER appuser

# Specify the command to run your FastAPI application using Poetry and UVicorn
CMD ["sh", "entrypoint.sh"]
