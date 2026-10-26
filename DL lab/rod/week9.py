# Week 9: AlexNet-inspired CNN on MNIST

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load MNIST dataset
print("Step 1: Loading MNIST dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Normalize and reshape images
print("\nStep 2: Preparing images")
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# Step 3: Build AlexNet-inspired CNN
print("\nStep 3: Building CNN")

model = Sequential([
    Conv2D(32, (3, 3), padding="same",
           activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), padding="same", activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(10, activation="softmax")
])

# Step 4: Compile model
print("\nStep 4: Compiling model")

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# Step 5: Train model
print("\nStep 5: Training model")

model.fit(x_train, y_train,
          epochs=2,
          batch_size=128,
          validation_split=0.1,
          verbose=1)

# Step 6: Evaluate model
print("\nStep 6: Evaluating model")

loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print("Test accuracy:", round(accuracy * 100, 2), "%")

# Step 7: Predict digits
print("\nStep 7: Making predictions")

pred = np.argmax(model.predict(x_test, verbose=0), axis=1)

# Step 8: Classification report
print("\nStep 8: Classification report")
print(classification_report(y_test, pred))

# Step 9: Confusion matrix
print("\nStep 9: Confusion matrix")
print(confusion_matrix(y_test, pred))
