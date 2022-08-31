# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:33:12 2022

@author: Teezzy
"""

from scipy.special import legendre
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
print(legendre(6)(x))
plt.plot(x, legendre(6)(x))

plt.show()

