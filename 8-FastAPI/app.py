from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import uvicorn

model = pickle.load(open("models/model.pkl","rb"))

app = FastAPI()

@app.get("/")
def welcome_message():
    return {"message": "Welcome to Salary Prediction API, how can I help you today?"}

class SalaryRequest(BaseModel):
    age: int

@app.post("/predict")
def predict_salary(data: SalaryRequest):
    prediction = model.predict([[data.age]])[0]*1000
    return {
        "predicted_salary": prediction
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
