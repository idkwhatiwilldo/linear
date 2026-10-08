import numpy as np

# 2x + y = 5 and x + 3y = 6
A = np.array([[2, 1], [1, 3]])
B = np.array([5, 6])
solution = np.linalg.solve(A, B)
x, y = solution

print("x =", x)
print("y =", y)
print("Verification:")
print(2 * x + y)
print(x + 3 * y)
