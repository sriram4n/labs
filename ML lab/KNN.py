from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print("KNN Classifier: ")
print("accuracy: ",accuracy)

new_flower = [[5.1,3.5,1.4,0.2]]
ans = model.predict(new_flower)
print("Predicted clasS: ", ans[0])
print("predicted class: ", iris.target_names[ans[0]])

