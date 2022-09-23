import sqlite3
import time

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

name = input('이름: ')
tel = input('전화번호: ')
addr = input('주소: ')
memo = input('메모: ')
input_time=str(time.asctime(time.localtime(time.time())))

#print('INSERT INTO TEL (NAME, TEL, ADDR, INPUT_TIME, MEMO) \
#VALUES ('" +name+ "','" +tel+ "','" +addr+ "','" +input_time+ "','" +memo+ "')")

#dbcursor.execute('INSERT INTO TEL (NAME, TEL, ADDR, INPUT_TIME, MEMO) \
#VALUES ('" +name+ "','" +tel+ "','" +addr+ "','" +input_time+ "','" +memo+ "')")

# dbcursor.execute('INSERT INTO TEL (NAME, TEL, ADDR, INPUT_TIME, MEMO) VALUES '
#                  '(:name, :tel, :addr, :input_time, :memo)'
#                  ,{"name":name, "tel":tel, "addr":addr, "input_time":input_time, "memo":memo})

#values에 ?쓰고 변수넣어도됨(react db랑 같음)
dbcursor.execute('INSERT INTO TEL (NAME, TEL,ADDR,INPUT_TIME,MEMO) VALUES (?,?,?,?,?)',
                 (name, tel, addr, input_time, memo))

dbconn.commit()
#insert문은 DML 이므로 commit을 해줘야 한다.

for row in dbcursor.execute('SELECT * FROM TEL'):
    print(row)


dbcursor.close()
dbconn.close()