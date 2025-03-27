# publisher.py
import json
import time
import random
from google.cloud import pubsub_v1

# --- CONFIGURATION ---
PROJECT_ID = "scalable-streaming-analytics"
TOPIC_ID = "streaming-events-topic"  # Confirm this matches your Dataflow input topic
NUM_MESSAGES = 20  # Number of events to send
DELAY_BETWEEN_MESSAGES = 1  # seconds

# --- Initialize Publisher ---
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

# --- Function to generate a fake event ---
def generate_event():
    return {
        "user_id": random.randint(1, 100),
        "event": random.choice(["watch", "like", "share", "click"]),
        "content_id": f"content_{random.randint(1, 50)}",
        "timestamp": time.time()  # current Unix timestamp in seconds
    }

# --- Publish Events ---
def publish_events():
    print(f"\nPublishing {NUM_MESSAGES} messages to topic '{TOPIC_ID}'...\n")

    for i in range(NUM_MESSAGES):
        event = generate_event()
        data = json.dumps(event).encode("utf-8")

        # Publish message
        future = publisher.publish(topic_path, data)
        message_id = future.result()

        print(f"[{i+1}] Published: {event} -> msg_id: {message_id}")
        time.sleep(DELAY_BETWEEN_MESSAGES)

    print("\n✅ All events published.\n")

# --- Entry point ---
if __name__ == "__main__":
    publish_events()
