
# ESP32 Firmware Deployment and Provisioning

## Overview

This document describes the complete firmware deployment process used to configure the ESP32-S3 sensing nodes for WiFi Channel State Information (CSI) collection and integration with the RuView sensing platform.

The deployment included:

- ESP-IDF setup
    
- Firmware compilation
    
- Firmware flashing
    
- Node provisioning
    
- WiFi configuration
    
- CSI activation
    
- Multi-node deployment
    

At the conclusion of this process, two ESP32-S3 nodes were successfully collecting CSI data and streaming it to the RuView backend.

---

# Firmware Architecture

## Firmware Component

```text
esp32-csi-node
```

This firmware is responsible for:

- WiFi connectivity
    
- CSI collection
    
- CSI packet formatting
    
- UDP streaming
    
- ESP-NOW synchronization
    
- Node coordination
    

---

# Development Environment

## Operating System

```text
Kali Linux
```

## Framework

```text
ESP-IDF v5.4
```

## Toolchain

```text
Xtensa ESP32-S3 Toolchain
```

---

# ESP-IDF Installation

A dedicated ESP-IDF environment was installed for firmware development.

## Clone ESP-IDF

```bash
git clone -b v5.4 --recursive https://github.com/espressif/esp-idf.git
```

---

## Install Toolchain

```bash
cd ~/esp/esp-idf

./install.sh
```

---

## Load Environment

```bash
source ~/esp/esp-idf/export.sh
```

---

## Verification

```bash
idf.py --version
```

Expected:

```text
ESP-IDF v5.4
```

---

# Obtaining Firmware Source

## Clone RuView Repository

```bash
git clone https://github.com/ruvnet/RuView.git
```

---

## Firmware Location

```text
RuView/firmware/esp32-csi-node
```

---

# Firmware Compilation

## Configure Target

```bash
idf.py set-target esp32s3
```

---

## Build Firmware

```bash
idf.py build
```

---

## Build Result

Successful build generated:

```text
bootloader.bin
partition-table.bin
ota_data_initial.bin
esp32-csi-node.bin
```

Build output indicated:

```text
Project build complete.
```

Firmware size remained within partition limits.

---

# Flashing Firmware

## Node 1

```bash
idf.py -p /dev/ttyACM0 flash
```

---

## Node 2

```bash
idf.py -p /dev/ttyACM1 flash
```

---

# Initial Issues Encountered

## idf.py Command Not Found

### Error

```text
idf.py: command not found
```

### Cause

ESP-IDF environment variables were not loaded.

### Resolution

```bash
source ~/esp/esp-idf/export.sh
```

---

## ESP32 Port Detection

Serial ports appeared as:

```text
/dev/ttyACM0
/dev/ttyACM1
```

Used to identify connected boards.

---

# Node Provisioning

Provisioning was required to store:

- WiFi credentials
    
- Backend IP address
    
- Node ID
    
- Communication parameters
    

---

# NVS Partition Generator Issue

## Error

```text
NVS partition generator not available
```

Provisioning could not continue.

---

## Resolution

Installed required package:

```bash
pip3 install esp-idf-nvs-partition-gen --break-system-packages
```

After installation, provisioning completed successfully.

---

# Node 1 Provisioning

## Configuration

```bash
python3 provision.py \
  --port /dev/ttyACM0 \
  --ssid "redacted" \
  --password "redacted" \
  --target-ip 192.168.1.10 \
  --node-id 1
```

---

## Result

Provisioning completed successfully.

```text
NVS provisioning complete
```

---

# Node 2 Provisioning

## Configuration

```bash
python3 provision.py \
  --port /dev/ttyACM1 \
  --ssid "redacted" \
  --password "redacted" \
  --target-ip 192.168.1.10 \
  --node-id 2
```

---

## Result

Provisioning completed successfully.

```text
NVS provisioning complete
```

---

# MicroPython Discovery

While validating the second board, unexpected output appeared:

```text
MicroPython v1.19.1
```

The board contained a previously installed MicroPython firmware image.

Additional flashing was required to replace it with the RuView CSI firmware.

After reflashing, the board operated correctly.

---

# Firmware Validation

## Serial Monitoring

Monitoring performed using:

```bash
idf.py -p /dev/ttyACM0 monitor
```

and

```bash
idf.py -p /dev/ttyACM1 monitor
```

---

## Successful WiFi Connection

Firmware logs confirmed:

```text
Connected to WiFi
Got IP
```

---

## CSI Collection Enabled

Firmware logs reported:

```text
CSI streaming active
```

---

## UDP Streaming Enabled

Streaming destination:

```text
192.168.1.10:5005
```

---

# Multi-Node Operation

Two sensing nodes were deployed.

## Node IDs

```text
Node 1
Node 2
```

---

## Backend Target

```text
192.168.1.10:5005
```

---

## Purpose

Each node independently collects CSI measurements and streams them to the RuView backend.

Multiple nodes improve:

- Coverage
    
- Signal diversity
    
- Occupancy estimation
    
- Presence detection reliability
    

---

# ESP-NOW Synchronization

The firmware supports ESP-NOW synchronization between nodes.

Observed firmware logs included:

```text
c6_espnow
leader=1
```

indicating synchronization activity.

---

# Verification Steps

The following checks confirmed successful deployment:

## Firmware Validation

- Firmware compiled successfully
    
- Firmware flashed successfully
    
- Boot process completed successfully
    

## Connectivity Validation

- WiFi association successful
    
- IP address assigned
    
- Backend reachable
    

## CSI Validation

- CSI callbacks observed
    
- CSI packet generation observed
    
- CSI packet transmission observed
    

## Multi-Node Validation

- Two nodes active simultaneously
    
- Independent CSI streams observed
    
- Shared backend communication verified
    

---

# Lessons Learned

Key technical lessons from firmware deployment:

- Proper ESP-IDF environment configuration is critical.
    
- Provisioning requires NVS generation support.
    
- Existing board firmware should be verified before deployment.
    
- Multi-node systems require consistent configuration.
    
- Network configuration significantly impacts sensing reliability.
    

---

# Firmware Deployment Status

Status: Operational

Nodes Flashed: 2

Nodes Provisioned: 2

WiFi Connectivity: Operational

CSI Collection: Operational

ESP-NOW Synchronization: Operational

UDP Streaming: Operational

Backend Communication: Operational

Deployment Result: Successful