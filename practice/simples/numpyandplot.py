import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,2,3,4,5,6,7])
b = np.array([11,22,33,44,55,66,77])

print("Addition: ", np.add(a,b))
print("Subtraction: ", np.subtract(a,b))
print("Multiplication: ",np.multiply(a,b))
print("Division: ", np.divide(a,b))

print("mean:", np.mean(a))
print("var: ", np.var(a))
print("std: ", np.std(a))

print("max:" , np.max(a))
print("min: ", np.min(a))

plt.scatter(a,b, color = 'red', label = 'points')
plt.plot(a,b, color = 'blue' , label = 'line plot')
plt.xlabel("a")
plt.ylabel("b")
plt.legend()
plt.show()

plt.bar(range(len(a)), a)
plt.show()