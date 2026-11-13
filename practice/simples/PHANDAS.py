import pandas as pd

data = {
    'id': [1,2,3,4,5],
    'names': ["RAvi", "sushma", "Jensen", "Rakesh", "prakash"],
    'salary': [20000,30000,23000,32000,23000],
    'projects': [1,3,2,2,1]
}

df = pd.DataFrame(data)

# adding
df.loc[len(df)] = [6, "huang", 10000, 0]
print("After adding", df)

df = df.drop(5) #index
print("After dropping:", df)

print("emp with sal > 20000")
print(df[df["salary"] > 25000])

print("names")
print(df["names"])

print("first 2")
print(df.head(2))

print("last 2")
print(df.tail(2))

df.to_csv("employee.csv")