# Multi-Node WiFi CSI Human Sensing Platform using ESP32-S3 and RuView

> Real-time human presence detection, motion sensing, occupancy estimation, and RF-based environment awareness using WiFi Channel State Information (CSI).

---

## Project Overview

This project demonstrates a multi-node WiFi sensing system built using ESP32-S3 development boards and the RuView WiFi DensePose ecosystem.

The platform captures WiFi Channel State Information (CSI) from multiple sensing nodes and processes it through a Rust-based backend to estimate:

- Human Presence Detection
- Motion Detection
- Occupancy Estimation
- CSI Heatmaps
- Pose Visualization
- Vital Sign Visualization
- Multi-Node RF Sensing

Unlike camera-based systems, the platform uses wireless signal variations to understand environmental activity while preserving privacy.

---

## Project Highlights

✅ Multi-Node ESP32-S3 Deployment

✅ Real-Time CSI Collection

✅ UDP-Based CSI Streaming

✅ Rust Backend Processing

✅ Web Dashboard Visualization

✅ Occupancy Estimation

✅ Presence Detection

✅ Motion Detection

✅ CSI Heatmap Visualization

✅ Real-Time WebSocket Telemetry

---

## System Architecture

```
ESP32-S3 Node 1
        \
         \
          ---> RuView Backend ---> Dashboard
         /
        /
ESP32-S3 Node 2
```

The sensing nodes continuously collect WiFi CSI measurements and stream them to the RuView backend for processing and visualization.

---

## Hardware Used

### Sensing Nodes

- 2 × ESP32-S3-WROOM-1-N16R8
- 16 MB Flash
- 8 MB PSRAM

### Host System

- Windows 11
- VMware Workstation
- Kali Linux

### Wireless Network

- 2.4 GHz WiFi
- Channel 6

---

## Hardware Setup

### Connected ESP32-S3 Nodes



### ESP32-S3 Hardware

---

## Dashboard Demonstration

### Dashboard Overview

### System Metrics

### CSI Heatmap

---

## Human Sensing Results

### Multi-Person Detection

### Pose Estimation

### Vital Sign Monitoring

---

## Technical Stack

### Embedded Systems

- ESP32-S3
- ESP-IDF
- WiFi CSI APIs
- ESP-NOW

### Backend

- Rust
- Cargo
- Axum
- Tokio
- WebSockets

### Networking

- UDP Streaming
- WiFi CSI
- TCP/IP
- Real-Time Telemetry

### Monitoring & Analysis

- tcpdump
- ss
- Serial Console Monitoring

---

## Performance Summary

|Capability|Status|
|---|---|
|CSI Collection|✅|
|UDP Streaming|✅|
|Multi-Node Operation|✅|
|Dashboard Integration|✅|
|Motion Detection|✅|
|Presence Detection|✅|
|Occupancy Estimation|✅|
|Pose Visualization|✅|
|Vital Sign Visualization|✅|

---

## Key Findings

### Strengths

- Reliable presence detection
- Responsive motion detection
- Stable backend performance
- Successful multi-node deployment
- Real-time visualization

### Current Limitations

- Person counting occasionally fluctuates
- Environmental calibration can improve results
- Limited evaluation with only two sensing nodes

---

## Project Structure

```
.
├── README.md
├── docs
│   ├── 01_Project_Overview.md
│   ├── 02_Hardware_Setup.md
│   ├── 03_ESP32_Firmware.md
│   ├── 04_RuView_Backend.md
│   ├── 05_Dashboard.md
│   ├── 06_Troubleshooting.md
│   ├── 07_Performance_Evaluation.md
│   ├── 08_Future_Work.md
│   ├── 09_Results_and_Lessons_Learned.md
│   └── 10_References.md
├── images
├── firmware
└── backend
```

---

## Future Roadmap

### Short Term

- Deploy 4 sensing nodes
- Improve occupancy estimation
- Optimize node placement

### Medium Term

- Activity recognition
- Gesture recognition
- Room localization

### Long Term

- Smart building integration
- Healthcare monitoring
- Digital twin environments
- Large-scale distributed sensing networks

---

## Documentation

Detailed documentation is available in the `docs/` directory:

|Document|Description|
|---|---|
|01_Project_Overview|Project introduction|
|02_Hardware_Setup|Hardware deployment|
|03_ESP32_Firmware|Firmware build and flashing|
|04_RuView_Backend|Backend deployment|
|05_Dashboard|Visualization and observatory|
|06_Troubleshooting|Debugging log|
|07_Performance_Evaluation|Performance analysis|
|08_Future_Work|Research roadmap|
|09_Results_and_Lessons_Learned|Final conclusions|
|10_References|References and resources|

---

## Project Status

```
Status: Completed
Deployment: Successful
Nodes: 2 ESP32-S3
Backend: Operational
Dashboard: Operational
Research Potential: High
```