import numpy as np

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix[1, 2])
print(matrix[2])
print(matrix[:, 2])
print(matrix[1:3, 0:2])
print(matrix[matrix > 2])

