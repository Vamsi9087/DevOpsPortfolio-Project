FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (if needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

# Run app using python (NOT flask run)
CMD ["python", "app.py"]
