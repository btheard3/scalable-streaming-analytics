# cloud-function/main.py

from flask import jsonify
from googleapiclient.discovery import build
import google.auth

PROJECT_ID = "scalable-streaming-analytics"
REGION = "us-central1"
TEMPLATE_GCS_PATH = "gs://dataflow-staging-us-central1-1013083167773/templates/streaming_pipeline_template"
SERVICE_ACCOUNT_EMAIL = "pubsub-service-account@scalable-streaming-analytics.iam.gserviceaccount.com"

def trigger_pipeline(request):
    try:
        credentials, _ = google.auth.default()
        dataflow = build("dataflow", "v1b3", credentials=credentials)

        job = {
            "jobName": "streaming-pipeline-run",
            "parameters": {
                "input_topic": f"projects/{PROJECT_ID}/topics/streaming-events-topic",
                "output_table": f"{PROJECT_ID}:streaming_dataset.streaming_events"
            },
            "environment": {
                "tempLocation": "gs://dataflow-staging-us-central1-1013083167773/temp",
                "serviceAccountEmail": SERVICE_ACCOUNT_EMAIL
            }
        }

        result = dataflow.projects().locations().templates().launch(
            projectId=PROJECT_ID,
            location=REGION,
            gcsPath=TEMPLATE_GCS_PATH,
            body=job
        ).execute()

        return jsonify({"message": "Pipeline triggered", "result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
