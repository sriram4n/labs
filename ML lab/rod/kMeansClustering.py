import math

X = [2, 2, 8, 5, 7, 6, 1, 4]
Y = [10, 5, 4, 8, 5, 4, 2, 9]

# centroid points on cluster
a = [2, 10]
b = [5, 8]
c = [1, 2]

cluster1 = []
cluster2 = []
cluster3 = []

# Euclidean distance
def dist(a, b):
    return math.sqrt(
        (a[0] - b[0])**2 + (a[1] - b[1])**2
    )

# Calculate centroid, aka mean
def find_centroid(points):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return [x, y]

while True:
    c1, c2, c3 = [], [], []

    for i in range(len(X)):
        point = [X[i], Y[i]]

        d1 = dist(a, point)
        d2 = dist(b, point)
        d3 = dist(c, point)

        # appening minimum point
        if d1 <= d2 and d1 <= d3:
            c1.append(point)
        elif d2 <= d1 and d2 <= d3:
            c2.append(point)
        else:
            c3.append(point)
    # tie, do nothing
    if (c1 == cluster1 and
        c2 == cluster2 and
        c3 == cluster3):
        break
    
    # add to main clusters
    cluster1 = c1
    cluster2 = c2
    cluster3 = c3
    
    # update centroids
    if len(c1) > 0:
        a = find_centroid(c1)
    if len(c2) > 0:
        b = find_centroid(c2)
    if len(c3) > 0:
        c = find_centroid(c3)

print("Cluster 1:")
print("Points:", cluster1)
print("Centroid:", a)

print("\nCluster 2:")
print("Points:", cluster2)
print("Centroid:", b)

print("\nCluster 3:")
print("Points:", cluster3)
print("Centroid:", c)
