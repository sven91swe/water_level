#!/usr/bin/env python3

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	temp = float(ser.readline())
	print(temp)
	time.sleep(0.01)
