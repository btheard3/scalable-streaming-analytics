import subprocess
import os

PROJECT_ID = "scalable-streaming-analytics"
REGION = "us-central1"
BUCKET = "dataflow-staging-us-central1-1013083167773"
PY_FILE = "dataflow/dataflow_pipeline.py"  # Adjust if it's named differently

def run_dataflow_pipeline():
    input_topic = "projects/scalable-streaming-analytics/topics/streaming-events"

    command = [
        "python", PY_FILE,
        f"--project={PROJECT_ID}",
        f"--region={REGION}",
        f"--runner=DataflowRunner",
        f"--temp_location=gs://{BUCKET}/temp",
        f"--staging_location=gs://{BUCKET}/staging",
        f"--input_topic={input_topic}",
        "--streaming"
    ]

    print("[INFO] Launching pipeline with command:")
    print(" ".join(command))
    subprocess.run(command, check=True)


if __name__ == "__main__":
    run_dataflow_pipeline()
