import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris

# there is a short version in same folder


# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Number of samples:", len(X))
print("Number of features:", X.shape[1])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Train Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, y_pred))

# Hyperparameter grid
param_grid = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 3, 4, 5, 6],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Grid Search with Cross Validation
grid_search = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("\n--- Best Hyperparameters ---")
print(grid_search.best_params_)
print("Best Cross-validation Accuracy:",
      grid_search.best_score_)

# Best Decision Tree
best_model = grid_search.best_estimator_
print("\nBest Decision Tree:")
print(best_model)

# Final test performance
y_pred_best = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred_best)

print("\n--- Final Test Performance ---")
print("Test accuracy:", test_accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_best)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(
    y_test, y_pred_best,
    target_names=iris.target_names
))

# Display Grid Search results
results = pd.DataFrame(grid_search.cv_results_)
print("\nGrid Search Results:")
print(results[
    ['param_criterion', 'param_max_depth',
     'param_min_samples_split', 'param_min_samples_leaf',
     'mean_test_score']
].sort_values(
    by='mean_test_score', ascending=False
).head(10))

# Plot Decision Tree
plt.figure(figsize=(15, 8))
plot_tree(
    best_model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)
plt.title("Decision Tree after Hyperparameter Tuning")
plt.show()
