# Week 11: RNN for MNIST classification

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.models import mnist
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, confusion_matrix


# Step 1: Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Normalize images
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 3: Construct RNN model
model = Sequential([
    SimpleRNN(64, input_shape=(28, 28)),
    Dense(10, activation="softmax")
])

# Step 4: Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Step 5: Train model
model.fit(x_train, y_train, epochs=5, batch_size=128)

# Step 6: Predict digits
y_pred = np.argmax(model.predict(x_test), axis=1)

# Step 7: Evaluate performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average="weighted"))
print("Recall:", recall_score(y_test, y_pred, average="weighted"))
print("F1 Score:", f1_score(y_test, y_pred, average="weighted"))

# Step 8: Confusion matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
