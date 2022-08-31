# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:49:27 2022

@author: Teezzy
"""

import re, math, glob, os, random
import numpy as np
import pandas as pd
from collections import Counter, defaultdict

def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)

def count_words(training_set):
    counts = defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in tokenize(message):
            counts[word][0 if is_spam else 1] += 1
    return counts

def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
    return [(w, (spam + k) / (total_spams + 2 * k),
            (non_spam + k) / (total_non_spams + 2 * k))
            for w, (spam, non_spam) in counts.items()]

def spam_probability(word_probs, message):
    message_words = tokenize(message)
    log_prob_if_spam = log_prob_if_not_spam = 0
    
    for word, prob_if_spam, prob_if_not_spam in word_probs:
        if word in message_words:
            log_prob_if_spam += math.log(prob_if_spam)
            log_prob_if_not_spam += math.log(prob_if_not_spam)
        else:
            log_prob_if_spam += math.log(1.0 - prob_if_spam)
            log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)
            
    prob_if_spam = math.exp(log_prob_if_spam)
    prob_if_not_spam = math.exp(log_prob_if_not_spam)
    return prob_if_spam / (prob_if_spam + prob_if_not_spam)

def split_data(data, prob):
    results = [], []
    
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    
    return results

class NaiveBayesClassifier:
    
    def __init__(self, k = 0.5):
        self.k = k
        self.word_probs = []
    
    def train(self, training_set):
        
        num_spams = len([is_spam for message, is_spam in training_set if is_spam])
        
        num_non_spams = len(training_set) - num_spams
        
        word_counts = count_words(training_set)
        self.word_probs = word_probabilities(word_counts, num_spams, num_non_spams)
        return self.word_probs
    
    def classify(self, message):
        return spam_probability(self.word_probs, message)

path = r"C:\Users\Teezzy\Desktop\Data_Science\machine_learning\archive\*\*\*"

data = []

for fn in glob.glob(path):
    is_spam = "ham" not in fn
    #print(fn)
    
    with open(fn, 'r', encoding="ISO-8859-1") as file:
        for line in file:
            subject = re.sub(r"subject: ", "", line).strip()
            data.append((subject, is_spam))

#print(data)
random.seed(0)
train_data, test_data = split_data(data, 0.75)
#print(train_data, test_data)

classifier = NaiveBayesClassifier()
#pd.DataFrame(classifier.train(train_data)).to_csv('train_data.csv')
pd.DataFrame(classifier.train(test_data)).to_csv('text_data.csv')

list_data = []
list_data2 = []

with open("./text_data.csv", 'r') as file:
        for line in file:
            list_data = np.append(line.split(","))
            #list_data.append(line.split(","))

# with open("./text_data.csv", 'r') as file:
#         for line in file:
#             list_data.append(line.split(","))
# #train_data2 = pd.DataFrame(list_data)

# for line in list_data:
#     del line[0:1]

# #classified = [(subject, is_spam, classifier.classify(subject))
# #                for subject, is_spam in test_data]
# #print(classified)

# #counts = Counter((is_spam, spam_probability > 0.5)
# #                    for _, is_spam, spam_probability in classified)

# #print(counts)
print(list_data)