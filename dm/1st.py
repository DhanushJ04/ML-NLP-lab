# Create a NumPy array using linspace and arrange and display details

import numpy as np


arr = np.linspace(1, 20, 10)
arr_reshaped = arr.reshape(2, 5)
print("Original array : ", arr)
print("Modified array :", arr_reshaped)
print("Shape of the array : ", arr_reshaped.shape)
print("Size of the array : ", arr_reshaped.size)
print("Number of dimensions : ", arr_reshaped.ndim)
print("Data type of elements : ", arr_reshaped.dtype)
