# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:18:09 2022

@author: Teezzy
"""

from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

def dvdt(v, t):
    return 3 * v**2 - 5

v0 = 0

t = np.linspace(0, 1, 100)

sol = odeint(dvdt, v0, t)

plt.plot(t, sol)

print(sol.T[0])