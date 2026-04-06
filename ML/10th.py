import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# k-fold cross validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy score with random forest : ")
print(accuracy_score(y_test, y_pred))

# Perform cross validation
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
print(f"Individual fold accuracies : {scores}")
print(f"Mean accuracy across all folds : {np.mean(scores) : .4f}")
