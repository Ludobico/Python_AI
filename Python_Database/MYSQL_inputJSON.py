import pymysql
import urllib.request
import json

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

dbcursor.execute("""
CREATE TABLE IF NOT EXISTS JSONINFO (
ID INT PRIMARY KEY AUTO_INCREMENT,
TITLE VARCHAR(500),
LINK VARCHAR(500),
POSTDATE VARCHAR(500),
BLOGGERNAME VARCHAR(100))
""")

searchdata = input('검색어를 입력해라: ')
client_id = "ATbPbxPKStU6LlBj8ilh"
client_secret = "mdkJgPEY9p"
encText = urllib.parse.quote("{0}".format(searchdata))
url = "https://openapi.naver.com/v1/search/blog?query={0}".format(encText) # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    file_path='{0}.json'.format(searchdata)
    dataJson = json.loads(response_body.decode('utf-8'))
    with open(file_path, 'w', encoding='utf-8') as makefile:
        json.dump(dataJson, makefile, ensure_ascii=False, indent=4)

    for data in dataJson['items']:
        dbcursor.execute('INSERT INTO JSONINFO (TITLE,LINK,POSTDATE,BLOGGERNAME) VALUES '
                         '(%s,%s,%s,%s)',(data['title'],data['link'],data['postdate'],data['bloggername']))
        dbconn.commit()
    print('db에 넣었다. 확인해라')
else:
    print("Error Code:" + rescode)

dbcursor.close()
dbconn.close()