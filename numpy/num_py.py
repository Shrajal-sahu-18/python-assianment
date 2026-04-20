import numpy as np
import time

size = 10_000_000

py_list = list(range(size))
start = time.time()
sqare = [x**2 for x in py_list]
end = time.time()
print(f"pythonlist time = {end-start}")

np_arr = np.array(py_list)
start = time.time()
sqare = np_arr ** 2
end = time.time()
print(f"numpy array time = {end-start}")


import sys
print(f"size of py_list = {sys.getsizeof(py_list)*len(py_list)}bytes")
print(f"size of numpy array = {np_arr.nbytes} bytes")



arr1 = np.array([1,2,3,4,5,6])
print(arr1,type(arr1),arr1.shape,arr1.dtype)

arr2 = np.array([1,2,3,4,5,"prime"])
print(arr2.dtype,arr2.shape,arr2,type(arr2))


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d.shape,arr2d.dtype,arr2d,type(arr2d))


#zeros in numpy
arr3 = np.zeros((2,3))
print(arr3,arr3.shape)

arr4 = np.zeros((2,3),dtype = "int64")
print(arr4,arr4.dtype)

arr5 = np.ones((2,3),dtype = "int64")
print(arr5,arr5.shape,arr5.dtype)


arr6 = np.full((2,3),100)
print(arr6)

arr7 = np.eye(3,dtype = "int64")
print(arr7)