import re
from tokenize import group

from pyrsistent import s

def modify(match):
    letter = match.group()
    return letter.lower()

def modify2(match):
    letter, number = match.group()
    return letter.lower() + str(int(number)+10)

print(re.sub(r'a', '*', 'aababababa', count=2))

print(re.sub(r'([A-Z])[a-z]', modify, 'PEACH Apple ApriCoT'))

print(re.sub(r'([A-Z])(\d)', modify2, 'A1 + B2 + C7'))

print(re.findall(r'[AB]\d*', 'A3 + B + AB3'))

print(re.split(r'\+|\-', '3x+4y-12x^2+7'))

if (re.match(r'ZZZ', 'ZZZ ZZZ xyz')):
    print('match found at beginning.')
else:
    print('No match at beginning')

if (re.search(r'ZZZ', 'abc ZZZ xyz')):
    print("match found")
else:
    print('No Match found')

a = re.search(r'([ABC])(\d)', '= A3+B2+C8')

print(a.group())
print(a.group(1))
print(a.group(2))

for s in re.finditer(r'([AB])(\d)', 'A3+B3'):
    print(s.group(1))

pattern = re.compile(r'[AB]\d')
print(pattern.sub('*', 'A3 + B4'))
print(pattern.sub('x', 'A8 + B9'))

pattern = re.compile(r'[AB]\d')
print(pattern.findall('A3+B4+C9+D8', 2, 6))
