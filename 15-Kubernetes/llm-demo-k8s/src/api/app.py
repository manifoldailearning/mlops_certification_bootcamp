from dotenv import load_dotenv
import os
from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel
import sys
from pathlib import Path
import logging
import uvicorn

# Load environment variables from .env file
load_dotenv()

project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.models.lora_inference import LoRAInference

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="LoRA Inference API", version="1.0.0")

model = None # Global Variable for the model

class GenerationRequest(BaseModel):
    prompt: str
    max_length: Optional[int] = int(os.getenv("DEFAULT_MAX_LENGTH", 512))
    temperature: Optional[float] = float(os.getenv("DEFAULT_TEMPERATURE", 0.7))
    top_p: Optional[float] = float(os.getenv("DEFAULT_TOP_P", 0.7))
    num_return_sequences: Optional[int] = int(os.getenv("DEFAULT_NUM_RETURN_SEQUENCES", 1))

class GenerationResponse(BaseModel):
    generated_text: str

@app.on_event("startup")
def startup_event():
    global model
    model_path = os.getenv("BASE_MODEL_PATH")
    if not model_path:
        logger.error("MODEL_PATH environment variable is not set.")
        raise ValueError("MODEL_PATH environment variable is not set.")
    adapter_path = os.getenv("ADAPTER_MODEL_PATH")
    logger.info(f"Loading model from {model_path}")
    model = LoRAInference(
        base_model_name=model_path,
        adapter_path=adapter_path
    )
    logger.info("Model loaded successfully.")

@app.post("/generate", response_model=GenerationResponse)
def generate_text(request: GenerationRequest):
    global model
    if model is None:
        logger.error("Model is not loaded.")
        raise RuntimeError("Model is not loaded.")
    
    logger.info(f"Generating text for prompt: {request.prompt}")
    generated_text = model.generate(
        prompt=request.prompt,
        max_length=request.max_length,
        temperature=request.temperature,
        top_p=request.top_p,
        num_return_sequences=request.num_return_sequences
    )
    
    logger.info("Text generation completed.")
    return GenerationResponse(generated_text=generated_text)

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

if __name__ == "__main__":
    port = int(os.getenv("API_PORT", 8000))
    logger.info(f"Starting FastAPI server on port {port}")
    host = os.getenv("API_HOST")
    uvicorn.run(app, host=host, port=port)
# To run the server, use the command:
# uvicorn src.api.app:app --host