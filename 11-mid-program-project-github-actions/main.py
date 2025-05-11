from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import uvicorn

from fastapi.middleware.cors import CORSMiddleware # <--- Import this

app = FastAPI()

# --- CORS Configuration ---
# Define the origins allowed to make requests.
# For development, you can allow all origins with "*"
# For production, you should restrict this to your frontend's actual domain.
origins = [
    "http://localhost",  # If you serve your frontend locally via a web server on a port
    "http://127.0.0.1", # Common alias for localhost
    "null",             # Important for 'file://' origins (when opening HTML directly)
    "http://localhost:8080",
    "http://localhost:8080",    # Origin of your Nginx frontend (ui-1)
    "http://127.0.0.1:8080",  # Alternative for localhost
    "http://0.0.0.0:8080",    # If you ever use this directly in a browser that supports it for origin                  # For 'file://' origins (less relevant in Docker but good for local dev)
    # Add any other specific origins if needed, e.g., http://localhost:3000 if using a dev server for frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins or ["*"] for all
    allow_credentials=True, # Allows cookies to be included in requests (if applicable)
    allow_methods=["*"],    # Allows all methods (GET, POST, OPTIONS, etc.) or specify like ["GET", "POST"]
    allow_headers=["*"],    # Allows all headers or specify like ["Content-Type"]
)
# --- End CORS Configuration ---
print(f"os.path.dirname(__file__): {os.path.dirname(__file__)}")
model_path = os.path.join(os.path.dirname(__file__), 'model/model.joblib')
model = joblib.load(model_path)

class Iris(BaseModel):
    sepal_length: float

@app.post("/predict")
def predict(data: Iris):
    prediction = model.predict([[data.sepal_length]])
    if prediction[0] == 0:
        return {"prediction": "setosa"}
    elif prediction[0] == 1:
        return {"prediction": "versicolor"}
    else:
        return {"prediction": "virginica"}
  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    