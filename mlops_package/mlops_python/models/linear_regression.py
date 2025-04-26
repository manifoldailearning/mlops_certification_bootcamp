import numpy as np
from typing import Tuple

class LinearRegression:
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        """
        Initialize the Linear Regression model.
        
        Args:
            learning_rate (float): Learning rate for gradient descent
            n_iterations (int): Number of iterations for gradient descent
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        
    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the linear regression model to the training data.
        
        Args:
            X (np.ndarray): Training features
            y (np.ndarray): Training target
        """
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for _ in range(self.n_iterations):
            # Calculate predictions
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the trained model.
        
        Args:
            X (np.ndarray): Input features
            
        Returns:
            np.ndarray: Predicted values
        """
        return np.dot(X, self.weights) + self.bias
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate the R-squared score of the model.
        
        Args:
            X (np.ndarray): Test features
            y (np.ndarray): Test target
            
        Returns:
            float: R-squared score
        """
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - (ss_res / ss_tot) 