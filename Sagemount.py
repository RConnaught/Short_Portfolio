import bs4 as bs
import urllib.request

sce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Bregal_Sagemount').read()
soup = bs.BeautifulSoup(sce, 'lxml')

for paragraph in soup.find_all('p'):
     print(paragraph.text)