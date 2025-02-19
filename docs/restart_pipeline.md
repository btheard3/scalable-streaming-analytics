Steps to Restart the Data Pipeline

1️⃣ Activate Google Cloud SDK & Authenticate
If your Google Cloud CLI session has expired, re-authenticate:

bash
gcloud auth login
gcloud config set project scalable-streaming-analytics

2️⃣ Ensure Google Cloud Storage Has Required Files
Check if the schema.json and input files exist in your Google Cloud Storage (GCS) bucket:

bash
gsutil ls gs://scalable-streaming-bucket-bthea/

If missing, re-upload:

bash
gsutil cp path/to/schema.json gs://scalable-streaming-bucket-bthea/
gsutil cp path/to/input/\* gs://scalable-streaming-bucket-bthea/input/

3️⃣ Restart the Google Cloud Dataflow Job
If the Dataflow job is stopped or needs to be restarted:

Restart from Cloud Console:
Go to Google Cloud Console
Navigate to Dataflow > Jobs
Find the job "stream-gcs-to-bq-job-001"
If stopped, click Restart
If running, click Stop first, then Start Again

4️⃣ Verify the Data is Flowing into BigQuery
Run a simple query in BigQuery to check incoming data:

sql
SELECT \* FROM `scalable-streaming-analytics.streaming_data.events`
ORDER BY timestamp DESC
LIMIT 10;

If no new data appears, check the Dataflow job logs for errors.
