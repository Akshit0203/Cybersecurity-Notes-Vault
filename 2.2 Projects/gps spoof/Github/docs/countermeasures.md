# Countermeasures & Detection

Defending against GNSS spoofing requires layers: making spoofing harder to fake, detecting it
when it happens, and surviving it with independent backups. No single control is sufficient.

## 1. Authentication — make the signal verifiable

- **Galileo OSNMA (Open Service Navigation Message Authentication).** Cryptographically signs the
  Galileo navigation message so receivers can verify authenticity. The strongest standardized
  civil defense available today; pairing GPS with authenticated Galileo raises the bar
  significantly.
- **Chips‑Message Robust Authentication (Chimera)** and other emerging signal‑authentication
  schemes for GPS.

## 2. Integrity monitoring — detect inconsistency

- **RAIM / ARAIM** (Receiver Autonomous Integrity Monitoring): cross‑checks redundant satellite
  measurements to flag inconsistent (potentially spoofed/faulty) solutions.
- **Consistency & plausibility checks:** sudden position/time jumps, implausible velocity, or
  clock bias discontinuities are spoofing red flags.
- **Received‑power / AGC monitoring:** spoofing often arrives abnormally strong; monitoring
  signal power and automatic‑gain‑control behavior can reveal it.

## 3. Antenna‑ and physics‑based defenses

- **Multi‑element / CRPA antennas** and **direction‑of‑arrival** analysis: genuine satellites
  arrive from many directions; a spoofer typically arrives from one, which array processing can
  detect and null.
- **Carrier‑phase and polarization checks** to distinguish a single spoofing source from a true
  constellation.

## 4. Diversity — don't depend on one system

- **Multi‑constellation positioning:** combine **GPS + Galileo + GLONASS + BeiDou + NavIC**. An
  attacker must now spoof several independent systems consistently, which is far harder.
- **Regional systems (e.g. NavIC / IRNSS)** add independent cross‑checks for the Indian region.

## 5. Independent backups — survive a successful spoof

- **Inertial Navigation Systems (INS/IMU):** self‑contained; drift over time but immune to RF
  spoofing, ideal for cross‑checking and bridging GNSS loss.
- **Terrestrial aids:** **VOR/DME**, ILS, and barometric altitude provide GNSS‑independent
  navigation and should remain available as fallbacks.

## 6. Monitoring & operations

- **Spectrum monitoring at airports and critical sites** to detect interference/spoofing in real
  time and locate sources.
- **Crew and ATC procedures** for recognizing and responding to GNSS anomalies, with fallback to
  conventional navigation.
- **Reporting** events to the relevant authorities (e.g. DGCA/AAI, CERT‑In/NCIIPC in India) to
  build situational awareness.

## Defense‑in‑depth summary

| Layer | Example controls |
|---|---|
| Authenticate | Galileo OSNMA, Chimera |
| Detect | RAIM/ARAIM, power/AGC & consistency monitoring |
| Resist (antenna) | CRPA arrays, direction‑of‑arrival nulling |
| Diversify | Multi‑GNSS (GPS/Galileo/GLONASS/BeiDou/NavIC) |
| Back up | INS, VOR/DME, baro‑altitude |
| Operate | Spectrum monitoring, crew/ATC procedures, reporting |

The lesson from this demonstration is simple: because civil GNSS is unauthenticated and weak,
**safety‑critical systems must not treat a GPS fix as inherently trustworthy.** Layered
authentication, detection, diversity, and backups are what turn a cheap, effective attack into a
detectable and survivable one.
