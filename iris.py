# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
from sklearn import datasets


def load_data():
    data = load_iris(as_frame=True)
    iris_dataframe = data.as_frame
    return iris_dataframe


if __name__ == "__main__":
    load_data.info()
