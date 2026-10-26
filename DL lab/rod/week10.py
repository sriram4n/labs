# Week 10: VGG16 Transfer Learning for Cats and Dogs

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Droput
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Step 1: Load dataset
print("Step 1: Loading dataset")

dataset_path = r"C:\Users\YourName\Downloads\KaggleCatsAndDogs\PetImages"
# basically normalization
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)
# basically train test split
train = datagen.flow_from_directory(
    dataset_path,
    batch_size=32,
    class_mode="binary",
    target_size=(224, 224),
    subset="training"
)

val = datagen.flow_from_directory(
    dataset_path,
    batch_size=32,
    class_mode="binary",
    target_size=(224, 224),
    subset="validation"
)

# Step 2: Load pre-trained VGG16
print("Step 2: Loading VGG16")

base_model = VGG16(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

# Step 3: Freeze VGG16 layers
base_model.trainable = False

# Step 4: Build classification model
print("Step 3: Building model")

model = Sequential([
    base_model,
    Flatten(),
    Dense(128, activation="relu"),
    Dropout(0.5),
    Dense(1, activation="sigmoid")
])

# Step 5: Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Step 6: Train model
print("Step 4: Training model")

model.fit(
    train,
    validation_data=val,
    epochs=1
)

# Step 7: Evaluate model
print("Step 5: Evaluating model")

loss, accuracy = model.evaluate(val)

print("Validation accuracy:", round(accuracy * 100, 2), "%")
