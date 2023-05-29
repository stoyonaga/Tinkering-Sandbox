from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor


california = fetch_california_housing()
"""
Task: Predicting the median value of homes in several California neighbourhoods using information from our feature_names.
"""
print("Shape of the housing data: ", california["data"].shape)


"""
keys:
    data
    target
    frame
    target_names
    feature_names
    DESCR
"""

X = california["data"]
y = california["target"]

print("===== Generating Training and Testing Data =====")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
print("===== Generating KNN Regressor Model =====")
reg = KNeighborsRegressor(n_neighbors=3)
print("===== Training the KNN Regressor Model on n=3 =====")
reg.fit(X_train, y_train)
print("===== Evaluating Model on Testing Data =====")
print("Test Set Predictions: ", reg.predict(X_test))
print("Test Set R^2: {:.2f}".format(reg.score(X_test, y_test)))
