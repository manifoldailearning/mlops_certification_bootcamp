from typing import Tuple
from sklearn.linear_model import LinearRegression
import numpy as np

class LinearRegressionModel:
    def __init__(self):
        pass

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the linear regression model to the training data.
        
        Parameters:
        X (np.ndarray): Features
        y (np.ndarray): Target variable
        """
        # Add a bias term (intercept) to the features
        self.lr = LinearRegression()
        self.lr.fit(X, y)
        # self.coefficients = self.lr.coef_
        # self.intercept = self.lr.intercept_
        return self.lr
        
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict using the linear regression model.
        
        Parameters:
        X (np.ndarray): Features
        
        Returns:
        np.ndarray: Predicted values
        """
        # Add a bias term (intercept) to the features
        self.y_pred = self.lr.predict(X)
        
        return self.y_pred