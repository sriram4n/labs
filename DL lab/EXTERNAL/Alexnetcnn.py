import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.metrics import classification_report, confusion_matrix

# load data
print("Loading mnist dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize
print("Preparing images")
x_train = x_train.astype("float32")/255.0
x_test = x_test.astype("float32")/255.0

# reshape
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

# build AlexNet
print("Building model")

model = Sequential([
    Conv2D(96, (3,3), padding='same', activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),

    Conv2D(256, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),

    Conv2D(384, (3,3), padding='same', activation='relu'),
    Conv2D(384, (3,3), padding='same', activation='relu'),
    Conv2D(256, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2,2)),

    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),

    Dense(512, activation='relu'),
    Dropout(0.5),

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
    epochs=2,
    batch_size=128,
    validation_split=0.1
)

# evaluate
loss, acc = model.evaluate(x_test, y_test)
print("Test acc: ", acc*100)

# prediction
print("Prediction:")
pred = np.argmax(model.predict(x_test), axis=1)

# classification report
print("Classification report:")
print(classification_report(y_test, pred))

# confusion matrix
print("Confusion matrix:")
print(confusion_matrix(y_test, pred))
