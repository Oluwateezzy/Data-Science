import re


d = {
    'jan': '1', 'feb': '2', 'mar': '3', 'apr': '4',
    'may': '5', 'jun': '6', 'jul': '7', 'aug': '8',
    'sep': '9', 'oct': '10', 'nov': '11', 'dec': '12'
}

date = input('Enter date: ')
m = re.match('([A-Za-z]+)\.?\s*(\d{1, 2}),?\s*(\d{4})', date)

print('{}/{}/{}'.format(d[m.group(1).lower()[:3]], m.group(2), m.group(3)[-2:]))