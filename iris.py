# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_iris


def load_data():
    data = load_iris(as_frame=True)
    iris_dataframe = data.frame
    return iris_dataframe


if __name__ == "__main__":
    df_data = load_data()
    df_data.info()
