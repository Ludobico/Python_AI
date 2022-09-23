import pymysql

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

sql = 'SELECT * FROM TEL'
dbcursor.execute(sql)
rows = dbcursor.fetchall()

print(rows)

dbcursor.close()
dbconn.close()