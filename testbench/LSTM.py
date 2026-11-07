import numpy as np
from tensorflow.keras.datasets import Sequential
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.layers import Dense, LSTM 
from sklearn.metrics import classification_report, confusion_matrix

path = r''

train = image_dataset_from_directory(
    path,
    validation_split = 0.2,
    seed = 123,
    batch_size = 32,
    image_size = (64,64),
    label_mode = 'binary',
    subset = 'training'
)

test = image_dataset_from_directory(
    path, 
    validation_split = 0.2,
    seed = 123,
    batch_size = 32,
    image_size = (64,64),
    label_mode = 'binary',
    subset = 'validation'
)

def prepaer_data(data):
    x = [], y = []

    for image, lable in data:
        image = image.numpy() / 255.0
        image = image.reshape(-1, 64, 192)
        
        x.append(image)
        y.append(label.numpy())

    return np.concatenate(x), np.concatenate(y)


x_train , y_train = prepaer_data(train)
x_test, y_test = prepaer_data(test)

model = Sequential([
    LSTM(64, input_shape=(64,192)),
    Dense(1, activation = 'sigmoid')
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=32,
)

y_prob = mode.predict(x_test)
y_pred = (y_prob > 0.5).astype(int).flatten()
y_true = y_test.astype(int).flatten()


loss, acc = model.evulate(y_test, y_pred)
print("Clasif report, conf matrix")