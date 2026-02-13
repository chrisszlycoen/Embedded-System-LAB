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
