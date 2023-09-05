import tkinter as tk
import paho.mqtt.client as mqtt


broker_address = "mqtt.eclipseprojects.io"
topic = "Chatroom"


def on_connect(client, userdata, flags, rc):
     
     
     if rc == 0:
        print("Connected to broker")
        global Connected  
        Connected = True  
        client.subscribe(topic)
     else:
        print("Connection failed")

Connected = False

def on_message(client, userdata, message):
    received_message = message.payload.decode()
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{received_message}\n")
    chat_display.config(state=tk.DISABLED)

def send_message():
    user_message = message_entry.get()
    if user_message:
        mqtt_client.publish(topic, f"User1: {user_message}")
        chat_display.config(state=tk.NORMAL)
        chat_display.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(broker_address, 1883, 60)


root = tk.Tk()
root.title("CHATPY APP")

chat_display = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_display.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()


mqtt_client.loop_start()

root.mainloop()