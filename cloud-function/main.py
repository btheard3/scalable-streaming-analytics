from google.cloud import bigquery
import base64
import json
import os

# Initialize BigQuery client
client = bigquery.Client()

def pubsub_to_bigquery(event, context):
    dataset_id = "streaming_data"
    table_id = "events"

    # Decode Pub/Sub message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message_data = json.loads(pubsub_message)

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    errors = client.insert_rows_json(table, [message_data])
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print("Inserted rows successfully.")

# [END functions_pubsub_to_bigquery