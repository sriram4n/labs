import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

x_mean = np.mean(x)
y_mean = np.mean(y)

# y = a + bx

b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean )**2)
a = y_mean - b * x_mean

y_pred = a + b * x

print("predicted eqn")
print("y = " , a ," + " , b , " * ", " x ")

plt.scatter(x,y , color = "blue", label = "Actual data")
plt.plot(x,y_pred, color = "red", label = "regression line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()