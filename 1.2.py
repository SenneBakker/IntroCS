from scipy.optimize import curve_fit as cv
import numpy as np
import math
import matplotlib.pyplot as plt


def diff_eqs(a,t):
    y = a*math.exp(-t)
    return y


Day=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Number=[3, 8, 28, 75, 221, 291, 255, 235, 190, 125, 70, 28, 12,5]
popt, _ = cv(diff_eqs, Day, Number)

plt.plot(Day, Number)
plt.plot(Day, popt[1]*math.exp(Day))
