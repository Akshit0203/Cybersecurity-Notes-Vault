# OSCP Exam Guide

> [!tip] How to use this guide
> Bookmark the official OSCP Exam Guide and read it end‑to‑end multiple times before your exam — set a daily reminder once your exam is scheduled and spend 30–60 minutes re‑reading every sentence in the days before. Candidates **fail even after getting every flag** because of rule violations or weak reporting. Treat the rules with a "deny‑by‑default" mindset: verify a tool is allowed before you run it.

---

## 1. Exam Duration

- **Practical phase: 23 hours 45 minutes.** Colloquially a "24‑hour" exam, but you actually get **15 minutes less than 24 hours**.
  - The 15‑minute reduction is OffSec's operational buffer to tear down your dedicated exam network and terminate all VMs.
  - Example: start **09:00 GMT → access ends 08:45 GMT** the next day.
- **Reporting phase: a further uninterrupted 24 hours** to write and upload your report (no network teardown involved here).

---

## 2. Proctoring & Environment

- **All OSCP+ exams are proctored.** Proctoring is active only during the **23h 45m** practical phase; the 24‑hour reporting phase is **not** proctored.
- Proctoring software runs on your **physical host OS** (e.g. base Windows), not inside the VM. Your **entire physical desktop is recorded**, not just the Kali VM window.
- **Headphones:** permitted, but must be physically connected to the proctored machine.
- **Audio:** proctors watch via webcam but **you are muted** — they have no microphone access, so verbal venting is not heard.
- Read the proctoring tool manual + FAQ: https://help.offsec.com/hc/en-us/sections/360008126631-Proctored-Exams

---

## 3. Exam Structure & Point Allocation

**100 points max · 70 points to pass.**

### 3 Stand‑alone / independent machines — 60 pts (20 each)
- Two stages per machine:
  - **10 pts** — initial low‑privilege access (`local.txt`)
  - **10 pts** — privilege escalation to admin/root (`proof.txt`)
- **Partial points allowed** on stand‑alones.

### 1 Active Directory set (3 machines) — 40 pts
- A dedicated network: **two client workstations + one Domain Controller (DC)**.
- You are given a **username and password** simulating a breach/assumed‑breach scenario.
- Point breakdown: **10 pts machine #1 + 10 pts machine #2 + 20 pts machine #3 (DC)**.
- Requires the complete, unbroken exploit chain from initial foothold to **Domain Admin on the DC** (recover every flag across the set).

> [!warning] AD scoring nuance
> The walkthrough describes AD as effectively **all‑or‑nothing** in practice — you need the full chain to the DC to be useful. The official breakdown does list 10/10/20 sub‑values, but you should plan to fully own the set.

### Grading order & objectives
- Machines are graded **in the order you document them** in your report.
- Each machine has specific objectives/point values shown in your **exam control panel**.

### Example passing combinations (70/100)
- 40 (AD) + 3 × `local.txt` = **70**
- 40 (AD) + 2 × `local.txt` + 1 × `proof.txt` = **70**
- 20 (AD) + 3 × `local.txt` + 2 × `proof.txt` = **70**
- 10 (AD) + 3 fully completed stand‑alones = **70**

> [!note] Bonus points
> Historically, **10 bonus points** were awarded for completing ≥80% of lab exercises across all course modules **and** submitting 30 correct challenge‑lab proof hashes before the exam.

---

## 4. Proof Files & Required Privilege

| File | Meaning | Location |
|------|---------|----------|
| `local.txt` | Initial low‑privilege access | Compromised user's profile — `C:\Users\<user>\Desktop` (Win) or `/home/<user>/` (Linux) |
| `proof.txt` | Full admin/root compromise | `C:\Users\Administrator\Desktop` (Win) or `/root/` (Linux) |

**Required privilege level for full points:**
- **Windows:** shell running as **`NT AUTHORITY\SYSTEM`** (strongly recommended), the built‑in **`Administrator`**, or a user in the local **`Administrators`** group.
- **Linux:** an interactive shell running as **`root`**.

> Proof files must be retrieved and displayed from their **original file‑system location**. Copying them to temp directories or public shares is forbidden.

---

## 5. Interactive Shell Requirement

Proof contents must be shown from an **authenticated interactive shell** using `type` (Windows) or `cat` (Linux) from the file's original location.

