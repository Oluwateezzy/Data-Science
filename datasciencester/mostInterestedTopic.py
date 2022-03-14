from collections import Counter

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit_learn"), (2, "Scipy"),
    (2, "Numpy"), (2, "Statsmodel"), (2, "Pandas"), (3, "R"), (3, "Python"),
    (3, "Statistics"), (3, "Regression"), (3, "Probability"),
    (4, "Machine Learning"), (4, "Regression"), (4, "Decision Trees"),
    (4, "Libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "Programming Laguages"), (6, "Statistics"),
    (6, "Probability"), (6, "Mathematics"), (6, "Theory"),
    (7, "Machine Learning"), (7, "Scikit_learn"), (7, "Mahout"),
    (7, "Neural Networks"), (8, "Neural Networks"), (8, "Deep Learning"),
    (8, "Big Data"), (8, "Artificial Intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReducer"), (9, "Big Data")
]

words_and_counts = Counter(word
                            for user, interest in interests
                            for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
print(words_and_counts)