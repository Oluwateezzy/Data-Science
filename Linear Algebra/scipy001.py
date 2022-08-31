# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:42:49 2022

@author: Teezzy
"""

from scipy.optimize import minimize

def f(x):
    return (x-3)**2

res = minimize(f, 2)

print(res.x[0])