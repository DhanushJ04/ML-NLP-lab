import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Linear regression plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.title('Linear Regression')
plt.plot(x, mymodel)
plt.show()


# Polynomial regression plot
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 99, 100]

mymodel = np.poly1d(np.polyfit(x, y, 2))
myline = np.linspace(1, 22, 100)
plt.scatter(x, y)
plt.title('Polynomial  Regression')
plt.plot(myline, mymodel(myline))
plt.show()
