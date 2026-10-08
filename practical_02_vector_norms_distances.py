import numpy as np

A = np.array([3, 4])
B = np.array([6, 8])

print("L1 Norm:", np.linalg.norm(A, ord=1))
print("L2 Norm:", np.linalg.norm(A))
print("Euclidean Distance:", np.linalg.norm(A - B))
