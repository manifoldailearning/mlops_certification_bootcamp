# unit test for the model
import joblib
import os 
import numpy as np

def test_model_loading():
    model_path = os.path.join("model","model.joblib")
    model = joblib.load(model_path)
    assert model is not None
    
def test_model_prediction():
    model_path = os.path.join("model","model.joblib")
    model = joblib.load(model_path)
    sample_test_data = np.array([[5.1], [3.5], [1.4], [0.2]])
    prediction = model.predict(sample_test_data)
    assert prediction[0] in [0,1,2]
    
    
    
    