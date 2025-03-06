from airflow import DAG
from airflow.operators.python import PythonOperator  # Corrected import
from datetime import datetime
import random

def simulate_data_ingestion():
    data = {"timestamp": datetime.now().isoformat(), "value": random.randint(1, 100)}
    print(f"Simulated data: {data}")

with DAG(
    "data_ingestion_dag",
    default_args={"start_date": datetime(2025, 3, 2)},
    schedule="*/5 * * * *",  # Corrected parameter
    catchup=False
) as dag:

    ingest_task = PythonOperator(
        task_id="simulate_ingestion",
        python_callable=simulate_data_ingestion
    )

ingest_task