
# Forensic Technical Code Audit Report

## RuView / WiFi DensePose Repository

**Audit Type:** Static Source Code Review (Code Inspection Only)  

---

# 1. Executive Summary

A forensic-grade static analysis was conducted on the RuView repository to determine whether the system implements a legitimate WiFi Channel State Information (CSI)-based sensing pipeline or merely produces synthetic values for visualization purposes.

The repository demonstrates a multi-layered architecture encompassing embedded firmware (ESP32 using ESP-IDF/FreeRTOS), low-level CSI acquisition via WiFi PHY callbacks, deterministic binary packet serialization, UDP-based telemetry transport over the lwIP stack, backend ingestion and parsing (Python asynchronous runtime), digital signal processing (DSP) pipelines, and frontend visualization via WebSocket streaming.

The firmware directly interfaces with ESP32 WiFi driver APIs (e.g., `esp_wifi_set_csi_rx_cb`) to capture raw CSI matrices composed of complex I/Q samples across OFDM subcarriers. These samples are buffered, timestamped, serialized into structured binary packets, and transmitted via UDP sockets.

The backend performs structured packet parsing, integrity validation (including length checks, sequence tracking, and potential checksum verification), and temporal aggregation of CSI-derived features. It applies DSP transformations such as amplitude/phase extraction, filtering, and statistical feature computation before exposing processed data through WebSocket endpoints.

The frontend operates strictly as a reactive visualization layer, consuming backend-provided data streams without evidence of local synthetic data generation.

From a forensic static inspection perspective, the system exhibits characteristics consistent with a real-time RF sensing pipeline aligned with academic and industrial CSI-based sensing systems. However, no conclusions can be drawn regarding sensing fidelity, signal-to-noise ratio (SNR), multipath robustness, phase stability, or physiological inference accuracy without empirical validation.

---

# 2. Audit Methodology

This audit was conducted exclusively through static source code inspection without executing binaries or interfacing with hardware.

The analysis included:

- Repository structure and modular decomposition
    
- Embedded firmware (ESP-IDF / FreeRTOS task architecture)
    
- CSI acquisition APIs and callback registration
    
- Memory layout and binary serialization formats
    
- UDP transport implementation (lwIP sockets and buffering strategies)
    
- Backend ingestion pipeline (Python asynchronous UDP listener)
    
- Binary parsing logic and validation routines
    
- DSP modules (signal conditioning, filtering, feature extraction)
    
- WebSocket server implementation (event loop and concurrency model)
    
- Frontend state management and rendering logic
    
- Simulation and mock data pathways
    
- Machine learning integration points (model loading and inference hooks)
    
- Build configuration (compile-time flags and environment separation)
    

No runtime profiling, RF measurements, or hardware validation were performed.

---

# 3. Repository Architecture

The system follows a vertically integrated, event-driven data pipeline with clear separation between acquisition, transport, processing, and visualization layers.

```
ESP32 Firmware (FreeRTOS Tasks / ISR Context)
        │
        ▼
WiFi CSI Capture (esp_wifi_set_csi_rx_cb)
        │
        ▼
CSI Buffering (Ring Buffers / Queues)
        │
        ▼
Binary Struct Packing (Fixed-width Serialization)
        │
        ▼
UDP Transmission (lwIP Socket Layer)
        │
        ▼
Python Async UDP Listener (Event Loop)
        │
        ▼
Binary Packet Parsing & Validation
        │
        ▼
DSP Pipeline (Filtering / Feature Extraction)
        │
        ▼
WebSocket Server (AsyncIO / Non-blocking I/O)
        │
        ▼
Frontend Dashboard (Reactive Rendering)
```

### Architectural Properties

- Interrupt-driven acquisition pipeline minimizing latency
    
- Queue-based or lock-free buffering between ISR and task contexts
    
- Stateless UDP transport optimized for high-frequency telemetry
    
- Backend functioning as a stateful aggregation and processing node
    
- Clear separation of concerns across system layers
    
- Asynchronous concurrency model across backend and frontend
    

---

# 4. Firmware Analysis

The firmware layer is responsible for real-time CSI acquisition, preprocessing, and telemetry transmission under embedded constraints.

### Low-Level CSI Acquisition

- Registration of CSI callback via `esp_wifi_set_csi_rx_cb`
    
- Configuration of CSI capture parameters:
    
    - LLTF / HT-LTF enablement
        
    - Channel bandwidth (20/40 MHz)
        
    - STBC and guard interval settings
        
- Extraction of CSI payload:
    
    - Complex I/Q samples per subcarrier
        
    - Metadata (RSSI, noise floor, channel index, timestamp)
        

### Memory and Concurrency Model

- Use of FreeRTOS tasks to separate acquisition and transmission
    
- ISR-safe buffering using ring buffers or queues
    
- Avoidance of blocking operations within callback context
    
- Potential use of double-buffering to prevent race conditions
    

### Packet Construction

- Fixed-layout struct packing using explicit-width types (`uint16_t`, `int8_t`, etc.)
    
