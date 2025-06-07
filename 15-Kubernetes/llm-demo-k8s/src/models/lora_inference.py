import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig
import logging

logger = logging.getLogger(__name__)

class LoRAInference:
    def __init__(self,
                 base_model_name: str,
                 adapter_path:str,
                 device: str = None):
        # determine the device
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        else:
            self.device = device
        
        logger.info(f"Using device: {self.device}")
        self.base_model_name = base_model_name
        self.adapter_path = adapter_path
        logger.info(f"Loading base model: {self.base_model_name}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.base_model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.base_model_name, 
                                                          torch_dtype = torch.float32,
                                                          device_map="auto")
        logger.info(f"Loading adapter from: {self.adapter_path}")
        #adapter_config = PeftConfig.from_pretrained(self.adapter_path)
        self.model = PeftModel.from_pretrained(self.model, 
                                               self.adapter_path)
        
        logging.info(f"Model loaded with adapter: {self.adapter_path}")

        self.model.eval()  # Set the model to evaluation mode
        self.model.to(self.device)
        logger.info("Model and tokenizer initialized for inference")

    def generate(
            self, prompt:str,
            max_length: int = 512,
            temperature: float = 0.7,
            top_p: float = 0.9,
            num_return_sequences: int = 1)-> str:
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True,
                                truncation=True).to(self.device)
        logger.info(f"Generating text for prompt: {prompt}")
        # move the inputs to the device
        inputs = {key: value.to(self.device) for key, value in inputs.items()}

        with torch.no_grad(): 
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                temperature=temperature,
                top_p=top_p,
                num_return_sequences=num_return_sequences,
                do_sample=True,
                num_beams=1,  # Use beam search if needed
                early_stopping=True,  # Stop generation when the model is confident,
                pad_token_id=self.tokenizer.eos_token_id  # Use EOS token for padding
            )
        outputs = outputs.cpu().numpy()  # Move outputs to CPU for decoding
        logger.info(f"Generated {len(outputs)} sequences with max length {max_length}, temperature {temperature}, top_p {top_p}")
        #generated_texts = [self.tokenizer.decode(outputs, skip_special_tokens=True) for output in outputs]  # This will work with multiple sequences
        generated_texts = self.tokenizer.decode(outputs[0], skip_special_tokens=True) # this will work with single sequence
        logger.info(f"Generated {len(generated_texts)} sequences")
        # Clean up the generated texts
        try:
            generated_texts = generated_texts.split("Output:")[-1].strip()  # Assuming the output starts after "Output:"
            sentences = generated_texts.split(".")
            unique_sentences = set(sentences)  # Remove duplicates
            return ". ".join(unique_sentences).strip()  # Join unique sentences back into a string

        except:
            return generated_texts.strip()
    

# create batch generation function

    def batch_generate(self, prompts: list, max_length: int = 512,
            temperature: float = 0.7,
            top_p: float = 0.9,
            num_return_sequences: int = 1)-> str:
        return [self.generate(prompt, max_length, temperature, top_p, num_return_sequences) for prompt in prompts]  
