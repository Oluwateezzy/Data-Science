import re


lines = [line.split() for line in open('text.txt')]

s = open('text.txt').read()

# = open('write.txt', 'w')
#print('#This is line 1', file=f)
#print('This is line 2', file=f)

#f.close()

start_with_hash = 0

with open('write.txt', 'r') as f:
    for line in f:
        if re.match("^#", line):
            start_with_hash += 1

#print(start_with_hash)