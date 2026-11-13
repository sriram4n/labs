from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target

model = KNeighborsClassifier(n_neighbors= 3)

x_train, x_test, y_train, y_test = train_test_split(x,y)

model.fit(x_train,y_train)

ans = model.predict([[1,2,3,4]])

print("predicted: ", iris.target_names[ans])

y_pred = model.predict(x_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))