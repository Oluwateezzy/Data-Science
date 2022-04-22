import json5

serialized = """{
    "title": "Data Science Book",
    "author": "Joel Guru",
    "publicationYear": 2014,
    "topics": ["data", "science", "data science"]
}"""

deserialized = json5.loads(serialized)

print(deserialized)