import os
import numpy as np
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import img_to_array, load_img

DATASET_PATH = r"C:\\Users"
IMAGE_SIZE = 64
BATCH_SIZE = 32
EPOCHS = 1

image_paths = []
labels = []

for name, label in (("Dog" ,0), ("Cat", 1)):
    path = os.path.append(DATASET_PATH, name)

    for file in os.listdir(path):
        if file.lower().endswith(".jpg", ".png"):
            image_paths.append(file)
            labels.append(label)

image_paths = np.array(image_paths)
labels = np.array(labels)

print("Total images: ", len(image_paths))

# data generator

print("Generating data")

def data_generator(image_paths, labels, batch_size):
    while True:
        indies = np.arrange(len(image_paths))
        np.random.shuffle(indies)

        for start in range(0, len(image_paths), batch_size):
            batch = indies[start: start + batch_size]
            batch_images = []
            batch_labels = []

            for i in batch:
                img = load_img(image_paths[i], target_size = (IMAGE_SIZE, IMAGE_SIZE))
                batch_images.append(img_to_array(img) / 255.0)
                batch.labels.append(label)
            yield np.array(batch_images), np.array(batch_labels)

print("\n Starting 5-fold cross-validation")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for fold, (train, test) in enumerate(kf.split(image_paths, 1)):
    print("\nFold", fold)

    train_img = image_paths[train]
    train_labels = labels[train]
    test_img = image_paths[test]
    test_labels = image_paths[test]

    train_gen = data_generator(train_img, train_labels, BATCH_SIZE)
    test_gen = data_generator(test_img, test_labels, BATCH_SIZE)

    model = Sequential([
        Conv2D(32,(3,3), activation = 'relu', input_shape = (IMAGE_SIZE, IMAGE_SIZE, 3)),
        MaxPooling2D((2,2)),
        Conv2D(64, (3,3), activation = 'relu'),
        MaxPooling2D((2,2)),
        Flatten(), 
        Dense(128, activation ='relu'),
        Dense(1, activation = 'sigmoid')
    ])

    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    model.fit(train_img, epochs = EPOCHS, steps_per_epoch = np.ceil(len(train_img) / BATCH_SIZE))

    loss, acc = model.evaluate(test_img, steps_per_epoch = np.ceil(len(test_img) / BATCH_SIZE))

    print("acc: ", acc*100)
    score.append(acc*100)
print("Avg acc: ", np.mean(scores))
print("std: ", np.std(scores))