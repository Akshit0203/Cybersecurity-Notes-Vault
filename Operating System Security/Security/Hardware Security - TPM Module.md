
A **TPM (Trusted Platform Module)** is a small security chip inside a computer that helps **protect passwords, encryption keys, and the system itself from hackers or malware**.

Think of it like:

> A **hardware security vault** built into your motherboard or CPU.

It stores sensitive secrets in a way that normal software cannot easily steal.

---

# Why TPM Exists

Normally, passwords and encryption keys are stored in software or on disk.

Problem:

- Malware can steal them
- Hackers can dump memory
- Attackers can modify boot files
- Stolen laptops can have disks removed and read

TPM solves this by:

- Storing secrets in hardware
- Verifying system integrity during boot
- Helping with encryption and authentication

---

# Real-Life Analogy

Imagine your laptop is a building.

- OS = employees
- Files = documents
- Passwords = important keys
- TPM = ultra-secure vault room guarded by hardware

Even if someone breaks into the building (malware/rootkit), opening the vault is extremely difficult.

---

# Where TPM Is Found

Most modern systems have TPM:

- Windows laptops
- Business desktops
- Servers
- Some Raspberry Pi projects (via external TPM)
- Enterprise devices

Windows 11 actually requires TPM 2.0.

---

# Types of TPM

## 1. Discrete TPM

Dedicated physical chip on motherboard.

Most secure.

---

## 2. Firmware TPM (fTPM)

Implemented inside CPU firmware.

Examples:

- AMD fTPM
- Intel PTT

No separate chip needed.

---

## 3. Software TPM

Emulated in software.

Mostly used for:

- Virtual machines
- Testing
- Labs

Least secure.

---

# What TPM Actually Does

---

# 1. Secure Key Storage

TPM stores:

- Encryption keys
- Certificates
- Password hashes
- BitLocker keys
- VPN keys

The important part:

> The private keys NEVER leave the TPM.

Even the OS often cannot directly read them.

---

# 2. Secure Boot Verification

TPM checks whether:

- BIOS/UEFI changed
- Bootloader modified
- Kernel tampered
- Rootkit inserted

This helps stop:

- Bootkits
- Rootkits
- Evil maid attacks

---

# 3. Device Encryption (BitLocker)

In Windows, TPM works with BitLocker.

Process:

1. TPM stores disk encryption key
2. Laptop boots normally → TPM releases key
3. If system files are modified → TPM refuses

Result:

- Stolen SSD is useless
- Removing drive won't bypass encryption

---

# 4. Platform Integrity Measurements

TPM measures boot components using hashes.

It records:

- BIOS hash
- Bootloader hash
- Kernel hash
- Driver hashes

These are stored in special registers called:

# PCRs (Platform Configuration Registers)

If hashes change unexpectedly:

- TPM detects tampering
- Keys may not unlock

---

# TPM Boot Flow (Easy Version)

## Normal Boot

```
Power ON   ↓UEFI/BIOS starts   ↓TPM measures BIOS hash   ↓Bootloader measured   ↓OS measured   ↓Everything trusted?   ↓ YESRelease encryption key   ↓Windows boots
```

---

## Tampered Boot

```
Attacker changes bootloader   ↓TPM detects different hash   ↓PCR values change   ↓TPM refuses to release key   ↓BitLocker recovery mode
```

---

# Main TPM Concepts

# 1. Endorsement Key (EK)

Unique key burned into TPM during manufacturing.

Acts like:

- TPM identity
- Hardware identity

---

# 2. Storage Root Key (SRK)

Master key inside TPM.

Used to protect other keys.

---

# 3. PCR Registers

Special registers storing integrity measurements.

Very important in:

- Secure boot
- Attestation
- BitLocker

---

# 4. Sealing

TPM can lock data so it only opens if:

- Same boot state
- Same firmware
- Same configuration

Example:

- Encryption key only works if boot files unchanged.

---

# 5. Remote Attestation

TPM can prove to another system:

> "This machine booted securely and hasn't been tampered with."

Used in:

- Enterprise security
- Cloud systems
- Zero Trust
- Device compliance

---

# TPM and Windows 11

Microsoft requires TPM 2.0 because it enables:

- Secure Boot
- BitLocker
- Credential Guard
- Windows Hello
- Virtualization-Based Security (VBS)

---

# TPM vs HSM

People confuse these.

|TPM|HSM|
|---|---|
|Built into PC|Dedicated enterprise hardware|
|Endpoint security|Enterprise cryptography|
|Cheap|Expensive|
|Local device trust|Datacenter/cloud trust|

---

# TPM vs Secure Enclave vs TEE

|Technology|Used In|
|---|---|
|TPM|PCs|
|Secure Enclave|Apple devices|
|Titan M|Google Pixel|
|TrustZone|ARM devices|
|TEE|Isolated execution environments|

All aim to protect secrets using hardware isolation.

---

# TPM 1.2 vs TPM 2.0

|TPM 1.2|TPM 2.0|
|---|---|
|Older|Modern|
|SHA-1 focused|SHA-256 support|
|Less flexible|More algorithms|
|Limited features|Better security|

Windows 11 needs TPM 2.0.

---

# Common TPM Use Cases

## Enterprise

- Disk encryption
- Device authentication
- Secure VPN auth
- Compliance

## Cloud

- Trusted boot
- Remote attestation

## Developers/Security

- Hardware-backed SSH keys
- Secure signing
- Credential protection

---

# TPM Attacks

TPM is strong, but not magic.

---

# 1. Physical Attacks

Advanced attackers may:

- Probe motherboard
- Use microscopes
- Perform side-channel attacks

Very difficult and expensive.

---

# 2. Cold Boot Attacks

RAM contents may still leak if keys enter memory after unlock.

TPM reduces risk but doesn't eliminate all attacks.

---

# 3. Evil Maid Attack

Attacker physically modifies bootloader.

TPM helps detect this through PCR changes.

---

# 4. DMA Attacks

Thunderbolt/PCIe attacks may target unlocked systems.

---

# TPM in Cybersecurity

As someone interested in:

- cloud security
- SOC
- VAPT
- endpoint security
- malware analysis

TPM is important because modern defenses rely heavily on:

- hardware trust
- secure boot
- credential isolation
- attestation

This is heavily used in:

- EDR/XDR systems
- enterprise Windows hardening
- Zero Trust architecture
- cloud workload identity

---

# Simple Summary

## TPM is basically:

> A hardware-based trust anchor for a computer.

It:

- securely stores secrets
- verifies system integrity
- helps encryption
- protects credentials
- detects tampering

---

# One-Line Understanding

> TPM ensures the computer is trusted before sensitive secrets are released.