# Initial Project Setup

📁 Create Folder & File Structure

bash
mkdir scalable-streaming-analytics
cd scalable-streaming-analytics

## Create subfolders

mkdir data notebooks scripts docs

### Create essential files

touch README.md .gitignore docs/setup_pipeline.md docs/restart_pipeline.md

Initialize Git Repository
bash
git init
git add .
git commit -m "Initial commit - project structure"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main

## Setting Up Google Cloud Environment

🔹 Create a Google Cloud Project
Open Google Cloud Console
Navigate to IAM & Admin > Manage Resources
Click Create Project and name it scalable-streaming-analytics
Set up billing & permissions

🔹 Enable Required APIs
bash
gcloud services enable compute.googleapis.com
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable dataflow.googleapis.com

🔹 Set Up Google Cloud Storage (GCS) Bucket
bash
gsutil mb -c STANDARD -l us-central1 gs://scalable-streaming-bucket-bthea/
(Stored schema.json and raw data input files in this bucket)

🔹 Set Up BigQuery Dataset & Table
bash
bq mk --dataset scalable-streaming-analytics:streaming_data
Created tables:

events
events_distribution
events_with_time

### Implementing the Streaming Data Pipeline

🔹 Creating the Schema File (schema.json)
We defined a BigQuery schema for ingestion using a JSON file:

json
[
{"name": "user_id", "type": "INTEGER"},
{"name": "event", "type": "STRING"},
{"name": "content_id", "type": "STRING"},
{"name": "timestamp", "type": "TIMESTAMP"}
]

Uploaded to GCS Bucket:

bash
gsutil cp schema.json gs://scalable-streaming-bucket-bthea/schema.json

🔹 Deploying the Dataflow Job
Used Google Cloud Dataflow to stream data from GCS → BigQuery:

bash
gcloud dataflow jobs run stream-gcs-to-bq-job-001 \
 --gcs-location gs://dataflow-templates/latest/Stream_GCS_to_BigQuery \
 --parameters inputFilePattern=gs://scalable-streaming-bucket-bthea/input/\*.json,\
 outputTable=scalable-streaming-analytics:streaming_data.events,\
 bigQuerySchema=gs://scalable-streaming-bucket-bthea/schema.json

Checked data ingestion in BigQuery using:

sql
SELECT \* FROM `scalable-streaming-analytics.streaming_data.events`
LIMIT 10;

### Data Processing & Analysis

🔹 Jupyter Notebook for EDA
Set up Python virtual environment:

bash
python -m venv venv
source venv/bin/activate # Mac/Linux
venv\Scripts\activate # Windows
pip install jupyter pandas google-cloud-bigquery

Connected Jupyter Notebook to BigQuery
Performed Exploratory Data Analysis (EDA)
Checked data quality
Analyzed event distribution
Created visualizations

### .gitignore File for This Project

Create or edit .gitignore and add the following:

gitignore

## Ignore virtual environment

venv/
.env
\*.env

## Ignore Python cache files

**pycache**/
_.pyc
_.pyo
\*.pyd

## Ignore Jupyter Notebook checkpoints

.ipynb_checkpoints/

## Ignore data files (optional, keep raw datasets if needed)

data/
_.csv
_.json
_.parquet
_.db
\*.sqlite

## Ignore logs & temporary files

logs/
_.log
_.out
_.err
_.pid

## Ignore cloud storage authentication files

google*credentials.json
*.key.json
\_.pem

## Ignore compiled files

_.so
_.o
_.a
_.dll
_.dylib
_.lib

## Ignore editor/IDE-specific files

.vscode/
.idea/
.DS_Store

## Ignore dependencies

pip-log.txt
pip-delete-this-directory.txt
node_modules/

### Ignore output files from experiments or ML models

models/
_.h5
_.pkl
_.ckpt
_.onnx

## Ignore Docker, if using

docker-compose.override.yml
.envrc
