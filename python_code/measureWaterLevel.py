#!/usr/bin/env python3

import serial
import numpy as np
from datetime import timedelta
from datetime import datetime

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

ser = serial.Serial('/dev/ttyACM0', 9600)

timeperiod = 10

while True:
	currentTime = datetime.now()
	arr = np.array([])
	
	while datetime.now() < currentTime + timedelta(0,timeperiod):
		try:
			temp = int(max(float(ser.readline())/2.18*100, 0))
			print(temp)
			arr = np.append(arr, temp)
		except:
			print("Unable to read input")
			import time
			time.sleep(2)

	print(arr)
	median = int(10*np.median(arr))
	
	save_to_database(median)
