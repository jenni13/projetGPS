#! /usr/bin/python3
#sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock

import paho.mqtt.publish as publish
 
MQTT_SERVER = "192.168.1.68"
MQTT_PATH = "Longitude_Latitude "

 
publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
