# Dockerfile

FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt -r requirements-dev.txt

# Copy source code
COPY . .

# Set environment vars
ENV PYTHONUNBUFFERED=1
ENV TOKENIZERS_PARALLELISM=false

# Default command: run Gradio app
CMD ["python", "entrypoints/gradio_app.py"]