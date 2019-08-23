#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
style.use('ggplot')

#importing the dataset
dataset = pd.read_csv('Mall_customers.csv')
X = dataset.iloc[:, [3,4]].values

#splitting the dataset into the training set and the test set