import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4,6,73,8,10])
arr3 = np.array([[4,6,73,8,10],[4,2,34,5,6]])
arr1 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arrar = np.concatenate((arr1, arr4), axis=1)
print("concatenated array:", np.concatenate((arr, arr2)))
print("arrar ", arrar)
try:
    ar = np.array([1, 2, 3, 4, 5])
    ar2 = np.array([4,6,73,8,10])
    ar3 = np.array([[4,6,73,8,10],[4,2]])
    a = np.concatenate((ar, ar3))
    print("concatenated array:",a)
except Exception as e :
    print("Error")
x = arr.copy()
y = arr.view()
print("Original array:", arr)
print("Copy of the array:", x)
print("View of the array:", y)
arr[0] = 10
y[1] = 20
x[2] = 30
print("After modifying the original array:")
print("Original array:", arr)
print("Copy of the array (unchanged):", x)
print("View of the array (changed):", y)

print(x.base)
print(y.base)