FROM python:3.11-slim

WORKDIR /app

#install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    python3-pip \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

ENV PYTHONPATH=/app
ENV BASE_MODEL_PATH=facebook/opt-350m
ENV ADAPTER_MODEL_PATH=/app/output/final_model

EXPOSE 8000
CMD ["python", "./src/api/app.py"]