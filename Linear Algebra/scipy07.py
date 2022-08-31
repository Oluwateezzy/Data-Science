# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:46:59 2022

@author: Teezzy
"""

from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np

def dSdx(S, t):
    theta, omega = S
    return [omega, np.sin(theta)]

theta0 = np.pi/4
omega0 =  0

S_0 = (theta0, omega0)

t = np.linspace(0, 20, 100)

sol = odeint(dSdx, S_0, t)

theta, omega = sol.T

plt.plot(t, theta)
#plt.plot(t, omega)

plt.show()