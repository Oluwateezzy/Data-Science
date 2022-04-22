from aiohttp import request
from bs4 import BeautifulSoup
import html5lib
import requests

def is_video(td):
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith("video"))

url = "http://shop.oreilly.com/category/browse-subjects/" + \
"data.do?sortby=publicationDate&page=1"

soup = BeautifulSoup(requests.get(url).text, 'html5lib')

tds =soup.div

print(tds)