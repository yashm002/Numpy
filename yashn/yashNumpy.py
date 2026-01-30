import numpy as np

arr = np.array([1, 2, 3, 4, 5], ndmin=5)
print("5D Array element:", arr[0, 0, 0, 0, 1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Every second element:", arr[::2])

arr2 = np.array([
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10]
])
print("2D slice:\n", arr2[0:2, 1:3])

d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [12, 5, 6]]
])
print("3D element:", d[1, 1, 2])


arrz = np.array(12)
print("Type of arr:", type(arr))
print("Type of arr2:", type(arr2))

print("Dimensions of arr:", arr.ndim)
print("Dimensions of arrz:", arrz.ndim)
print("Dimensions of arr2:", arr2.ndim)

print("Sum of arr2:", np.sum(arr2))
print("Mean of arr2:", np.mean(arr2))
print("Max of arr2:", np.max(arr2))
