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
#os.system('clear')                             # Works only in linux
print('\t\tPOWER CONSUMPTION')

def extractData(packet):
        data = packet.split(';')
        return data

while True:
        packet = obj.read(100)
        if packet:
                data = extractData(packet)
        
                print('-------------------------------------------------------')
                tm = data[0]
                power = data [1]
                print '|',tm,'\tConsumption => \t',power,'Unit','|','\n'
                db.insertDb(tm,power)

            
