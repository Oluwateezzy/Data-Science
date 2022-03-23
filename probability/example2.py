from random import random

extreme_value_count = 0

for _ in range(100000):
    num_heads = sum(1 if random() < 0.5 else 0
                    for _ in range(1000))
    print(num_heads)
    
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

print(extreme_value_count / 100000)