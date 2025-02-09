from google.cloud import pubsub_v1
import os

# Set authentication credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/gcp-key.json"

# Replace with your actual GCP Project ID and Subscription ID
PROJECT_ID = "scalable-streaming-analytics"
SUBSCRIPTION_ID = "streaming-events-sub"

# Initialize Pub/Sub Subscriber Client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def callback(message):
    """Callback function to process received messages."""
    print(f"✅ Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message so it doesn't reappear

# Ensure the subscriber listens indefinitely
with subscriber:
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"📡 Listening for messages on {SUBSCRIPTION_ID}...")

    try:
        streaming_pull_future.result()  # Keeps the subscriber running
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
