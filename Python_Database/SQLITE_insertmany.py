import sqlite3
import time

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

data = [
    ('홍기자', '010-1231-1231','서울',str(time.asctime(time.localtime(time.time()))),'테스트1'),
    ('한기자', '010-1231-1231','수원',str(time.asctime(time.localtime(time.time()))),'테스트2'),
    ('길기자', '010-1231-1231','경주',str(time.asctime(time.localtime(time.time()))),'테스트3')]

sql = 'INSERT INTO TEL (NAME,TEL,ADDR,INPUT_TIME,MEMO) VALUES (?,?,?,?,?)'
dbcursor.executemany(sql, data)

dbconn.commit()

for row in dbcursor.execute('SELECT * FROM TEL'):
    print(row)

dbcursor.close()
dbconn.close()