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

