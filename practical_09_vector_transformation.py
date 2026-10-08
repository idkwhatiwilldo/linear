import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 1])
A = np.array([[2, 0], [0, 3]])
transformed_v = A @ v

print("Original Vector:", v)
print("Transformation Matrix:")
print(A)
print("Transformed Vector:", transformed_v)

plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1,
           color="blue", label="Original")
plt.quiver(0, 0, transformed_v[0], transformed_v[1], angles="xy",
           scale_units="xy", scale=1, color="red", label="Transformed")
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid(True)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Vector Transformation")
plt.show()
