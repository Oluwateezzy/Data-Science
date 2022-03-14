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

print(vector_add([1,2,3,4], [2,4,6,8]))
print(vector_sub([1,2,3,4], [2,4,6,8]))
print(vector_sum([[1,2,3,4], [2,4,6,8],[1,2,3,4], [2,4,6,8]]))
print(scalar_multiply(3, [1,2,3,4]))