import pandas as pd

num_series = pd.Series([10, 20, 30, 40, 50])
str_series = pd.Series(["Apple", "Banana", "Cherry", "Mango", "Orange"])

num_list = num_series.tolist()
str_list = str_series.tolist()

print("Numeric Series : ")
print(num_series)
print("Converted to Python list : ", num_list)
print("\nString Series : ")
print(str_series)
print("Converted to Python list : ", str_list)
