from collections import Counter, defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Delvin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1,3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

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

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"]
                    for foaf in friend["friends"]
                    if not_the_same(user, foaf)
                    and not_friends(user, foaf))

#two users are not the same if they have different ids
def not_the_same(user, other_user):
    return user["id"] != other_user["id"]

#other user is not a friend if he is not in user's friends
def not_friends(user, other_user):
    return all(not_the_same(friend, other_user)
            for friend in user["friends"])

def data_scientists_who_like(target_interest):
    return [user_id
    for user_id, user_interest in interests
    if user_interest == target_interest]

user_ids_by_interest = defaultdict(list)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
            for interest in interests_by_user_id[user["id"]]
            for interested_user_id in user_ids_by_interest[interest]
            if interested_user_id != user["id"])

print(friends_of_friend_ids(users[3]))
print(data_scientists_who_like("Regression"))
print(user_ids_by_interest)
print()
print()
print(interests_by_user_id)
print(most_common_interests_with(users[0]))