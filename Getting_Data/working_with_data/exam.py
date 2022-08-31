# after identifying the question you're trying to answer and you have your data to work with 
# First, is to explore your data

# EXPLORING ONE_DIMENSIONAL DATA
# first, compute a few summary statistics
# second, create a histogram, in which you group your data into discrete buckets and count how many points fall into each bucket

from collections import Counter
import math
from random import random
import string
from hypothesis import seed

from matplotlib import pyplot as plt

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

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


def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

seed(0)

uniform = [200 * random() - 100 for _ in range(10000)]

normal = [57 * inverse_normal_cdf(random()) for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform Histogram")