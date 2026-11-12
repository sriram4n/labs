import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics import classification_report, confusion_matrix

# load data
print("Loading mnist dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

# reshape
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# convert grayscale to rgb
x_train = np.repeat(x_train, 3, axis=-1)
x_test = np.repeat(x_test, 3, axis=-1)

# resize images
print("Resizing images")
x_train = tf.image.resize(x_train, (32,32))
x_test = tf.image.resize(x_test, (32,32))

# preprocess for vgg16
x_train = preprocess_input(x_train)
x_test = preprocess_input(x_test)

# load vgg16 with imagenet weights
print("Loading VGG16 model")
base_model = VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(32,32,3)
)

# freeze vgg16 layers
base_model.trainable = False

# build model
print("Building model")

model = Sequential([
    base_model,
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# display model
model.summary()

# train
print("Training model")
model.fit(x_train, y_train,
    epochs=1,
    batch_size=128,
    validation_split=0.1
)

# evaluate
loss, acc = model.evaluate(x_test, y_test)
print("Test accuracy: ", acc*100)

# prediction
print("Prediction:")
pred = np.argmax(model.predict(x_test), axis=1)

# classification report
print("Classification report:")
print(classification_report(y_test, pred))

# confusion matrix
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
