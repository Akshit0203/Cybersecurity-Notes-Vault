# RuView Backend Deployment and Multi-Node CSI Processing

## Overview

This document describes the deployment, troubleshooting, compilation, and validation of the RuView sensing backend used to process WiFi Channel State Information (CSI) streams from multiple ESP32-S3 sensing nodes.

The backend serves as the central processing component of the sensing platform and is responsible for:

- Receiving CSI packets
    
- Processing wireless sensing data
    
- Managing multi-node streams
    
- Running occupancy detection algorithms
    
- Generating real-time telemetry
    
- Providing dashboard updates
    
- Supporting WebSocket communication
    

The backend was deployed on a Kali Linux virtual machine using the Rust programming language and Cargo build system.

---

# Backend Architecture

## Responsibilities

The sensing server performs the following functions:

### CSI Ingestion

Receives CSI packets transmitted from ESP32-S3 sensing nodes.

### Signal Processing

Processes incoming CSI frames for:

- Motion detection
    
- Presence detection
    
- Occupancy estimation
    
- Vital sign analysis
    

### Data Distribution

Publishes processed information through:

- WebSocket streams
    
- Dashboard interfaces
    
- Observatory modules
    

---

# Software Stack

## Operating System

```text
Kali Linux
```

## Language

```text
Rust
```

## Build System

```text
Cargo
```

## Frameworks

- Axum
    
- Tokio
    
- WebSocket Services
    
- UDP Networking
    

---

# Rust Environment Verification

Before compilation, Rust was verified.

## Rust Compiler

```bash
rustc --version
```

Output:

```text
rustc 1.96.0
```

---

## Cargo

```bash
cargo --version
```

Output:

```text
cargo 1.96.0
```

---

# Sensing Server Location

Backend source code:

```text
RuView/v2/crates/wifi-densepose-sensing-server
```

---

# Initial Compilation Attempt

Compilation began using:

```bash
cargo build --release
```

---

# Dependency Issues Encountered

Several workspace dependency failures occurred before successful compilation.

These represented the most time-consuming portion of the deployment.

---

# Issue 1 – Missing RuField Dependency

## Error

```text
failed to load manifest for dependency rufield-core
```

Cargo could not locate:

```text
vendor/rufield/crates/rufield-core
```

---

## Investigation

Submodule directory existed but contained only:

```text
.git
```

No source files were present.

---

## Resolution

Navigate:

```bash
cd ~/RuView/vendor/rufield
```

Reset repository:

```bash
git reset --hard HEAD
```

---

## Result

RuField source restored successfully.

Verification:

```bash
ls
```

Output:

```text
Cargo.toml
crates
README.md
```

---

# Issue 2 – Missing RuView Swarm Dependency

## Error

```text
failed to read ruview-swarm/Cargo.toml
```

---

## Investigation

Repository contained staged deletions.

Workspace could not locate:

```text
Cargo.toml
```

---

## Resolution

Navigate:

```bash
cd ~/RuView/v2/crates/ruview-swarm
```

Restore repository:

```bash
git reset --hard HEAD
```

---

## Result

Project files restored successfully.

Verification:

```bash
ls
```

Output:

```text
Cargo.toml
src
README.md
```

---

# Issue 3 – WorldGraph Dependency Resolution

## Error

```text
failed to load wifi-densepose-geo
```

---

## Investigation

Dependency paths referenced:

```text
worldgraph/wifi-densepose-geo
```

Verification performed using:

```bash
find . -name Cargo.toml
```

Confirmed required projects existed:

```text
wifi-densepose-geo
wifi-densepose-worldgraph
wifi-densepose-worldmodel
```

---

## Result

Dependency resolution completed successfully.

---

# Successful Compilation

After resolving workspace issues:

```bash
cargo build --release
```

completed successfully.

Compilation included:

- WiFi DensePose Engine
    
- WiFi DensePose Hardware
    
- WiFi DensePose Signal Processing
    
- WiFi DensePose Geo
    
- WiFi DensePose RuField
    
- Sensing Server
    

---

# Final Build Status

```text
Finished release profile [optimized]
```

Build duration:

```text
Approximately 4 minutes
```

---

# Launching the Backend

Server started using:

```bash
cargo run -p wifi-densepose-sensing-server --release
```

---

# Server Initialization

Successful startup produced:

```text
WiFi-DensePose Sensing Server
```

---

## Services Started

### HTTP Server

```text
http://localhost:8080
```

---

### WebSocket Server

```text
ws://localhost:8765/ws/sensing
```

---

### UDP CSI Receiver

```text
0.0.0.0:5005
```

---

# Automatic Source Detection

The backend supports multiple CSI sources.

At startup:

```text
Source: auto
```

---

# Initial State

Before nodes were active:

```text
Data source: simulated
```

The backend automatically generated demonstration data.

---

# Transition to Live Data

Once ESP32 nodes connected:

```text
ESP32 CSI detected on UDP :5005
```

---

## Active Source

```text
Data source: esp32
```

This confirmed successful transition from simulation mode to live sensing mode.

---

# UDP Validation

Port verification:

```bash
sudo ss -ulpn | grep 5005
```

Output:

```text
0.0.0.0:5005
```

---

# CSI Traffic Validation

Network inspection:

```bash
sudo tcpdump -nn -i any udp port 5005
```

---

## Observed Traffic

```text
192.168.1.8 -> 192.168.1.10:5005
192.168.1.9 -> 192.168.1.10:5005
```

---

## Result

Verified:

- Node 1 streaming
    
- Node 2 streaming
    
- Backend receiving packets
    
- UDP transport functioning
    

---

# Multi-Node Processing

The backend simultaneously processed CSI streams from:

## Node 1

```text
192.168.1.8
```

## Node 2

```text
192.168.1.9
```

Both nodes transmitted to:

```text
192.168.1.10:5005
```

---

# WebSocket Communication

Dashboard connections established through:

```text
ws://localhost:8765/ws/sensing
```

Observed logs:

```text
WebSocket client connected
```

This verified frontend-backend communication.

---

# Backend Features Verified

## CSI Ingestion

Operational

## UDP Receiver

Operational

## Multi-Node Processing

Operational

## WebSocket Streaming

Operational

## Dashboard Integration

Operational

## Presence Detection Pipeline

Operational

## Motion Detection Pipeline

Operational

## Occupancy Estimation Pipeline

Operational

---

# Lessons Learned

Major lessons from backend deployment:

- Large Rust workspaces often fail due to incomplete submodules.
    
- Git submodule validation should occur before compilation.
    
- UDP packet inspection is invaluable for troubleshooting.
    
- Automatic source switching simplifies deployment.
    
- Multi-node CSI systems require both network and application-layer validation.
    

---

# Backend Deployment Status

Status: Operational

Compilation: Successful

HTTP Server: Operational

WebSocket Server: Operational

UDP Receiver: Operational

ESP32 CSI Detection: Operational

Multi-Node Processing: Operational

Dashboard Integration: Operational

Project Outcome: Successful Deployment of RuView Backend Infrastructure
