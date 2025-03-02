import joblib
import os
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

# Get absolute path to models directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets the scripts/api directory
ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))  # Moves up TWO levels to scalable-streaming-analytics/
MODEL_PATH = os.path.join(ROOT_DIR, "models", "logistic_regression_tuned.pkl")

# Debugging: Print the path to verify
print(f"Looking for model at: {MODEL_PATH}")

# Load the trained model
model = joblib.load(MODEL_PATH)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask API is running"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON input
        input_data = request.get_json()
        if not input_data or "features" not in input_data:
            return jsonify({"error": "Invalid input format. Expected {'features': [values]}"}), 400

        # Convert JSON to Pandas DataFrame
        df = pd.DataFrame(input_data["features"])

        # Debugging: Print the received input shape
        print("Received input shape:", df.shape)

        # Ensure input shape matches the model's expected features
        if df.shape[1] != model.n_features_in_:
            return jsonify({"error": f"Expected {model.n_features_in_} features, but got {df.shape[1]}"}), 400

        # Make prediction
        prediction = model.predict(df).tolist()

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    print("Starting Flask API...")
    app.run(debug=True, host="0.0.0.0", port=5000)


