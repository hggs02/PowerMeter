import time
import sqlite3
from datetime import datetime as dt


while True:
	try:
		conn = sqlite3.connect('database.db')
		cur = conn.cursor()
		break
        except Exception as e:
                print 'backfill.py: ',e
                time.sleep(1) #Wait 1 secs before retrying


class database_class():
	def insertDb(self,time,power):
		try:
			cur.execute('''INSERT INTO backfill (time,power) VALUES (?,?);''', (time,power))
			conn.commit()

		except Exception as e:
			print ('insertDb: '+str(e))
