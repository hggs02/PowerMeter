import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='aaggss',db='dredger')
cur = conn.cursor()


def table_create():
     cur.execute('drop table db')
     cur.execute('drop table users')
     cur.execute('CREATE TABLE db (id INTEGER NOT NULL AUTO_INCREMENT,\
     time DATETIME,\
     consumption VARCHAR(5),\
     PRIMARY KEY (id))')


     cur.execute('CREATE TABLE users (id INTEGER NOT NULL AUTO_INCREMENT,\
     email VARCHAR(64),\
     username VARCHAR(64),\
     password_hash VARCHAR(128),\
     PRIMARY KEY (id))')
     
     """
     insert into users values(1,\
     "email@gmail.com",\
     "admin",\
     "pbkdf2:sha1:1000$j91KH4E6$31901435f98bff4bf0dd99fc10331de4f65274e8");
     """
table_create()
