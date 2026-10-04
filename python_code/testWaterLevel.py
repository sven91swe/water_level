#!/usr/bin/env python3

import serial
import time
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
	temp = ser.readline()
	d = json.loads(temp)
	print(d["waterlevelvoltage"])
	time.sleep(0.01)
