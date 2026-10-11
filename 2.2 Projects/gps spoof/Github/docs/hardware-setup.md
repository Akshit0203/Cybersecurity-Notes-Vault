# Hardware Setup & RF Isolation

> ⚠️ Transmitting on GPS/GNSS frequencies over the air is illegal and dangerous. Everything below
> describes a **contained bench** used for defensive research. See [../DISCLAIMER.md](../DISCLAIMER.md).

## Bill of materials

| Item | Notes |
|---|---|
| **HackRF One** | Half‑duplex SDR transceiver, 1 MHz–6 GHz. The transmitter in this project. |
| **PortaPack H2+** | Add‑on with screen + controls; runs **Mayhem** firmware for standalone operation. |
| **Host PC running DragonOS** | SDR toolchain, `hackrf_transfer`, GPS‑SDR‑SIM build. |
| **Active GPS antenna (1575.42 MHz)** | *Test only.* Radiating element — **not** used over the air. |
| **GPS receiver under test** | A phone / GNSS module used to observe the spoofed fix. |
| **Shielded enclosure / direct cabling / attenuators** | To keep all RF energy contained. |

![Bench overview](../assets/images/17-hardware-setup.jpg)

The photo shows the receiver (left) reporting a position at IGI Airport while the HackRF +
PortaPack (right) is tuned to **1 575 420 000 Hz**.

## RF isolation — the non‑negotiable part

A spoofed GPS signal that leaks out can mislead **any** GNSS receiver in range — phones,
vehicles, drones, aircraft on approach, and timing systems. To keep the experiment legal and
safe, the RF energy must be fully contained. Acceptable approaches:

1. **Direct wired connection** from the HackRF TX port to the receiver's antenna input,
   with appropriate **attenuation** (GPS receivers expect ~−125 to −130 dBm; a direct feed is
   vastly stronger and must be attenuated to avoid damage and leakage).
2. **A shielded RF enclosure / Faraday setup** containing both the transmit antenna and the
   receiver, verified to prevent emissions escaping.

Keep transmit power at the **minimum** that produces a lock (`-x 0` and modest `-a` settings).
More power is never "better" here — it only increases leakage risk.

## Frequency & sampling reference

| Parameter | Value |
|---|---|
| Carrier (GPS L1 C/A) | **1575.42 MHz** (`-f 1575420000`) |
| Sample rate | **2.6 Msps** (`-s 2600000`) |
| I/Q format | **8‑bit signed** (`-b 8`) |
| Amplifier | enabled (`-a 1`) |
| TX VGA gain | minimal (`-x 0`) |

The sample rate used at transmit **must match** the rate used when generating `gpssim.bin`.

## Firmware

PortaPack/Mayhem firmware is flashed via **WebUSB** at <https://hackrf.app/> (see the
[methodology](methodology.md#4-prepare-the-hackrf-one)). Confirm the running firmware and device
identity with `hackrf_info` before transmitting.
