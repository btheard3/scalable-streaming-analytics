from google.cloud import bigquery

# GCP Configuration
PROJECT_ID = "scalable-streaming-analytics"
DATASET_ID = "streaming_data"
RAW_TABLE_ID = "events"
PROCESSED_TABLE_ID = "processed_events"

# Initialize BigQuery Client
client = bigquery.Client()

def extract():
    """Extract transformed data from BigQuery."""
    query = f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{RAW_TABLE_ID}`"
    query_job = client.query(query)
    return query_job.result()

def transform(rows):
    """Transform extracted data."""
    transformed_data = []
    for row in rows:
        transformed_data.append({
            "user_id": row.user_id,
            "event": row.event.upper(),  # Example transformation: Convert event to uppercase
            "content_id": row.content_id,
            "timestamp": row.timestamp
        })
    return transformed_data

def load(transformed_data):
    """Load processed data into BigQuery."""
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{PROCESSED_TABLE_ID}"
    errors = client.insert_rows_json(table_ref, transformed_data)
    if errors:
        print(f"BigQuery Insert Errors: {errors}")
    else:
        print(f"Successfully inserted processed data into {PROCESSED_TABLE_ID}")

# Run the ETL pipeline
if __name__ == "__main__":
    extracted_data = extract()
    transformed_data = transform(extracted_data)
    load(transformed_data)
