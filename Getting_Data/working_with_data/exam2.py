from random import random

import math
from statistics import covariance

from matplotlib import pyplot as plt

def shape(A):
    nums_rows = len(A)
    nums_cols = len(A[0]) if A else 0
    return nums_rows, nums_cols

def get_columns(data, j):
    return [a_i[j] for a_i in data]

def mean(x):
    return sum(x) / len(x)

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def de_mean(x): #population mean
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    if n > 2:
        deviations = de_mean(x)
        return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def make_matrix(nums_row, nums_col, entry_fn):
    return [[entry_fn(i, j) for i in range(nums_col)] for j in range(nums_row)]

def is_diagonal(i, j):
    return 1 if i == j else 0

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

def correlation_matrix(data):
    _, num_columns = shape(data)


    def matrix_entry(i, j):
        return correlation(get_columns(data, i), get_columns(data, j))
    
    return make_matrix(num_columns, num_columns, matrix_entry)

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10
    low_p = 0
    hi_z = 10
    hi_p = 1

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            low_z = mid_z
            low_p = mid_p
        elif mid_p > p:
            hi_z = mid_z
            hi_p = mid_p
        else:
            break
    
    return mid_z

def random_normal():
    return inverse_normal_cdf(random())

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

print(correlation(xs, ys1))
print(correlation(xs, ys2))

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')

plt.xlabel("xs")
plt.ylabel("ys")
plt.legend(loc=9)
plt,plt.title("very different joint distribution")
plt.show()

