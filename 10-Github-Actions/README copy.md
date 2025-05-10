# Coffee Shop API

A simple FastAPI application that simulates a coffee shop ordering system. This API allows users to place drink orders and receive confirmation details.

## Features

- Welcome endpoint to greet users
- Order placement endpoint with drink and size specifications
- Automatic ETA calculation for orders
- Input validation using Pydantic models

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd 8-FastAPI
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

To start the application, run:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### 1. Welcome Message
- **URL**: `/`
- **Method**: GET
- **Response**: 
```json
{
    "message": "Welcome to Coffee Shop API, how can I help you today?"
}
```

### 2. Place Order
- **URL**: `/order`
- **Method**: POST
- **Request Body**:
```json
{
    "drink": "string",
    "size": "string"
}
```
- **Response**:
```json
{
    "status": "confirmed",
    "drink": "string",
    "size": "string",
    "eta": "5 minutes"
}
```

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## Example Usage

Using curl:
```bash
# Get welcome message
curl http://localhost:8000/

# Place an order
curl -X POST http://localhost:8000/order \
  -H "Content-Type: application/json" \
  -d '{"drink": "latte", "size": "medium"}'
```

Using Python requests:
```python
import requests

# Get welcome message
response = requests.get("http://localhost:8000/")
print(response.json())

# Place an order
order_data = {
    "drink": "latte",
    "size": "medium"
}
response = requests.post("http://localhost:8000/order", json=order_data)
print(response.json())
```

## Project Structure

```
8-FastAPI/
├── main.py          # Main application file
└── README.md        # This documentation file
```

# Demo -2

```
docker build -t salary-fastapi .
docker run -p 8000:8000 salary-fastapi
```