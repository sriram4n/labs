# 5 input, 3,2,3 hidden, 1 output 
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

def tanH(x):
    return np.tanh(x)

#input
x = np.array([1,2,3,4,5]).reshape(5,1)
print("Input: ",x)

# weighted sum 
z1 = np.dot(w1,x) + b1
print("Weighted sum layer 1: ",z1)

# activation 
a1 = tanH(z1)
print("Activation layer 1: ",a1)

# weighted sum for 2nd layer
z2 = np.dot(w2,a1) + b2
print("Weighted sum layer 2: ",z2)

# activation layer 2
a2 = tanH(z2)
print("Activation layer 2: ",a2)

# weighted sum for layer 3
z3 = np.dot(w3,a2) + b3
print("Weighted sum layer 3: ",z3)

# activation layer 3
a3 = tanH(z3)
print("Activation layer 3: ",a3)

# weighted sum layer 4
z4 = np.dot(w4, a3) + b4
print("Weighted sum layer 4: ",z4)

# activation layer 4
output = tanH(z4)
print("output: ",output)
