from sklearn.datasets import make_classification
import pandas as pd

X,y = make_classification(n_samples=1000, n_features=5, n_classes=2, random_state=42)
df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(5)])
df['target'] = y

df.to_csv('data/reference.csv', index=False)

X2,y2 = make_classification(n_samples=500, n_features=5, n_classes=2, random_state=42,shift=0.6)
df2 = pd.DataFrame(X2, columns=[f"feature_{i}" for i in range(5)])
df2['target'] = y2

df2.to_csv('data/current.csv', index=False)

