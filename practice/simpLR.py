import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


x = np.array([10,20,30,40,50,60]).reshape(-1,1)
y = np.array([1,2,4,5,6,7])

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

print("slope: ", model.coef_[0])
print("Intercept: ", model.intercept_)

plt.scatter(x,y, label = "Points")
plt.xlabel("x")
plt.ylabel("Y")
plt.plot(x,y_pred, label = "regression line")
plt.legend()
plt.show()