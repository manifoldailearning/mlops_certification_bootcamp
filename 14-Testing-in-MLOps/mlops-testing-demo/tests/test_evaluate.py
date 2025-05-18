# Unit test for metrics
import numpy as np
from sklearn.metrics import accuracy_score

def test_metrics():
    y_true = np.array([0,1,2,0,1,2])
    y_pred = np.array([0,2,1,0,0,2])
    
    accuracy = accuracy_score(y_true, y_pred)
    assert accuracy >= 0.2
    