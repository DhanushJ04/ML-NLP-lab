import pandas as pd

# First DataFrame
data1 = {
    "Roll_No": [101, 102, 103],
    "Name": ["Amita", "Ravi", "Sneha"],
    "Age": [21, 22, 20],
    "Course": ["MBA", "BBA", "MBA"]
}
df1 = pd.DataFrame(data1)

# Second DataFrame
data2 = {
    "Roll_No": [102, 103, 104],
    "Name": ["Ravi", "Sneha", "Kiran"],
    "Age": [22, 20, 23],
    "City": ["Delhi", "Mumbai", "Chennai"]
}
df2 = pd.DataFrame(data2)

print("Data Frame 1 : ")
print(df1)
print("Data Frame 2 : ")
print(df2)

# Inner Join (Common records only)
inner_join = pd.merge(df1, df2, on="Roll_No", how="inner")
print("\nInner Join : \n")
print(inner_join)

# Left Join (All records from df1)
left_join = pd.merge(df1, df2, on="Roll_No", how="left")
print("\nLeft Join : \n")
print(left_join)

# Right Join
right_join = pd.merge(df1, df2, on="Roll_No", how="right")
print("\nRight Join : \n")
print(right_join)

# Outer Join (All records from both)
outer_join = pd.merge(df1, df2, on="Roll_No", how="outer")
print("\nOuter Join : \n")
print(outer_join)

