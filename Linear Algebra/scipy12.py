# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:41:21 2022

@author: Teezzy
"""

from scipy.linalg import solve_triangular, solve_toeplitz, toeplitz, eigh_tridiagonal, fiedler
import numpy as np

#Solve Triangular Matrices
a = np.array([
    [3, 0, 0, 0],
    [2, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1]
    ])
b = np.array([4, 2, 4, 2])

x = solve_triangular(a, b, lower=True)

print(x)

#solve Toeplitz Matrices 

c = np.array([1, 3, 6, 10])

r = np.array([1, -1, -2, -3])

x = np.array([1, 2, 2, 5])

b = solve_toeplitz((c, r), x)

T = toeplitz(c, r)

print(b)

print(T.dot(b))

#Eigenvalue Problems

d = 3*np.ones(4)
e = -1*np.ones(3)

w, v = eigh_tridiagonal(d, e)
A = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)

print(A)
print(v)
print(fiedler([1, 4, 6, 8]))

print(toeplitz([1, 2, 3, 4, 5], [7, 8, 9, 0, 6]))