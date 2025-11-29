# Use official Python image
FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Copy application files
COPY app.py .
COPY requirements.txt .
COPY clean_netflix.csv .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
