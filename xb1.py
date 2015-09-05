from serial import Serial
import random
import time

xb = Serial('/dev/port2',9600,timeout=1)

def dummyPacket():
    val = random.randint(0,55)
    return str(val)

while True:
	t  = time.strftime("%Y-%m-%d %H:%M:%S")
	value = dummyPacket()
	packet = t+';'+value
	#data = raw_input("Data: ")

	xb.write(packet)
	time.sleep(3)
