# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:25:27 2022

@author: Teezzy
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
#plt.scatter(x, y)

f = interp1d(x, y, kind="cubic")
x_dense = np.linspace(0, 10, 100)
y_dense = f(x_dense)

plt.plot(x_dense, y_dense)
plt.show()