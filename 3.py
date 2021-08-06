import numpy as np

arr = np.random.randint(-5, 10, 10)
print(arr)
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.sum())
print(arr.std())
print(np.median(arr))
print(arr < 2)


x = np.insert(arr, 2, -20)
print(x)
x = np.delete(arr,2)
print(x)
x = np.sort(arr)
print(x)
arr2 = np.array([0,0,0])
arr = np.concatenate((arr, arr2))
print(arr)
x = np.array_split(arr,3)
print(x)