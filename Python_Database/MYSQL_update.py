import pymysql

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

dbcursor.execute('SELECT * FROM TEL ORDER BY ID DESC')
res = dbcursor.fetchall()

name = input('수정할 이름 입력 : ')
flag = 0
for row in res:
    if row[1] == name:
        tel=input('전화번호: ')
        addr=input('주소: ')
        memo=input('메모: ')
        dbcursor.execute('UPDATE TEL SET TEL=%s, ADDR=%s, MEMO=%s WHERE NAME=%s',(tel,addr,memo,name))
        dbconn.commit()
        flag = 1

if flag == 0:
    print('\n 수정실패 \n')
else:
    print('\n 수정성공 \n')

dbcursor.close()
dbconn.close()