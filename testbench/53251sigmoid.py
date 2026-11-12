import numpy as np
np.random.seed(42)

w1 = np.random.randn(3,5)
b1 = np.random.randn(3,1)

w2 = np.random.randn(2,3)
b2 = np.random.randn(2,1)

w3 = np.random.randn(3,2)
b3 = np.random.randn(3,1)

w4 = np.random.randn(1,3)
b4 = np.random.randn(1,1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

input = np.array([1,2,3,4,5]).reshape(5,1)

z1 = np.dot(w1, input) + b1
print("Weighted sum (first: )", z1)
a1 = sigmoid(z1)
print("Activation (first layer): ", a1)

z2 = np.dot(w2, a1) + b2
print("Weighted sum (second layer: )", z2)
a2 = sigmoid(z2)
print("Activation (second layer): ", a2)

z3 = np.dot(w3, a2) + b3
print("Weighted sum (third layer): ", z3)
a3 = sigmoid(z3)
print("Activation (layer 3): ", a3)

z4 = np.dot(w4, a3) + b4
print("Weighted sum (layer 4): ", z4)
a4 = sigmoid(z4)
print("network output: ", a4)