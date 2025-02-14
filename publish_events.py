from google.cloud import pubsub_v1
import json
import time
import random

# Set up Pub/Sub publisher
PROJECT_ID = "scalable-streaming-analytics"
TOPIC_ID = "streaming-events-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# Function to publish random events
def publish_event():
    user_id = random.randint(1, 100)
    events = ["watch", "like", "share", "subscribe"]
    event = random.choice(events)
    content_id = f"content_{random.randint(1, 50)}"
    timestamp = time.time()

    message = {
        "user_id": user_id,
        "event": event,
        "content_id": content_id,
        "timestamp": timestamp
    }

    # Convert to JSON & publish message
    future = publisher.publish(topic_path, json.dumps(message).encode("utf-8"))
    print(f"Published event: {message} | Message ID: {future.result()}")

# Simulate streaming by publishing messages every 2 seconds
while True:
    publish_event()
    time.sleep(2)  # Adjust timing as needed
