# RFID System - VPS Deployment Guide

**Target VPS**: `157.173.101.159`
**User**: `user272`
**Password**: `ZK!@9QM7`

## 1. Connect to VPS
Open your terminal and run:
```bash
ssh user272@157.173.101.159
# Enter password: ZK!@9QM7
```

## 2. Install Node.js (If not installed)
```bash
cd ~
wget https://nodejs.org/dist/v18.20.2/node-v18.20.2-linux-x64.tar.xz
tar -xf node-v18.20.2-linux-x64.tar.xz
export PATH=$HOME/node-v18.20.2-linux-x64/bin:$PATH

# Add to profile so it stays after logout
echo 'export PATH=$HOME/node-v18.20.2-linux-x64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

## 3. Setup Backend
```bash
mkdir -p rfid-backend
cd rfid-backend

# Initialize and Install
npm init -y
npm install express ws mqtt cors body-parser

# Create/Edit server.js
nano server.js
# Paste the content of your server.js here! 
# (Right-click to paste in most terminals, or Ctrl+Shift+V)
# Press Ctrl+O, Enter, Ctrl+X to save and exit.

# Run Server (in background)
nohup node server.js > server.log 2>&1 &
```

## 4. Setup Frontend (Optional, or run locally)
Since checking the dashboard from your local computer:
1.  Open `index.html` on your **local computer**.
2.  Ensure the "Backend URL" input is `http://157.173.101.159:3000`.
3.  Click "Set".

*Note: You can also serve file on VPS using `python3 -m http.server 9252` if you want a hosted link.*

## 5. Flash ESP8266
1.  Open `main.py` in Thonny.
2.  Ensure `MQTT_BROKER = "157.173.101.159"`.
3.  Flash/Run.

## Troubleshooting
- If `node server.js` fails with `EADDRINUSE`, change `HTTP_PORT` in `server.js` to something like `3001` or `3002`, and update `index.html`.
- If MQTT fails, ensure the VPS broker is actually running (`mosquitto` service).
