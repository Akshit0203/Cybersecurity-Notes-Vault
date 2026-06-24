# Multi-Node WiFi CSI Sensing Platform for Real-Time Human Presence, Occupancy, and Motion Detection using ESP32-S3 and RuView

## Project Overview

This project demonstrates the deployment and validation of a multi-node WiFi sensing platform capable of detecting human presence, occupancy, and motion using WiFi Channel State Information (CSI).

The system utilizes multiple ESP32-S3 sensing nodes running CSI collection firmware and the RuView sensing framework to capture variations in wireless signal propagation caused by human movement within an indoor environment. CSI data is streamed to a centralized sensing server where it is processed, analyzed, and visualized through a real-time web dashboard.

Unlike traditional occupancy sensing systems that rely on cameras or wearable devices, WiFi CSI sensing leverages existing wireless infrastructure to infer environmental changes while preserving privacy.

---

# Motivation

Modern smart buildings, security systems, and occupancy monitoring platforms commonly depend on:

- CCTV cameras
    
- Passive Infrared (PIR) sensors
    
- Radar sensors
    
- Wearable tracking devices
    

While effective, these approaches introduce challenges such as:

- Privacy concerns
    
- Additional hardware costs
    
- Line-of-sight limitations
    
- Deployment complexity
    
- Limited sensing coverage
    

WiFi CSI sensing provides an alternative approach by using changes in wireless signal characteristics to detect human presence and movement without requiring cameras or user participation.

This project was undertaken to explore the practical deployment of a distributed WiFi CSI sensing system using low-cost ESP32-S3 hardware and open-source sensing software.

---

# Project Objectives

## Primary Objectives

- Deploy multiple ESP32-S3 CSI sensing nodes
    
- Capture real-time WiFi Channel State Information
    
- Stream CSI data to a centralized sensing backend
    
- Enable human presence detection
    
- Enable occupancy estimation
    
- Enable motion detection
    
- Validate multi-node sensing operation
    

## Secondary Objectives

- Gain practical experience with WiFi CSI sensing
    
- Understand distributed sensing architectures
    
- Explore real-time signal processing workflows
    
- Study occupancy detection techniques
    
- Evaluate sensing accuracy in real-world environments
    

---

# Hardware Configuration

## Sensing Nodes

### Node 1

- ESP32-S3-WROOM-1-N16R8
    
- 16 MB Flash
    
- 8 MB PSRAM
    
- WiFi CSI Collection Enabled
    

### Node 2

- ESP32-S3-WROOM-1-N16R8
    
- 16 MB Flash
    
- 8 MB PSRAM
    
- WiFi CSI Collection Enabled
    

## Access Point

- Airtel Broadband Router
    
- 2.4 GHz Network
    
- WPA2-Personal Security
    
- Operating Channel: 6
    

## Processing Environment

### Host System

- Windows 11
    

### Virtualization Platform

- VMware Workstation
    

### Guest Operating System

- Kali Linux
    

### Network Mode

- Bridged Adapter
    

---

# Software Stack

## Embedded Layer

- ESP-IDF v5.4
    
- ESP32 CSI Node Firmware
    
- ESP-NOW Synchronization
    

## Backend Layer

- Rust
    
- Cargo
    
- WiFi-DensePose Sensing Server
    
- UDP CSI Ingestion Pipeline
    
- WebSocket Streaming Engine
    

## Frontend Layer

- RuView Dashboard
    
- RuView Observatory
    
- Real-Time Monitoring Interface
    

## Networking

- WiFi CSI Transport
    
- UDP Data Streaming
    
- WebSocket Communication
    

---

# System Architecture

```text
ESP32-S3 Node 1
          \
           \
            ---> RuView Sensing Server ---> Dashboard
           /
          /
ESP32-S3 Node 2
```

## Data Flow

1. ESP32-S3 nodes capture CSI measurements.
    
2. CSI packets are streamed over WiFi.
    
3. UDP packets are transmitted to the sensing server.
    
4. The backend processes incoming CSI streams.
    
5. Features are extracted and analyzed.
    
6. Results are published via WebSockets.
    
7. The dashboard displays live sensing information.
    

---

# Deployment Process

The deployment consisted of the following stages:

## Stage 1 – Environment Setup

- ESP-IDF installation
    
- Toolchain configuration
    
- Rust installation
    
- Cargo configuration
    

## Stage 2 – Firmware Preparation

- RuView repository cloning
    
- Dependency initialization
    
- Firmware compilation
    
- ESP32-S3 target configuration
    

## Stage 3 – Device Provisioning

