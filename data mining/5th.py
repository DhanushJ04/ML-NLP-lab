import pandas as pd

data = input("Enter numbers separated by space : ")

num_list = list(map(int, data.split()))

series = pd.Series(num_list)

print("\nGiven series : ")
print(series)
print("\nMean : ", series.mean())
print("Median : ", series.median())
print("Mode : ", list(series.mode()))
print("Standard Deviation : ", series.std())
