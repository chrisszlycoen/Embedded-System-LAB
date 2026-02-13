import network
import time
import json
import ubinascii
import machine
from umqtt.simple import MQTTClient
from mfrc522 import MFRC522

# ===================== CONFIG - CHANGE THESE =====================
TEAM_ID         = "code888"
WIFI_SSID       = "EdNet"
WIFI_PASSWORD   = "Huawei@123"

MQTT_BROKER     = "157.173.101.159"
MQTT_PORT       = 1883
MQTT_CLIENT_ID  = b"esp8266_" + ubinascii.hexlify(machine.unique_id())
