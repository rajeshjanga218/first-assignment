import requests
import urllib.request
import re
from bs4 import BeautifulSoup

url=" http://quotes.toscrape.com/"
try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")
soup = BeautifulSoup(page, 'html.parser')
regex = re.compile('^text-^')
quotes = soup.find_all('span', attrs={'class': regex})
#quotes = soup.find_all('span',class_='text')
print(quotes)
