# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:40:16 2022

@author: Teezzy
"""

from scipy.special import jv
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, jv(3, x))

print(jv(3, x))
plt.show()