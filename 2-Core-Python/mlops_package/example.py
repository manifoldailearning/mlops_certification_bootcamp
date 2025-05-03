from mlops_python.data import data_loader
from mlops_python.utils import preprocessor, serializer
from mlops_python.models import linear_regression
import pandas as pd
import numpy as np

def main():
    # Load the data
    loader = data_loader.DataLoader("Advertising.csv")
    df = loader.load_data()
    
    # Prepare the data
    X, y = loader.prepare_data()
    
    # Preprocess the data
    pp = preprocessor.Preprocessor()
    X_train, X_test, y_train, y_test = pp.train_test_split(X, y)
    
    # Train the model
    model = linear_regression.LinearRegressionModel()
    lr = model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Save the model
    obj = serializer.Serializer()
    obj.save_to_pickle(lr, "mlops_python/models/linear_regression_model.pkl")

if __name__ == "__main__":
    main()