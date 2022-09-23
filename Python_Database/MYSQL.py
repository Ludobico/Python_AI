import pymysql

dbconn = pymysql.connect(host='localhost', user='root', password='kali', db='testdb', charset='utf8')
dbcursor = dbconn.cursor()

dbcursor.execute("""
CREATE TABLE IF NOT EXISTS TEL (
ID INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(10),
TEL VARCHAR(20),
ADDR VARCHAR(40),
INPUT_TIME VARCHAR(30),
MEMO VARCHAR(50) )
""")
dbcursor.close()
dbconn.close()