> [!danger] Obtaining proof any other way = **zero points** for that target. This explicitly includes **any type of web‑based shell.**

**Valid interactive shells** — operate via an allocated pseudo‑terminal (TTY), keep persistent session state (`cd`, command chaining), show continuous interactive prompts:
- Netcat reverse TCP shells
- SSH terminal sessions
- Meterpreter command shells
- RDP graphical desktop sessions
- Windows/Linux command prompts simulating a standard terminal

**Invalid (NOT interactive):**
- A **web shell** — e.g. a PHP script calling `system()`, `exec()`, `passthru()`. Each command spawns a separate background process; no persistent state, no TTY. Running `cat local.txt` through a browser/web shell is invalid.

![[4. OSCP/Done/Bitten Tech PEN1/14. Preparing for OSCP/1. OSCP Exam Guide/Attachments/Pasted image 20261016212649.png]]

- Even **OS command injection / RCE** by itself is not a shell.

![[4. OSCP/Done/Bitten Tech PEN1/14. Preparing for OSCP/1. OSCP Exam Guide/Attachments/Pasted image 20261016212837.png]]

> [!tip] Fix
> If you have a web shell or RCE, use it to **stage a reverse‑shell callback** and catch an authentic interactive shell on a local listener **before** capturing proof.

---

## 6. Screenshot Requirements

- **Pour in as many screenshots as you can** throughout the report; heavily document commands and full terminal output.
- **Mandatory flag screenshot:** every `local.txt` and `proof.txt` must appear in a screenshot showing **both the flag file contents AND the machine's IP address in the same terminal session**.
  - **Windows:** `type local.txt` / `type proof.txt` alongside `ipconfig`
  - **Linux:** `cat local.txt` / `cat proof.txt` alongside `ip a` / `ifconfig` / `ip addr`
- This proves the flag came from that target via a real interactive shell, not fabricated or moved.

![[4. OSCP/Done/Bitten Tech PEN1/14. Preparing for OSCP/1. OSCP Exam Guide/Attachments/Pasted image 20261016205822.png]]

---

## 7. Control Panel & Flag Submission

Access the control panel via the link in your exam email (VPN connects ~15–30 min before start). Through it you can:
- **View** target IPs, objectives, and point values.
- **Revert / re‑spawn machines** — reset a target to a clean state (see Reverts below).
- **Submit captured flags** — each target IP has a flag submission field. There is **no separate field for `local.txt` vs `proof.txt`**; both hashes from a host are submitted against that machine's IP.

> The control panel will **not** tell you whether a submitted proof is correct.

![[4. OSCP/Done/Bitten Tech PEN1/14. Preparing for OSCP/1. OSCP Exam Guide/Attachments/Pasted image 20261016205632.png]]

> [!important] Proof contents must be submitted in the control panel **before your exam ends.**

### Machine Reverts
- **24 reverts total**, resettable **once** during the exam.
- All machines are freshly reverted at the start — no need to revert at the beginning.
- Click the revert button **once per attempt** and wait patiently.
- Reverting returns a machine to its original state — **any changes you made are lost**. You may also revert for documentation purposes.

---

## 8. Exam‑Day Workflow (avoid the flag‑submission trap)

> [!danger] Common fatal mistake
> Candidates wait to submit all flags at the end while focused on reporting, run out of time when the 23h 45m window closes, and **can no longer submit** — failing despite compromising the machines.

**Recommended per‑machine loop:**
1. Compromise the system and capture `local.txt` / `proof.txt`.
2. Take the mandatory screenshot (flag contents **+** host IP).
3. **Submit the flag to the control panel immediately.**
4. Record commands and terminal output for your report before moving on.

---

## 9. Documentation & Reporting Requirements

Documentation is roughly **half the exam weight** and is graded strictly. Getting every flag but submitting a weak report is an **immediate fail**.

- Write a **professional penetration‑test report** describing the exploitation of each target: all steps, commands issued, and console output — thorough enough that a competent reader can replicate your attack step‑by‑step.

> [!warning] Once submitted, your report is **final.** Missing screenshots/info will **not** be requested and **cannot** be re‑sent.

