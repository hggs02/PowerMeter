#!/usr/bin/python3

import minimalmodbus
import serial
from time import sleep
import datetime 

import random


class Xbee(object):
    def __init__ (self):
        self.obj = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    
    def xbee_write(self,data):
        self.obj.write(data+'\r\n')
        

    def xbee_read(self):
        while True:
            #val = self.obj.read(100).decode('ascii').strip()
            val = self.obj.read(100).strip()
            if val:
                return val
    
    def __del__(self):
        self.obj.close()
        
def dummyPacket():
    val = random.randint(0,55)
    return val


if __name__ == '__main__':

    xb = Xbee()
    
    print('\t\tPOWER CONSUMPTION')

    while True:
        try:
             
            """
            instrument = minimalmodbus.Instrument('/dev/port1',1)
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
            time                = datetime.datetime.now()
            #consumption  = instrument.read_float(4201)/100000
            consumption = dummyPacket()

            
            print('-------------------------------------------------------------')
            print('{0:20} ==> {1:5} units'.format('consumption',consumption))
            xb.xbee_write(str(time)+';'+str(consumption))
            print('-------------------------------------------------------------')
            
            #raw_input()
            sleep(1)
            #print (level)
        except Exception as e:
            print(e)
            sleep(1)
    
   
        
