# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:29:06 2022

@author: Teezzy
"""

from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

def dSdx(S, x):
    y1, y2 = S
    return [y1+(y2**2)+3*x, 3*y1 + y2**3 - np.cos(x)]

y1_0 = 0
y2_2 = 0
S_0 = (y1_0, y2_2)

x = np.linspace(0, 1, 100)

sol = odeint(dSdx, S_0, x)
y1 = sol.T[0]
y2 = sol.T[1]

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()