import numpy as np

matrix = np.array([(1, 2, 3), (4, 5, 6)], dtype=np.float64)
print(matrix)

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.reshape(1, 9))

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (11, 12, 13)])
print(matrix)
print(matrix.reshape((2, 6)))

matrix2 = np.random.random((2, 2))
print(matrix2)
matrix = np.resize(matrix, (2, 2))
print(matrix)

new_matrix = np.arange(16).reshape(2, 8)
print(new_matrix)
