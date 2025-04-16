# Use lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV AIRFLOW_HOME=/app/airflow
WORKDIR /app

# Install system-level dependencies
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

# Copy files
COPY requirements.txt .
COPY airflow/ /app/airflow/
COPY notebooks/ /app/notebooks/
COPY .secrets/gcp-key.json /app/.secrets/gcp-key.json

# Install Python packages
RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install apache-airflow==2.7.3 \
               apache-airflow-providers-google \
               apache-airflow-providers-postgres \
               jupyterlab
RUN pip install Flask-Session


# Expose Jupyter and Airflow webserver ports
EXPOSE 8080 8888

# Default command: starts both Jupyter and Airflow webserver/scheduler
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' & \
    airflow db init && \
    airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin && \
    airflow webserver --port 8080 & \
    airflow scheduler





















