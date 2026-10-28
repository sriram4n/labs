import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("Test accuracy:", accuracy_score(y_test, model.predict(X_test)))

param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 4, 6],
    'min_samples_split': [2, 10],
    'min_samples_leaf': [1, 4]
}

grid = GridSearchCV(DecisionTreeClassifier(random_state=42),
                        param_grid, cv=5,
                        scoring='accuracy',
                        n_jobs=-1
                    )
grid.fit(X_train, y_train)

print("\nBest parameters:", grid.best_params_)
print("Best CV accuracy:", grid.best_score_)
print("\nBest model:", grid.best_estimator_)

y_pred = grid.predict(X_test)

print("\nFinal test accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification report:\n",
      classification_report(y_test, y_pred, target_names=iris.target_names))

# results = pd.DataFrame(grid.cv_results_)
# cols = ['param_criterion', 'param_max_depth', 'param_min_samples_split',
#         'param_min_samples_leaf', 'mean_test_score']
# print("\nTop 10 grid search results:")
# print(results[cols].sort_values('mean_test_score', ascending=False).head(10))

plt.figure(figsize=(15, 8))
plot_tree(grid.best_estimator_, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.show()
