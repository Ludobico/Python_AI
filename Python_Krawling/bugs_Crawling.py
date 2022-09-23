import urllib.request as READYtoCRAWLING
from bs4 import BeautifulSoup
import pymysql
import csv
import json

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

dbcursor.execute("""
CREATE TABLE IF NOT EXISTS BUGS (
ID INT PRIMARY KEY AUTO_INCREMENT,
KCJDATE TEXT,
KCJRANK TEXT,
TITLE TEXT,
ARTIST TEXT)
""")

chartdate = int(input('날짜를 입력해라: '))
url = 'https://music.bugs.co.kr/chart/track/day/total?chartdate={0}'.format(chartdate)
response = READYtoCRAWLING.urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
drank = []
dtitle = []
dartist = []
sql = "SELECT KCJDATE FROM BUGS WHERE KCJDATE = %s"

def rankingfunc():
    for data in soup.findAll('td'):
        for data1 in data.findAll(class_='ranking'):
            for data2 in data1.findAll('strong'):
                # print(data2.string)
                drank.append(data2.string)

def titlefunc():
    for title in soup.findAll('th'):
        for title1 in title.findAll(class_='title'):
            for title2 in title1.findAll('a'):
                # print(title2.string)
                dtitle.append(title2.string)

def artistfunc():
    for artist in soup.findAll('td'):
        for artist1 in artist.findAll(class_='artist'):
            for artist2 in artist1.findAll('a'):
                # print(artist2.string)
                dartist.append(artist2.string)

rankingfunc()
titlefunc()
artistfunc()

filepath = '벅스차트{0}'.format(chartdate)
csvf = open(filepath, 'wt', encoding='utf-8', newline='')
csvwr = csv.writer(csvf, delimiter="", quotechar='"')

test1 = dbcursor.execute("SELECT KCJDATE FROM BUGS WHERE KCJDATE = %s",chartdate)
test1 = dbcursor.fetchone()


i = 0
while (i < 100):
    print('날짜:{3}\n순위:{0}위\n제목:{1}\n아티스트:{2}\n'.format(drank[i], dtitle[i], dartist[i], chartdate))
    dbcursor.execute("INSERT INTO BUGS (KCJDATE,KCJRANK,TITLE,ARTIST) VALUES (%s,%s,%s,%s)",
                 (chartdate,drank[i],dtitle[i],dartist[i]))
    dbconn.commit()
    csvwr.writerow(drank[i])
    csvwr.writerow(dtitle[i])
    csvwr.writerow(dartist[i])
    csvf.close()
    i = i + 1

dbcursor.close()
dbconn.close()


