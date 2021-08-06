import numpy as np

matrix1 = np.array([(1, 2), (3, 4)])
print(matrix1)
matrix2 = np.array([(5, 6), (7, 8)])
print(matrix2)
print(matrix1+matrix2)
print(matrix1-matrix2)
print(matrix1*matrix2)
print(matrix1/matrix2)
print(matrix1.dot(matrix2))