import numpy as np
from typing import Tuple

class Preprocessor:
    @staticmethod
    def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Split the dataset into training and testing sets.
        
        Args:
            X (np.ndarray): Features
            y (np.ndarray): Target
            test_size (float): Proportion of the dataset to include in the test split
            random_state (int): Random seed for reproducibility
            
        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: X_train, X_test, y_train, y_test
        """
        np.random.seed(random_state)
        indices = np.random.permutation(len(X))
        test_size = int(len(X) * test_size)
        
        train_indices = indices[test_size:]
        test_indices = indices[:test_size]
        
        X_train = X[train_indices]
        X_test = X[test_indices]
        y_train = y[train_indices]
        y_test = y[test_indices]
        
        return X_train, X_test, y_train, y_test
    
    @staticmethod
    def normalize(X: np.ndarray) -> np.ndarray:
        """
        Normalize the features using min-max scaling.
        
        Args:
            X (np.ndarray): Features to normalize
            
        Returns:
            np.ndarray: Normalized features
        """
        return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) 