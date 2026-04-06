import pandas as pd

df = pd.read_csv("Emp.csv")
print(df)

# a
df = df.rename(columns={'Name': 'EmpName', 'Department': 'Dept'})
print("\nAfter renaming columns : ")
print(df)

# b
df['Dept'] = df['Dept'].replace('Accounts', 'Finance')
print("\nAfter replacing departments : ")
print(df)

# c
df_sorted = df.sort_values(by=['City', 'Salary'], ascending=[True, False])
print("\nSorted data is : ")
print(df_sorted)

# d
print("\nDepartment-Wise Average and Total Salary : ")
print(df.groupby('Dept')['Salary'].agg(['mean', 'sum']))

# e
print("\nCity and Department-Wise Salary Stats : ")
print(df.groupby(['City', 'Dept'])['Salary'].agg(['max', 'min', 'mean']))

# f
print("\nDepartment Groups : ")
for name, group in df.groupby('Dept'):
    print("\nDepartment : ", name)
    print(group)

# g
df_no_mang = df[df['City'] != "Mangalore"]
print("\nDepartment-Wise Salary (Excluding Mangalore) : ")
print(df_no_mang.groupby('Dept')['Salary'].agg(['mean', 'sum']))

# h
print("\nEmployees Containing 'Raj' : ")
print(df[df['EmpName'].str.contains('Raj', case=False, na=False)])

# i
print("\nRows with missing values : ")
print(df[df.isnull().any(axis=1)])

# j
print("\nTotal Duplicate Rows : ", df.duplicated().sum())
print("Null Values in each column : ")
print(df.isnull().sum())

# k
df_final = df.drop(columns=['Age', 'No.Depen'])
print("\nAfter Dropping Age and Number of Dependencies : ")
print(df_final)


