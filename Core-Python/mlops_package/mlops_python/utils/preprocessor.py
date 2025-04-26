import numpy as np
from typing import Tuple
from sklearn.model_selection import train_test_split

class Preprocessor:
    def train_test_split(self, X: np.ndarray, y: np.ndarray, ts: float = 0.2) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Split the data into training and testing sets.
        
        Parameters:
        X (np.ndarray): Features
        y (np.ndarray): Target variable
        ts (float): Proportion of the dataset to include in the test split
        
        Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: Split data
        """
        return train_test_split(X, y, test_size=ts, random_state=42)
    
