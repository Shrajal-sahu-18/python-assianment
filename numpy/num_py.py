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

arr8  = np.arange(0,10)
print(arr8)

arr = np.array([[1,2,3],[4,5,6]])
print(arr,arr.shape)
reshaped = arr.reshape(3,2)
print(reshaped)

#for converting 2d array to 1d array
flattened = arr.flatten()
print(flattened) 

#normal indexing
arr = np.array([1,2,3,4,5,6,7])
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1[0][2])
print(arr1[1][1])
print(arr[3])

#fancy indexing
arr = np.array([1,2,3,4,5,6])
idx = [2,3,4]
print(arr[idx])



#bollean indexing
arr = np.array([1,2,3,4,5,6])
print(arr[arr>2])
print("even number",arr[arr % 2 == 0])
print("odd number",arr[arr % 2 != 0])


#slicing
arr  = np.array([1,2,3,4,5,6])
print(arr[1:4])
print(arr[2:6])
print(arr[:5])
print(arr[0:])
print(arr[::2])



#copy vs view in python list and numpy array
nums = [1,2,3,4,5]
sub_list = nums[1:3]
print(sub_list)
sub_list[0] = 200
print(sub_list)
print(nums)

arr =  np.array([1,2,3,4,5])
sub_arr = arr[1:3]
print(sub_arr)
sub_arr[0] = 200
print(sub_arr)
print(arr)


#string data type 
arr = np.array([1,2,3,4,5.4,"prime"])
print(arr,arr.dtype)

#complex data type
arr = np.array([3+5j])
print(arr,arr.dtype)

arr1 = np.array([3+5j])
arr2 = np.array([3+5j])
print(arr1+arr2)
print(arr1-arr2)

#object data type
arr = np.array(["prime",{1,2,3},3.14])
print(arr.dtype)

#multidimensional array
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d,arr2d.shape)
print(np.sum(arr2d))
sum_column = np.sum(arr2d,axis = 0)
print(sum_column)
sum_row = np.sum(arr2d,axis = 1)
print(sum_row)
print(arr2d[0:2,2:])
print(arr2d[0:2,1:2])



#3d array
arr3d = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]])# 2 x 3 x2
print(arr3d,arr3d.shape)

#indexing
print(arr3d[0,1,1])
print(arr3d[0,2,1])
print(arr3d[1,1,1])
#slicing
print(arr3d[:,0,:]) #first row from both layers
print(arr3d[:,:,0]) #column
arr3d[:,0,:] = 99
print(arr3d)


#vectorization and broadcasting
arr = np.array([1,2,3,4,5,6])
arr1 = np.array([7,8,9,10,11,12])
print(arr**2)
print(arr + 10)
print(arr+arr1)

#noramalize
arr = np.array([[1,2],[3,4]])
mean = (np.mean(arr))
std_dev = (np.std(arr))
normalized_array = (arr-mean)/std_dev
print(normalized_array)
print(mean)
print(std_dev)
print(np.sqrt(5/4))


#mathematical fnx
arr = np.array([1,2,3,4,5])
print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.median(arr))
print(np.var(arr))