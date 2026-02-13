import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "157.173.101.159"
TEAM_ID = "code888"
TOPIC_STATUS = f"rfid/{TEAM_ID}/card/status"
