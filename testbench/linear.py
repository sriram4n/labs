import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 


df = pd.read_csv("testbench/Studied.csv")

x = df[["hours_studied"]]
y = df["marks"]

model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)
sree = model.predict([[3]])

plt.scatter(x,y, color = 'red', label = 'Hours Studied')
plt.plot(x, y_pred, label = 'regression line')
plt.legend()
plt.show()

print("sree's marks: ", sree)
