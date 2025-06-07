import os
import torch
import sys 
import logging
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
import argparse
from src.models.lora_inference import LoRAInference

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="LoRA Inference Script")
    parser.add_argument("--model_path", type=str, required=True, help="Base model name or path")
    parser.add_argument("--adapter_path", type=str, required=True,
                      help="Path to the LoRA adapter")
    parser.add_argument("--prompt", type=str, required=True,
                      help="Input prompt for generation")
    parser.add_argument("--max_length", type=int, default=512,
                      help="Maximum length of generated text")
    parser.add_argument("--temperature", type=float, default=0.7,
                      help="Sampling temperature")
    parser.add_argument("--top_p", type=float, default=0.9,
                      help="Top-p sampling parameter")
    args = parser.parse_args()

    model = LoRAInference(
        base_model_name=args.model_path,
        adapter_path=args.adapter_path
    )

    logger.info("Starting text generation")
    generated_text = model.generate(
        prompt=args.prompt,
        max_length=args.max_length,
        temperature=args.temperature,
        top_p=args.top_p
    )
    logger.info(f"Generated text: {generated_text}")
    print(generated_text)

if __name__ == "__main__":
    main()