- Firmware flashing
    
- WiFi credential provisioning
    
- Target IP configuration
    
- Node ID assignment
    

## Stage 4 – Backend Deployment

- Rust workspace compilation
    
- Dependency resolution
    
- Sensing server deployment
    
- UDP listener validation
    

## Stage 5 – Validation

- CSI packet verification
    
- Network traffic inspection
    
- Dashboard testing
    
- Multi-node operation testing
    

---

# Technical Challenges Encountered

Several issues were encountered during deployment:

## ESP-IDF Environment Issues

Problems:

- `idf.py: command not found`
    

Resolution:

- ESP-IDF environment sourcing using:
    

```bash
source ~/esp/esp-idf/export.sh
```

---

## Missing NVS Partition Generator

Problems:

- Provisioning script unable to generate NVS partitions
    

Resolution:

```bash
pip3 install esp-idf-nvs-partition-gen --break-system-packages
```

---

## Broken Git Submodules

Problems:

- Missing Rust workspace dependencies
    
- Missing Cargo manifests
    

Resolution:

```bash
git submodule update --init --recursive
git reset --hard HEAD
```

Applied to:

- rufield
    
- ruview-swarm
    

---

## VMware Network Configuration

Problems:

- ESP32 nodes unable to reach backend
    

Resolution:

- Switched VMware networking to Bridged Mode
    

---

# System Validation

## Firmware Validation

Verified:

- Successful flashing
    
- Successful provisioning
    
- Successful WiFi association
    
- CSI capture enabled
    

## Network Validation

Verified:

- UDP packet transmission
    
- Node-to-server communication
    
- Multi-node packet reception
    

Example packet flow:

```text
192.168.1.8  -> 192.168.1.10:5005
192.168.1.9  -> 192.168.1.10:5005
```

## Backend Validation

Verified:

- UDP listener active
    
- CSI ingestion active
    
- WebSocket server active
    
- Dashboard connectivity active
    

## Dashboard Validation

Verified:

- Presence detection
    
- Occupancy estimation
    
- Motion detection
    
- RSSI monitoring
    
- Vital sign visualization
    
- Pose visualization
    

---

# Results

## Successfully Achieved

### Multi-Node Deployment

- Two ESP32-S3 sensing nodes deployed successfully
    

### CSI Collection

- Real-time CSI capture operational
    

### UDP Streaming

- Live CSI streaming operational
    

### Backend Processing

- Rust sensing backend operational
    

### Dashboard Operation

- Real-time dashboard operational
    

### Presence Detection

- Human presence successfully detected
    

### Motion Detection

- Motion events successfully detected
    

### Occupancy Estimation

- Person counting operational
    

### Vital Sign Monitoring

- Visualization operational
    

---

# Observations

During testing:

- Presence detection performed reliably.
    
- Motion detection responded consistently to movement.
    
- Occupancy estimation worked but occasionally produced minor inaccuracies.
    
- Additional sensing nodes are expected to improve spatial coverage and estimation accuracy.
    

These observations are consistent with the limitations and characteristics of CSI-based sensing systems.

---

# Skills and Technologies Demonstrated

## Embedded Systems

- ESP32-S3
    
- ESP-IDF
    
- Firmware Deployment
    

## Networking

- WiFi
    
- UDP
    
- WebSockets
    
- ESP-NOW
    

## Software Engineering

- Rust
    
- Cargo
    
- Linux
    
- Virtualization
    

## Wireless Security and Sensing

- WiFi Channel State Information (CSI)
    
- Device-Free Sensing
    
- Occupancy Detection
    
- Human Presence Detection
    

## Troubleshooting

- Dependency Resolution
    
- Network Debugging
    
- Embedded Device Debugging
    
- Build System Troubleshooting
    

---

# Future Improvements

Potential future enhancements include:

- Deployment of additional sensing nodes
    
- Multi-room sensing coverage
    
- CSI dataset collection
    
- Machine learning-based activity recognition
    
- Device-free localization
    
- Indoor tracking
    
- Enhanced occupancy estimation
    
- Sensor fusion techniques
    

---

# Project Status

**Status:** Completed and Operational

**Deployment Type:** Multi-Node WiFi CSI Sensing Platform

**Number of Nodes:** 2 ESP32-S3 Nodes

**CSI Streaming:** Operational

**Backend Processing:** Operational

**Dashboard:** Operational

**Presence Detection:** Operational

**Motion Detection:** Operational

**Occupancy Estimation:** Operational

**Project Outcome:** Successful End-to-End Deployment and Validation of a Distributed WiFi CSI Sensing System