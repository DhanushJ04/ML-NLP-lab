import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('iris.csv')

X = data.drop('variety', axis=1)
y = data['variety']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
MLModel = LogisticRegression()
MLModel.fit(X_train, y_train)
y_pred = MLModel.predict(X_test)
print("Accuracy : ", accuracy_score(y_test, y_pred))
df = pd.DataFrame([{'sepal.length': 4.2, 'sepal.width': 3.5, 'petal.length': 2.8, 'petal.width': 4.3}])

# Predicting with user input
ac = MLModel.predict(df)
print("Own input : ", ac)
