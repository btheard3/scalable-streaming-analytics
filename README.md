#📌 Scalable Streaming Analytics Project

🎯 Project Overview
This project builds a real-time data pipeline that ingests, processes, and analyzes streaming events using Google Cloud Dataflow, BigQuery, and Machine Learning models. The goal is to generate insights from live event data, optimize feature selection, and train predictive models.

Additionally, Apache Airflow is used to orchestrate the pipeline.

## 📂 Project Structure

```
/scalable-streaming-analytics
    ├── airflow/                     # Airflow DAGs & Config
    │   ├── dags/
    │   │   ├── data_ingestion_dag.py   # Ingests streaming data
    │   │   ├── model_training_dag.py   # Trains ML models
    │   │   ├── feature_engineering_dag.py  # Feature processing
    │   ├── airflow.cfg               # Airflow configuration
    ├── notebooks/                 # Jupyter Notebooks
    │   ├── 01_data_preprocessing.ipynb
    │   ├── 02_eda.ipynb
    │   ├── 03_feature_engineering.ipynb
    │   ├── 04_model_training.ipynb
    │   ├── 05_model_evaluation.ipynb
    ├── scripts/                    # Additional Python scripts
    ├── restart_pipeline.md          # Steps to restart Airflow & pipeline
    ├── setup_pipeline.md            # Steps to configure the full pipeline
    ├── requirements.txt              # Python dependencies
    ├── .gitignore
    ├── README.md

```

## 🚀 Steps to Set Up the Project

### **1️⃣ Environment Setup**

Ensure you have the following dependencies installed:

```bash
pip install -r requirements.txt
```

### **2️⃣ Start the Jupyter Notebook**

```bash
jupyter notebook
```

### **3️⃣ Data Pipeline Setup**

Follow the instructions in `setup_pipeline.md` to configure Google Cloud Storage, Dataflow, and BigQuery.

### **4️⃣ Run the Notebooks in Order**

1. **Data Preprocessing (`01_data_preprocessing.ipynb`)**

   - Load raw data from Google Cloud Storage
   - Handle missing values, duplicates, and formatting
   - Save cleaned dataset

2. **Exploratory Data Analysis (`02_eda.ipynb`)**

   - Summary statistics, visualizations, correlation heatmaps
   - Identify key trends and outliers

3. **Feature Engineering (`03_feature_engineering.ipynb`)**

   - Feature selection and new feature creation
   - Encoding categorical variables and scaling numerical data

4. **Model Training (`04_model_training.ipynb`)**

   - Train multiple models and perform hyperparameter tuning
   - Save best-performing model

5. **Model Evaluation (`05_model_evaluation.ipynb`)**
   - Compare model performance
   - Generate feature importance charts and validation metrics

### **5️⃣ Restarting the Data Pipeline**

Refer to `restart_pipeline.md` for step-by-step instructions on restarting the pipeline.

## 📌 Additional Notes

- Use `restart_pipeline.md` if the pipeline needs to be restarted after stopping.
- Update `.gitignore` to prevent committing large files (datasets, models, etc.).

🚀 1️⃣ Setup Instructions
1️⃣ Install Dependencies
Ensure you have the required Python packages installed:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Set Up & Start Apache Airflow
Apache Airflow is used for orchestration of data pipelines.

🔹 Initializing Airflow
Run the following only the first time to initialize the Airflow database:

bash
Copy
Edit
export AIRFLOW_HOME=$(pwd)/airflow
airflow db init
🔹 Start Airflow Webserver & Scheduler
To start the Airflow UI (on localhost:8080) and run DAGs, use:

bash
Copy
Edit
cd ~/scalable-streaming-analytics
source venv/bin/activate # Activate virtual environment

airflow webserver --port 8080 &
airflow scheduler &
Then visit http://localhost:8080.

📌 2️⃣ Streaming Data Pipeline
DAG: data_ingestion_dag.py
📌 Purpose: Simulates a real-time data ingestion pipeline.

How to Manually Run This DAG
Open Airflow UI (localhost:8080)
Find data_ingestion_dag
Click ▶ (Trigger DAG)
View logs:
bash
Copy
Edit
airflow tasks logs data_ingestion_dag simulate_ingestion

3️⃣ Machine Learning Pipeline
Steps
Preprocess Data (01_data_preprocessing.ipynb)
Perform EDA (02_eda.ipynb)
Feature Engineering (03_feature_engineering.ipynb)
Train Model (04_model_training.ipynb)
Evaluate Model (05_model_evaluation.ipynb)
Run the Jupyter Notebook
bash
Copy
Edit
jupyter notebook
🔄 4️⃣ Restarting the Pipeline
If the pipeline crashes or is stopped:

bash
Copy
Edit
pkill -f "airflow"
source venv/bin/activate
airflow db init
airflow webserver --port 8080 &
airflow scheduler &
