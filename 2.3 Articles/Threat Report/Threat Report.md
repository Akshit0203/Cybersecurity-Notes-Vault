# Threat Report: Alleged Aadhaar Data Leak Distributed via Underground Forum

> **Classification:** Internal — Threat Intelligence Research
> **Report date:** 2026-10-12
> **Handling:** TLP:AMBER — share only on a need-to-know basis.
> **Disclaimer:** This document records a controlled threat-intelligence investigation conducted for defensive and research purposes. All data acquisition was performed in an isolated environment. No leaked personal data was redistributed, retained in cleartext, or used beyond verification and analysis.

---

## 1. Executive Summary

During routine monitoring of underground forums, a listing advertising a bulk dataset of Indian **Aadhaar** identity records was identified on the clearweb-accessible forum `darkforums.as`. The sample was hosted on a public Google Drive link rather than a Tor hidden service, lowering the barrier to acquisition for low-skilled actors.

Analysis confirmed that the distributed archive was **weaponized**: in addition to the claimed identity records, it contained malware. The payload was isolated and neutralised inside a disposable cloud sandbox before any data review took place. During the investigation, the analysis instance exhibited **unauthorised third-party authentication attempts**, suggesting the download and/or the hosting infrastructure is actively targeted by other actors.

**Key findings:**

| # | Finding | Impact |
|---|---------|--------|
| 1 | Aadhaar-themed dataset openly advertised on `darkforums.as` | Identity-theft / fraud exposure for affected individuals |
| 2 | Distribution via public Google Drive, not Tor | Wider, lower-skill reach |
| 3 | Archive contains embedded malware ("poisoned" dataset) | Compromise of anyone who opens it without sandboxing |
| 4 | Analysis EC2 instance terminated after repeated failed logins not initiated by the analyst | Indicates hostile scanning / credential-stuffing of exposed infrastructure |

---

## 2. Scope and Objectives

- Validate whether the advertised Aadhaar dataset is genuine or a scam/lure.
- Acquire a sample **safely** for verification without exposing analyst identity or corporate infrastructure.
- Determine whether the distributed file poses a secondary threat (malware).
- Document tooling, OPSEC, and sanitisation methodology for reproducibility.

---

## 3. Methodology Overview

The investigation followed four phases, each covered in the sections below:

1. **OPSEC preparation** — establishment of an anonymous, attributable-only-to-research identity.
2. **Source access** — navigation to and enumeration of the hosting forum.
3. **Sample acquisition** — retrieval of the dataset from the distribution link.
4. **Isolation & sanitisation** — malware handling in a disposable environment prior to review.

---

## 4. Phase 1 — OPSEC: Anonymous Identity Provisioning

To avoid linking the investigation to a personal or corporate identity, a dedicated anonymous mailbox was provisioned using **Proton Mail** (end-to-end encrypted, privacy-focused, no personal information required for a free tier).

**Procedure:**

1. Navigate to Proton Mail — <https://proton.me/mail>
2. Select **Create a free account** and complete registration using no personally identifiable information.

![Proton Mail landing page](attachments/Pasted%20image%2020261012150845.png)

![Proton Mail sign-up](attachments/Pasted%20image%2020261012150923.png)

![Create free account](attachments/Pasted%20image%2020261012150944.png)

![Account configuration](attachments/Pasted%20image%2020261012151006.png)

![Mailbox setup](attachments/Pasted%20image%2020261012151224.png)

![Mailbox setup (cont.)](attachments/Pasted%20image%2020261012151250.png)

![Account verification](attachments/Pasted%20image%2020261012151307.png)

![Inbox ready](attachments/Pasted%20image%2020261012151318.png)

![Research identity provisioned](attachments/Pasted%20image%2020261012151326.png)

> **Rationale:** A segregated mailbox contains any forum notifications, confirmation emails, and account recovery traffic away from analyst or organisational accounts, and can be discarded after the engagement.

---

## 5. Phase 2 — Source Access: Forum Enumeration

With the research identity ready, the hosting forum was accessed at:

- `https://darkforums.as/`

The forum was registered to, browsed, and searched for the relevant Aadhaar-related threads. The listing of interest was located and opened, confirming the advertised dataset and its distribution link.

![Forum landing page](attachments/Pasted%20image%2020261012151419.png)

![Forum registration / login](attachments/Pasted%20image%2020261012151434.png)

![Forum navigation](attachments/Pasted%20image%2020261012151517.png)

![Forum navigation (cont.)](attachments/Pasted%20image%2020261012151542.png)

![Category listing](attachments/Pasted%20image%2020261012151613.png)

![Thread discovery](attachments/Pasted%20image%2020261012151628.png)

![Thread discovery (cont.)](attachments/Pasted%20image%2020261012151638.png)

![Search interface](attachments/Pasted%20image%2020261012151652.png)

**Search:** Enter the relevant keywords in the forum search and submit (press Enter).

![Search query entered](attachments/Pasted%20image%2020261012151710.png)

![Search submitted](attachments/Pasted%20image%2020261012151727.png)

![Search results](attachments/Pasted%20image%2020261012151756.png)

![Target thread located](attachments/Pasted%20image%2020261012151812.png)

![Thread contents](attachments/Pasted%20image%2020261012151832.png)

![Advertised dataset details](attachments/Pasted%20image%2020261012151847.png)

