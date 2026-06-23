
# RuView Setup Guide (2-Node ESP32-S3 Deployment)

## Project Overview

This document records the complete setup process used to deploy RuView WiFi DensePose Sensing with two ESP32-S3 N16R8 nodes and a Kali Linux VM running in VMware.

---

# Hardware Used

## Host System

- Windows 11 Host
    
- VMware Workstation
    

## Virtual Machine

- Kali Linux
    
- 4 CPU Cores
    
- 4 GB RAM
    
- Bridged Network Mode
    

## Router

- SSID: (Redacted)
    
- Security: WPA2-PSK
    
- Channel: 6
    
- Bandwidth: 20/40 MHz
    

## ESP32 Boards

### Node 1

- ESP32-S3-WROOM-1-N16R8
    
- 16 MB Flash
    
- 8 MB PSRAM
    
- IP: 192.168.1.9
    
- Node ID: 1
    

### Node 2

- ESP32-S3-WROOM-1-N16R8
    
- 16 MB Flash
    
- 8 MB PSRAM
    
- IP: 192.168.1.8
    
- Node ID: 2
    

---

# Network Architecture

```text
ESP32 Node 1 (192.168.1.9)
            \
             \
              ---> RuView Server (192.168.1.10:5005)
             /
            /
ESP32 Node 2 (192.168.1.8)

Router/AP
SSID: (Redacted)
Channel: 6
```

---

# Verify ESP32 Connection

Connect ESP32 board.

```bash
lsusb
```

Expected:

```text
1a86:55d3 QinHeng Electronics USB Single Serial
```

Check serial devices:

```bash
ls /dev/ttyACM*
```

Example:

```text
/dev/ttyACM0
/dev/ttyACM1
```

Verify board:

```bash
python3 -m esptool --chip esp32s3 -p /dev/ttyACM0 flash_id
```

Expected:

```text
ESP32-S3
16MB Flash
8MB PSRAM
```

---

# ESP-IDF Installation

Create workspace:

```bash
mkdir -p ~/esp
cd ~/esp
```

Clone ESP-IDF:

```bash
git clone -b v5.4 --recursive https://github.com/espressif/esp-idf.git
```

Install tools:

```bash
cd ~/esp/esp-idf
./install.sh
```

Load environment:

```bash
source ~/esp/esp-idf/export.sh
```

Verify:

```bash
idf.py --version
```

Expected:

```text
ESP-IDF v5.4
```

---

# Clone RuView

```bash
cd ~

git clone https://github.com/ruvnet/RuView.git
```

---

# Fix Broken Submodules

Initialize submodules:

```bash
git submodule update --init --recursive
```

---

## Fix rufield

```bash
cd ~/RuView/vendor/rufield

git reset --hard HEAD
```

Verify:

```bash
ls
```

Expected:

```text
Cargo.toml
crates/
README.md
```

---

## Fix ruview-swarm

```bash
cd ~/RuView/v2/crates/ruview-swarm

git reset --hard HEAD
```

Verify:

```bash
ls
```

Expected:

```text
Cargo.toml
src/
README.md
```

---

## Verify worldgraph

```bash
cd ~/RuView/v2/crates/worldgraph

find . -name Cargo.toml
```

Expected:

```text
wifi-densepose-geo/Cargo.toml
wifi-densepose-worldgraph/Cargo.toml
wifi-densepose-worldmodel/Cargo.toml
```

---

# Build ESP32 Firmware

```bash
cd ~/RuView/firmware/esp32-csi-node

source ~/esp/esp-idf/export.sh
```

Set target:

```bash
idf.py set-target esp32s3
```

Build:

```bash
idf.py build
```

Expected build time:

```text
3-5 minutes
```

---

# Flash Firmware

## Node 1

```bash
idf.py -p /dev/ttyACM0 flash
```

## Node 2

```bash
idf.py -p /dev/ttyACM1 flash
```

---

# Install NVS Generator

```bash
pip3 install esp-idf-nvs-partition-gen --break-system-packages
```

---

# Provision Node 1

```bash
python3 provision.py \
  --port /dev/ttyACM0 \
  --ssid "(Redacted)" \
  --password "(Redacted)" \
  --target-ip 192.168.1.10 \
  --node-id 1
```

---

# Provision Node 2

```bash
python3 provision.py \
  --port /dev/ttyACM1 \
  --ssid "(Redacted)" \
  --password "(Redacted)" \
  --target-ip 192.168.1.10 \
  --node-id 2
```

---

# Verify Node Operation

Monitor:

```bash
idf.py -p /dev/ttyACM0 monitor
```

or

```bash
idf.py -p /dev/ttyACM1 monitor
```

Expected:

```text
Got IP
Connected to WiFi
CSI streaming active
```

Expected Node IDs:

```text
node_id=1
node_id=2
```

---

# Build RuView Backend

Install Rust:

```bash
rustc --version
cargo --version
```

Verify:

```text
rustc 1.96+
cargo 1.96+
```

Build:

```bash
cd ~/RuView/v2

cargo build --release
```

Expected build time:

```text
3-5 minutes
```

---

# Run RuView Server

```bash
cd ~/RuView/v2

cargo run -p wifi-densepose-sensing-server --release
```

Expected:

```text
HTTP server listening on 127.0.0.1:8080
WebSocket server listening on 127.0.0.1:8765
UDP listening on 0.0.0.0:5005
ESP32 CSI detected on UDP :5005
```

---

# Verify CSI Traffic

```bash
sudo tcpdump -nn -i any udp port 5005
```

Expected:

```text
192.168.1.8 -> 192.168.1.10:5005
192.168.1.9 -> 192.168.1.10:5005
```

This confirms multi-node CSI streaming.

---

# Open Dashboard

Open browser:

```text
http://localhost:8080/ui/observatory.html
```

or

```text
http://127.0.0.1:8080/ui/observatory.html
```

---

# Expected Dashboard Features

- Live CSI Data
    
- Presence Detection
    
- Person Counting
    
- Motion Detection
    
- Vital Sign Monitoring
    
- RSSI Monitoring
    
- Pose Visualization
    
- WebSocket Streaming
    

---

# VMware Configuration

VM Settings:

```text
Network Adapter
→ Bridged Mode
```

Do NOT use:

```text
NAT
```

The ESP32 devices must be able to reach the VM directly.

---

# Troubleshooting

## idf.py command not found

```bash
source ~/esp/esp-idf/export.sh
```

---

## Port Busy

```bash
Ctrl + ]
```

Exit monitor first.

---

## NVS Generator Missing

```bash
pip3 install esp-idf-nvs-partition-gen --break-system-packages
```

---

## ESP32 Not Appearing

Check VMware:

```text
VM → Removable Devices → Connect
```

---

## No CSI Traffic

Verify:

```bash
sudo tcpdump -nn -i any udp port 5005
```

---

# Final Status

Deployment Status: SUCCESS

Configuration:

- ESP32-S3 Node 1: Operational
    
- ESP32-S3 Node 2: Operational
    
- ESP-NOW Synchronization: Operational
    
- WiFi CSI Collection: Operational
    
- UDP Streaming: Operational
    
- RuView Backend: Operational
    
- Dashboard: Operational
    
- Multi-Node CSI Sensing: Operational
    

Date Completed: June 2026  
Environment: Kali Linux VM on VMware  
Project: RuView WiFi DensePose Sensing Observatory