# Use slim Python 3.10 base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install OS-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
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

# Copy project files
COPY requirements.txt .
COPY airflow/ /app/airflow/
COPY notebooks/ /app/notebooks/
COPY .secrets/gcp-key.json /app/.secrets/gcp-key.json

# Install Python packages
RUN pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install \
    apache-airflow==2.7.3 \
    apache-airflow-providers-google \
    apache-airflow-providers-postgres \
    Flask-Session==0.4.0 \
    jupyterlab

# Expose ports
EXPOSE 8080 8888

# Default command: starts both Jupyter and Airflow
CMD ["bash", "-c", "airflow db init && airflow webserver & jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' --no-browser --port=8888"]























