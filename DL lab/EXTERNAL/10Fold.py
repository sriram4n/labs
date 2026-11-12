
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import KFold

# load data
print("Loading mnist dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# combine train and test data
X = np.concatenate((x_train, x_test)) 
y = np.concatenate((y_train, y_test)) 

# normalize
print("Preparing images")
X = X.astype("float32")/255.0

# reshape
X = X[..., np.newaxis]
y = y.astype("int64")

print("Dataset shape: ", X.shape)
print("Labels shape: ", y.shape)

# 10 fold cross validation
kf = KFold(n_splits=10, shuffle=True, random_state=42)

fold_accuracies = []

for fold, (train, val) in enumerate(kf.split(X), start=1):

    print("Fold: ", fold)

    X_train = X[train]
    X_val = X[val]

    y_train = y[train]
    y_val = y[val]

    # build model
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

    # train
    model.fit(X_train, y_train,
        epochs=1,
        batch_size=128,
        verbose=1
    )

    # evaluate
    loss, acc = model.evaluate(X_val, y_val, verbose=0)

    print("Fold", fold, "Accuracy: ", acc)
    fold_accuracies.append(acc)


print("Mean Accuracy: ",  np.mean(fold_accuracies))
print("Standard Deviation: ",  np.std(fold_accuracies))
