import mlflow
from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.model_selection import train_test_split
logged_model = 'runs:/68d53dd541ff4570a0f6405c78c9ae89/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Load the diabetes dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Make predictions
predictions = loaded_model.predict(X_test)
# Calculate the mean squared error
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")