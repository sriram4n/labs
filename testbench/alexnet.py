# alexnet on mnist
import numpy
from tensorflow.keras.dataset import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from sklearn.metrics import confusion_matrix, classification_report

print("Step 1: Loading MNIST dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize and reshape
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

model = Sequential([
    Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1))
    MaxPooling2D((2,2))
    Conv2D(64, (3,3), activation = 'relu')
    MaxPooling2D((2,2))
    Flatten()
    Dense(128, activation = 'relu')
    Droput(0.5)
    Dense(10, activation = 'softmax')
])

model.compile(optimizer = 'adam', loss = 'categoraical_crossentroypy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 2)

y_pred = np.argmax(model.predict(x_test),axis=1)
