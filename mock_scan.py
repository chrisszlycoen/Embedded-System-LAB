import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "xxx.xxx.xxx.xxx"
TEAM_ID = "Any_team_id"
TOPIC_STATUS = f"rfid/{TEAM_ID}/card/status"

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to MQTT (RC: {rc})")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.connect(BROKER, 1883, 60)
client.loop_start()

time.sleep(1)

# 1. Simulate Card Scan
print(">>> Simulating Card SCAN...")
uid = "A1 B2 C3 D4"
client.publish(TOPIC_STATUS, json.dumps({
    "uid": uid,
    "balance": random.randint(1000, 50000)
}))
time.sleep(3)

# 2. Simulate Card Removal
print(">>> Simulating Card REMOVAL...")
client.publish(TOPIC_STATUS, json.dumps({"uid": None}))

time.sleep(1)
client.loop_stop()
print("Done.")
