import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('SELECT * FROM TEL ORDER BY ID DESC')

name = input('수정할 이름 입력 : ')
flag = 0
for row in res:
    if row[1] == name: #row[1]은 tel.db 컬럼에서 name을 가르킴
        tel=input('전화번호: ')
        addr=input('주소: ')
        memo=input('메모: ')
        dbcursor.execute('UPDATE TEL SET TEL=?, ADDR=?, MEMO=? WHERE NAME=?',(tel,addr,memo,name))
        dbconn.commit()
        flag = 1

if flag == 0:
    print('\n 수정실패 \n')
else:
    print('\n 수정성공 \n')

dbcursor.close()
dbconn.close()
