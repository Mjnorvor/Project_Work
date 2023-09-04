import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc): #called when broker connects.
    print("Active" + str(rc))

def on_message(client, userdata, message): #called when a message has been recieved
    global FLAG
    global chat
    if str(message.topic) != publishtopic:
        msg = str(message.payload.decode("utf-8"))
        print(str(message.topic),msg)
        if msg == "Stop" or msg == "stop":
            FLAG = False
        else:
            chat = input("Enter Message: ")
            client.publish(publishtopic, chat)
            
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: ")

def on_unsubscribe(client, userdata, mid):
    print("Left Chat." + str(mid))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Disconnected")
        
user = "mqtt.eclipseprojects.io"
port = 1883

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message
client.on_unsubscribe = on_unsubscribe
client.on_disconnect = on_disconnect
client.connect("mqtt.eclipseprojects.io", 1883, 60)

time.sleep(1)

publishtopic = "Username2"
subtopic = "Username1"
FLAG = True
chat = None

client.loop_start()
client.subscribe(subtopic)

while True:
    if FLAG == False or chat == "Stop" or chat == "stop":
        break

client.disconnect()
client.loop_stop()
