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

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

print("P(both / older):", both_girls / older_girl)
print("P(both / either):", both_girls / either_girl)