![Distribution link identified](attachments/Pasted%20image%2020261012151900.png)

---

## 6. Phase 3 — Sample Acquisition

The dataset was advertised with a **public Google Drive** distribution link:

- `https://drive.google.com/file/d/1gAQPgU3XND4vyV4n-4wYsDGSBNgtzHO5/view`

![Google Drive hosted file](attachments/Pasted%20image%2020261012151918.png)

![Download quota reached](attachments/Pasted%20image%2020261012151927.png)

### 6.1 Bypassing the Google Drive Download Quota

The file returned Google's *"too many users have viewed or downloaded this file recently"* quota error. Two standard workarounds were available; both rely on copying the object into a Drive account under analyst control.

**Method 1 — Shortcut method**

1. Open the research Google Drive account.
2. Locate the file via the shared link or under **Shared with me** / **Starred**.
3. Right-click the file → **Add to Starred** (or open it first if required).
4. Create a **new folder** inside **My Drive**.
5. From the **Starred** tab, right-click the file → **Organize → Add shortcut**, and place it in the new folder.
6. Return to **My Drive**, right-click the **folder** containing the shortcut, and select **Download** (download the folder — not the shortcut file on its own).

**Method 2 — "Make a copy" method**

1. Sign in to the research Google account.
2. Navigate to the restricted file under **Shared with me** / **Starred**.
3. Right-click the file → **Make a copy** (if unavailable, open the file in a new window / preview mode first).
4. Open **My Drive**, where the new copy now resides.
5. Right-click the copy → **Download**.

> **Note:** The "Make a copy" method requires sufficient free storage in the Drive account. Acquisition was performed under the dedicated research identity, never a personal or corporate Google account.

---

## 7. Phase 4 — Isolation & Sanitisation

> ⚠️ **Critical finding:** The downloaded archive is **malware-laden ("poisoned")**. It must be sanitised in an isolated environment before any inspection. Opening it on a production or personal host would result in compromise.

### 7.1 Disposable Cloud Sandbox (AWS EC2)

A throwaway **AWS EC2** instance was provisioned to serve as an air-gapped analysis environment, keeping the malware off local and corporate hardware. The sample was transferred to the instance for examination and cleaning.

### 7.2 Incident: Unauthorised Access Attempts & Instance Termination

During analysis, the EC2 instance was **terminated by the platform following repeated failed login attempts**. These attempts were **not** performed by the analyst.

**Assessment:** The repeated authentication failures against an instance that was handling this sample indicate hostile activity — most plausibly automated credential-stuffing / SSH brute-forcing against the exposed public instance, or targeting associated with the poisoned dataset's infrastructure. This reinforces that the distribution channel and anyone interacting with it are under active, opportunistic attack.

> **Open question for follow-up:** Confirm the exact termination trigger from AWS CloudTrail / console logs, identify the source IP(s) of the failed logins, and determine whether they correlate with the forum or Drive infrastructure.

### 7.3 Malware Removal ("Desanitisation")

The archive was scanned and cleaned before any data review and before transferring the (claimed) records to the analyst workstation.

**Process:**

1. Evaluated multiple anti-malware engines (trial licences) to maximise detection coverage against a single, unknown sample.
2. Scanned the archive, quarantined and removed all identified malicious components.
3. Verified the cleaned payload across engines before extracting the data for verification.
4. Only the **sanitised** output was moved to the analyst PC for review.

> **Items to complete / confirm before finalising this report:**
> - Record the specific AV/EDR products trialled and their individual detections.
> - Capture file hashes (SHA-256) of the original and sanitised archives.
> - Document the malware family / classification identified.
> - Note the data format and a non-sensitive assessment of whether the "Aadhaar" records are genuine, recycled, or fabricated.

---

## 8. Indicators of Compromise (IOCs)

| Type | Value | Notes |
|------|-------|-------|
| URL | `https://darkforums.as/` | Hosting forum |
| URL | `https://drive.google.com/file/d/1gAQPgU3XND4vyV4n-4wYsDGSBNgtzHO5/view` | Distribution link |
| Hash | *(to be added)* | SHA-256 of original archive |
| Malware family | *(to be added)* | From AV classification |
| Source IP(s) | *(to be added)* | Failed-login origins against EC2 |

---

## 9. Recommendations

1. **Do not open the sample outside isolation.** Treat the archive as live malware at all times.
2. **Report the leak** through appropriate channels (e.g., CERT-In / UIDAI) if the Aadhaar records are assessed as genuine.
3. **Request takedown** of the Google Drive object and the forum thread via the respective abuse channels.
4. **Harden any future sandbox:** restrict inbound SSH/RDP to analyst IPs only, disable password auth, use key-based access, and prefer ephemeral, network-isolated instances.
5. **Preserve evidence:** retain hashes, logs, and screenshots; purge sanitised data once analysis is complete per data-handling policy.

---

## 10. Appendix — Evidence Index

All screenshots referenced in this report are stored under `attachments/` and are dated 2026-10-12. Phases map to the figure ranges as follows:

- **Phase 1 (OPSEC / Proton Mail):** `20261012150845` – `20261012151326`
- **Phase 2 (Forum enumeration):** `20261012151419` – `20261012151900`
- **Phase 3 (Google Drive acquisition):** `20261012151918` – `20261012151927`
