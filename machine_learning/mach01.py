# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:57:02 2022

@author: Teezzy
"""
from collections import Counter
import math
from matplotlib import pyplot as plt
from random import random, seed

def mean(v):
    return sum(v)/len(v)

def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def distance(v, w):
    return magnitude(vector_substract(v, w))
    

def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, c = votes.most_common(1)[0]
    return winner, c

def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count 
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])
    
def knn_classifier(k, labeled_point, new_point):
    by_distance = sorted(labeled_point, key=lambda point : distance(point[0], new_point))

    k_nearest_labels = [label for _, label in by_distance[:k]]
    
    return majority_vote(k_nearest_labels)

def random_point(dim):
    return [random() for _ in range(dim)]

def random_distance(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim)) for _ in range(num_pairs)]

cities = [
    ([-122.3, 47.53], "python"),
    ([-96.85, 32.85], "java"),
    ([-89.33, 43.13], "r")
]

plots = {"java": ([], []), "python" : ([], []), "r" : ([], [])}

markers = {
    "java": "o",
    "python": "s",
    "r": "^"
    }

colors = {
    "java": "r",
    "python": "b",
    "r": "g"
    }

for (longitude, latitude), language in cities:
    plots[language][0].append(longitude)
    plots[language][1].append(latitude)

for language, (x, y) in plots.items():
    print(x, y)
    plt.scatter(x, y, color=colors[language],
                marker=markers[language], zorder=10)
    


plt.legend(loc=0)
plt.axis([-130, 60, 20, 55])

plt.title("Favourite Programming Language")
plt.show()


for k in [1, 3, 5, 7]:
    num_correct = 0
    
    for city in cities:
        location, actual_language = city
        other_cities = [
            other_city
            for other_city in cities
            if other_city != city]
        predicted_language = knn_classifier(k, other_cities, location)
        
        if predicted_language == actual_language:
            num_correct += 1
    
    print(k, "neigbour[s]", num_correct, "correct out of", len(cities))

plots = {"java": ([], []), "python": ([], []), "r": ([], [])}

k = 1 

for longitude in range(-130, -60):
    for latitude in range(20, 55):
        predicted_language = knn_classifier(k, cities, [longitude, latitude])
        plots[predicted_language][0].append(longitude)
        plots[predicted_language][1]
        
dimensions = range(1, 101)

avg_distance = []
min_distance = []

seed(0)
for dim in dimensions:
    distances = random_distance(dim, 10000)
    avg_distance.append(mean(distances))
    min_distance.append(min(distances))

min_avg_ratio = [min_dist / avg_dist for min_dist, avg_dist in zip(min_distance, avg_distance)]
















