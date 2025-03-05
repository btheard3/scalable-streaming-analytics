from google.cloud import bigquery
import json
import os
from datetime import datetime

# GCP Configuration
PROJECT_ID = "scalable-streaming-analytics"
DATASET_ID = "streaming_data"
TABLE_ID = "events"

# Authenticate with GCP
client = bigquery.Client()

def transform_data(message):
    """Transform raw Pub/Sub message into structured format for BigQuery."""
    try:
        # Decode and parse JSON
        data = json.loads(message)

        # Convert user_id to integer
        data["user_id"] = int(data["user_id"])

        # Keep timestamp as float (Unix format) for BigQuery TIMESTAMP compatibility
        data["timestamp"] = float(data["timestamp"])

        return data
    except Exception as e:
        print(f"Error in data transformation: {e}")
        return None

def write_to_bigquery(data):
    """Write transformed data to BigQuery table."""
    if not data:
        return

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    errors = client.insert_rows_json(table_ref, [data])  # Insert row
    if errors:
        print(f"BigQuery Insert Errors: {errors}")
    else:
        print(f"Successfully inserted data: {data}")

# Test transformation logic
if __name__ == "__main__":
    # Simulated incoming message from Pub/Sub
    raw_message = json.dumps({
        "user_id": "12345",
        "event": "play",
        "content_id": "video_001",
        "timestamp": 17000000.0  # Example Unix timestamp
    })

    transformed_data = transform_data(raw_message)
    if transformed_data:
        print("Transformed Data:", transformed_data)
        write_to_bigquery(transformed_data)
