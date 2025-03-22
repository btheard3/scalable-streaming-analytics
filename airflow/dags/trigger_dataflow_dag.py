from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    'trigger_dataflow_job',
    default_args=default_args,
    schedule_interval='@hourly',  # Run hourly or adjust as needed
    catchup=False,
) as dag:

   start_dataflow_job = DataflowTemplatedJobStartOperator(
    task_id="start_dataflow",
    project_id="scalable-streaming-analytics",
    location="us-central1",
    job_name="airflow-triggered-dataflow",
    template="gs://scalable-streaming-analytics-dataflow/templates/dataflow_template",
    parameters={
        "input": "gs://scalable-streaming-analytics-dataflow/input/input-data.csv",
        "output": "scalable-streaming-analytics:streaming_data.events"  # Replace with your actual table name
    },
    gcp_conn_id="google_cloud_default"
)



start_dataflow_job
