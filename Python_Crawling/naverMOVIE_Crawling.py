import urllib.request as READYtoCRAWLING
from bs4 import BeautifulSoup
import csv


secondranklist = []
thirdranklist = []
# commit


def mainmenu():
    print('*******메뉴*******')
    print('1.조회순')
    print('2.평점순(현재상영영화)')
    print('3.평점순(모든영화)')
    print('4.종료')


def firstmenu():
    inputdate = input('날짜를 선택해라: ')
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date={0}'.format(
        inputdate)
    response = READYtoCRAWLING.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    f1 = open('naverMOVIE 조회순{0}.csv'.format(
        inputdate), 'w', encoding='utf8', newline='')
    wr1 = csv.writer(f1, delimiter=',', quotechar='"')
    for data in soup.findAll(class_='tit3'):
        for data2 in data.findAll('a'):
            firstlist = ['{0}등 {1}'.format(i, data2.string)]
            print('{0}등 {1}'.format(i, data2.string))
            wr1.writerow(firstlist)
            i += 1
    f1.close()


def secondmenu():
    inputdate = input('날짜를 선택해라: ')
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date={0}'.format(
        inputdate)
    response = READYtoCRAWLING.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    i = 1
    r = 0
    f2 = open('naverMOVIE 평점순(현재상영영화){0}.csv'.format(
        inputdate), 'wt', encoding='utf8', newline='')
    wr2 = csv.writer(f2, delimiter=',', quotechar='"')
    for data2 in soup.select('td.point'):
        secondranklist.append(data2.string)
    for data in soup.select('div.tit5 a'):
        print('{0}등 {1} {2}점'.format(i, data.string, secondranklist[r]))
        secondlist = ['{0}등 {1} {2}'.format(i, data.string, secondranklist[r])]
        wr2.writerow(secondlist)
        i += 1
        r += 1
    f2.close()


def thirdmenu():
    inputdate = int(input('날짜를 선택해라: '))
    firstpage = int(input('첫번째 페이지를 선택해라: '))
    lastpage = int(input('마지막 페이지를 선택해라(최대 40): '))
    if (firstpage >= lastpage):
        print('제대로 써라')
        return False
    if (firstpage == 1):
        i = 1
    elif (firstpage <= 0):
        print('제대로 써라')
        return False
    else:
        i = ((firstpage - 1) * 50) + 1
    r = 0
    f3 = open('naverMOVIE 평점순(모든영화){0}.csv'.format(
        inputdate), 'wt', encoding='utf8', newline="")
    wr3 = csv.writer(f3, delimiter=",", quotechar="|")
    while (firstpage <= lastpage):
        url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date={0}&page={1}'.format(
            inputdate, firstpage)
        response = READYtoCRAWLING.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        for data2 in soup.select('td.point'):
            thirdranklist.append(data2.string)
        for data in soup.select('div.tit5 a'):
            print('{0}등 {1} {2}점'.format(i, data.string, thirdranklist[r]))
            thirdlist = ['{0}등 {1} {2}'.format(
                i, data.string, thirdranklist[r])]
            wr3.writerow(thirdlist)
            i += 1
            r += 1
        firstpage += 1
    f3.close()


while True:
    mainmenu()
    selector = int(input('메뉴를 선택해라: '))
    if (selector == 1):
        firstmenu()
    if (selector == 2):
        secondmenu()
    if (selector == 3):
        thirdmenu()
    if (selector == 4):
        break
