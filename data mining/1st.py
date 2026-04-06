import numpy as np
arr = np.linspace(1, 20, 10)
print(arr)
arr_reshaped = arr.reshape(2, 5)
print("Array elements : \n", arr_reshaped)
print("Shape of array : \n", arr_reshaped.shape)
print("Size of array : \n", arr_reshaped.size)
print("Number of dimensions : ", arr_reshaped.ndim)
print("Data type of elements : ", arr_reshaped.dtype)
