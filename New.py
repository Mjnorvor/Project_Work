import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "mqtt.eclipse.org"
port = 1883

# Unique client ID for each user
client_id = "client1"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# Create an MQTT client
client = mqtt.Client(client_id)

# Set the callback
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect(broker_address, port, 60)

# Main loop to send messages
while True:
    message = input("Client 1: Enter your message: ")
    client.publish("chatroom", message)
