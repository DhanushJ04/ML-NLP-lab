# compare elements of two pandas series

import pandas as pd

# create two pandas series
s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

# compare the two series
print("Series1 == Series2")
print(s1 == s2)

print("\nSeries1 > Series2")
print(s1 > s2)

print("\nSeries1 < Series2")
print(s1 < s2)
