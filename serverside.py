import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc): #called when broker connects.
    print("Active" + str(rc))
def on_message(client, userdata, msg): #called when a message has been recieved
    global FLAG
    global chat
    if str(msg.topic) != publishtopic:
        msg = str(msg.payload.decode("utf-8"))
        print(str(msg.topic),msg)
        if msg == "Stop" or msg == "stop":
            FLAG = False
        else:
            chat = input("Enter Message: ")
            client.publish(publishtopic, chat)
def on_subscribe(client, userdata):
    print("Subscribed: ")

def on_unsubscribe(client, userdata, mid):
    print("Left Chat." + str(mid))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Disconnected")
        
user = "localhost"
port = 1883

client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message
client.on_unsubscribe = on_unsubscribe
client.on_disconnect = on_disconnect
client.connect("localhost", 1883, 60)

time.sleep(1)

publishtopic = "Username1"
subtopic = "Username2"
FLAG = True

client.loop_start()
client.subscribe(subtopic)

time.sleep(1)

chat = input("Enter Message: ")
client.publish(publishtopic, chat)
while True:
    if FLAG == False:
        break

client.disconnect()
client.loop_stop()
