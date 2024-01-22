import urllib3
from bs4 import BeautifulSoup
url = "https://www.imdb.com/search/title/" + year + “,” + year + “&title_type=feature”
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)