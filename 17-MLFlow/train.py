import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# Load the diabetes dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#set the tracking URI for MLflow
mlflow.set_tracking_uri("http://localhost:5001")  

#logging with mlflow
mlflow.set_experiment("diabetes_experiment")

with mlflow.start_run():
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, predictions)
    
    # Log the model and metrics
    mlflow.log_metric("mse", mse) # log metric
    mlflow.sklearn.log_model(model, "model") # kig the model
    mlflow.log_params({"model_type": "LinearRegression", "dataset": "diabetes"})
    
    print(f"Mean Squared Error: {mse}")