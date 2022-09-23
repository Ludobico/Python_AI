import sqlite3

dbconn = sqlite3.connect('tel.db') #데이터베이스가 없으면 이런 이름으로 만듬

dbcursor = dbconn.cursor() #커서객체만듬
dbcursor.execute("""
CREATE TABLE IF NOT EXISTS TEL (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT,
TEL TEXT,
ADDR TEXT,
INPUT_TIME TEXT,
MEMO TEXT)
""")
dbcursor.close()
dbconn.close()