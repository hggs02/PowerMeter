#!/usr/bin/python3

import minimalmodbus
import serial
from time import sleep, strftime
from database_handler import database_class

import random



class Xbee(object):
    
    def __init__ (self):
        self.obj = serial.Serial('/dev/port2',9600,timeout=1)
    
    def xbee_write(self,data):
        self.obj.write(data)
    
    def __del__(self):
        self.obj.close()
        
def dummyPacket():
    val = random.randint(0,55)
    return val

db = database_class()

if __name__ == '__main__':

    xb = Xbee()
    
    print('\t\tPOWER CONSUMPTION')

    while True:
        try:
             
            """
            instrument = minimalmodbus.Instrument('/dev/ttyUSB0',1)
            #instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1, minimalmodbus.MODE_ASCII)
            instrument.serial.baudrate = 9600
            instrument.serial.bytesize = 8
            instrument.serial.parity = serial.PARITY_EVEN
            instrument.serial.stopbits = 1
            instrument.serial.timeout = 0.1
            #instrument.debug='false'
            instrument.mode = minimalmodbus.MODE_ASCII
            #print instrument
            """
            time  = strftime("%Y-%m-%d %H:%M:%S")
            #consumption  = instrument.read_register(4209)
            consumption = dummyPacket()

            
            print('-------------------------------------------------')
            print '|',time,'\tConsumption => \t',consumption,'Unit','|','\n'
            packet = str(time)+';'+str(consumption)
            db.insertDb(time,consumption)
            xb.xbee_write(packet)
            
            sleep(3)
            
        except Exception as e:
            print(e)
            sleep(1)
    
   
        
