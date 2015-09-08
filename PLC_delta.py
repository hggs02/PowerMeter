#!/usr/bin/python2

import minimalmodbus
import serial
from time import sleep, strftime
from database_handler import database_class

import random

import RPi.GPIO as gpio
from RPi.GPIO import OUT as out
from RPi.GPIO import LOW as low 
from RPi.GPIO import HIGH as high 

class LED():
	def __init__(self,threshold):
		self.pin_no = 11
		self.threshold = threshold
		self.led_init()

	def led_init():
		gpio.setmode(gpio.BOARD)
		gpio.setwarnings(False)
		gpio.setup(self.pin_no, out)
		gpio.output(self.pin_no, low)

	def on():
		gpio.output(self.pin_no, high)

class XBEE():
    
    def __init__ (self):
        self.obj = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    
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
            self.instrument.serial.baudrate = 19200
            self.instrument.serial.bytesize = 7
            self.instrument.serial.parity = serial.PARITY_EVEN
            self.instrument.serial.stopbits = 1
            self.instrument.serial.timeout = 0.1
            self.instrument.mode = minimalmodbus.MODE_ASCII
            
            #self.instrument.debug='false'
            #print self.instrument

        except Exception as e:
           # print 'plc init():'+str(e)
            print 'class PLC __init__(): %s' %(str(e),)
        
        
    def read_int(self):
        data  = self.instrument.read_register(5146)
        return data
    
    def read_float(self):
        data  = self.instrument.read_float(5147)/100000
        return data


db = database_class() 

xb = XBEE()
plc = PLC()
led = LED(12)	# Here 12 is the max threshold value

print('\t\tPOWER CONSUMPTION')

while True:
    try:
        time  = strftime("%Y-%m-%d %H:%M:%S")
        #consumption = dummyPacket()
        consumption  = plc.read_float()
        
        if(consumption > led.threshold)
        {
        	led.on()		# Switch ON the led if consumption exceeds the threshold
        }
        
        print('-------------------------------------------------')
        print '|',time,'\tConsumption => \t',consumption,'Unit','|','\n'
        packet = str(time)+';'+str(consumption)
        db.insertDb(time,consumption)
        xb.xbee_write(packet)
        
        sleep(30)
        
    except Exception as e:
        print(e)
        sleep(30)
    
   
        
