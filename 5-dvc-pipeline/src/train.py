import argparse
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str)
    parser.add_argument("model_path", type=str)
    parser.add_argument("metrics_path", type=str)
    args = parser.parse_args()

    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    df = pd.read_csv(args.data_path)
    feature = params["train"]["features"]
    target = params["train"]["target"]
    X = df[[feature]]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)
# comment
    with open(args.model_path, "wb") as f:
        pickle.dump(model, f)

    with open(args.metrics_path, "w") as f:
        f.write(f"R-squared: {model.score(X, y)}")

if __name__ == "__main__":
    main()
