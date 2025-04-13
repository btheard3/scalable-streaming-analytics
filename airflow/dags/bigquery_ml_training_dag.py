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
                    OPTIONS(model_type='logistic_reg') AS
                    SELECT 
                        user_id, 
                        content_id, 
                        CASE 
                            WHEN event = 'like' THEN 1
                            WHEN event = 'watch' THEN 0
                        END AS label  -- Explicitly defining the label column
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

