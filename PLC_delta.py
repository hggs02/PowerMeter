#!/usr/bin/python3

import minimalmodbus
import serial
from time import sleep, strftime
from database_handler import database_class

import random



class Xbee(object):
    
    def __init__ (self):
        self.obj = serial.Serial('/dev/xb1',9600,timeout=1)
    
    def xbee_write(self,data):
        self.obj.write(data)
    
    def __del__(self):
        self.obj.close()
        
def dummyPacket():
    val = random.randint(0,55)
    return val

class PLC():

    def __init__(self):
        try:
            self.instrument = minimalmodbus.Instrument('/dev/plc',1)
            self.instrument.serial.baudrate = 9600
            self.instrument.serial.bytesize = 8
            self.instrument.serial.parity = serial.PARITY_EVEN
            self.instrument.serial.stopbits = 1
            self.instrument.serial.timeout = 0.1
            self.instrument.mode = minimalmodbus.MODE_ASCII
            
            #self.instrument.debug='false'
            #print self.instrument

        except Exception, e:
            print 'class PLC __init__(): %s' %(str(e),)
        
        
    def read_int():
        data  = self.instrument.read_register(4209)
        return data
    
    def read_float():
        data  = self.instrument.read_float(4201)/100000
        return data


db = database_class()

if __name__ == '__main__':

    xb = Xbee()
    plc = PLC()
    
    print('\t\tPOWER CONSUMPTION')

    while True:
        try:
            time  = strftime("%Y-%m-%d %H:%M:%S")
            #consumption  = plc.read_int()
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
    
   
        
