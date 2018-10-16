#! /usr/bin/python3

import paho.mqtt.client as mqtt
import webbrowser

#MQTT_SERVER = "localhost"
MQTT_SERVER = "192.168.0.88"
MQTT_PATH = "LongLat"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload)+" "+str(msg.payload))
    msg.payload = msg.payload.decode("utf-8")
    print(str(msg.payload))
    url = "http://maps.google.com/maps?q="+str(msg.payload)
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(url)


    # more callbacks, etc

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()

#long= msg.payload
#latt = msg.payload
   # url = "http://maps.google.com/maps?q="+str(long)+","+str(lat)
   # chrome_path = '/usr/bin/google-chrome %s'
   # webbrowser.get(chrome_path).open(url)

client.loop_forever()
