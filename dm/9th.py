# join operations

import pandas as pd

# first dataframe
data1 = {
    "Roll_No": [101, 102, 103],
    "Name": ["Amita", "Ravi", "Sneha"],
    "Age": [21, 22, 20],
    "Course": ["MBA", "BBA", "MBA"]
}
df1 = pd.DataFrame(data1)

# second dataframe
data2 = {
    "Roll_No": [102, 103, 104],
    "Name": ["Ravi", "Sneha", "Kiran"],
    "Age": [22, 20, 23],
    "City": ["Delhi", "Mumbai", "Chennai"]
}
df2 = pd.DataFrame(data2)

print("DataFrame 1 : ")
print(df1)
print("\nDataFrame 2 : ")
print(df2)

# Inner Join
inner_join = pd.merge(df1, df2, on="Roll_No", how="inner")
print("\nInner Join : ")
print(inner_join)

# Left Join
left_join = pd.merge(df1, df2, on="Roll_No", how="left")
print("\nLeft Join : ")
print(left_join)

# Right Join
right_join = pd.merge(df1, df2, on="Roll_No", how="right")
print("\nRight Join : ")
print(right_join)

# Outer Join
outer_join = pd.merge(df1, df2, on="Roll_No", how="outer")
print("\nOuter Join : ")
print(outer_join)