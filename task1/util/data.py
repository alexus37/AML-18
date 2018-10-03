import pandas as pd

TRAIN_FILE_PATH = "data/X_train.csv"
TARGET_FILE_PATH =  "data/y_train.csv"
TEST_FILE_PATH = "data/X_test.csv"

def load():
    train_set = pd.read_csv(TRAIN_FILE_PATH)
    test_set =  pd.read_csv(TEST_FILE_PATH)

    # add target to dataframe
    target =  pd.read_csv(TARGET_FILE_PATH)
    train_set = train_set.merge(target, left_on='id', right_on='id', how="left", validate="1:1")

    print("Training Data: ")
    print("  Amount of features: {}".format(len(list(train_set)) - 1)) # -1 due to id
    print("  Amount of observations: {}".format(len(train_set.index)))
    print("  Min age: {} Max age: {}".format(train_set["y"].min(), train_set["y"].max()))

    print("\nTest Data: ")
    print(f"  Amount of observations: {len(test_set.index)}")

    return train_set, test_set


def write_submission(test_set: pd.DataFrame, filename: str):
    test_set[["id", "y"]].to_csv(f"submissions/{filename}.csv", index= False)
