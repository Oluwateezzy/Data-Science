# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:43:51 2022

@author: Teezzy
"""
import random, numpy as np
from matplotlib import pyplot as plt

def split_data(data, prob):
    results = [], []
    
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    
    return results

def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_text, y_text = zip(*test)
    return x_train, x_text, y_train, y_text

def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct/total

def precision(tp, fp, fn, tn):
    return tp / (tp + fp)

def recall(tp, fp, fn, tn):
    return tp / (tp + fn)

def f1_score(tp, fn, fp, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)


x = np.linspace(1, 10, 50)
y = [random.random() for _ in range(50)]

x_train, x_text, y_train, y_text = train_test_split(x, y, 0.33)
#print("x_train",x_train)
#print("x_text",x_text)
#print("y_train",y_train)
#print("y_text",y_text)

plt.plot(x_text, y_text)
plt.show()