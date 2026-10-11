# Aviation Security Implications

GPS/GNSS is woven into nearly every layer of modern aviation. This document explains why a
spoofed position — trivially generated with a low‑cost SDR, as demonstrated in this project —
is a serious safety and security concern, and how a single spoof cascades through dependent
systems.

## Why GNSS is an attractive target

Civil GPS was designed for **openness**, not security:

- **No authentication.** The civil L1 C/A message carries no cryptographic signature, so a
  receiver cannot tell a genuine satellite from a simulated one.
- **Extremely weak signals.** By the time GPS reaches the ground it is around **−125 to
  −130 dBm** — below the thermal noise floor. A nearby SDR can easily be louder.
- **Predictable structure.** The signal format (IS‑GPS‑200) and the broadcast ephemeris are
  public, so a valid‑looking waveform is straightforward to synthesize.

The result: overpowering the real signal with a false one is cheap and, technically, easy.

## How a spoof propagates through aviation systems

### 1. Navigation & Flight Management System (FMS)
Aircraft use GNSS for en‑route navigation, RNAV/RNP procedures, and GNSS‑assisted approaches. A
spoofed position/time can push the FMS and navigation displays off the true track, and may
trigger confusing or contradictory alerts for the crew.

### 2. ADS‑B surveillance (the cascade)
**Automatic Dependent Surveillance–Broadcast (ADS‑B)** has each aircraft broadcast its **own
GPS‑derived position** on 1090 MHz for air‑traffic awareness and collision avoidance. Critically:

> If the aircraft's GNSS receiver accepts a spoofed position, its ADS‑B Out will **truthfully
> broadcast that false position** — and every ground station, ATC‑style display, and nearby
> aircraft that receives it will **trust it**.

ADS‑B has **no encryption, no authentication, and no GNSS‑integrity validation**, so spoofed GPS
becomes spoofed aircraft telemetry downstream. This directly affects:

- Air‑traffic situational awareness and separation.
- Collision‑avoidance inputs.
- Flight‑tracking tools and services.
- Navigation‑assisted landings and ground navigation aids.

### 3. Timing
GPS also distributes precise time. GPS‑disciplined oscillators in telecom and power
infrastructure — and some ground aviation systems — can be dragged off by a time spoof, with
effects well beyond the cockpit.

## Real‑world context

GPS spoofing and jamming have moved from theory to frequent operational reports since 2023–2025,
particularly in and around conflict zones and contested airspace: the Middle East, the Eastern
Mediterranean, the Baltic and Black Sea regions, and parts of South Asia including the Delhi and
Ladakh regions. Crews have reported sudden, large position jumps, false terrain/traffic alerts,
and loss of GNSS integrity — forcing reliance on conventional navigation aids.

## Takeaway

The barrier to entry is low and the blast radius is wide. Because so many safety systems *assume*
GNSS is trustworthy, the mitigation cannot be "trust GPS less" alone — it requires authentication,
cross‑checking across constellations, and GNSS‑independent backups. See
[countermeasures.md](countermeasures.md).
