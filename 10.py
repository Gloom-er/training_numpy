import numpy as np

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(matrix)

print(matrix.T)
print(matrix.flatten())
print(np.trace(matrix))
print(np.linalg.det(matrix))
print(np.linalg.matrix_rank(matrix))

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)

print(np.info(np.eye))

np.loadtxt('file.txt')  # загрузка в текстовый файл
np.genfromtxt('file.csv', delimiter=',')  # загрузка из csv файла
np.savetxt('file.text', matrix, delimiter=' ')  # сохранение тексового файла
np.savetxt('file.csv', matrix, delimiter=' ')  # сохранение csv файла
