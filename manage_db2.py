import sqlite3
#conn = sqlite3.connect('./backfill.db',check_same_thread=False)
conn = sqlite3.connect('../database.db',check_same_thread=False)
cur = conn.cursor()


def table_create():
     cur.execute('''CREATE TABLE backfill(id INTEGER PRIMARY KEY AUTOINCREMENT,time DATETIME,power VARCHAR(5))''')
          
     

table_create()
