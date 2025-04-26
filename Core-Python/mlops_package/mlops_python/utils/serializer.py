import pickle
import json
import os
from pathlib import Path

class Serializer:
    def save_to_pickle(self, obj, file_path):
        """Saves an object to a pickle file."""
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        print(f"Object saved to {file_path}")
    
    def load_from_pickle(self, file_path):
        """Loads an object from a pickle file."""
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
        print(f"Object loaded from {file_path}")
        return obj