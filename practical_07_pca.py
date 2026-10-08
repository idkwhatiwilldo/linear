import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = np.array([
    [2, 4, 1, 3],
    [3, 5, 2, 4],
    [4, 6, 3, 5],
    [5, 7, 4, 6],
    [6, 8, 5, 7],
    [7, 9, 6, 8],
])

data_scaled = StandardScaler().fit_transform(data)
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

print("Principal Components:")
print(data_pca)
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

plt.scatter(data_pca[:, 0], data_pca[:, 1])
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Projection")
plt.grid(True)
plt.show()