### Exploit Code documentation
- **Unmodified public exploit (e.g. a public CVE):** provide **only the source URL** — do not paste long unmodified code. If the code is short, you may paste the full PoC into the PDF.
- **Modified exploit:** include **(1)** the modified code, **(2)** the URL to the original, **(3)** the shellcode‑generation command (if any), **(4)** highlighted changes, and **(5)** why you made them.

### Shellcode & payloads
- If you generated custom shellcode/payloads (e.g. `msfvenom`), document the **exact generation command**, how the payload was constructed, and any adjustments.

---

## 10. Exam Restrictions (Prohibited)

**You may NOT use:**
- **Spoofing / MITM** — IP, ARP, DNS, NBNS/NBT‑NS, **LLMNR poisoning via Responder**, etc. (These will not appear on the exam.)
  - *Local OS privilege impersonation (PrintSpoofer, token manipulation) is fully permitted.*
- **Commercial tools/services** — Metasploit Pro, Burp Suite Pro, Core Impact, Canvas, SAINT, etc. (Free/Community editions are fine.)
- **Automatic exploitation tools** — `db_autopwn`, `browser_autopwn`, **SQLmap**, SQLninja, etc. (SQLi must be exploited **manually** — build queries, test clauses, stack statements, run commands via `xp_cmdshell`/UDFs, etc.)
- **Mass vulnerability scanners** — Nessus, NeXpose, OpenVAS, Canvas, Core Impact, SAINT (commercial or open‑source — all banned).
- **AI chatbots / LLMs** — OffSec KAI, ChatGPT, Deepseek, Gemini, YouChat, etc. This counts as third‑party help and violates the Academic Policy. Having an AI interface visible on your proctored screen = **immediate disqualification**.
- **Wrapper utilities** — any custom/third‑party wrapper that encapsulates a restricted tool (e.g. SQLmap under another name) or performs equivalent automated exploitation.
- Features in any tool that use the forbidden/restricted techniques above.

> You are **not** required to disable built‑in AI features in tools like Notion or Google's AI Overview. You **may** use Discord to search for information — but never to seek or receive help from others.

**Do not download** applications, files, or source code from the exam environment to your local machine unless necessary to compromise a target — and delete it afterward.

> OffSec **will not comment** on allowed/restricted tools beyond this guide.

---

## 11. Permitted Tools

**Network & web enumeration:** Nmap (standard scans + **recon/enumeration NSE scripts only**), Nikto, Burp Suite Community, DirBuster, Gobuster, Feroxbuster, Wfuzz, AutoRecon *(provided no automated exploitation modules are invoked)*.

**Exploit repos & utilities:** Searchsploit, Exploit‑DB, Netcat, interactive PowerShell core sessions (`Enter-PSSession` / `New-PSSession`).

**Active Directory assessment:** BloodHound, SharpHound, PowerView, PowerShell Empire, Covenant, evil‑winrm, CrackMapExec, PrintSpoofer, Impacket.
- *Responder may not be used for LLMNR/NBT‑NS poisoning, but non‑poisoning utilities are acceptable.*

---

## 12. Metasploit Restrictions

> [!important] The single‑machine rule
> You may use **Metasploit modules (Auxiliary, Exploit, Post)** or the **Meterpreter payload** against **ONE single target machine of your choice**, for the entire exam.

- Once used on a machine (foothold or privesc), it **cannot** be used against any other machine or step.
- It **cannot** be used across the **Active Directory** environment.
- It **cannot** be used for **pivoting** (that would use it on >1 target). Pivot with **SSH port forwarding**, **Chisel**, or **sshuttle** instead.
- Do **not** use Metasploit/Meterpreter to *test* vulnerabilities on multiple machines before choosing your one target — this includes `check`.
- Use is **locked in** the moment you use it: if it fails on your chosen target, you **may not** try it on a second target.
- You may use Metasploit/Meterpreter as many times as you like against your one chosen machine.
- All limitations also apply to Metasploit interfaces: **Armitage, Cobalt Strike, Metasploit Community Edition**, etc.

> [!tip] Advice from the walkthrough: **avoid Metasploit entirely.** Passing without it is completely achievable and avoids relying on a single‑use safety net.

### Tooling distinctions (unrestricted vs restricted)
| Tool | Status |
|------|--------|
| **`msfvenom`** | **Unrestricted** — use unlimited times on all machines to generate reverse shells, binaries (EXE, MSI), scripts (Python, Ruby, ELF). |
| **`multi/handler`** (`exploit/multi/handler`) | Allowed on **all** machines to catch standard (non‑Meterpreter) reverse shells. |
| **Meterpreter** | Subject to the **single‑machine, single‑use** limit. |

