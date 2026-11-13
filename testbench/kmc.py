import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x = np.array([
    [1, 2], [2, 3], [3, 2],
    [8, 8], [9, 10], [10, 9],
    [15, 2], [16, 3], [17, 2]
])

model = KMeans(n_clusters = 3)

labels = model.fit_predict(x)
print("labels: ", labels)
print("Cluster centers: ", model.cluster_centers_)

plt.scatter(x[:,0], x[:,1], c = labels)
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], marker = 'x')

plt.show()