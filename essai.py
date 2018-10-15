#! /usr/bin/python3

from gps3 import agps3
import os
import time
import sys

gps_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()

gps_socket.connect()
gps_socket.watch()

t_end = time.time()+15

for new_data in gps_socket:
	if new_data:
		os.system('clear')
		data_stream.unpack(new_data)
		print(' GPS reading')
		print('---------------------------------------')
		print('Latitude = ', data_stream.lat)
		print('Longitude =', data_stream.lon)
		if time.time() >= t_end:
			break

lon = data_stream.lat
lat = data_stream.lon

sys.exit(0)
