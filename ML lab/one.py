import statistics

arr = [10,10,30,40,20,30,24,20,31,12,33]

mean = sum(arr) / len(arr)

sorted_arr = sorted(arr)
n = len(arr)

if n % 2 == 0:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
else:
    median = sorted_arr[n // 2]

mode = max(arr, key=arr.count)

var = sum((x - mean) ** 2 for x in arr) / n
stddev = var ** 0.5

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Variance:", var)
print("Standard deviation:", stddev)

print("Mean:", statistics.mean(arr))
print("Median:", statistics.median(arr))
print("Mode:", statistics.mode(arr))
print("Sample variance:", statistics.variance(arr))
print("Sample standard deviation:", statistics.stdev(arr))
