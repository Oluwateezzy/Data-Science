# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:01:10 2022

@author: Teezzy
"""

from scipy.integrate import quad, dblquad
import numpy as np

integrand = lambda x: x**2 * np.sin(x) * np.exp(-x)

integral, integral_error = quad(integrand, 0, 1)

print(integral, integral_error)

integrand = lambda x, y: np.sin(x+y**2)
lwr_y = lambda x: -x
upr_y = lambda x: x**2
integral, integral_error = dblquad(integrand, 0, 1, lwr_y, upr_y)

print(integral, integral_error)
