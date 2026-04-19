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