---

## 13. Exam Connection (OpenVPN)

Connect using **Kali Linux + OpenVPN** (no VPN support for other setups). Your connection pack and credentials arrive by email **at the exact start time** (~10–15 min before, per the walkthrough), as a `exam-connection.tar.bz2` archive. Authenticate with your **OS ID** as the username and the exam password from the email.

Extracting the archive yields an **OpenVPN config file** and a **troubleshooting script**.

**1) Extract the archive:**
```
┌──(kali㉿kali)-[~]
└─$ tar xvfj exam-connection.tar.bz2
OS-XXXXXX-OSCP.ovpn
troubleshooting.sh
```

**2) Connect:**
```
┌──(kali㉿kali)-[~]
└─$ sudo openvpn OS-XXXXXX-OSCP.ovpn
```

**3) Authenticate with the emailed username/password:**
```
┌──(kali㉿kali)-[~]
└─$ sudo openvpn OS-XXXXXX-OSCP.ovpn
[sudo] password for kali:
2022-01-11 04:15:50 Note: Treating option '--ncp-ciphers' as '--data-ciphers' (renamed in OpenVPN 2.5).
2022-01-11 04:15:50 OpenVPN 2.5.0 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Oct 28 2020
2022-01-11 04:15:50 library versions: OpenSSL 1.1.1g 21 Apr 2020, LZO 2.10
🔐 Enter Auth Username: OS-XXXXXX
🔐 Enter Auth Password: ***********
2022-01-11 04:16:01 TCP/UDP: Preserving recently used remote address: [AF_INET]x.x.x.x:1194
2022-01-11 04:16:01 UDP link local (bound): [AF_INET][undef]:1194
2022-01-11 04:16:01 UDP link remote: [AF_INET]x.x.x.x:1194
2022-01-11 04:16:01 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
2022-01-11 04:16:02 [offensive-security.com] Peer Connection Initiated with [AF_INET]x.x.x.x:1194
2022-01-11 04:16:03 TUN/TAP device tun0 opened
2022-01-11 04:16:03 net_iface_mtu_set: mtu 1500 for tun0
2022-01-11 04:16:03 net_iface_up: set tun0 up
2022-01-11 04:16:03 net_addr_v4_add: 192.168.xx.xx/24 dev tun0
2022-01-11 04:16:03 Initialization Sequence Completed
```

---

## 14. Disqualification Triggers

You receive **no points for a target** if you:
- Use a **restricted tool**.
- Use Metasploit **Auxiliary/Exploit/Post** modules on **multiple** machines.
- Use the **Meterpreter payload** on **multiple** machines.
- Fail to provide `local.txt` / `proof.txt` contents in **both** the control panel **and** an interactive‑shell screenshot.
- Provide **insufficient documentation**.
- Omit the **host IP address** in a flag proof screenshot.
- Use a commercial tool (Burp Pro, Metasploit Pro) or submit a poorly formatted/incomplete report.

---

## 15. Report Submission Instructions

**Submission checklist:**
- Report is in **PDF** format.
- PDF named exactly: `OSCP-OS-XXXXX-Exam-Report.pdf` (`OS-XXXXX` = your OSID).
- PDF archived into a **`.7z`** file — **no password**.
- `.7z` named exactly: `OSCP-OS-XXXXX-Exam-Report.7z`.
- Archive is **≤ 200 MB**.
- Uploaded to https://upload.offsec.com within the 24‑hour reporting window.

> [!warning] Filenames are **case‑sensitive** and must match the exact format, or the upload will be rejected. Include **all scripts/PoCs as text inside the PDF** — only PDF is accepted inside the `.7z`.

**Create the archive (on Kali):**
```
┌──(kali㉿kali)-[~]
└─$ sudo 7z a OSCP-OS-XXXXX-Exam-Report.7z OSCP-OS-XXXXX-Exam-Report.pdf

7-Zip 9.20 Copyright (c) 1999-2010 Igor Pavlov 2010-11-18 p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,2 CPUs)

Scanning
Updating archive OSCP-OS-XXXXX-Exam-Report.7z

Everything is Ok
```

