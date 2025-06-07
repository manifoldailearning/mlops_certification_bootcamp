```bash
conda create --prefix ./envs python=3.11 -y
conda activate ./envs
```
To use the fine-tuned LoRA adapters for inference:

```bash
python scripts/inference.py \
    --model_path facebook/opt-350m \
    --adapter_path output/final_model \
    --prompt "What is machine learning?"
```
