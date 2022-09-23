import os
import sys
import urllib.request
import json
import csv

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
    csvfilereader = response_body.decode('utf-8')
    # print(response_body.decode('utf-8'))

    file_path='{0}.csv'.format(searchdata)
    csvf = open(file_path, 'wt', encoding='utf-8', newline='')
    csvwr = csv.writer(csvf,delimiter = " ",quotechar='')
    dataJson = json.loads(csvfilereader)
    json.dump(dataJson,csvf , ensure_ascii=False, indent=4)
    print(type(dataJson))
    csvf.close()

else:
    print("Error Code:" + rescode)