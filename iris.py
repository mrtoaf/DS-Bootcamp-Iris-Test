import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import parallel_coordinates
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'

col_name = ['sepal-lenght','sepal-width','petal-lenght','petal-width','class']

dataset = pd.read_csv(url, names = col_name)

dataset.shape