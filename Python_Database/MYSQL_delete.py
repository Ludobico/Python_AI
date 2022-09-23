import pymysql

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

res = dbcursor.execute('SELECT * FROM TEL ORDER BY ID DESC')

name = input('삭제할 이름 입력: ')
flag = 0
for row in res:
    if row[1] == name:
        dbcursor.execute('DELETE FROM TEL WHERE NAME=%s',(name,))
        dbconn.commit()
        flag=1

if flag == 0:
    print('삭제 실패')
else:
    print('삭제 성공')

dbconn.close()
dbcursor.close()