import json
from typing import List, Dict, Optional
from datasets import Dataset 
from transformers import PreTrainedTokenizer 

class DataProcessor:
    def __init__(self, tokenizer: PreTrainedTokenizer, max_length: int):
        self.tokenizer = tokenizer
        self.max_length = max_length

    def load_data(self, file_path: str) -> Dataset:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            fomatted_data = {
                "input": data["input"],
                "output": data["output"]
            }
            print(data)
            print(type(data))
            print(fomatted_data)
            print(type(fomatted_data))
        return Dataset.from_dict(fomatted_data)

    def preprocess_function(self, dataset: Dict) -> Dict:
        texts = [f"Input: {inp}\nOutput: {out}" for inp,out in zip(dataset['input'], dataset['output']) ]
        tokenized_inputs = self.tokenizer(
            texts,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt"
        )

        return {
            "input_ids": tokenized_inputs["input_ids"],
            "attention_mask": tokenized_inputs["attention_mask"],
            "labels": tokenized_inputs["input_ids"].clone()  # For language modeling, labels are the same as input_ids
        }

    def prepare_dataset(self, file_path: str) -> Dataset:
        dataset = self.load_data(file_path)
        processed_dataset = dataset.map(
            self.preprocess_function,
            batched=True,
            remove_columns=dataset.column_names
        )
        return processed_dataset

    def create_sample_data(self,output_file: str):
        sample_data = {"input": [
                "What is Machine Learning?",
                "Explain the concept of Neural Networks.",
                "What is the difference between supervised and unsupervised learning?"
            ], 
            "output": ["Machine Learning is a subset of artificial intelligence that focuses on building systems that learn from data.",
                       "Neural Networks are computational models inspired by the human brain, consisting of interconnected nodes (neurons) that process data.", 
                      "Supervised learning uses labeled data to train models, while unsupervised learning uses unlabeled data to find patterns or groupings."]
            }
        # Save the sample data to a JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
        print(f"Sample data created at {output_file}")