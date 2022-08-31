# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:58:16 2022

@author: Teezzy
"""
from random import random, seed
import numpy as np
from matplotlib import pyplot as plt

from scipy.optimize import curve_fit

def func(x, A, w, phi):
    return A*np.cos(w*x+phi)

seed(0)
t_data = [random()*10 for i in range(30)]

y_data = [np.cos(data) for data in t_data]

popt, pcov = curve_fit(func, t_data, y_data, p0=(1, 1, 0))

A, w, phi = popt

print(np.sqrt(np.diag(pcov)))

t = np.linspace(0, 10, 100)
y = func(t, A, w, phi)

plt.scatter(t_data, y_data)
plt.plot(t, y)
plt.show()