import numpy as np

arr = np.array([1, -2, 3, -4, 5])
arr[0] = 0
print(arr[2])
print(arr[0:2])
print(arr[::-1])
print(arr[(arr < 2) & (arr > 0)])
print(arr[(arr > 4) | (arr < 0)])
arr[1:4] = 0
print(arr)
