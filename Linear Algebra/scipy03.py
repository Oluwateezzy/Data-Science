# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:44:51 2022

@author: Teezzy
"""

from matplotlib import pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

def f(x, a, b):
    return a*x**2 + b

x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2

popt, pcov = curve_fit(f, x_data, y_data, p0=(1,1))

print(popt)

plt.scatter(x_data, y_data)
plt.show()