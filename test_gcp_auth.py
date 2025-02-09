from google.cloud import pubsub_v1
import os

# Set authentication credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/gcp-key.json"

project_id = "scalable-streaming-analytics"

try:
    publisher = pubsub_v1.PublisherClient()
    print(f"✅ Authentication successful! Connected to GCP Project: {project_id}")
except Exception as e:
    print(f"❌ Authentication failed: {e}")
