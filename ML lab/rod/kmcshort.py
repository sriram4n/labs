import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = np.array([
    [1, 2], [2, 3], [3, 2],
    [8, 8], [9, 10], [10, 9],
    [15, 2], [16, 3], [17, 2]
])

model = KMeans(n_clusters = 3)

labels = model.fit_predict(X)

print("Labels: ", labels)
print("Centers: ", model.cluster_centers_)

# points
plt.scatter(X[:,0], X[:,1], c = labels)
# cluster center
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:,1], marker = 'x')


plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.show()