from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import random

def simulate_data_ingestion():
    data = {"timestamp": datetime.now().isoformat(), "value": random.randint(1, 100)}
    print(f"Simulated data: {data}")

with DAG(
    "data_ingestion_dag",
    default_args={"start_date": datetime(2025, 3, 2)},
    schedule_interval="*/5 * * * *",  # Runs every 5 minutes
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="simulate_ingestion",
        python_callable=simulate_data_ingestion
    )
