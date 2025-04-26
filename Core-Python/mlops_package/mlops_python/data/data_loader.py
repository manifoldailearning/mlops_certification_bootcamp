# create a class to load data from a csv file
import pandas as pd
from typing import Tuple
import numpy as np

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        # Load the data from the csv file
        data = pd.read_csv(self.file_path)
        return data
    
    def prepare_data(self):
        df = self.load_data()
        X = df[["TV","radio","newspaper"]]
        y = df["sales"]
        return X, y