# Convert a  numpy array to a pandas series

import numpy as np
import pandas as pd

# numpy array
arr = np.array([10, 20, 30, 40, 50])
print("Numpy array : ")
print(arr)

# numpy to pandas
series = pd.Series(arr)

print("\nPandas series : ")
print(series)
