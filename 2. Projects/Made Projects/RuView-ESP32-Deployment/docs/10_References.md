# References

## Overview

This project builds upon WiFi Channel State Information (CSI) sensing research, ESP32 wireless hardware capabilities, and the RuView WiFi DensePose ecosystem.

The following references were used throughout the deployment, configuration, troubleshooting, and validation phases of the project.

---

# Research Papers

## WiFi CSI Sensing

### WiFi-Based Human Activity Recognition Using CSI

Provides foundational concepts for extracting human activity information from WiFi Channel State Information.

Topics:

- CSI amplitude analysis
- CSI phase analysis
- Activity recognition
- Human sensing

---

## Device-Free Human Sensing Using WiFi Signals

Introduces the concept of detecting and monitoring human activity without requiring wearable devices.

Topics:

- Device-free sensing
- Occupancy detection
- Presence detection
- Wireless environment monitoring

---

## RF-Based Human Pose Estimation

Research into estimating human body posture and movement using wireless signal measurements.

Topics:

- Pose estimation
- RF sensing
- Human tracking
- Privacy-preserving sensing

---

## WiFi DensePose Research

DensePose-inspired wireless sensing approaches that use CSI measurements to infer human spatial information.

Topics:

- Wireless pose estimation
- Occupancy analytics
- Multi-node sensing

---

# Official Documentation

## ESP32-S3 Documentation

Vendor:

```
Espressif Systems
```

Documentation Used:

- ESP32-S3 Technical Reference Manual
- ESP-IDF Programming Guide
- WiFi CSI API Documentation
- ESP-NOW Documentation

Purpose:

- Firmware development
- CSI collection
- Device provisioning
- Network configuration

---

## ESP-IDF Documentation

Framework:

```
ESP-IDF v5.4
```

Topics Referenced:

- Project configuration
- Build system
- Flashing firmware
- Monitoring serial output
- WiFi development

---

# RuView Project

## RuView

Primary sensing platform used throughout the project.

Components Used:

- WiFi DensePose Sensing Server
- CSI Processing Pipeline
- Dashboard Interface
- Observatory Interface
- Multi-Node CSI Support

Purpose:

- CSI processing
- Visualization
- Occupancy estimation
- Motion detection

---

## RuField

Used by the sensing backend for wireless sensing data processing and fusion.

Topics:

- Data fusion
- Sensing abstraction
- Event handling

---

## WorldGraph

Used within the RuView ecosystem for spatial reasoning and environmental modeling.

Topics:

- Spatial representation
- Environment modeling
- Sensing integration

---

# Software Tools

## Rust

Version:

```
Rust 1.96
```

Purpose:

- Backend compilation
- Sensing server deployment

---

## Cargo

Purpose:

- Dependency management
- Project compilation
- Workspace management

---

## Git

Purpose:

- Source control
- Repository management
- Submodule synchronization

---

# Network Analysis Tools

## tcpdump

Purpose:

- UDP packet inspection
- CSI traffic verification
- Network debugging

Example Usage:

```
sudo tcpdump -nn -i any udp port 5005
```

---

## ss

Purpose:

- Socket inspection
- Port validation

Example Usage:

```
sudo ss -ulpn | grep 5005
```

---

# Development Environment

## Kali Linux

Purpose:

- Firmware deployment
- Backend deployment
- Network diagnostics
- System integration

---

## VMware Workstation

Purpose:

- Virtualized development environment
- Backend hosting

---

# Hardware References

## ESP32-S3-WROOM-1-N16R8

Specifications:

- 16 MB Flash
- 8 MB PSRAM
- Integrated WiFi
- Integrated Bluetooth

Used As:

- CSI sensing node
- Wireless telemetry device

---

# Communication Technologies

## WiFi CSI

Used For:

- Presence detection
- Motion detection
- Occupancy estimation
- Signal analysis

---

## UDP

Used For:

- Real-time CSI transport
- Backend communication

Port:

```
5005
```

---

## WebSocket

Used For:

- Dashboard communication
- Real-time updates

Port:

```
8765
```

---

# Concepts and Topics Studied

The following technical concepts were explored during the project:

## Wireless Sensing

- CSI collection
- RF sensing
- Signal propagation
- Multipath analysis

---

## Embedded Systems

- Firmware flashing
- Device provisioning
- Serial monitoring
- ESP-IDF development

---

## Distributed Systems

- Multi-node sensing
- Real-time data streaming
- Backend processing

---

## Human-Centric Sensing

- Presence detection
- Occupancy estimation
- Motion recognition
- Pose estimation

---

## Privacy-Preserving Monitoring

- Camera-free sensing
- Device-free sensing
- Non-intrusive monitoring

---

# Additional Learning Resources

Recommended topics for further study:

- WiFi CSI Signal Processing
- RF-Based Activity Recognition
- Wireless Localization
- Device-Free Human Sensing
- ESP32 Advanced Networking
- Indoor Positioning Systems
- Digital Twin Architectures
- Sensor Fusion Systems
- Edge AI for Wireless Sensing

---

# Reference Summary

Primary Hardware:

```
ESP32-S3
```

Primary Framework:

```
ESP-IDF
```

Primary Platform:

```
RuView WiFi DensePose
```

Primary Language:

```
Rust
```

Primary Communication Method:

```
WiFi CSI over UDP
```

Primary Research Area:

```
Device-Free Wireless Human Sensing
```