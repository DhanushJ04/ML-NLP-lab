# total and avg of qty sold city-wise, product-wise and salesman-wise

import pandas as pd
data = {
    'SalesManName': ['Ravi', 'Prakash', 'Seema', 'Ravi', 'Anil', 'Seema', 'Prakash', 'Ravi'],
    'City': ['Mangaluru', 'Udupi', 'Mangaluru', 'Bengaluru', 'Mangaluru', 'Udupi', 'Bengaluru', 'Mangaluru'],
    'ProductName': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet', 'Laptop', 'Tablet'],
    'Qty': [6, 3, 8, 2, 7, 9, 4, 10]
}

df = pd.DataFrame(data)

# 1
c = df.groupby('City')['Qty'].agg(['sum', 'mean'])
print("\nCity-wise Total and Average Qty : ")
print(c)

# 2
p = df.groupby('ProductName')['Qty'].agg(['sum', 'mean'])
print("\nProduct-wise Total and Average Qty : ")
print(p)

# 3
s = df.groupby('SalesManName')['Qty'].agg(['sum', 'mean'])
print("\nSalesman-wise Total and Average Qty : ")
print(s)
