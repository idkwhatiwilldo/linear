import numpy as np

A = np.array([[4, 2], [3, 1]])
B = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])

print("Determinant of A:", np.linalg.det(A))
print("Rank of A:", np.linalg.matrix_rank(A))
print("Rank of B:", np.linalg.matrix_rank(B))
