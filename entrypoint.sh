#!/bin/bash

poetry run uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --workers 1 --no-access-log