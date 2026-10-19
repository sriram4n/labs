# Week 8: CNN classification of cats and dogs using 5-fold cross-validation

import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Step 1: Load image paths and labels
print("Step 1: Loading dataset")

DATASET_PATH = r"D:\LabImages"  # Change to your dataset path
IMG_SIZE = 64
BATCH_SIZE = 32
EPOCHS = 1

image_paths = []
labels = []
# adding the paths to our list
for folder, label in [("Cat", 0), ("Dog", 1)]:
    path = os.path.join(DATASET_PATH, folder)

    for file in os.listdir(path):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            image_paths.append(os.path.join(path, file))
            labels.append(label)

image_paths = np.array(image_paths)
labels = np.array(labels)

print("Total images:", len(image_paths))

# Step 2: Create data generator
print("\nStep 2: Creating data generator")

def data_generator(paths, labels, batch_size):
    while True:
        # grab indices
        indices = np.arange(len(paths))
        np.random.shuffle(indices)
        # sliding window
        for start in range(0, len(paths), batch_size):
            batch = indices[start:start + batch_size]
            images = []
            batch_labels = []
            # every pic in batch
            for i in batch:
                img = load_img(paths[i], target_size=(IMG_SIZE, IMG_SIZE))
                images.append(img_to_array(img) / 255.0)
                batch_labels.append(labels[i])
            # yield produces gradually 
            yield np.array(images), np.array(batch_labels)

# Step 3: Create 5-fold cross-validation
print("\nStep 3: Starting 5-fold cross-validation")

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for fold, (train, test) in enumerate(kf.split(image_paths), start=1):
    print("\nFold", fold)

    train_paths = image_paths[train]
    train_labels = labels[train]
    test_paths = image_paths[test]
    test_labels = labels[test]

    train_gen = data_generator(train_paths, train_labels, BATCH_SIZE)
    test_gen = data_generator(test_paths, test_labels, BATCH_SIZE)

    # Step 4: Build CNN model
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu",
               input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    # Step 5: Compile and train model
    model.compile(optimizer="adam",
                  loss="binary_crossentropy",
                  metrics=["accuracy"])

    model.fit(
        train_gen,
        steps_per_epoch=int(np.ceil(len(train_paths) / BATCH_SIZE)),
        epochs=EPOCHS,
        verbose=1
    )

    # Step 6: Evaluate model
    loss, acc = model.evaluate(
        test_gen,
        steps=int(np.ceil(len(test_paths) / BATCH_SIZE)),
        verbose=0
    )

    print("Accuracy:", round(acc * 100, 2), "%")
    scores.append(acc * 100)

# Step 7: Display final results
print("\nAverage accuracy:", round(np.mean(scores), 2), "%")
print("Standard deviation:", round(np.std(scores), 2), "%")
