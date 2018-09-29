import csv
import numpy as np
from tqdm import tqdm
from sklearn.metrics import mean_squared_error
import pandas as pd


TRAIN_FILE_PATH = "data/train.csv"
TEST_FILE_PATH = "data/test.csv"


def read_csv(path):
    data =  pd.read_csv(path)

    return data

def create_submission(df):
    print("Creating submission")
    df[["Id", "y_pred"]].to_csv("submission.csv", index=False, header=["Id", "y"])


def compute_mean(df):
    df["y_pred"]  = df[["x" + str(i) for i in range(1, 11)]].mean(axis=1)
    return df

def main():
    train_data = read_csv(TRAIN_FILE_PATH)
    train_data = compute_mean(train_data)

    # test if the y is actually the mean
    error = mean_squared_error(train_data["y"], train_data["y_pred"])**0.5
    print("Error between the y and the mean is {}".format(error))

    test_data = read_csv(TEST_FILE_PATH)
    test_data = compute_mean(test_data)
    print(test_data.head(5))
    create_submission(test_data)


if __name__ == '__main__':
    main()
