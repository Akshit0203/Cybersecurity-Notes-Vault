# Legal & Ethical Disclaimer

## Read this before using anything in this repository.

This project is published **for cybersecurity education, defensive research, and academic
awareness only**. It documents how GPS/GNSS spoofing works so that engineers, researchers, and
aviation/security professionals can understand the threat and build defenses against it.

### 1. GPS/GNSS is a protected, safety‑critical service

The GPS L1 band (**1575.42 MHz**) and other GNSS bands are reserved for radio navigation.
Aircraft, ships, emergency services, vehicles, mobile networks, financial systems, and power
grids rely on them. **Interfering with these signals can endanger human life.**

### 2. Transmitting is illegal almost everywhere

Deliberately transmitting a spoofed or jamming signal on GNSS frequencies — even at low power,
even "briefly," even "just to test" — is a **criminal offense** in virtually every country
(e.g., violations of radio/telecom law, aviation safety law, and anti‑interference statutes).
Penalties include heavy fines and imprisonment.

### 3. What was actually done here

All experiments described in this repository were performed **inside an isolated, non‑radiating
RF test environment** — a wired/shielded connection into a dedicated receiver under test, with
transmit power kept minimal. **No signal was radiated over the air into any public space, and no
live aircraft, vehicle, ship, or third‑party device was ever targeted.**

### 4. What you must NOT do

- ❌ Do **not** connect an antenna and transmit on GPS/GNSS frequencies over the air.
- ❌ Do **not** use this to interfere with, mislead, or disable any navigation or timing system.
- ❌ Do **not** target aircraft, vehicles, ships, phones, or any device you do not own and
  fully control in isolation.
- ❌ Do **not** use this near airports, ports, roads, or any operational environment.

### 5. Your responsibility

You are **solely responsible** for how you use this material and for complying with all
applicable laws and regulations in your jurisdiction. If you are unsure whether something is
legal, **assume it is not** and consult the relevant authority.

### 6. No liability

This material is provided "as is," without warranty of any kind. The author assumes **no
liability** for any misuse, damage, or legal consequence arising from the use of this
repository. By using it, you accept full responsibility for your own actions.

---

**The intent of this work is to strengthen GNSS and aviation security — not to undermine it.**
