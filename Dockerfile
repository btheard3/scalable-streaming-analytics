# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variable for Airflow home
ENV AIRFLOW_HOME=/app/airflow

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    gcc \
    libpq-dev \
    libsasl2-dev \
    libldap2-dev \
    libssl-dev \
    libffi-dev \
    vim \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install project Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Install Apache Airflow separately with constraints
ENV AIRFLOW_VERSION=2.7.3
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.10.txt"
RUN pip install "apache-airflow[celery,postgres,async,fab]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Install JupyterLab explicitly
RUN pip install jupyterlab

# Create required Airflow folders
RUN mkdir -p $AIRFLOW_HOME/dags $AIRFLOW_HOME/logs $AIRFLOW_HOME/plugins

# Copy DAGs and notebooks
COPY airflow/dags/ $AIRFLOW_HOME/dags/
COPY notebooks/ /app/notebooks/

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/.secrets/gcp-key.json

# Expose ports
EXPOSE 8080 8888

# Default command
CMD ["bash", "-c", "airflow db init && airflow scheduler & airflow webserver & jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser"]



















