# API endpoint testing
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_endpoint_valid():
    response = client.post("/predict", json={"sepal_length": 5.1})
    assert response.status_code == 200
    assert response.json()["prediction"]  in ["setosa", "versicolor", "virginica"]
    
def test_predict_endpoint_invalid():
    response = client.post("/predict", json={"sepal_length": "invalid"})
    assert response.status_code == 422
    
    
    
    
    