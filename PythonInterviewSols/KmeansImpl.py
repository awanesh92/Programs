import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#cluster centroids with k-means
def centroidsrand(ds,k):
    np.random.seed(42)
    centroids = [ds[0]]
    result=[]
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
    for i in range(len(ds)):
        mi=[]
        for j in range(len(centroids)):
            mi.append([ds[i][0]-centroids[j][0],ds[i][1]-centroids[j][1]])
        
    return np.array(centroids),result


def Kmeans(X, k):
    centrd1,rest=centroidsrand(X,k)
    print(rest)
    plt.scatter(X[:, 0], X[:, 1])
    plt.scatter(centrd1[:,0],centrd1[:,1],c='red')
    plt.show()

x, y = make_blobs(n_samples=50, centers=5, cluster_std=0.35, random_state=0)
print(y)
Kmeans(x, 5)
