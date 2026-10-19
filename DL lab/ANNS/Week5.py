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

x = np.array([1,2,3,4,5]).reshape(5,1)
print("Input: ",x)

def ReLU(x):
    return np.maximum(0,x)

# first layer 
z1 = np.dot(w1,x) + b1
a1 = ReLU(z1)
print("Layer 1 weighted sum: ",z1)
print("Layer 1 activation: ", a1)

# 2nd layer
z2 = np.dot(w2, a1) + b2
a2 = ReLU(z2)
print("Layer 2 weighted sum: ",z2)
print("Layer 2 activation: ", a2)

# 3rd layer
z3 = np.dot(w3, a2) + b3 
a3 = ReLU(z3)
print("Layer 3 weighted sum: ",z3)
print("Layer 3 activation: ", a3)

# 4th layer 
z4 = np.dot(w4, a3) + b4
a4 = ReLU(z4)
print("Layer 4 weighted sum: ",z4)
print("output: ", a4)
