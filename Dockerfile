# Use slim Python 3.10 image
FROM python:3.10-slim

# Set environment variables
ENV AIRFLOW_HOME=/app/airflow
WORKDIR /app

# Install OS-level dependencies
RUN apt-get update && apt-get install -y \
    gcc g++ curl git build-essential \
    libssl-dev libffi-dev libpq-dev \
    libsasl2-dev libldap2-dev \
    default-libmysqlclient-dev \
    python3-dev libbz2-dev \
    vim tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Install Airflow and providers with constraints
ENV AIRFLOW_VERSION=2.7.3
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.10.txt"

RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}" && \
    pip install "apache-airflow-providers-google" --constraint "${CONSTRAINT_URL}" && \
    pip install "apache-airflow-providers-cncf-kubernetes" --constraint "${CONSTRAINT_URL}"

# Create Airflow folders
RUN mkdir -p $AIRFLOW_HOME/dags $AIRFLOW_HOME/logs $AIRFLOW_HOME/plugins

# Copy project files (optional — if DAGs exist)
COPY . .

# Expose Airflow and Jupyter ports
EXPOSE 8080 8888

# Default command to initialize and launch Airflow
CMD ["bash", "-c", "airflow db init && airflow scheduler & airflow webserver"]










