from google.cloud import pubsub_v1
import os

# Set authentication credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/gcp-key.json"

# Replace with your actual GCP Project ID and Subscription ID
PROJECT_ID = "scalable-streaming-analytics"  # Update this
SUBSCRIPTION_ID = "streaming-events-sub"  # Ensure this matches your Pub/Sub subscription name

# Initialize Pub/Sub Subscriber Client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

def callback(message):
    """Callback function to process received messages."""
    print(f"✅ Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge message to remove it from the queue

print(f"📡 Listening for messages on {SUBSCRIPTION_ID}...")
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

try:
    streaming_pull_future.result()  # Blocks indefinitely to listen for messages
except KeyboardInterrupt:
    streaming_pull_future.cancel()
