import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import re

searchdata = input('검색어를 입력해라: ')
client_id = "ATbPbxPKStU6LlBj8ilh"
client_secret = "mdkJgPEY9p"
encText = urllib.parse.quote("{0}".format(searchdata))
# url = "https://openapi.naver.com/v1/search/blog?query={0}".format(encText) # JSON 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query={0}".format(encText) # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))

    xmldoc = response_body.decode('utf-8')
    soup = BeautifulSoup(xmldoc, 'html.parser')

    # print(soup.prettify())
    for data in soup.findAll('item'):
        print('제목:',data.title.string)
        print('링크:',data.link.string)
        print('내용:',data.description.string)
        print('블로거이름:',data.bloggername.string)
        print('일자:',data.postdate.string)
        print()

else:
    print("Error Code:" + rescode)