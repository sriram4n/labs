import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.metrics import classification_report, confusion_matrix

# load data
print("Loading mnist dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize
print("Preparing images")
x_train = x_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0

# convert labels
y_train = y_train.astype("int64")
y_test = y_test.astype("int64")

# reshape
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# display shapes
print("Training data: ", x_train.shape)
print("Testing data: ", x_test.shape)
print("Training labels: ", y_train.shape)
print("Testing labels: ", y_test.shape)
print("Image dtype: ", x_train.dtype)
print("Label dtype: ", y_train.dtype)

# build cnn
print("Building model")

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),

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
model.fit(x_train, y_train,
    epochs=1,
    batch_size=128,
    validation_split=0.1
)

# prediction
print("Prediction:")
pred = np.argmax(model.predict(x_test), axis=1)

# classification report
print("Classification report:")
print(classification_report(y_test, pred))

# confusion matrix
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
