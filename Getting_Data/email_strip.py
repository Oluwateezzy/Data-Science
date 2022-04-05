from typing import Counter


def get_domain(email_address):

    return email_address.lower().split("@")[-1]
with open('write.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)
print(domain_counts)