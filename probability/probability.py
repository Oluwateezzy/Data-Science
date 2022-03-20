from cProfile import label
from matplotlib import pyplot as plt
import math
from random import choice, seed

#Conditional Probability
def random_kid():
    return choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

seed(0)

for _ in range(1000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

#Measure of Dispersion
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mean(x):
    return sum(x) / len(x)

def data_range(x):
    return max(x) - min(x)

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

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

#Uniform probability Density function
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

#Uniform Cummulative Density Function
def uniform_cdf(x):
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

#Normal Probability Density Function
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x/10.0 for x in range(-50, 50)]

plt.plot(xs, [normal_pdf(x) for x in xs], '-', label='mu = 0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal PDFs")
plt.show()

print("P(both / older):", both_girls / older_girl)
print("P(both / either):", both_girls / either_girl)