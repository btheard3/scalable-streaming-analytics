from datetime import datetime, timedelta
from airflow import models
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with models.DAG(
    dag_id="trigger_dataflow_job",
    default_args=default_args,
    schedule_interval=None,  # Set to desired cron string if needed
    catchup=False,
    tags=["dataflow", "gcp"],
) as dag:

    start_dataflow = DataflowTemplatedJobStartOperator(
        task_id="start_dataflow",
        project_id="scalable-streaming-analytics",
        location="us-central1",
        template="gs://scalable-streaming-analytics-dataflow/templates/dataflow_template",
        parameters={},  # Add parameters if required by your template
        gcp_conn_id="google_cloud_default",
    )
