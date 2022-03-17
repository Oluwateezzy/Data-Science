import math
from functools import reduce

def vector_add(v, w):
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_sub(v, w):
    return [v_i - w_i 
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    return reduce(vector_add,vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_sub(v, w))

def distance(v, w):
    return magnitude(vector_sub(v, w))


print(vector_add([1,2,3,4], [2,4,6,8]))
print(vector_sub([1,2,3,4], [2,4,6,8]))
print(vector_sum([[1,2,3,4], [2,4,6,8],[1,2,3,4], [2,4,6,8]]))
print(scalar_multiply(3, [1,2,3,4]))
print(vector_mean([[1,2,3,4], [2,4,6,8],[1,2,3,4]]))
print(dot([1,2,3,4], [2,4,6,8]))
print(sum_of_squares([1,2,3,4]))