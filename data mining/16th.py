import pandas as pd

data = {
    "SalesManName": ["Ravi", "Prakash", "Seema", "Ravi", "Anil", "Seema", "Prakash", "ravi"],
    "City": ["Mangaluru", "Udupi", "Mangaluru", "Bengaluru", "Mangaluru", "Udupi", "Bengaluru", "Mangaluru"],
    "ProductName": ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile", "Tablet", "Laptop", "Tablet"],
    "Qty": [6, 3, 8, 2, 7, 9, 4, 10]
}

df = pd.DataFrame(data)

# 1
c = df.groupby('City')['Qty'].agg(['sum', 'mean'])
print("City wise Total and Average Qty : ")
print(c)

# 2
p = df.groupby('ProductName')['Qty'].agg(['sum', 'mean'])
print("Product wise Total and Average Qty : ")
print(p)

# 3
s = df.groupby('SalesManName')['Qty'].agg(['sum', 'mean'])
print("Salesman wise Total and Average Qty : ")
print(s)
