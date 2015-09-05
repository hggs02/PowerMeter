import serial
import time
import os
from database_handler import database_class


class Xbee(object):
    def __init__ (self):
        self.obj = serial.Serial('/dev/xb2',9600,timeout=1)
    
    def xbee_write(self,data):
        self.obj.write(data)
        

    def xbee_read(self):
        val = self.obj.read(100).strip()
        return val

    def __del__(self):
        self.obj.close()



def extractData(packet):
        data = packet.split(';')
        return data

def main():
        db = database_class()
        #os.system('clear')                             # Works only in linux
        print('\t\tPOWER CONSUMPTION')

        while True:
                xb = Xbee()
                packet = xb.xbee_read()
                if packet:
        		data = extractData(packet)
                
                        print('-------------------------------------------------')

                        try:
                                tm = data[0]
                                power = data [1]
                                print '|',tm,'\tConsumption => \t',power,'Unit','|','\n'
                                db.insertDb(tm,power)
                        except Exception as e:
                                print e
            
if __name__ == '__main__':
        main()