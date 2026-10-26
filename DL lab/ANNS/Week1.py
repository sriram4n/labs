import numpy as np 

np.random.seed(42)
# input to hidden layer
w1 = np.random.randn(2,2)
b1 = np.random.randn(2,1)
w2 = np.random.randn(2,1)
b2 = np.random.randn(1,1)

print("Weights (Input -> hidden): ",w1)
print("bais (Hidden layer): ", b1)
print("Weights (hidden -> output): ",w2)
print("bais (output layer): ",b2)
