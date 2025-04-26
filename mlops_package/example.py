from mlops_python.data.data_loader import DataLoader
from mlops_python.models.linear_regression import LinearRegression
from mlops_python.utils.preprocessor import Preprocessor
from mlops_python.utils.serializer import ModelSerializer
import numpy as np
import os

def main():
    # Create directories for saving models and metrics
    os.makedirs('models', exist_ok=True)
    os.makedirs('metrics', exist_ok=True)
    
    # Initialize data loader
    data_loader = DataLoader('mlops_python/Advertising.csv')
    
    # Load and prepare data
    X, y = data_loader.prepare_data()
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = Preprocessor.train_test_split(X, y)
    
    # Normalize features
    X_train = Preprocessor.normalize(X_train)
    X_test = Preprocessor.normalize(X_test)
    
    # Initialize and train the model
    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    print(f"Training R-squared score: {train_score:.4f}")
    print(f"Testing R-squared score: {test_score:.4f}")
    
    # Save the model
    ModelSerializer.save_model(model, 'models/linear_regression_model.pkl')
    print("\nModel saved to 'models/linear_regression_model.pkl'")
    
    # Save metrics
    metrics = {
        'train_score': train_score,
        'test_score': test_score
    }
    ModelSerializer.save_metrics(metrics, 'metrics/model_metrics.json')
    print("Metrics saved to 'metrics/model_metrics.json'")
    
    # Make predictions
    sample_input = np.array([[230.1, 37.8, 69.2]])  # Example input
    sample_input = Preprocessor.normalize(sample_input)
    prediction = model.predict(sample_input)
    print(f"\nPrediction for sample input: {prediction[0]:.2f}")
    
    # Demonstrate loading the saved model
    print("\nLoading saved model...")
    loaded_model = ModelSerializer.load_model('models/linear_regression_model.pkl')
    
    # Make prediction with loaded model
    loaded_prediction = loaded_model.predict(sample_input)
    print(f"Prediction using loaded model: {loaded_prediction[0]:.2f}")
    
    # Verify the loaded model works the same as the original
    assert np.allclose(prediction, loaded_prediction), "Loaded model predictions don't match original model"
    print("Loaded model verified - predictions match original model")

if __name__ == "__main__":
    main() 