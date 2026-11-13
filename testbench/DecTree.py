import nupy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
model = DecisionTreeClassifier()
iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accurcay score: ", accuracy_score(y_test, y_pred))