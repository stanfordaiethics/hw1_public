"""
CS 281. Homework 1. Fairness in the Wild
Correspondence to: khkim@cs.stanford.edu
"""
import json
from typing import Union

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV


## Load the COMPAS Dataset
raw_data = pd.read_csv('./compas-scores-two-years.csv')
print('Num rows: %d' % len(raw_data))


######## Q1. Data pre-processing ########
## TODO: filter out corrupted rows from raw_data and store in a variable name "df"
## df should be a pandas.DataFrame object
df =
print('Q1: Num data points after filtering: %d' % len(df))


######## Q2. Data Visualization ########
## TODO: Visualize decile_scores as a histogram for different races, genders.


######## Q3. Learning a Predictor #########
## Do not remove this random seed as it will change the results
np.random.seed(0)


## (a). Process subset of features in df into one-hot vectors. Store result in features
## TODO:
features =
target = df.two_year_recid


## (b). Split (features, target) into 75% training set, 25% test set
## TODO:


## (c). Fit a logistic regression model on training set.
## TODO:


######## Q4: Compute demographic parity ########
## TODO:


######## Q6: Calibration Fairness ########
## TODO:


######## Q7: Post-hoc Calibration Fairness ########
## TODO:


######## Q8: Calibration effect on Demographic Parity ########
## TODO:


