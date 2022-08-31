import requests, json5

data = """{
    "title": "Data Science Book",
    "author": "Joel Grus",
    "publicationYear": "2014",
    "topics": ["data", "science", "data science"]
}"""

deserialized = json5.loads(data)

print(deserialized)