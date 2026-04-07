import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generating sample data
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualize
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Unlabelled Data")
plt.show()

# Initialize the K-Means model
kmeans = KMeans(n_clusters=4, random_state=0, n_init=10)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Visualize
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50)

# Plot
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200)
plt.title("Data Clustered with K-Means")
plt.show()