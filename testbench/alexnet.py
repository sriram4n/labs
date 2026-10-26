import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from sklearn.metrics import classification_report, confusion_matrix

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# alexnet normalization n reshape
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
# reshape to add a color channel dimension
x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]


model = Sequential([
    Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1), padding = 'same'),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation = 'relu', padding = 'same'),
    Flatten(), 
    Dense(128, activation = 'relu'), 
    Dropout(0.5), 
    Dense(10, activation = 'softmax')
])

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
model.fit(x_train, y_train, epochs = 2, batch_size = 128, validation_split = 0.1)
loss, acc = model.evaluate(x_test, y_test)
# print acc, 

pred = np.argmax(model.predict(x_test), axis= 1)

print(classification_report(y_test, pred))

print(confusion_matrix(y_test, pred))