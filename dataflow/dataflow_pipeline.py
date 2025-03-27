import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json
import logging

# Define input Pub/Sub topic
TOPIC = "projects/scalable-streaming-analytics/topics/streaming-events-topic"

# Define BigQuery output table
BQ_TABLE = "scalable-streaming-analytics.streaming_data.processed_events"

class ParseEventFn(beam.DoFn):
    def process(self, element):
        try:
            data = json.loads(element.decode('utf-8'))
            yield {
                "user_id": data.get("user_id"),
                "event": data.get("event"),
                "content_id": data.get("content_id"),
                "timestamp": data.get("timestamp")
            }
        except Exception as e:
            logging.error(f"Failed to process element: {element} | Error: {e}")


def run():
    """Runs the Apache Beam pipeline."""
    pipeline_options = PipelineOptions(
        streaming=True,  # Enables streaming mode
        project="scalable-streaming-analytics",
        region="us-central1",
        temp_location="gs://scalable-streaming-analytics-dataflow/tmp",
        runner="DataflowRunner"
    )

    with beam.Pipeline(options=pipeline_options) as p:
        (
            p
            | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=TOPIC)
            | "Parse JSON" >> beam.ParDo(ParseEventFn())
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                BQ_TABLE,
                schema="user_id:STRING, content_id:STRING, event_type:STRING, event_time:TIMESTAMP",
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == "__main__":
    run()
