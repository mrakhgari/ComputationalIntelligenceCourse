import pandas as pd
from sklearn.model_selection import train_test_split


def read_data(filepath='Resources/dataset.csv', test_size=0.3):
    # read csv file as a list of lists
    df = pd.read_csv(filepath, names=['x1', 'x2', 'label'])

    # X_train, Y_train = read_data()
    train, test = train_test_split(df, test_size=test_size)

    X_train, Y_train = train.to_numpy()[:, [0, 1]], train['label'].to_numpy()
    X_test, Y_test = test.to_numpy()[:, [0, 1]], test['label'].to_numpy()

    X_train = X_train.T
    Y_train = Y_train.T

    X_test = X_test.T
    Y_test = Y_test.T
    return X_train, X_test, Y_train, Y_test
