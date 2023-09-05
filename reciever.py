import paho.mqtt.client as mqtt

# MQTT broker settings
broker_address = "mqtt.eclipse.org"
port = 1883

# Unique client ID for each user
client_id = "client2"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("chatroom")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(msg.payload.decode())

# Create an MQTT client
client = mqtt.Client(client_id)

# Set callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port, 60)

# Loop forever to handle incoming messages
client.loop_forever()
