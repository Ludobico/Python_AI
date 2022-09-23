from bs4 import BeautifulSoup
import urllib.request as MYURL

jURL = 'http://rss.joins.com/joins_news_list.xml' #중앙일보 기사 관련 xml 문서
response = MYURL.urlopen(jURL)
soup = BeautifulSoup(response, 'html.parser')

print(soup)
print('---------------------------------------------------------------')
for item in soup.findAll('item'):
    print('title:',item.title.string)
    print('description:',item.description.string)
    print('pubdate:',item.pubdate.string)
    print('--------------------------------------------------------')
