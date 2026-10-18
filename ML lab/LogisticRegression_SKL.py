from sklearn.linear_model import LogisticRegression
import numpy as np 
# any data, ex: weights (isObese), marks(isPass)
x = np.array([40, 50, 44, 30, 45, 30, 23, 34, 45]).reshape(-1, 1)
# 1 = pass, 0 = fail
y = np.array([1,1,1,0,1,0,0,1,1])

model = LogisticRegression()
model.fit(x, y)

marks = np.array([[32]])
y_pred = model.predict(marks)
prob = model.predict_proba(marks)

if(y_pred == 1):
    print("qualified")
else:
    print("not qualified")

print("not qualified chance: ", prob[0][0])
print("qualified chance: ", prob[0][1])