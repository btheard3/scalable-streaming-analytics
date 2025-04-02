# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential \
    && apt-get clean

# Copy everything into the container
COPY . /app

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Set environment variable for GCP credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/scalable-streaming-analytics-17002e5f0ca4.json

# Expose port for JupyterLab
EXPOSE 8888

# Default command (can override in docker-compose)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
