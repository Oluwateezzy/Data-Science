lines = [line.split() for line in open('text.txt')]

s = open('text.txt').read()

f = open('write.txt', 'w')
print('This is line 1', file=f)
print('This is line 2', file=f)

f.close()

print(s)