from fairlearn.reductions import GridSearch
from fairlearn.reductions import DemographicParity, ErrorRate

from sklearn import svm, neighbors, tree
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
import shap

import numpy as np

shap.initjs()
X_raw, Y = shap.datasets.adult()
print(X_raw)
