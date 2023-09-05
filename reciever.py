import tkinter as tk
import paho.mqtt.client as mqtt

# MQTT settings
broker_address = "mqtt.eclipse.org"  # Change to your MQTT broker address
topic = "chatroom"

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, message):
    received_message = message.payload.decode()
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Received: {received_message}\n")
    chat_display.config(state=tk.DISABLED)

def send_message():
    user_message = message_entry.get()
    if user_message:
        mqtt_client.publish(topic, user_message)
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You: {user_message}\n")
        chat_display.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)

# MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker_address, 1883, 60)

# Create GUI
root = tk.Tk()
root.title("MQTT Chat App")

chat_display = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_display.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start MQTT client loop
mqtt_client.loop_start()

root.mainloop()
