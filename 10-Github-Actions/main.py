from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class OrderRequest(BaseModel):
    drink: str
    size: str

@app.get("/")
def welcome_message():
    return {"message": "Welcome to Coffee Shop API, how can I help you today?"}

@app.post("/order")
def place_order(order: OrderRequest):
    return {
        "status": "confirmed",
        "drink": order.drink,
        "size": order.size,
        "eta": "5 minutes"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)