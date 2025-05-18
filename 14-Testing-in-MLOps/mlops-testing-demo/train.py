from sklearn.datasets import load_iris
import joblib
import os 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    # Load the iris dataset
    iris = load_iris()
    X = iris.data[:,0].reshape(-1,1) # single feature
    y = iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save the model
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/model.joblib')

if __name__ == '__main__':
    main()

    