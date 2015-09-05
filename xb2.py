from serial import Serial

xb = Serial('/dev/port4',9600,timeout=1)


while True:
	data = xb.read(100)
	if data:
		print data