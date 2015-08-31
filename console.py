import serial
import time
import os
from database_handler import database_class

obj = serial.Serial('COM6',
	9600,
	serial.EIGHTBITS,
	serial.PARITY_NONE,
	serial.STOPBITS_ONE,
	1)
db = database_class()
os.system('clear') 				# Works only in linux
print('\t\tPOWER CONSUMPTION')

while True:
	packet = obj.read(1000)
	data = extractData(packet)
	if data:
	    print('-------------------------------------------------------')
	    tm = data[0]
	    power = data [1]
	    print '|',tm,'\tConsumption => \t',power,'Unit','|','\n'
	    db.insertDb(tm,power)

	    