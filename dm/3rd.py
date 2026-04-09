# Create pandas series and convert to python list

import pandas as pd

# create a series
num_series = pd.Series([10, 20, 30, 40, 50])
str_series = pd.Series(["Apple", "Banana", "Cherry", "Mango", "Orange"])

# convert series to list
num_list = num_series.tolist()
str_list = str_series.tolist()

# Display
print("Numeric Series : ")
print(num_series)
print("\nConverted to python : ")
print(num_list)
print("\nString Series : ")
print(str_series)
print("\nConverted to python : ")
print(str_list)
