# Use an activation function and calculate weighted sums
import numpy as np
np.random.seed(42)

# Initialize weights and biases
w1 = np.random.randn(2, 2)
b1 = np.random.randn(2, 1)
w2 = np.random.randn(1, 2)
b2 = np.random.randn(1, 1)

# Input as a column vector
x = np.array([1, 2]).reshape(2, 1)
print("Input:", x)

# Activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Weighted sum at hidden layer
z1 = np.dot(w1, x) + b1
print("\nWeighted sum at hidden layer (z1):")
print(z1)

# Activation of hidden layer
A1 = sigmoid(z1)

print("\nActivation of first hidden node:")
print(A1[0][0])

print("\nActivation of second hidden node:")
print(A1[1][0])

print("\nHidden layer activation:")
print(A1)

# Weighted sum at output layer
z2 = np.dot(w2, A1) + b2
print("\nWeighted sum at output layer (z2):")
print(z2)
