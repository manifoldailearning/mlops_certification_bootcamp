from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class LoRAConfig:
    model_name: str = "facebook/opt-350m" # gemini
    max_length: int = 512
    batch_size: int = 8
    output_dir: str = "output/final_model"
    # Lora parameters
    lora_r: int = 8
    lora_alpha: int = 16
    lora_dropout: float = 0.1
    lora_target_modules: list = None

    # Training parameters
    num_epochs: int = 3
    learning_rate: float = 2e-5
    weight_decay: float = 0.01
    warmup_steps: int = 100

    # Data Parameters
    train_file: str = "data/train.json"
    eval_file: Optional[str] = None

    # Hardware Configurations
    use_cuda: bool = False
    device: str = "cpu"
    fp16: bool = False

    def __post_init__(self):
        if self.lora_target_modules is None:
            self.lora_target_modules = ["q_proj", "v_proj"]