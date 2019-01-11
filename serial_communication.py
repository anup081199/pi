import serial
import time

ser=serial.Serial('/dev/ttyACM0',9600)
while True:
	data=ser.readline()
	time.sleep(1)
	data=ser.readline()
	print data
	#if (data=="reached"):
	#	ser.write()
