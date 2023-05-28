# pip install pip install numpy scipy matplotlib ipython scikit-learn pandas pillow mglearn notebook

"""
This is the completed code for the section, "A First Application: Classifying Iris Species"
It has been ported from Jupyter Notebooks to any Python IDE of your choice. 

Textbook Credits: 
    Introduction to Machine Learning with Python: A Guide for Data Scientists

"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import mglearn
from sklearn.neighbors import KNeighborsClassifier

"""
This is an optional method to run, although it is recommended to at least run it once.
It generates a pair plot, which looks at every possible permutation of features. 

However, it does not show the interaction for every feature at once.

Generating visualizations is helpful as it can show abnormalities within our dataset.
Additionally, it can show us if the classes are relatively separated, indicating whether our machine learning model will be able 
to sufficiently learn to separate new data points within the respective classes / labels.
"""

def visualize_data() -> None:
    iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
    pd.plotting.scatter_matrix(iris_dataframe, 
                           c=y_train, 
                           figsize=(15, 15),
                           marker='o',
                           hist_kwds={"bins": 20},
                           s = 60,
                           alpha = 0.8
                           # cmap=mglearn.cm3
                           )
    plt.show()


# iris_dataset is a Bunch datatype (similar to a dictionary, so to speak)
iris_dataset = load_iris()
print(iris_dataset.keys())

"""
Keys:
data: Raw data (one data point per row)
target: Classification of each data point
frame: None in this case
target_names: Classes of the types of iris flowers
DESCR: A string description of the Data Set
feature_names: Names of the columns (features) 
filename
data_module
"""

print("===== Data Structure =====")
data_shape = iris_dataset['data'].shape
print("There are {} data points which are built of {} features in our (raw) data.".format(data_shape[0], data_shape[1]))
print("===== Creating Training and Testing Data =====")
# x_train contains 75% of the rows of the dataset and X_test contains the remaining 25%
# Note: We set random_state = 0 so that the output for this particular example is always deterministic
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0
)
print("===== Creating and training the Machine Learning Model: k-nearest neighbour =====")
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print("===== Predicition Test #1 =====")
X_new = np.array([[5, 2.9, 1, 0.2]])
print("For a data point with features:")
for i in range(len(iris_dataset["feature_names"])):
    print("\t {} -> {}".format(iris_dataset["feature_names"][i], X_new[0][i]))
prediction = knn.predict(X_new)
print("We predict that the data point belongs to class ", prediction)
print("The Predicted target name corresponds to ", iris_dataset["target_names"][prediction])
print("===== Evaluating the k-nearest neighbours model with testing data =====")
y_pred = knn.predict(X_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
