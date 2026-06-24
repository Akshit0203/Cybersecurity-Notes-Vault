# Troubleshooting and Debugging Log

## Overview

This document records the major technical issues encountered during deployment of the RuView WiFi CSI sensing platform and the solutions used to resolve them.

The troubleshooting process covered:

- ESP-IDF configuration
- Firmware deployment
- ESP32 provisioning
- Rust workspace dependencies
- Git submodules
- UDP communication
- Backend services
- Dashboard connectivity

---

# Issue 1: NVS Partition Generator Missing

## Symptom

Provisioning failed with:

```
NVS partition generator not available
```

---

## Cause

Required Python package was not installed.

---

## Error Message

```
NVS partition generator not available.Install: pip install esp-idf-nvs-partition-gen
```

---

## Resolution

Installed package:

```
pip3 install esp-idf-nvs-partition-gen --break-system-packages
```

---

## Result

Provisioning completed successfully.

```
NVS provisioning complete
```

---

# Issue 2: ESP32 Serial Port Not Found

## Symptom

Provisioning failed.

```
Could not open /dev/ttyACM0
```

---

## Cause

Board disconnected or serial device reassigned.

---

## Diagnostic Commands

```
ls /dev/ttyACM*
```

```
lsusb
```

---

## Resolution

Verified active device and used the correct serial port.

---

## Result

ESP32 communication restored.

---

# Issue 3: ESP-IDF Environment Not Loaded

## Symptom

Commands failed.

```
idf.py: command not found
```

---

## Cause

ESP-IDF environment variables were not loaded.

---

## Resolution

```
source ~/esp/esp-idf/export.sh
```

---

## Verification

```
idf.py --version
```

---

## Result

ESP-IDF commands became available.

---

# Issue 4: Second ESP32 Running MicroPython

## Symptom

Unexpected console output:

```
MicroPython v1.19.1
```

---

## Cause

The board contained a previously installed MicroPython firmware image.

---

## Impact

RuView firmware was not running.

No CSI packets were generated.

---

## Resolution

Reflashed the board using the RuView CSI firmware.

```
idf.py -p /dev/ttyACM1 flash
```

---

## Result

Board booted into RuView firmware successfully.

---

# Issue 5: Missing RuField Dependency

## Symptom

Cargo build failed.

```
failed to load manifest for dependency rufield-core
```

---

## Cause

Git submodule contents were missing.

Repository contained only:

```
.git
```

---

## Resolution

Navigate:

```
cd ~/RuView/vendor/rufield
```

Restore files:

```
git reset --hard HEAD
```

---

## Result

Source code restored successfully.

---

# Issue 6: Missing RuView Swarm Dependency

## Symptom

Cargo reported:

```
failed to read ruview-swarm/Cargo.toml
```

---

## Cause

Repository contained staged deletions.

---

## Resolution

```
cd ~/RuView/v2/crates/ruview-swarmgit reset --hard HEAD
```

---

## Result

Workspace restored.

---

# Issue 7: WorldGraph Dependency Failure

## Symptom

Compilation failed.

```
failed to load wifi-densepose-geo
```

---

## Cause

Workspace dependency validation issue.

---

## Diagnostic Commands

```
find . -name Cargo.toml
```

```
find . -type d
```

---

## Resolution

Verified dependency structure and completed workspace restoration.

---

## Result

Compilation proceeded successfully.

---

# Issue 8: Backend Running in Simulated Mode

## Symptom

Backend started with:

```
Data source: simulated
```

instead of:

```
Data source: esp32
```

---

## Cause

No CSI packets were reaching the backend.

---

## Investigation

Verified listening port:

```
sudo ss -ulpn | grep 5005
```

Output:

```
0.0.0.0:5005
```

Backend was functioning correctly.

---

## Resolution

Verified firmware operation and node provisioning.

Once CSI packets arrived:

```
ESP32 CSI detected on UDP :5005
```

---

## Result

Backend automatically switched to live mode.

```
Data source: esp32
```

---

# Issue 9: Verifying CSI Packet Reception

## Symptom

Need to confirm whether packets were reaching the backend.

---

## Diagnostic Tool

```
sudo tcpdump -nn -i any udp port 5005
```

---

## Observed Traffic

```
192.168.1.8 -> 192.168.1.10:5005192.168.1.9 -> 192.168.1.10:5005
```

---

## Result

Confirmed:

- Node 1 transmitting
- Node 2 transmitting
- Backend receiving packets

---

# Issue 10: Web Dashboard Connectivity

## Symptom

Dashboard occasionally disconnected.

Observed logs:

```
WebSocket client disconnected
```

---

## Cause

Browser refreshes and page reloads.

---

## Verification

Backend logs showed:

```
WebSocket client connected
```

after reconnecting.

---

## Result

Dashboard communication functioning normally.

---

# Issue 11: ZSH History Corruption

## Symptom

Terminal displayed:

```
zsh: corrupt history file ~/.zsh_history
```

---

## Cause

History file corruption.

---

## Impact

No impact on project functionality.

---

## Resolution

Can be fixed later using:

```
mv ~/.zsh_history ~/.zsh_history.badstrings ~/.zsh_history.bad > ~/.zsh_history
```

---

# Deployment Validation Checklist

## Firmware

- [x]  Build successful
- [x]  Flash successful
- [x]  Provision successful

---

## Networking

- [x]  WiFi connected
- [x]  IP assigned
- [x]  UDP communication verified

---

## Backend

- [x]  Rust build successful
- [x]  Sensing server running
- [x]  UDP listener active

---

## Multi-Node Deployment

- [x]  Node 1 operational
- [x]  Node 2 operational
- [x]  Concurrent CSI streams verified

---

## Dashboard

- [x]  Web interface accessible
- [x]  WebSocket communication operational
- [x]  Occupancy visualization active

---

# Key Lessons Learned

1. Always verify ESP-IDF environment variables before flashing.
2. Validate Git submodules before compiling large Rust workspaces.
3. Use `tcpdump` to verify packet flow before debugging application code.
4. Check serial output immediately after flashing.
5. Verify backend listening ports before investigating firmware issues.
6. Multi-node CSI deployments require both firmware and network validation.

---

# Final Outcome

All critical deployment issues were resolved successfully.

Final system state:

- 2 ESP32-S3 sensing nodes operational
- CSI collection operational
- UDP streaming operational
- Multi-node sensing operational
- Backend operational
- Dashboard operational
- End-to-end sensing pipeline operational
