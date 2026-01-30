import numpy as np
arr = np.array([1, 2, 3, 4, 5],ndmin=5)
# print(arr[0,0,0,0,1])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[::2])

arr1 = [1,[2,4,5],3,4,5]
'''
arr1[1] ==> [2,4,5] (list)
arr1[1][1] ==> 4 
'''
arrz = np.array(12)
arr2 = np.array([[1, 2, 3, 4, 5],[2,4,6,8,10]])
# print(arr2[0:2, 1:3])  
# print(arr2[0, 1:3])

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr3[1:, 1:])

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [12, 5, 6]]])
# print("Original array:", d[1,1,0])
# print(type(arr))
# print(type(arr1))
# print(arr.ndim)
# print(arrz.ndim)
# print(arr2.ndim)

# print("Array with single value:", arrz)
