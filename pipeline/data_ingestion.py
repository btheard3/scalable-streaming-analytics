from google.cloud import pubsub_v1
import json

# GCP Configuration
PROJECT_ID = "scalable-streaming-analytics"
SUBSCRIPTION_ID = "streaming-events-topic-sub"  # Replace with your actual subscription

def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message

def listen_for_messages():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...\n")

    try:
        streaming_pull_future.result()  # Keep listening
    except KeyboardInterrupt:
        streaming_pull_future.cancel()  # Stop listening

if __name__ == "__main__":
    listen_for_messages()
