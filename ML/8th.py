import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Create a decision tree classifier object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)

# Train the model
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy : {accuracy : 0.4f}")

# Visualize
plt.figure(figsize=(20, 10))
plot_tree(clf,  filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True, precision=2)
plt.show()