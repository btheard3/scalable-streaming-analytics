from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.utils.dates import days_ago
from datetime import datetime

with DAG("bigquery_ml_training",
        schedule_interval="0 12 * * 1",  # Runs weekly on Mondays
        start_date=datetime(2025, 3, 10),
        catchup=False) as dag:

    train_model = BigQueryInsertJobOperator(
        task_id="train_bigquery_model",
        configuration={
            "query": {
                "query": """
                    CREATE OR REPLACE MODEL `scalable-streaming-analytics.streaming_data.user_behavior_model`
                    OPTIONS(
                        model_type='logistic_reg',
                        input_label_cols=['event']  -- Explicitly defining the label column
                    ) AS
                    SELECT 
                        user_id, 
                        content_id, 
                        event 
                    FROM `scalable-streaming-analytics.streaming_data.events`
                    WHERE event IN ('like', 'watch');
                """,
                "useLegacySql": False
            }
        },
        location="US",  # Ensure correct location
        gcp_conn_id="google_cloud_default",
        dag=dag,
    )
