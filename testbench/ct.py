x = [24,32,4,32,4,23,12,3,23,42,34,21,3,12,3,1,23,12,3,123,12,3,2,2]
mean = sum(x) / len(x)
print("mean: ", mean)
n = len(x)
xs = sorted(x)
if(n % 2 == 0):
    median = xs[n // 2] + xs[n // 2 - 1] / 2
else: median = xs[n // 2]
print("Median", median)
print("Mode: ", max(x, key = x.count))

std = sum((a - mean)**2 for a in x) / n
print("std: ", std)

print("var: ", std**0.5)