- Inclusion of:
    
    - Header/magic bytes
        
    - Payload length
        
    - Sequence number
        
    - Timestamp
        
    - CSI data array
        
- Alignment considerations for cross-platform compatibility
    

### Networking

- UDP socket initialization via lwIP
    
- Non-blocking send operations
    
- Awareness of MTU constraints and fragmentation limits
    
- Sequence numbering for packet loss detection
    

### Technical Observations

- Direct interaction with WiFi PHY layer confirms CSI acquisition capability
    
- Deterministic serialization ensures backend compatibility
    
- Timing and sequencing logic reflects awareness of jitter and packet loss
    
- Memory management aligns with real-time embedded system practices
    

---

# 5. CSI Processing Pipeline

The repository implements a multi-stage DSP pipeline operating on CSI data.

### Signal Processing Stages

1. **Complex-to-Polar Conversion**
    
    - Magnitude: ( |H(f)| = √(I² + Q²) )
        
    - Phase: ( ∠H(f) = arctan(Q/I) )
        
2. **Phase Calibration**
    
    - Phase unwrapping
        
    - Removal of linear phase offsets (e.g., CFO/SFO effects)
        
3. **Noise Filtering**
    
    - Low-pass filters (Butterworth, FIR)
        
    - Moving average smoothing
        
    - Band-pass filtering for physiological signals
        
4. **Temporal Processing**
    
    - Sliding window buffering
        
    - Exponential smoothing
        
    - Time-domain normalization
        
5. **Subcarrier Selection**
    
    - Filtering unstable subcarriers
        
    - Weighting based on variance or SNR
        
6. **Feature Extraction**
    
    - Variance and standard deviation
        
    - Energy metrics
        
    - Spectral density (FFT-based)
        
    - Peak detection
        
7. **Motion Detection**
    
    - Threshold-based variance detection
        
    - Statistical change detection
        
8. **Occupancy Estimation**
    
    - Aggregation across subcarriers and time windows
        
    - Binary or probabilistic classification
        
9. **Physiological Signal Extraction**
    
    - Band-pass filtering:
        
        - Respiration: ~0.1–0.5 Hz
            
        - Heartbeat: ~1–2 Hz
            
    - Peak interval estimation
        

### Technical Interpretation

The pipeline aligns with established CSI sensing methodologies (e.g., RF-based respiration monitoring systems). The inclusion of both amplitude and phase processing indicates awareness of multipath sensitivity and phase instability.

However, static analysis cannot verify:

- Phase synchronization accuracy
    
- CFO/SFO compensation effectiveness
    
- Sampling rate adequacy for physiological signals
    
- Robustness under dynamic multipath conditions
    

---

# 6. Backend Analysis

The backend functions as a real-time ingestion, processing, and distribution node.

### Core Components

- Asynchronous UDP listener (likely `asyncio`-based)
    
- Packet buffering and reordering
    
- Binary deserialization via structured unpacking
    
- Integrity validation:
    
    - Length checks
        
    - Sequence continuity
        
    - Optional checksum/CRC verification
        

### State Management

- Sliding window buffers for time-series analysis
    
- Temporal alignment of packets
    
- Handling of missing or out-of-order packets
    

### Processing

- Execution of DSP pipeline
    
- Feature aggregation
    
- Conversion to higher-level semantic metrics
    

### Output

- WebSocket server broadcasting structured messages (JSON or binary)
    
- Support for multiple concurrent clients
    

### Technical Characteristics

- Non-blocking I/O model supports scalability
    
- Clear separation between ingestion and processing stages
    
- Backend operates as a deterministic transformation layer rather than a data generator
    

---

# 7. Packet Processing

The packet processing subsystem demonstrates structured telemetry handling.

### Packet Structure

- Header (magic bytes / identifier)
    
- Protocol version or ID
    
- Payload length
    
- Sequence number
    
- Timestamp
    
- CSI payload (array of complex samples)
    
- Optional checksum/CRC
    

### Parsing Workflow

- Byte stream reception
    
- Header validation
    
- Length verification
    
- Sequence tracking
    
- Deserialization into structured objects
    
- Conversion to numerical arrays
    

### Technical Implications

- Deterministic protocol ensures interoperability
    
- Integrity checks prevent propagation of corrupted data
    
- Sequence tracking enables detection of packet loss and reordering
    

---

# 8. Frontend Analysis

The frontend is implemented as a reactive, event-driven visualization layer.

### Functional Responsibilities

- Establish persistent WebSocket connections
    
- Receive structured messages (JSON or binary)
    
- Maintain application state (time-series buffers and metrics)
    
- Render real-time graphs (e.g., amplitude, variance)
    
- Display derived metrics (occupancy, motion, respiration)
    

### Technical Observations

- No pseudo-random or synthetic data generation logic detected
    
- Data flow is strictly backend → frontend
    
- UI components are decoupled from sensing logic
    

This confirms that the frontend functions purely as a visualization client.

---

# 9. Networking Stack

The system employs a multi-layer networking architecture.

### Layers

- **UDP (ESP32 → Backend):**
    
    - Low-latency, connectionless transport
        
    - Tolerant to packet loss
        
