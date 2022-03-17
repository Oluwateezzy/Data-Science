from collections import Counter
import math

num_friend = [70, 65, 72, 63, 71, 64, 60, 64, 67]
daily_minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]

#Basic Statistics for Data Science
num_points = len(num_friend)

largest_value = max(num_friend)
smallest_value = min(num_friend)
sorted_value = sorted(num_friend)

#Central of Tendencies
def mean(x):
    return sum(x) / len(x)

def median(x):
    n = len(x)
    sorted_value = sorted(x)
    mid_point = n // 2

    if n % 2 == 1:
        return sorted_value[mid_point]
    else:
        low = mid_point
        high = mid_point + 1
        return (sorted_value[low] + sorted_value[high])/2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    count = Counter(x)
    max_count = max(count.values())
    return [x_i for x_i, count in count.items() if count == max_count]

#Measure of Dispersion
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

#measure of Correlation

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

print(covariance(num_friend, daily_minutes))
print(correlation(num_friend, daily_minutes))