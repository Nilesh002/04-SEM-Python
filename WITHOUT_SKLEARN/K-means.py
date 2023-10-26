import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
X=np.random.rand(1000,2)

m,n=X.shape

iter=100

centroids=X[np.random.choice(m,k,replace='False')]

for i in range(iter):
  distances=np.linalg.norm(X[:,np.newaxis]-centroids,axis=2)
  labels=np.argmin(distances,axis=1)
  new_cenntroids=np.array([X[labels==i].mean(axis=0) for i in range(k)])

  if np.all(centroids==new_centroids):
    break
  centroids=new_centroids

colors=['r','g','b']
for i in range(k):
  plt.scatter(X[labels==i,0],X[labels==i,1],c=colors[i],label=f'cluster{i+1}')

plt.scatter(centroids[:,0],centroids[:,1],marker='X',c='k',label='centroids')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'K-means clustering K={k}')