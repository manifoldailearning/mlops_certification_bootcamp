FROM python:3.11


# Create app directory
WORKDIR /app

# Copy code first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

EXPOSE 7860

# Default command
CMD ["python", "app.py"]