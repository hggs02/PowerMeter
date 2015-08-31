import serial
import time
import os

obj = serial.Serial('COM6',
	9600,
	serial.EIGHTBITS,
	serial.PARITY_NONE,
	serial.STOPBITS_ONE,
	1)

os.system('clear') 				# Works only in linux
print('\t\tPOWER CONSUMPTION')

while True:
	data = obj.read(1000)
	if data:
	    print('-------------------------------------------------------')
	    tm = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	    print '|',tm,'\tConsumption => \t',data,'Unit','|','\n'
	    