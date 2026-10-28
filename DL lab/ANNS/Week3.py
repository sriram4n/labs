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

print("Weights: (input -> hidden) w1: ",w1)
print("bais: hidden layer 1: ", b1)
print("Weight (hidden layer 1 -> layer 2): ",w2)
print("bais: hidden layer 2: ", b2)
print("Weight (hidden layer 2 -> layer 3): ",w3)
print("bais: hidden layer 3: ", b3)
print("Weight (hidden layer 3 -> output layer): ",w4)
print("bais: output layer: ", b4)