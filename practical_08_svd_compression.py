import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [10, 10, 10, 10, 10],
    [10, 50, 50, 50, 10],
    [10, 50, 90, 50, 10],
    [10, 50, 50, 50, 10],
    [10, 10, 10, 10, 10],
])

U, S, VT = np.linalg.svd(A)
k = 2
compressed = U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

print("Singular Values:")
print(S)
print("Compressed Matrix:")
print(compressed)

plt.figure(figsize=(8, 3))
plt.subplot(1, 2, 1)
plt.imshow(A, cmap="gray")
plt.title("Original")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(compressed, cmap="gray")
plt.title("Compressed")
plt.axis("off")
plt.tight_layout()
plt.show()
