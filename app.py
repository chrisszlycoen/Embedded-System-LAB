from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
