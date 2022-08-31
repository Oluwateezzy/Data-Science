# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:46:00 2022

@author: Teezzy
"""

from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 * np.sin(2*x) * np.exp(-x)

x = np.linspace(0, 1, 100)

d = derivative(f, x, dx=1e-6)
h = derivative(f, x, dx=1e-6, n=2)

plt.plot(x, f(x))
plt.plot(x, d)
plt.plot(x, h)
plt.show()