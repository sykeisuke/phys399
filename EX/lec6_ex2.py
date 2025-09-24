import numpy as np

A = np.array([[2,1], [1,3]])
B = np.array([[4,0], [2,1]])

print("A x B =\n", A @ B)
print("A^T =\n", A.T)
print("A^-1 =\n", np.linalg.inv(A))

