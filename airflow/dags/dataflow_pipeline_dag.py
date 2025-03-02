from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from datetime import datetime, timedelta

# Set default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    'dataflow_streaming_pipeline',
    default_args=default_args,
    description='Run Google Dataflow Streaming Job from Airflow',
    schedule_interval='@hourly',  # Runs every hour
    catchup=False,
)

# Define Dataflow job
dataflow_task = DataflowTemplatedJobStartOperator(
    task_id='run_dataflow_job',
    template='gs://dataflow-templates/latest/Stream_GCS_to_BigQuery',
    parameters={
        'inputFilePattern': 'gs://scalable-streaming-bucket-bthea/input/*.json',
        'outputTable': 'scalable-streaming-analytics:streaming_data.events',
        'bigQuerySchema': 'gs://scalable-streaming-bucket-bthea/schema.json'
    },
    location='us-central1',
    project_id='scalable-streaming-analytics',
    dag=dag,
)

dataflow_task
