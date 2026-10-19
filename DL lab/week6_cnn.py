# Week 6: CNN classification using MNIST and 10-fold cross-validation

import numpy as np
from sklearn.model_selection import KFold
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

np.random.seed(42)

# Step 1: Load MNIST dataset
print("Step 1: Loading MNIST dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Training images:", x_train.shape)
print("Testing images:", x_test.shape)

# Step 2: Combine datasets
print("\nStep 2: Combining dataset")
x = np.concatenate((x_train, x_test), axis=0)
y = np.concatenate((y_train, y_test), axis=0)

print("Total images:", x.shape[0])

# Step 3: Normalize images
print("\nStep 3: Normalizing images")
x = x.astype("float32") / 255.0

# Step 4: Reshape images
print("\nStep 4: Reshaping images")
x = x.reshape(-1, 28, 28, 1)
print("Image shape:", x.shape)

# Step 5: One-hot encode labels
print("\nStep 5: One-hot encoding labels")
y = to_categorical(y, 10)
print("Label shape:", y.shape)

# Step 6: Create 10-fold cross-validation
print("\nStep 6: Starting 10-fold cross-validation")

kfold = KFold(n_splits=10, shuffle=True, random_state=42)
scores = []
fold = 1

kf = KFold(n_splits=10, shuffle=True, random_state=42)
scores = []

for train, test in kf.split(x):
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])

    model.fit(x[train], y[train], epochs=3, batch_size=64, verbose=0)

    loss, acc = model.evaluate(x[test], y[test], verbose=0)
    scores.append(acc * 100)

    print("Accuracy:", round(acc * 100, 2), "%")

print("Average accuracy:", round(np.mean(scores), 2), "%")
print("Standard deviation:", round(np.std(scores), 2), "%")
