from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

"""
Task: Learn to predict whether a tumor is malignant based on the measurements of the tissue.
"""

cancer = load_breast_cancer()

"""
keys:
    data
    target
    frame
    target_names
    DESCR
    feature_names
    filename
    data_module
"""

print("Shape of the cancer data: ", cancer["data"].shape)
print("Sample Counts per Class:\n\t", 
      {n: v for n, v in zip(cancer["target_names"], np.bincount(cancer["target"]))}
      )
print("This database consists of the following features:")
for i in cancer["feature_names"]:
    print("\t", i)

X = cancer["data"]
y = cancer["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=cancer["target"], random_state = 66)

training_accuracy = []
test_accuracy = []

neighbours_settings = range(1, 11)

for n_neibhours in neighbours_settings:
    clf = KNeighborsClassifier(n_neighbors=n_neibhours)
    clf.fit(X_train, y_train)
    training_accuracy.append(clf.score(X_train, y_train))
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbours_settings, training_accuracy, label="training accuracy")
plt.plot(neighbours_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbours")
plt.legend()
plt.show()

"""
The best performance is somewhere in the middle of too complex (n = 1) and too simple (n = 10).
The author recommends using about six neighbours.

Note: It is good to keep the said scale of the plot in mind. The worst performance is around 88% accuracy, which might still be acceptable.

Reference: 
    - Introduction to Machine Learning with Python: A Guide for Data Scientists
    - O'Reilly Media, Incorporated
"""
