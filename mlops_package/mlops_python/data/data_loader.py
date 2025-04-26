import pandas as pd
import numpy as np
from typing import Tuple

class DataLoader:
    def __init__(self, file_path: str):
        """
        Initialize the DataLoader with the path to the dataset.
        
        Args:
            file_path (str): Path to the CSV file containing the dataset
        """
        self.file_path = file_path
        
    def load_data(self) -> pd.DataFrame:
        """
        Load the dataset from CSV file.
        
        Returns:
            pd.DataFrame: Loaded dataset
        """
        return pd.read_csv(self.file_path)
    
    def prepare_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepare the data for training by separating features and target.
        
        Returns:
            Tuple[np.ndarray, np.ndarray]: Features (X) and target (y) arrays
        """
        df = self.load_data()
        X = df[['TV', 'radio', 'newspaper']].values
        y = df['sales'].values
        return X, y 