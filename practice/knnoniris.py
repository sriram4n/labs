import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

model = KNeighborsClassifier(n_neighbors= 5)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))

pred = model.predict([[1,2,3,4]])
print("Model prediction: ", pred[0])
print("Class name: ",iris.target_names[pred[0]])