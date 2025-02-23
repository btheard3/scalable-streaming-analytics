# Use official Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files from the correct path
COPY scripts/api/app.py /app/  # Ensure app.py is placed inside /app/
COPY models/logistic_regression_tuned.pkl /app/  # Place model in /app/
COPY scripts/api/requirements.txt /app/  # Ensure requirements.txt is copied

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose API port
EXPOSE 8080

# Run the Flask API using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]