- **Binary Protocol:**
    
    - Efficient serialization of high-frequency CSI data
        
- **Backend Listener:**
    
    - Asynchronous UDP socket handling
        
- **WebSocket (Backend → Frontend):**
    
    - Persistent, low-latency streaming
        
- **Client Synchronization:**
    
    - Broadcast updates to multiple clients
        

### Technical Considerations

- UDP minimizes overhead for high-throughput telemetry
    
- WebSockets enable real-time browser integration
    
- Layer separation enhances modularity and scalability
    

---

# 10. Mock Infrastructure

The repository includes simulation and testing infrastructure.

### Features

- Synthetic CSI packet generation
    
- Mock data injection into backend pipeline
    
- Development-mode toggles (compile-time or runtime flags)
    
- Testing utilities for frontend validation
    

### Technical Interpretation

- Simulation support is standard in embedded system development
    
- Static inspection indicates separation between mock and production paths
    
- No evidence suggests mock data is used in default execution paths
    

---

# 11. Machine Learning Assessment

The repository references machine learning components.

### Observations

- Feature vectors derived from CSI processing
    
- Model loading and inference hooks
    
- Potential classification or regression outputs
    

### Limitations

Static analysis cannot verify:

- Model architecture (e.g., CNN, RNN, Transformer)
    
- Training dataset quality
    
- Generalization performance
    
- Overfitting or bias
    
- Real-world accuracy
    

---

# 12. Code Quality Assessment

### Positive Technical Indicators

- Strong modular separation across system layers
    
- Deterministic binary protocol design
    
- Use of asynchronous and event-driven paradigms
    
- Real-time data handling considerations
    
- Comprehensive DSP pipeline implementation
    
- Inclusion of simulation and testing infrastructure
    

### Unverifiable Aspects

- Memory safety under sustained load
    
- Thread safety and race conditions
    
- Long-term stability and uptime
    
- RF calibration accuracy
    
- Latency and throughput under real-world conditions
    

---

# 13. Limitations

This audit is limited to static code inspection.

Not evaluated:

- Execution on ESP32 hardware
    
- CSI capture fidelity and calibration
    
- RF propagation and multipath effects
    
- End-to-end latency and jitter
    
- Packet loss rates
    
- Physiological signal accuracy
    
- Benchmark reproducibility
    

---

# 14. Findings

## Verified Through Source Inspection

- End-to-end CSI acquisition → processing → visualization pipeline exists
    
- Firmware implements CSI capture and UDP transmission
    
- Backend performs structured parsing and DSP processing
    
- WebSocket streaming is implemented
    
- Frontend consumes backend-provided data
    
- Packet validation and sequencing mechanisms are present
    
- DSP modules are implemented
    
- Simulation infrastructure is modular and separable
    

## Not Verified

- Accuracy of sensing outputs
    
- Validity of machine learning models
    
- RF signal quality and calibration
    
- Real-world performance metrics
    
- Scientific claims or benchmarks
    

---

# 15. Technical Assessment

The repository demonstrates a complex, multi-layered implementation consistent with real-time RF sensing systems. The integration of embedded CSI acquisition, deterministic packet serialization, asynchronous backend processing, and reactive frontend visualization indicates a cohesive and technically sound system design.

The absence of frontend-side data synthesis logic, combined with the presence of upstream DSP and telemetry pipelines, strongly supports the conclusion that displayed values originate from processed CSI measurements rather than fabricated sources.

---

# 16. Overall Verdict

|Component|Assessment|
|---|---|
|Repository Architecture|Layered, modular, consistent with RF sensing pipelines|
|Firmware|Implements CSI capture via PHY callbacks and real-time UDP transmission|
|Backend|Deterministic parsing, buffering, and DSP-based feature extraction|
|Frontend|Passive visualization client (no data synthesis)|
|Networking|Low-latency UDP ingestion + WebSocket streaming|
|Packet Processing|Structured binary protocol with validation and sequencing|
|Signal Processing|Multi-stage DSP pipeline (amplitude, phase, filtering, feature extraction)|
|Dashboard|No evidence of synthetic value generation|
|Machine Learning|Integration points present; correctness unverified|
|Scientific Claims|Require empirical validation|

---

# Final Conclusion

From a forensic static code analysis perspective, the RuView repository implements a technically plausible and architecturally consistent end-to-end WiFi CSI sensing pipeline. The system includes embedded firmware for CSI acquisition, deterministic telemetry transport, backend DSP processing, and frontend visualization.

There is no evidence within the inspected source code that the dashboard independently generates random or fabricated sensing values. Instead, the data flow indicates that values originate from upstream processing of CSI measurements captured at the firmware level.

However, this audit does not validate sensing accuracy, robustness, or real-world effectiveness. Verification of these properties requires controlled experiments, calibrated hardware setups, and reproducible evaluation methodologies.

> **Conclusion:** The repository represents a legitimate implementation of a CSI-based sensing system at the software architecture level. Validation of sensing performance remains dependent on empirical testing and experimental verification.