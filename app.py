from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

TEAM_ID = "code888"
MQTT_BROKER = "157.173.101.159"
TOPIC_STATUS = f"rfid/{TEAM_ID}/card/status"
TOPIC_TOPUP = f"rfid/{TEAM_ID}/card/topup"
TOPIC_BALANCE = f"rfid/{TEAM_ID}/card/balance"

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to MQTT with result code {rc}")
    client.subscribe(TOPIC_STATUS)
    client.subscribe(TOPIC_BALANCE)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Received MQTT: {payload}")
        
        socketio.emit('update_dashboard', payload)
    except Exception as e:
        print(f"Error parsing MQTT message: {e}")
