import numpy as np
from tensorflow.keras.dataests import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score

(x_train, y_train), (x_test, y_test) = mnist.load_data() 

# normalize
x_train = x_train / 255.0
y_train = y_train / 255.0

# model
model = Sequential([
    SimpleRNN(64, input_shape = (28,28))
    Dense(10, activation = "softmax")
])
# Step 4: Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
model.fit(x_train, y_train, epochs = 5)

y_pred = np.argmax(mdoel.predict(x_test), axis = 1)

print(accuracy_score(y_test, y_pred))
print(precision_score(y_test, y_pred, average = 'weighted'))