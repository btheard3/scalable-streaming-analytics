# Use lightweight base
FROM python:3.10-slim

# Set environment
ENV AIRFLOW_HOME=/app/airflow
WORKDIR /app

# Install OS-level dependencies
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

# Copy requirements and install core deps
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install \
      apache-airflow==2.7.3 \
      apache-airflow-providers-google \
      apache-airflow-providers-postgres \
      Flask-Session==0.4.0 \
      jupyterlab

# Copy notebooks and airflow code
COPY notebooks/ /app/notebooks/
COPY airflow/ /app/airflow/
COPY .secrets/gcp-key.json /app/.secrets/gcp-key.json

# Expose Jupyter and Airflow ports
EXPOSE 8080 8888

# Default command: init Airflow DB, launch both servers
CMD bash -c "airflow db init && airflow webserver & jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token=''"






