**Verify your upload with MD5** — the site shows the MD5 of the uploaded file; compare it to your local file. If they differ, the upload failed — re‑upload.
```
┌──(kali㉿kali)-[~]
└─$ sudo md5sum OSCP-OS-XXXXX-Exam-Report.7z
f7feecea01ac1eca9ee522906b087d5e  OSCP-OS-XXXXX-Exam-Report.7z
```

- After uploading, click the **"Submit File"** button (after verifying the MD5) — otherwise it is not submitted.
- A **confirmation email** is sent on success. If none arrives, confirm you clicked Submit File and check spam/junk.
- **Windows 11 upload bug:** some users get a *"file is not a proper format"* error — upload from a **Kali VM** instead.

**Report templates** (use the official ones; they match grading criteria):
- Microsoft Word: https://www.offsec.com/pwk-online/OSCP-Exam-Report.docx
- OpenOffice/LibreOffice: https://www.offsec.com/pwk-online/OSCP-Exam-Report.odt
- You may use your own template if it is structured, professional, and meets all requirements.

---

## 16. Breaks & Proctor Communication

- You are **not expected to work non‑stop**. Frequent breaks (e.g. 30–60 min after compromising a machine) are strongly encouraged to manage fatigue. There is **no limit** on break duration — a 5‑minute break or an 8–10 hour sleep are both fine.

> [!important] Mandatory communication protocol
> - **Notify the proctor via text chat every time you step away**: type `"I am taking a break"`. Leaving your desk without notifying triggers security suspicion.
> - If the proctor does not reply immediately, don't wait — post the message and step away.
> - On returning, type `"I am back"` so they can log your return.

---

## 17. Emergencies & Contingency Planning

OffSec expects you to **have a contingency plan** for issues outside your control. The 23h 45m window already accounts for rest, food, and sleep.

- **Power outages:** have a **UPS** capable of keeping networking gear online long enough to notify the proctor. (Real example: an OSWE candidate hit a 7–8 hour residential power outage; a basic UPS lasted only 30 min.) Check for scheduled power maintenance in your area on exam day.
- **Internet redundancy:** use a stable wired/Wi‑Fi connection and keep a **secondary backup** (e.g. a reliable 5G hotspot) ready to bridge ISP outages.
- **Physical well‑being:** if burned out, sleep 5–6 hours and resume refreshed rather than struggling while fatigued.
- **Legitimate severe issue:** email your OSID to **challenges AT offsec DOT com** immediately with supporting documentation (letter from power company/ISP, etc.). OffSec only extends time for issues on **their** side, and only if the subnet isn't needed immediately after; if the subnet is scheduled right after, they provide a **free retake** instead.

---

## 18. Contact & Support

- Connectivity problems with VPN or targets → report **immediately in the proctoring chat**.
- Can't access the proctoring tool → live chat at **https://chat.offsec.com/** or email **help AT offsec DOT com** (have your OS ID ready — support is **24/7**).
- OffSec will **not** help with or hint at exam objectives — technical problems only.

---

## 19. Results

- Official results arrive by email within **ten (10) business days** of submitting documentation (per the walkthrough, often within 2–3 days or even 24 hours).
- **Additional clarification:** if OffSec needs more info on your report, they'll email you; you must respond within **24 hours**.

---

> [!summary] Exam‑day quick reference
> - **Time:** 23h 45m practical + 24h reporting.
> - **Pass:** 70/100. 3 stand‑alones (20 each, 10/10 split) + AD set (40).
> - **Per machine:** exploit → screenshot (flag **+ IP**, interactive shell) → **submit to control panel immediately** → record for report.
> - **Shell:** interactive only (SSH/reverse/RDP) — **never** a web shell / raw RCE.
> - **Privilege:** SYSTEM/Administrator (Win) or root (Linux) for `proof.txt`.
> - **Metasploit:** ONE machine only; `msfvenom` + `multi/handler` unrestricted; no MSF pivoting.
> - **Banned:** spoofing/Responder‑LLMNR, SQLmap & autopwn, mass scanners (Nessus/OpenVAS), AI chatbots, commercial tools.
> - **Report:** PDF → `.7z` (no password, ≤200 MB), exact case‑sensitive names, verify MD5, click Submit File, use official template.
> - **Breaks:** announce `"I am taking a break"` / `"I am back"` in proctor chat.
