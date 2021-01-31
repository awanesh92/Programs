import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#cluster centroids with k-means
def clusterkmeans(ds,k):
    np.random.seed(43)
    centroids = [ds[0]]

    for _ in range(1, k):
        dsq = np.array([min([np.inner(c - x, c - x) for c in centroids]) for x in ds])
        probs = dsq / dsq.sum()
        cprobs = probs.cumsum()
        r = np.random.rand()

        for j, p in enumerate(cprobs):
            if r < p:
                i = j
                break

        centroids.append(ds[i])

    return np.array(centroids)


def Kmeans(X, k):
    centrd1=clusterkmeans(X,k)
    plt.scatter(X[:, 0], X[:, 1])
    plt.scatter(centrd1[:,0],centrd1[:,1],c='red')
    plt.show()

x, y = make_blobs(n_samples=48, centers=4, cluster_std=0.60, random_state=0)
Kmeans(x, 4)
