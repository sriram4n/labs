from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target
x_train, y_train, x_test, y_test = train_test_split(x,y, test_size = 0.2, random_state=42, stratify = y)
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy score: ", accuracy_score(y_test, y_pred))

# we need plot, GridSearchCV. 