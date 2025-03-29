import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json
import argparse
from apache_beam.options.pipeline_options import StandardOptions

# Define Pub/Sub topic
TOPIC = "projects/scalable-streaming-analytics/topics/streaming-events-topic"


# Define BigQuery output table
BQ_TABLE = "scalable-streaming-analytics.streaming_data.processed_events"

class ParseEventFn(beam.DoFn):
    """Parses incoming Pub/Sub messages."""
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
            print(f"Failed to parse message: {element} | Error: {e}")

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_topic', required=True)
    args, pipeline_args = parser.parse_known_args()

    options = PipelineOptions(pipeline_args)
    standard_options = options.view_as(StandardOptions)
    standard_options.streaming = True


    p = beam.Pipeline(options=options)

    # Use the input_topic from parsed args
    topic_path = args.input_topic

    (
        p
        | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=topic_path)
        | "Parse events" >> beam.ParDo(ParseEventFn())
        | "Write to BigQuery" >> beam.io.WriteToBigQuery(
            BQ_TABLE,
            schema={
                "fields": [
                    {"name": "user_id", "type": "INTEGER", "mode": "NULLABLE"},
                    {"name": "event", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "content_id", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "timestamp", "type": "FLOAT", "mode": "NULLABLE"},
                ]
            },
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        )
    )

    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
