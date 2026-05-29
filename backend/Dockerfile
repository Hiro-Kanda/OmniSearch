FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir -U pip \
 && pip install --no-cache-dir "fastapi>=0.110" "uvicorn[standard]>=0.27" "pydantic-settings>=2.2" "httpx>=0.27"

COPY app /app/app
