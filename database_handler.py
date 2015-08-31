import time
import sqlite3
from datetime import datetime as dt


while True:
	try:
		conn = sqlite3.connect('../database.db',check_same_thread=False)
		#conn = sqlite3.connect('./backfill.db',check_same_thread=False)
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
			
	def deleteDb(self,arg):
		try:
			cur.execute("DELETE FROM backfill where time = ?",(arg['time'],))
			conn.commit()
		except Exception as e:
			print ('deleteDb: '+str(e))
	def fetchData(self):
		try:
			cur.execute("SELECT * FROM backfill order by time")
			row = cur.fetchone()
			
			if not row:
				return None  # If database is empty
			else:
				dictRow={}
				dictRow['dredger_name']        	= row[1]
				dictRow['time']                 = row[2]
				dictRow['storage_tank_level']   = row[3]
				dictRow['storage_tank_cap']     = row[4]
				dictRow['service_tank_level']   = row[5]
				dictRow['service_tank_cap']     = row[6]
				dictRow['flowmeter_1_in']       = row[7]
				dictRow['flowmeter_1_out']      = row[8]
				dictRow['engine_1_status']      = row[9]
				dictRow['flowmeter_2_in']       = row[10]
				dictRow['flowmeter_2_out']      = row[11]
				dictRow['engine_2_status']      = row[12]
				dictRow['errGsm']				= int(row[13],16)
				dictRow['errMain']				= int(row[14],16)
				dictRow['errTimeout']			= int(row[15],16)
				dictRow['errUnknown']			= int(row[16],16)
				return dictRow
		except Exception as e:
			print ('2fetchData: '+str(e))

