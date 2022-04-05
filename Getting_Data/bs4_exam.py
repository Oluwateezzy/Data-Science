from bs4 import BeautifulSoup

import requests
html = requests.get('http://www.barcelona.com').text
soup = BeautifulSoup(html, 'html5lib')

first_p = soup.find('p')
first_p_text = soup.p.text
first_p_words = soup.div.text
all_p = soup('div')
first_p_id = soup.p.get('id')
p_with_ids = [p for p in soup('div')]
important_p = soup('p', {'class': 'important'})

print(p_with_ids)


#with open('html.txt', 'w') as f:
 #   f.writelines(first_p_words)