import numpy as np

data = [1, 2, 3, 4, 5]
arr = np.array(data)
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.ndim)

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)
print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)

arr3 = np.array([1, 2, 3, 4, 5], dtype=float)
print(arr3)
print(arr3.shape)
print(arr3.dtype)
print(arr3.ndim)
print(len(arr3))
print(arr3.size)

arr3 = arr3.astype(np.int64)
print(arr3)
print(arr3.dtype)

arr4 = np.arange(0, 20, 1.5)
print(arr4)

arr5 = np.linspace(0, 2, 50)
print(arr5)

random_arr = np.random.random(5,)
print(random_arr)

random_arr2 = np.random.random_sample(5,)
print(random_arr2)

random_arr3 = (10--5) * np.random.random_sample(5,) - 5
print(random_arr3)