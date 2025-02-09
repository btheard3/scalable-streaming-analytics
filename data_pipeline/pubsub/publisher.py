from google.cloud import pubsub_v1
import json
import time
import os

# Set authentication credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/gcp-key.json"

# Define Google Cloud Pub/Sub settings
PROJECT_ID = "scalable-streaming-analytics"  # Replace with your actual GCP project ID
TOPIC_ID = "streaming-events-topic"  # Ensure this matches your Pub/Sub topic name

# Initialize Pub/Sub Publisher Client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_messages():
    """Publishes messages to Pub/Sub."""
    for i in range(10):  # Simulate sending 10 messages
        message_data = {
            "user_id": i + 1,
            "event": "watch",
            "content_id": f"content_{i+1}",
            "timestamp": time.time()
        }
        message_json = json.dumps(message_data)
        message_bytes = message_json.encode("utf-8")

        # Publish message
        future = publisher.publish(topic_path, message_bytes)
        print(f"✅ Published: {message_json}")

        time.sleep(1)  # Simulate real-time events

if __name__ == "__main__":
    publish_messages()
