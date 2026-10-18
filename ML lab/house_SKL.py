import numpy as np 
from sklearn.linear_model import LinearRegression

# x , [area, bedroom, age]
x = np.array(
    [[1000, 2, 3],
    [1240, 2, 2],
    [3000, 3, 10],
    [10000, 6, 15],
    [3000, 2, 4],
    [5000, 4, 4],
    [2300, 3, 6]]
)
# prices for each (lakhs)
y = np.array(
    [40,41,65,160,90,120,55]
)

model = LinearRegression()
model.fit(x,y)

print("Intercept coefficient : ", model.intercept_)
print("Area coef: ", model.coef_[0])
print("Bedroom coef: ", model.coef_[1])
print("Age coef:", model.coef_[2])
print()
print("Welcome to prediction")
area = int(input("Enter Area: "))
bedrooms = int(input("Enter no. of bedrooms: "))
age = int(input("Enter age: "))

y_pred = model.predict([[area,bedrooms,age]])
print("predicted price : ", y_pred , " lakhs")