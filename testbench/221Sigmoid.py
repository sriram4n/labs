import numpy as np
np.random.seed(42)
 
w1 = np.random.randn(2,2)
b1 = np.random.randn(2,1)

w2 = np.random.randn(1,2)
b2 = np.random.randn(1,1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

input = np.array([0.5,0.8]).reshape(2,1)

z1 = np.dot(w1, input) + b1
print("Weighted sum (hidden layer): ", z1)
a1 = sigmoid(z1)
print("Activation of hidden layer: ",a1)
print("Activation of first node: ", a1[0])
print("Activation of second node: ", a1[1])

z2 = np.dot(w2, a1) + b2
print("Weighted sum (output layer): ", z2)
a2 = sigmoid(z2)
print("network output: ",a2)
