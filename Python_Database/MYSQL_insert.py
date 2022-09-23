import pymysql
import time

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

name = input('이름: ')
tel = input('전화번호: ')
addr = input('주소: ')
memo = input('메모: ')
input_time=str(time.asctime(time.localtime(time.time())))

dbcursor.execute('INSERT INTO TEL (NAME, TEL,ADDR,INPUT_TIME,MEMO) VALUES (%s,%s,%s,%s,%s)',
                 (name, tel, addr, input_time, memo)) #파이썬에서 mysql은 ?대신에 %s만 사용
dbconn.commit()

res = dbcursor.execute('SELECT * FROM TEL')
res = dbcursor.fetchall()
for data in res:
    print(data)

dbcursor.close()
dbconn.close()