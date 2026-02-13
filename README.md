# RFID Card Top-Up System (Local Mode)

This project has been configured to run **completely locally** on your computer without any external VPS or public MQTT broker.

## Prerequisites
- Node.js installed.
- ESP8266 + MFRC522 (RC522) module.
- A computer and ESP8266 connected to the **same WiFi network**.

## 1. Setup Backend (Broker + Server)
The `server.js` file now includes its own MQTT broker (running on port 1883).

1.  Open terminal in project folder:
    ```bash
    npm install express mqtt ws cors body-parser aedes
    ```
2.  Start the server:
    ```bash
    node server.js
    ```
    You should see:
    > [Broker] MQTT Broker running on port 1883
    > [HTTP] Server running on http://localhost:3000

## 2. Configure ESP8266
You need to tell the ESP8266 the IP address of your computer.

1.  **Find your IP Address**:
    - Windows: Run `ipconfig` in CMD. Look for `IPv4 Address` (e.g., `192.168.1.105`).
    - Linux/Mac: Run `ip a` or `ifconfig`. Look for `inet` address (e.g., `192.168.1.105`).
2.  **Edit `main.py`**:
    - Open `main.py` in Thonny.
    - Change `MQTT_BROKER` to your computer's IP:
      ```python
      MQTT_BROKER = "192.168.1.105" # Example
      ```
    - Start the script on ESP8266.

## 3. Run Dashboard
1.  Open `index.html` in your browser.
