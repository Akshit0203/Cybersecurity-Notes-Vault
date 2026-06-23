# Complete Reproduction Guide

## Overview

This guide provides **fully detailed, step-by-step instructions based on exactly what was done during setup** to recreate the **Distributed WiFi CSI Human Sensing Platform** from scratch.

Every command, configuration step, and verification step is included so that **someone can follow this guide line-by-line and reproduce the system exactly as implemented**.

This includes:

- Installing all required tools
    
- Cloning and fixing the RuView repository
    
- Building the backend
    
- Building and flashing ESP32 firmware
    
- Configuring WiFi and networking
    
- Running the backend server
    
- Verifying CSI data flow
    
- Viewing the dashboard
    
- Testing sensing functionality
    

---

# System Overview

The system architecture used:

```text
ESP32-S3 Node 1
        \
         \
          ---> RuView Backend ---> Dashboard (Browser)
         /
        /
ESP32-S3 Node 2
```

### What Actually Happens (Step-by-Step)

1. Both ESP32 boards connect to the same WiFi network.
    
2. Each ESP32 captures WiFi CSI data continuously.
    
3. Each ESP32 sends CSI packets via UDP to the backend IP.
    
4. The backend listens on UDP port 5005.
    
5. The backend processes CSI data in real time.
    
6. The backend exposes:
    
    - HTTP server (dashboard)
        
    - WebSocket server (live updates)
        
7. The browser connects to the backend and displays:
    
    - CSI heatmaps
        
    - Motion detection
        
    - Presence detection
        
    - Occupancy estimation
        

---

# Hardware Requirements

## ESP32 Nodes

Quantity:

```text
2
```

Model used:

```text
ESP32-S3-WROOM-1-N16R8
```

### Why this model was used

- Supports CSI extraction
    
- Has enough RAM (8MB PSRAM)
    
- Stable WiFi performance
    

---

## USB Cables

Quantity:

```text
2
```

Used for:

- Flashing firmware
    
- Powering boards
    
- Viewing serial logs
    

---

## Host Computer

Used:

- Kali Linux machine
    

Minimum:

- Quad Core CPU
    
- 8 GB RAM
    

Recommended:

- 16 GB RAM
    
- SSD (important for Rust builds)
    

---

## WiFi Network

Requirements:

- 2.4 GHz network (ESP32 does NOT support 5 GHz)
    
- Same network for ESP32 and backend
    

Example used:

```text
SSID: YourWiFi
Password: YourPassword
```

---

# Software Setup (Exactly What Was Done)

## Step 1: Install Git

```bash
sudo apt update
sudo apt install git -y
```

Verify:

```bash
git --version
```

---

## Step 2: Install Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Press Enter for default install.

Then run:

```bash
source $HOME/.cargo/env
```

Verify:

```bash
rustc --version
cargo --version
```

---

## Step 3: Install Python

```bash
sudo apt install python3 python3-pip -y
```

Verify:

```bash
python3 --version
```

---

## Step 4: Install ESP-IDF (IMPORTANT)

### What was done exactly:

```bash
mkdir -p ~/esp
cd ~/esp
git clone --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
git checkout v5.4
```

Install tools:

```bash
./install.sh
```

Load environment:

```bash
source export.sh
```

Verify:

```bash
idf.py --version
```

---

# Clone RuView Repository

## Step 1: Create workspace

```bash
mkdir -p ~/projects
cd ~/projects
```

## Step 2: Clone repo

```bash
git clone https://github.com/ruvnet/RuView.git
```

## Step 3: Enter repo

```bash
cd RuView
```

---

# Initialize Submodules (THIS WAS REQUIRED)

Run:

```bash
git submodule update --init --recursive
```

Wait until everything finishes.

---

# Fix Broken Submodules (THIS ACTUALLY HAPPENED)

Some submodules were empty or broken.

### Symptoms seen:

```text
Cargo.toml missing
No such file or directory
```

### Fix used:

For each broken folder:

```bash
cd vendor/rufield
git reset --hard HEAD
ls
```

Repeat for:

```text
vendor/rufield
v2/crates/ruview-swarm
```

After this, files appeared correctly.

---

# Build Backend (What Was Done)

## Step 1: Navigate

```bash
cd ~/projects/RuView/v2
```

## Step 2: Build

```bash
cargo build --release
```

### Notes:

- First build took several minutes
    
- Dependencies downloaded automatically
    

Expected output:

```text
Finished release profile
```

---

# Verify Backend Build

```bash
ls target/release
```

Expected:

```text
sensing-server
```

---

# Build ESP32 Firmware

## Step 1: Navigate

```bash
cd ~/projects/RuView/firmware/esp32-csi-node
```

## Step 2: Load ESP-IDF

