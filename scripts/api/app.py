import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

# Load the trained model
model = joblib.load("../models/logistic_regression_tuned.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to make predictions on incoming JSON data.
    """
    try:
        # Parse JSON input
        input_data = request.get_json()
        df = pd.DataFrame(input_data)

        # Ensure correct features
        expected_features = ['hour_of_day', 'day_of_week', 'is_weekend', 'user_event_count',
                             'unique_content_count', 'avg_time_between_interactions',
                             'content_interaction_count', 'content_share_ratio', 'session_id', 'session_length']
        
        if not all(feature in df.columns for feature in expected_features):
            return jsonify({'error': 'Missing required features'}), 400

        # Make predictions
        prediction = model.predict(df)
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
