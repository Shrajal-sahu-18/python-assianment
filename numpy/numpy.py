import numpy as np
import time

size = 10_000_000

py_list = list(range(size))
start = time.time()
sqare = [x**2 for x in py_list]
end = time.time()
print(f"pythonlist time = {end-start}")
