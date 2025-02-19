# 📌 Scalable Streaming Analytics Project

## 🎯 Project Overview

This project aims to build a **real-time data pipeline** that ingests, processes, and analyzes streaming events using **Google Cloud Dataflow**, **BigQuery**, and **Machine Learning models**. The goal is to generate insights from live event data, optimize feature selection, and train predictive models.

## 📂 Project Structure

```
/scalable-streaming-analytics
    ├── notebooks/
    │   ├── 01_data_preprocessing.ipynb
    │   ├── 02_eda.ipynb
    │   ├── 03_feature_engineering.ipynb
    │   ├── 04_model_training.ipynb
    │   ├── 05_model_evaluation.ipynb
    ├── data/ (ignored in .gitignore)
    ├── models/ (ignored in .gitignore)
    ├── scripts/
    ├── restart_pipeline.md
    ├── setup_pipeline.md
    ├── requirements.txt
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

**Next Steps:** ✅ Begin working on `01_data_preprocessing.ipynb`. 🎯
