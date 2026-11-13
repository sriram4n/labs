import numpy as np
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

# add column of 1s to x 
x = np.c_[np.ones(x.shape[0]),x]

# use formula
b = np.linalg.inv(x.T @ x) @ x.T @ y

print("Intercept coefficient : ", b[0])
print("Area coef: ", b[1])
print("Bedroom coef: ",b[2])
print("Age coef:",b[3])
print()
print("Welcome to prediction")
area = int(input("Enter Area: "))
bedrooms = int(input("Enter no. of bedrooms: "))
age = int(input("Enter age: "))

y_pred = (b[0] + area * b[1] + bedrooms * b[2] + age * b[3])
print("predicted : ", y_pred ," lakhs ")