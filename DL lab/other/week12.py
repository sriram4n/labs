# LSTM for cats and dogs dataset

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.utils import image_dataset_from_directory
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Dataset path
DATASET_PATH = r"C:\Users\YourName\Downloads\PetImages"

# Load training dataset
train_ds = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    seed=123,
    batch_size=32,
    image_size=(64, 64),
    label_mode="binary",
    subset="training"
)

# Load testing dataset
test_ds = image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    seed=123,
    batch_size=32,
    image_size=(64, 64),
    label_mode="binary",
    subset="validation"
)

# Normalize images and convert them into sequences
def prepare_data(dataset):
    X, Y = [], []

    for images, labels in dataset:
        images = images.numpy() / 255.0

        # (batch, 64, 64, 3) -> (batch, 64, 192)
        images = images.reshape(-1, 64, 192)

        X.append(images)
        Y.append(labels.numpy())

    return np.concatenate(X), np.concatenate(Y)

X_train, y_train = prepare_data(train_ds)
X_test, y_test = prepare_data(test_ds)

# Build LSTM model
model = Sequential([
    LSTM(64, input_shape=(64, 192)),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train the model
model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)

# Predict test images
y_prob = model.predict(X_test)
y_pred = (y_prob >= 0.5).astype(int).flatten()

y_true = y_test.flatten().astype(int)

# Evaluate performance
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(
    y_true, y_pred,
    target_names=train_ds.class_names,
    zero_division=0
))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)
