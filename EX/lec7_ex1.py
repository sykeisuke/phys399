import numpy as np

A = np.array([
    [ 1,  1,  1,  1,  1],
    [ 3,  2,  1, -1, -1],
    [ 2, -1,  1,  1,  1],
    [ 1,  4,  2, -1,  1],
    [ 2,  1, -1,  3,  2]
])

b = np.array([11, 5, 8, 16, 13])

x = np.linalg.solve(A, b)  
print("[x, y, z, w, v] =", x)

print("A @ x =", A @ x)

