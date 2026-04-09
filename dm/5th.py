# mean, median, mode, and standard deviation

import pandas as pd

# accept input
data = input("Enter numbers separated by space : ")

# convert input string into list
num_list = list(map(int, data.split()))

# create pandas series
series = pd.Series(num_list)

# calculate statistics
mean_value = series.mean()
median_value = series.median()
mode_value = series.mode()
std_value = series.std()

# display results
print("\nGiven Series : ")
print(series)
print("\nMean : ", mean_value)
print("\nMedian : ", median_value)
print("\nMode : ", list(mode_value))
print("\nStandard Deviation : ", std_value)
