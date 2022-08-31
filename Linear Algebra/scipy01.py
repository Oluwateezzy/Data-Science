# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:52:14 2022

@author: Teezzy
"""

from scipy.optimize import minimize


f = lambda x: (x[0]-1)**2 + (x[1]-2.5)**2


cons = (
        {'type':'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
        {'type':'ineq', 'fun': lambda x: -x[0]-2*x[1]+6},
        {'type':'ineq', 'fun': lambda x: -x[0]+2*x[1]+2}
    )

bounds = ((0,None), (0,None))

res = minimize(f, (2, 0), bounds=bounds, constraints=cons)
print(res.x)