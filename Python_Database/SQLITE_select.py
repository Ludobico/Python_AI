import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()

print('No \t 성명 \t 전화번호 \t 주소 \t 메모 \t 입력일자')
print('---------------------------------------------------------------')
dbcursor.execute('SELECT * FROM TEL ORDER BY ID ASC')
res = dbcursor.fetchall()
print(res)
for row in res:
    print(str(row[0])+'\t'+row[1]+'\t'+row[2]+'\t'+row[3]+ '\t'+row[5]+'\t'+row[4])
    #문자타입에는 str안붙여도됨, 숫자타입만 str붙임
print('---------------------------------------------------------------')

dbcursor.execute('SELECT * FROM TEL ORDER BY ID ASC')
res = dbcursor.fetchone()
print(res)
res2 = dbcursor.fetchone()
print(res2)
dbcursor.close()
dbconn.close()