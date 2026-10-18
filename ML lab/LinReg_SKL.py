import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([10,20,30,40,50])

model = LinearRegression()
model.fit(x,y)

pred = model.predict(np.array([[6]]))
print("slope (b1) : ", model.coef_[0])
print("Intercept (b0): ", model.intercept_)
print("predicted value for x  = ", pred)

print("predicted eqn")
print("y = " , model.intercept_ ," + " , model.coef_[0] , " * ", " x ")

y_pred = model.predict(x)

plt.scatter(x,y, color = 'red', label = "initial data")
plt.plot(x,y_pred, color = 'blue' , label = 'regression line')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()