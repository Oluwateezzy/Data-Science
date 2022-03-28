from functools import partial
from random import randint
from turtle import distance
from matplotlib import pyplot as plt

def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)

def square(x):
    return x ** 2

def derivative(x):
    return 2 * x

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_estimate(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

v = [randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

print(step([1,2,3], sum_of_squares_gradient([1,2,3]), -0.01))

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v


derivative_estimate = partial(difference_quotient, square, h=0.00001)

x = range(-10, 10)
label_a = [derivative(i) for i in x]
label_b = [derivative_estimate(i) for i in x]