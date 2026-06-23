# Future Work and Research Roadmap

## Overview

The current implementation successfully demonstrates a functional multi-node WiFi CSI sensing platform using ESP32-S3 hardware and the RuView sensing ecosystem.

Future development will focus on improving sensing accuracy, expanding deployment scale, enhancing machine learning capabilities, and exploring real-world applications.

This document outlines potential research directions and engineering improvements for future versions of the platform.

---

# Current System Baseline

## Current Deployment

### Sensing Nodes

```
2 × ESP32-S3 Nodes
```

### Communication

```
WiFi CSI + UDP Streaming
```

### Backend

```
RuView WiFi DensePose Sensing Server
```

### Features

- Presence Detection
- Motion Detection
- Occupancy Estimation
- CSI Visualization
- Heatmap Generation
- Pose Estimation
- Vital Sign Visualization

---

# Phase 1: Enhanced Multi-Node Deployment

## Objective

Increase sensing coverage and reduce occupancy estimation uncertainty.

---

## Four Node Deployment

### Goals

Deploy:

```
4 ESP32-S3 sensing nodes
```

within a single environment.

---

### Expected Benefits

- Improved spatial diversity
- Better CSI coverage
- Reduced blind spots
- Improved occupancy estimation

---

### Research Questions

- How much does accuracy improve between 2 and 4 nodes?
- What placement strategy yields the best results?
- How does CSI quality vary across node locations?

---

## Eight Node Deployment

### Goals

Deploy:

```
8 ESP32-S3 sensing nodes
```

throughout a larger area.

---

### Expected Benefits

- Higher sensing density
- Improved environmental awareness
- Better localization capability

---

### Potential Applications

- Smart classrooms
- Office spaces
- Research laboratories
- Smart homes

---

# Phase 2: Occupancy and Localization

## Current State

The system estimates occupancy but does not accurately localize individuals.

---

## Future Goal

Estimate:

- Person count
- Person position
- Movement paths

within the monitored environment.

---

## Potential Techniques

### CSI Tomography

Use CSI measurements from multiple nodes to reconstruct signal disturbance maps.

---

### Multi-Static Sensing

Combine observations from multiple sensing perspectives.

---

### Signal Triangulation

Estimate occupant location through CSI variations observed by multiple nodes.

---

## Expected Outcomes

- Room-level localization
- Zone-level occupancy maps
- Movement tracking

---

# Phase 3: Activity Recognition

## Objective

Move beyond presence detection.

---

## Activities to Detect

### Static Activities

- Standing
- Sitting
- Sleeping

---

### Dynamic Activities

- Walking
- Running
- Falling
- Gesturing

---

### Household Activities

- Cooking
- Studying
- Working
- Exercising

---

## Potential Approaches

### Machine Learning

- Random Forest
- XGBoost
- Support Vector Machines

---

### Deep Learning

- CNN
- LSTM
- Transformers

---

### CSI Feature Engineering

Utilize:

- Amplitude features
- Phase features
- Temporal patterns
- Spectral features

---

# Phase 4: Gesture Recognition

## Objective

Enable contactless gesture-based interaction.

---

## Example Gestures

- Hand wave
- Swipe left
- Swipe right
- Raise hand
- Pointing actions

---

## Potential Applications

### Smart Home Control

- Lighting control
- Appliance control
- Media control

---

### Accessibility Systems

- Touchless interfaces
- Assistive technologies

---

# Phase 5: Vital Sign Research

## Current Capability

The observatory provides vital sign visualization.

---

## Future Goal

Improve estimation accuracy for:

- Breathing rate
- Heart rate
- Respiration patterns

---

## Research Areas

### Signal Filtering

Develop improved filtering techniques for low-amplitude physiological signals.

---

### Noise Reduction

Reduce interference caused by:

- Environmental movement
- RF noise
- Multipath effects

---

### Continuous Monitoring

Enable long-term passive monitoring.

---

# Phase 6: Digital Twin Integration

## Objective

Create a real-time digital representation of the monitored environment.

---

## Future Vision

The sensing platform continuously updates a digital twin using CSI-derived information.

---

## Potential Features

### Occupancy Mapping

Display occupant locations.

---

### Motion Visualization

Show movement patterns in real time.

---

### Environment Monitoring

Track environmental activity over time.

---

## Integration Targets

- RuView
- WorldGraph
- Building Management Systems

---

# Phase 7: Sensor Fusion

## Objective

Combine CSI sensing with complementary technologies.

---

## BLE Integration

Potential use:

- Device presence detection
- Indoor localization

---

## UWB Integration

Potential use:

- High-precision ranging
- Localization

---

## mmWave Radar

Potential use:

- Motion tracking
- Fall detection
- Fine-grained activity recognition

---

## Environmental Sensors

Potential use:

- Temperature
- Humidity
- Air quality

---

# Phase 8: Smart Building Applications

## Occupancy Monitoring

Automatically determine:

- Room utilization
- Occupancy trends
- Capacity usage

---

## Energy Optimization

Use occupancy information to control:

- Lighting
- HVAC systems
- Building automation

---

## Meeting Room Analytics

Track room usage and utilization patterns.

---

# Phase 9: Healthcare Applications

## Elderly Care

Potential capabilities:

- Presence monitoring
- Fall detection
- Activity monitoring

---

## Patient Observation

Passive sensing without cameras or wearables.

---

## Sleep Monitoring

Analyze respiration and movement patterns.

---

# Phase 10: Security Applications

## Intrusion Detection

Detect unauthorized movement.

---

## Area Monitoring

Monitor restricted spaces.

---

## Smart Perimeter Systems

Use distributed sensing nodes for environment awareness.

---

# Academic Research Opportunities

Potential research topics include:

- CSI-based occupancy estimation
- Multi-node wireless sensing
- Privacy-preserving sensing
- CSI tomography
- RF-based pose estimation
- Wireless digital twins
- Activity recognition using WiFi signals

---

# Engineering Improvements

## Software

- Improved dashboard analytics
- Better calibration workflows
- Automated node discovery
- Enhanced visualization

---

## Hardware

- Custom sensing node PCB
- External antenna support
- Battery-powered deployments
- PoE-powered nodes

---

## Scalability

Future deployments:

|Phase|Nodes|
|---|---|
|Current|2|
|Phase 1|4|
|Phase 2|8|
|Phase 3|16+|

---

# Long-Term Vision

The long-term objective is to develop a scalable, privacy-preserving wireless sensing platform capable of understanding human presence, movement, activities, and environmental dynamics without relying on cameras or wearable devices.

By combining distributed CSI sensing, machine learning, and multi-node processing, the platform can evolve into a practical solution for smart buildings, healthcare environments, security systems, and next-generation human-environment interaction research.

---

# Future Work Status

Current Phase: Completed Two-Node Deployment

Next Target: Four-Node Deployment

Long-Term Goal: Large-Scale Distributed WiFi CSI Sensing Network

Research Potential: High

Scalability Potential: High
