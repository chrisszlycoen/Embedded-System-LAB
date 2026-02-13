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

# MQTT Topics
BASE_TOPIC      = "rfid/{}/".format(TEAM_ID)
STATUS_TOPIC    = BASE_TOPIC + "card/status"      
TOPUP_TOPIC     = BASE_TOPIC + "card/topup"       
BALANCE_TOPIC   = BASE_TOPIC + "card/balance"     

# RFID pins - YOUR exact wiring (Preserved from original code888 request)
SCK_PIN   = 14   # D5
MOSI_PIN  = 13   # D7
MISO_PIN  = 12   # D6
RST_PIN   = 4    # D2
CS_PIN    = 15   # D8

# Balance storage on card (MIFARE Classic 1K)
BLOCK_NUMBER = 8
DEFAULT_KEY  = [0xFF] * 6

# ===================== RFID READER INIT =====================
reader = MFRC522(SCK_PIN, MOSI_PIN, MISO_PIN, RST_PIN, CS_PIN)

# ===================== NETWORK FUNCTIONS =====================
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
            print(".", end="")
    
    if wlan.isconnected():
        print("\nWiFi connected:", wlan.ifconfig())
    else:
        print("\nWiFi connection FAILED - check SSID/password")

# ===================== MQTT RECONNECT LOGIC =====================
def mqtt_connect(client):
    while True:
        try:
            print("Attempting MQTT connection...")
            client.connect()
            print("MQTT connected successfully!")
            client.subscribe(TOPUP_TOPIC)
            print("Subscribed to: {}".format(TOPUP_TOPIC))
            return True
        except OSError as e:
            print("MQTT connect failed:", e)
            print("Retrying in 5 seconds...")
            time.sleep(5)

# ===================== TOP-UP HANDLER =====================
def on_mqtt_message(topic, msg):
    try:
        data = json.loads(msg)
        target_uid = data.get("uid")
        amount = data.get("amount", 0)
        
        if amount <= 0:
            print("Invalid amount received")
            return
        
        print("Top-up command received -> UID: {}, Amount: {}".format(target_uid, amount))

        # Check if card is present and UID matches
        (status, uid) = reader.request(reader.REQIDL)
        if status != reader.OK:
            # Try anticoll directly just in case
            pass

        (status, uid) = reader.anticoll()
        if status != reader.OK:
            print("No card present")
            return
        
        current_uid = "".join("{:02X}".format(x) for x in uid)
        if current_uid != target_uid:
            print("UID mismatch (card: {}, requested: {})".format(current_uid, target_uid))
            return
        
        # Authenticate
        if reader.select_tag(uid) != reader.OK:
            print("Select tag failed")
            return

        if reader.auth(reader.AUTHENT1A, BLOCK_NUMBER, DEFAULT_KEY, uid) != reader.OK:
            print("Authentication failed")
            reader.stop_crypto1()
            return
        
        # Read current balance
