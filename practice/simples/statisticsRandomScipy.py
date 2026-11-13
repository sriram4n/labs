import statistics as st

a = [10, 20, 30, 40, 50, 20, 30]

print("Data:", a)

print("Mean:", st.mean(a))
print("Median:", st.median(a))
print("Mode:", st.mode(a))
print("Variance:", st.variance(a))
print("Standard Deviation:", st.stdev(a))

print("Population Variance:", st.pvariance(a))
print("Population Standard Deviation:", st.pstdev(a))

print("Harmonic Mean:", st.harmonic_mean(a))
print("Geometric Mean:", st.geometric_mean(a))


import random

print("Random number:", random.random())
print("Random integer:", random.randint(1, 100))
print("Random choice:", random.choice(['a','b']))



import numpy as np
import scipy
from scipy import integrate, optimize, linalg, stats, signal

a = np.array([10, 20, 30, 40, 50, 20, 30])

# Statistics
print("Mean:", stats.tmean(a))
print("Mode:", stats.mode(a).mode)
print("Skewness:", stats.skew(a))

# Integration
result, error = integrate.quad(lambda x: x**2, 0, 3)
print("Integration:", result)

# Optimization
result = optimize.minimize(lambda x: x**2, 5)
print("Minimum:", result.fun)

# Linear Algebra
b = np.array([[1, 2], [3, 4]])
print("Determinant:", linalg.det(b))
print("Inverse:\n", linalg.inv(b))
print("Eigenvalues:", linalg.eigvals(b))

# Signal Processing
print("Convolution:", signal.convolve([1, 2, 3], [1, 2]))
print("Peaks:", signal.find_peaks([1, 3, 1, 5, 1]))

