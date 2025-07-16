# Use a Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy script and requirements
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "consumer.py"]
