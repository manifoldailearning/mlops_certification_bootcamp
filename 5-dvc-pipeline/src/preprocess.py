import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)
    args = parser.parse_args()
    df = pd.read_csv(args.input_path)
    df["salary"] = df["salary"]/1000 # dividing by 1000 to get the salary in thousands
    df.to_csv(args.output_path, index=False)

if __name__ == "__main__":
    main()