#! /usr/bin/python3
#sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock
#sudo systemctl start mosquitto
#sudo journalctl -efu mosquitto

import paho.mqtt.publish as publish
from gps3 import agps3
import os
import time
import sys

gps_socket = agps3.GPSDSocket()
data_stream = agps3.DataStream()

gps_socket.connect()
gps_socket.watch()
exec_time = 10
t_end = time.time()+exec_time

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

lon = data_stream.lon
lat = data_stream.lat

MQTT_SERVER = "192.168.1.68"
MQTT_PATH = "LongLat"

publish.single(MQTT_PATH,str(lat)+","+str(lon),hostname=MQTT_SERVER)

#MQTT_SERVER = "192.168.1.68"
#MQTT_PATH = "LongLat"


for new_data in gps_socket:
        try:
                lon1=data_stream.lon
                lat1=data_stream.lat
                if lon1 != lon and lat1 != lat:
                        print("dans if "+new_data+"\n")
                        publish.single(MQTT_PATH,str(lat)+","+str(lon),hostname=MQTT_SERVER)
                        time.sleep(6)
                else:
                        time.sleep(5)

        except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
                print ("\nKilling Thread...")
                sys.exit(0)

