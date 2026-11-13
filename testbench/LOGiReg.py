import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('testbench/Pass.csv')

x = df[["marks"]]
y = df["pass"]

model = LogisticRegression()
model.fit(x,y)

inp = int(input("Enter marks: "))
pred = model.predict([[inp]])
if pred[0] == 1:
    print("pass")
else:
    print("Fail")
print("Chance of fail: ", model.predict_proba([[inp]])[0][0])
print("Chance of pass: ", model.predict_proba([[inp]])[0][1])