import scipy as sc
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def func(x,*y):
    a, b = y
    return a * x + b


def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))


xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
ydata = [3, 8, 28, 75, 221, 291, 255, 235, 190, 125, 70, 28, 12, 5]
bound = [250, 6, 2]

popt , pcov = curve_fit(gauss, xdata, ydata, p0=bound)
fitting = gauss(xdata, *popt)

xgrid = xdata
plt.plot(xdata, ydata, '.')
plt.plot(xdata, fitting)
print('a = ', popt[0], '±', np.sqrt(pcov[0, 0]))
print('a = ', popt[1], '±', np.sqrt(pcov[1, 1]))
plt.show()
