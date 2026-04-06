import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

model = SVC(kernel='linear')

kf = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')

print(f"Individual fold accuracies : {scores}")
print(f"Mean accuracy across all folds : {np.mean(scores) : .4f}")
print(f"Standard deviation of accuracies : {np.std(scores) : .4f}")