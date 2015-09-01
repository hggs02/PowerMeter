import sqlite3
#conn = sqlite3.connect('./backfill.db',check_same_thread=False)
conn = sqlite3.connect('database.db',check_same_thread=False)
cur = conn.cursor()


def table_create():
     cur.execute('''CREATE TABLE backfill(id INTEGER PRIMARY KEY AUTOINCREMENT,time DATETIME,power VARCHAR(5))''')
     cur.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,email VARCHAR(64),username VARCHAR(64),password_hash VARCHAR(128))''')
     #cur.execute('''INSERT INTO users (username,password_hash) VALUES (?,?);''', ('admin','pbkdf2:sha1:1000$M6Rpb3bE$3b97a31fa0667ef72c846476c8211a7698bac8b3'))
     #conn.commit()
     

table_create()
