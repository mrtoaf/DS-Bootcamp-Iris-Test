import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data():
    data = load_iris(as_frame=True)
    iris_dataframe = data.frame
    return iris_dataframe

def split_data(dataframe):
    x = dataframe.drop(['target'], axis=1)
    x = x.to_numpy()[:, (2, 3)]
    y = dataframe['target']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=42)
    return x_train, x_test, y_train, y_test

# 0 is Setosa
# 1 is Versicolor
# 2 is Virginica

if __name__ == "__main__":
    df_data = load_data()

    x_train, x_test, y_train, y_test = split_data(df_data)



