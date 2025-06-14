import pandas as pd
from prometheus_client import Gauge
from scipy.stats import wasserstein_distance

#metrics
model_accuracy = Gauge('model_accuracy', 'Accuracy of the trained model')
data_drift_metric = Gauge('data_drift_distance', 'Wasserstein distance between training and inference data')

def compute_drift(train_data, inference_data):
    """
    Compute the Wasserstein distance between training and inference data
    """
    drift_sum = 0
    for col in train_data.columns:
        if col != 'target':
            drift = wasserstein_distance(train_data[col], inference_data[col])
            drift_sum += drift
    return drift_sum

def monitor(reference_path="data/reference.csv", current_path="data/current.csv"):
    ref = pd.read_csv(reference_path)
    current = pd.read_csv(current_path)
    from model import train_model
    _, accuracy = train_model(current)
    model_accuracy.set(accuracy)

    drift = compute_drift(ref, current)
    data_drift_metric.set(drift)
