# Week 7: Visualize CNN features and confusion matrix

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix

# Step 1: Load MNIST dataset
print("Step 1: Loading MNIST dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Normalize and reshape images
print("\nStep 2: Preparing images")
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Step 3: One-hot encode labels
print("\nStep 3: Encoding labels")
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Step 4: Build CNN model
print("\nStep 4: Building CNN")
model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1), name="conv1"),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation="relu", name="conv2"),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

# Step 5: Compile and train model
print("\nStep 5: Training CNN")
model.compile(optimizer="adam",
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.fit(x_train, y_train_cat, epochs=2,
          batch_size=128, validation_split=0.1)

# Step 6: Evaluate model
print("\nStep 6: Evaluating model")
loss, accuracy = model.evaluate(x_test, y_test_cat, verbose=0)
print("Test accuracy:", round(accuracy * 100, 2), "%")

# Step 7: Create confusion matrix
print("\nStep 7: Confusion matrix")
pred = np.argmax(model.predict(x_test, verbose=0), axis=1)
cm = confusion_matrix(y_test, pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Confusion Matrix")
plt.show()

# Step 8: Extract hidden layer features
print("\nStep 8: Extracting features")
feature_model = Model(model.inputs, [
    model.get_layer("conv1").output,
    model.get_layer("conv2").output
])

image = x_test[0:1]
features = feature_model.predict(image, verbose=0)

# Step 9: Display original image
print("\nStep 9: Original image")
plt.imshow(image[0].reshape(28, 28), cmap="gray")
plt.title("Original MNIST Image")
plt.axis("off")
plt.show()

# Step 10: Display first layer feature maps
print("\nStep 10: First convolution layer")
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.imshow(features[0][0, :, :, i], cmap="viridis")
    plt.axis("off")
plt.show()

# Step 11: Display second layer feature maps
print("\nStep 11: Second convolution layer")
for i in range(16):
    plt.subplot(4, 4, i + 1)
    plt.imshow(features[1][0, :, :, i], cmap="viridis")
    plt.axis("off")
plt.show()
