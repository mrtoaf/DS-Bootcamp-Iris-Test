import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data():
    data = load_iris(as_frame=True)
    iris_dataframe = data.frame
    return iris_dataframe

def split_data():
    

# 0 is Setosa
# 1 is Versicolor
# 2 is Virginica

if __name__ == "__main__":
    df_data = load_data()
    df_data.info()


