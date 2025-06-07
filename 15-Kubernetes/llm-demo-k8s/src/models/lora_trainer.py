import os
from typing import Optional
import torch
from transformers import Trainer, TrainingArguments, AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType, prepare_model_for_kbit_training
from datasets import Dataset
import wandb 
from src.config.config import LoRAConfig
import logging

logger = logging.getLogger(__name__)

class LoRATrainer:
    def __init__(self,
                 config: LoRAConfig):
        self.config = config
        self.model_name = config.model_name
        self.output_dir = config.output_dir 
        os.makedirs(self.output_dir, exist_ok=True)

        self.device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu" # mps - metal performance shaders for macOS
        self.fp16 = config.fp16 and self.device == "cuda" # Use fp16 only if CUDA is available

        logger.info(f"Using device: {self.device}, fp16: {self.fp16}")

        # initialize the model and tokenizer
        logger.info(f"Loading model {self.model_name} with fp16={self.fp16}")
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16 if self.fp16 else torch.float32,
            device_map="auto" 
        )

        # Prepare the model for LoRA
        logger.info(f"Prepare the model for LoRA training")
        self.model = prepare_model_for_kbit_training(self.model)

        # configure LoRA
        logger.info(f"configure LoRA")
        self.lora_config = LoraConfig( # from LoRA library
            r=config.lora_r,
            lora_alpha=config.lora_alpha,
            lora_dropout=config.lora_dropout,
            bias="none",
            task_type=TaskType.CAUSAL_LM,
            target_modules=config.lora_target_modules # Default target modules
        )

        logger.info(f"Apply LoRA configuration to the model")

        self.model = get_peft_model(self.model, self.lora_config)
        self.model.print_trainable_parameters()

    def train(
            self,
            train_dataset: Dataset,
            eval_dataset: Optional[Dataset] = None
    ):
        logger.info("Starting training process")
        
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            per_device_train_batch_size= self.config.batch_size,
            per_device_eval_batch_size= self.config.batch_size,
            num_train_epochs= self.config.num_epochs,
            learning_rate= self.config.learning_rate,
            weight_decay= self.config.weight_decay,
            warmup_steps= self.config.warmup_steps,
            logging_dir=os.path.join(self.output_dir, "logs"),
            logging_steps=10,
            save_strategy="epoch",
            fp16=self.fp16,
            report_to="wandb" if wandb.run else None,  # Use wandb if available
        )
        logger.info(f"Training arguments: {training_args}")

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            tokenizer=AutoTokenizer.from_pretrained(self.model_name),
        )

        logger.info("Starting training")

        trainer.train()

        # save the model
        logger.info(f"Saving the model to {self.output_dir}")
        trainer.save_model(os.path.join(self.output_dir))

        if wandb.run is not None:
            logger.info("Saving model to wandb")
            wandb.finish()
        
        return trainer