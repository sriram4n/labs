import numpy as np
from sklearn.model_selection import KFold
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x = np.concatenate(x_train , x_test , axis = 0)
y = np.concatenate(y_train, y_test, axis = 0)

x = x.astype("float32") / 255.0
x = x.reshape(-1,28,28,1)

y = to_categorical(y,10)

kf = KFold(n_spits = 10, shuffle = True, random_state = 42)

scores = []

for train, test in kf.split(x):
    model = Sequential([
        Conv2D(32, (3,3), activation = 'relu', input_shape = (28,28,1))
        MaxPooling2D((2,2))
        Flatten()
        Dense(128, activation = 'relu')
        Dense(10 , activation = 'softmax')
    ])

    model.compile(optimizer="adam",
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])
    
    model.fit(x[train] , y[train] , epochs = 3)

    loss , acc = model.evaluate(x[test] , y[test])
    scores.append(acc*100)

# print avg sd