import paho.mqtt.client as mqtt
import socket 

connected = False



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
        global connected 
        connected = True  

    else:
        print("Connection failed")

s = socket.socket()
host = socket.gethostname()
port = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.connect("192.168.100.7", 1883, 60)
client.loop_start()
while connected:
    message = input("Message: ")
    client.publish("UG/MJNORVOR", message)
    
client.loop_forever()