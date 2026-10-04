#!/usr/bin/env python3

import numpy as np
from datetime import datetime, timedelta
import json


# Config, time between writing to database (seconds)
timeperiod = 180

# Setup serial
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

# Database settings
import MySQLdb
from database import db_user, db_password, db_name
db = MySQLdb.connect(user=db_user, passwd=db_password, db=db_name)

def save_to_database(value):
	c=db.cursor()
	command = "INSERT INTO `data` (`value`, `time`) VALUES ('"+str(median)+"','"+datetime.now().__str__()+"');"
	print(command)
	c.execute(command)	
	db.commit()
	c.close()

while True:
	currentTime = datetime.now()
	arr = np.array([])
	
	while datetime.now() < currentTime + timedelta(0,timeperiod):
		try:
			serialInput = ser.readline()
			data = json.loads(serialInput)

			voltage = float(data["waterlevelvoltage"])
			relayState = bool(data["relaystate"])

			tempWaterLevel = int(max(voltage/2.18*100, 0))
			print(f"Nivå: {tempWaterLevel}, relätillstånd: {relayState}")
			arr = np.append(arr, tempWaterLevel)
		except:
			print("Unable to read input")
			import time
			time.sleep(2)

	print(arr)
	median = int(10*np.median(arr))
	
	save_to_database(median)
