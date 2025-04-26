import pickle
import json
import numpy as np
from typing import Dict, Any
from pathlib import Path

class ModelSerializer:
    @staticmethod
    def save_model(model: Any, filepath: str) -> None:
        """
        Save the trained model to a file.
        
        Args:
            model: The trained model to save
            filepath: Path where the model will be saved
        """
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        # Save model using pickle
        with open(filepath, 'wb') as f:
            pickle.dump(model, f)
            
    @staticmethod
    def load_model(filepath: str) -> Any:
        """
        Load a saved model from a file.
        
        Args:
            filepath: Path to the saved model file
            
        Returns:
            The loaded model
        """
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    
    @staticmethod
    def save_metrics(metrics: Dict[str, float], filepath: str) -> None:
        """
        Save model metrics to a JSON file.
        
        Args:
            metrics: Dictionary containing metric names and values
            filepath: Path where metrics will be saved
        """
        # Create directory if it doesn't exist
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        # Convert numpy types to Python native types for JSON serialization
        metrics_serializable = {
            k: float(v) if isinstance(v, np.number) else v 
            for k, v in metrics.items()
        }
        
        with open(filepath, 'w') as f:
            json.dump(metrics_serializable, f, indent=4) 