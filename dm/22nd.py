# bar chart
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Raj', 'Anitha', 'Ramesh', 'Meena', 'Kiran', 'Suresh'],
    'Department': ['Finance', 'HR', 'IT', 'IT', 'HR', 'Finance'],
    'Salary': [40000, 35000, 50000, 48000, 36000, 42000]
}

df = pd.DataFrame(data)
print("Employee Data : ")
print(df)
dept_salary = df.groupby('Department')['Salary'].sum()
dept_salary.plot(kind='bar')
plt.title("Total salary by department")
plt.xlabel("Department")
plt.ylabel("Total Salary")
plt.show()