```bash
source ~/esp/esp-idf/export.sh
```

## Step 3: Build firmware

```bash
idf.py build
```

Expected:

```text
Build complete
```

---

# Connect ESP32 Boards

Plug both boards into USB.

Check ports:

```bash
ls /dev/ttyACM*
```

Example seen:

```text
/dev/ttyACM0
/dev/ttyACM1
```

---

# Configure Firmware (IMPORTANT STEP DONE BEFORE FLASHING)

Inside firmware project, configuration was edited to include:

```text
SSID
PASSWORD
TARGET_IP
TARGET_PORT
NODE_ID
```

### Example used:

```text
Node 1:
SSID: YourWiFi
PASSWORD: YourPassword
TARGET_IP: 192.168.1.10
TARGET_PORT: 5005
NODE_ID: 1

Node 2:
NODE_ID: 2
```

---

# Find Backend IP (What Was Done)

```bash
ip addr
```

Look for:

```text
192.168.1.10
```

This IP was used as:

```text
TARGET_IP
```

---

# Flash ESP32 Nodes

## Node 1

```bash
idf.py -p /dev/ttyACM0 flash
idf.py -p /dev/ttyACM0 monitor
```

## Node 2

```bash
idf.py -p /dev/ttyACM1 flash
idf.py -p /dev/ttyACM1 monitor
```

---

# Start Backend Server

## Step 1: Navigate

```bash
cd ~/projects/RuView/v2
```

## Step 2: Run

```bash
cargo run -p wifi-densepose-sensing-server --release
```

### Output observed:

```text
UDP listening on 0.0.0.0:5005
HTTP server listening on 127.0.0.1:8080
WebSocket server listening on 127.0.0.1:8765
```

---

# Verify CSI Data is Actually Arriving

## Step 1: Open new terminal

```bash
sudo tcpdump -nn -i any udp port 5005
```

### What was seen:

```text
192.168.1.x -> 192.168.1.10:5005
```

Packets continuously appeared.

---

# Verify Backend is Using Real Data

Backend logs showed:

```text
ESP32 CSI detected on UDP :5005
Data source: esp32
```

If it shows:

```text
Data source: simulated
```

→ No real data is arriving.

---

# Open Dashboard

Open browser:

```text
http://localhost:8080/ui/index.html
```

---

# Verify Dashboard Behavior

Observed:

- Live updating graphs
    
- CSI heatmaps
    
- Node information
    
- Occupancy values changing
    

---

# Functional Testing (What Was Done)

## Motion Test

1. Stood still → baseline stable
    
2. Walked through area → values increased
    

Observed:

```text
Motion increases when moving
```

---

## Presence Test

1. Entered sensing area → detected
    
2. Left area → detection dropped
    

Observed:

```text
Presence detected and decreases when leaving
```

---

## Multi-Person Test

Multiple people stood in area.

Observed:

```text
Occupancy value increased
```

---

# Common Issues Encountered

## No UDP Traffic

Checked:

```bash
tcpdump -nn -i any udp port 5005
```

Fix:

- Verified WiFi connection
    
- Verified IP address
    
- Verified port 5005
    

---

## Simulated Data Showing

Cause:

Backend not receiving CSI packets.

Fix:

- Corrected firmware config
    
- Ensured ESP32 connected to WiFi
    

---

## Build Errors (Submodules)

Fix used:

```bash
git submodule update --init --recursive
git reset --hard HEAD
```

---

## ESP32 Not Detected

Checked:

```bash
ls /dev/ttyACM*
```

Replugged USB cable.

---

# Validation Checklist

## Backend

-  Built successfully
    
-  UDP listening
    
-  HTTP running
    
-  WebSocket running
    

## Firmware

-  Built successfully
    
-  Flashed successfully
    
-  Connected to WiFi
    

## Networking

-  UDP packets visible
    
-  CSI data arriving
    

## Dashboard

-  Loads correctly
    
-  Updates live
    
-  Shows heatmaps
    

## Sensing

-  Motion detection works
    
-  Presence detection works
    
-  Occupancy estimation works
    

---

# Expected Results

- Real-time CSI streaming from both ESP32 nodes
    
- Multi-node sensing working simultaneously
    
- Accurate motion detection
    
- Presence detection working
    
- Occupancy estimation responding to number of people
    
- Live dashboard visualization updating continuously
    

---

# Tested Configuration

Hardware:

```text
2 × ESP32-S3-WROOM-1-N16R8
```

Backend:

```text
RuView WiFi DensePose Sensing Server
```

Operating System:

```text
Kali Linux
```

Ports used:

```text
UDP 5005
WebSocket 8765
HTTP 8080
```

Final Status:

```text
Fully reproduced and validated successfully
```