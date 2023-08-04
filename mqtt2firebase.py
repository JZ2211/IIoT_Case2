# paho MQTT client example
# Save received message to a local .txt file
# and push the message to Google Firebase Realtime database
#
# Modified 7/31/2023
# by Jin Zhu
#
# required package: firebase-admin 
# $sudo pip3 install firebase-admin==5.4.0


import time
from datetime import datetime

import paho.mqtt.client as mqtt
from savefile import save_tofile
from firebaseaccess import push_tofirebase

#Data will be save under the dirctory HOMEPATH/nodeID. For example, /home/pi/node1
HOMEPATH='/home/pi/' #adjust the home path if needed

TOPIC = "workshop/bme280"
USERNAME = "user1"        #MQTT server username
PASSWORD = "workshop"     #MQTT server pasword
mqtt_server = "127.0.0.1" #use localhost since it is in the same broker server
#if not, please use the IP address of the broker server, e.g. mqtt_server = "192.168.1.2"


### MQTT callback functions  ###
# The callback function for when the client receives a CONN ACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")  #display all system messages of MQTT
    client.subscribe(TOPIC)

# The callback function for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
    #print(len(msg.payload))
    timestamp = str(datetime.now()).split(' ') #obtain current time and date
    currentdate = timestamp[0]
    currenttime = timestamp[1]
    msglist = msg.payload.decode('utf-8').split(',') #convert the message to a list of strings
    nodeID = msglist.pop(0) #remove the first item in the list as the nodeID
    #print(nodeID)
    message= str(msg.payload).split("'")[1] #remove b' and convert to string
    push_tofirebase(nodeID, currentdate, currenttime, msglist)
    save_tofile(HOMEPATH, nodeID, currentdate, currenttime, message)
### end of call back functions ###
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(USERNAME,PASSWORD)
client.connect(mqtt_server,1883)  #use default MQTT port 1883

client.loop_forever()
