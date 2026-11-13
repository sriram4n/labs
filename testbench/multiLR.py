import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('testbench/house.csv')

x = df[["Area","Bedrooms","Age"]]
y = df["Price"]

model = LinearRegression()

model.fit(x, y)

pred = model.predict([[3200,3,1]])

print("predicted value: ", pred)
