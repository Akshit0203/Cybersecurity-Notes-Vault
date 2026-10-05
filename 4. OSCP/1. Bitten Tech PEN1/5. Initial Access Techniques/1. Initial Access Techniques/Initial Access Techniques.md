# Initial Access Techniques

> [!info] Module Context
> This is the **Modern Exploitation** bonus section of the System Hacking module. It covers the complete initial access methodology used in modern penetration testing (OSCP-style), bridging information gathering/scanning/enumeration with exploitation.

---

## What is Initial Access?

- Also known as **modern exploitation** or **initial foothold**
- The **first stage** in any cyber attack chain
- Goal: establish a foothold on a target system over a network link
- Typically yields **low-privilege access** (e.g., a service account like `www-data`) — not root/admin
- Followed by **privilege escalation** → **lateral movement** → **maintaining presence** → **completing the mission**

> [!tip] Attack Chain Flow (TryHackMe Model)
> **Initial Recon** → identify software, ports, versions, enumerate fully, search for exploits
> ↓
> **Initial Compromise** → find a vulnerability (web app CVE, SQLi, OWASP Top 10, etc.)
> ↓
> **Establish Foothold** → get RCE / shell access (web shell, reverse shell, etc.)
> ↓
> **Privilege Escalation** → escalate from service account to root/admin
> ↓
> **Lateral Movement** → pivot to other systems on the network (especially via AD)

### Key Concepts

- When you gain initial access externally, you typically land on an **internet-facing / publicly exposed system**
- From there, you discover network interfaces, find other systems, perform internal scanning, and pivot deeper
- **Example — WannaCry analogy:** WannaCry spread via SMB, but it first had to compromise one system (via phishing) before it could propagate to others on the network
- After landing on a target, you can perform **local enumeration**: inspect source code, check network interfaces, find locally open ports, discover connected systems

---

## Initial Access Techniques

### 1. Phishing (Social Engineering)

- Sending **deceptive emails/messages** to trick individuals into revealing sensitive information (usernames, passwords)
- Extends beyond email: **SMS (smishing)**, **phone calls (vishing)**, physical notes, impersonation
- Most commonly successful because **humans are the weakest link** in the security chain

**How it works in practice:**
- Send a targeted email to a company employee pretending to be their manager
- Example template: *"Your appraisal cycle is about to start. I've created your performance review — click this link to view it."*
- The link opens a **fake portal** mimicking the company's actual review system
- Victim enters their AD/domain credentials → **credential harvesting**
- Other templates: festival gift links (*"It's Diwali, accept your gift"*), urgency scenarios (family emergencies, fund requests)
- **Timing matters:** sending during actual performance review cycles (e.g., December) dramatically increases success

### 2. Password Guessing & Brute Force

- Trying different combinations of usernames and passwords until finding valid credentials
- Targets: login portals, FTP, SSH, or any service requiring authentication

**Online vs Offline attacks:**

| Aspect | Online | Offline |
|---|---|---|
| **Method** | Send login requests directly to the service | Crack captured hashes locally |
| **Speed** | Slow (network-bound) | **Extremely fast** |
| **Risk** | Account lockout possible | No lockout risk |
| **Example** | Brute-forcing FTP login | Cracking a hash from a database dump |

**Tools:**
- **Hydra** — online brute-forcing
- **Medusa** — online brute-forcing
- **John the Ripper** — offline hash cracking
- **Hashcat** — offline hash cracking (GPU-accelerated)

> [!tip] Defense Reminder
> Use strong passwords: long passphrases with a mix of lowercase, uppercase, special characters, and numbers.

### 3. Public Software Exploits

- Exploiting **unpatched or outdated software** with known vulnerabilities (CVEs)
- Targets: third-party/vendor software, open-source components, libraries
- Examples: old versions of **WordPress**, **vsFTPd**, **OpenSSH**, **Drupal**, etc.

**Methodology:**
1. Extract the **version** of the running service (banner grabbing, enumeration)
2. Search for known CVEs on **Exploit-DB**, **GitHub**, or via **Google Dorking**
3. Download the exploit code, run it, and gain access

**Real-world example — EternalBlue (MS17-010):**
- Exploited SMB vulnerability in Windows 7 via Metasploit

> [!warning] Remediation
> Keep all software updated. If no fix exists for a particular exploit, apply firewalls, disable the service, or implement temporary workarounds.

### 4. Client-Side Attacks

- Exploit vulnerabilities in **software running on the user's device** (not attacking the server directly)
- Triggered when a user **visits a website** or **opens a document**
- Targets: web browsers, browser plugins, Microsoft Office

**Microsoft Office Macros example:**
- Create a Word document with an embedded **VBA macro** (Visual Basic for Applications)
- Macros are designed to automate repetitive tasks but can also **execute shell commands**
- Save as `.docm` format (macro-enabled document) and send to the target
- If the victim opens and enables macros → your code executes → reverse shell

> [!note] Modern Defenses
> Microsoft has **disabled macros by default**. A prompt appears: *"Do you want to view the content or run the script?"* — adding a verification step. Non-security-aware users may still click through the warning.

**Limitations:**
- Not always reliable — depends on victim interaction and security awareness
- Even partial success can yield valuable data: usernames, passwords, or sensitive info from the victim's local system
- **Outdated browser plugins** can also be exploited

### 5. Web Application Attacks

- **Most common attack vectors** for initial access
- Web apps are primary targets because:
  - Businesses earn revenue through them → deployed quickly
  - Security is often deprioritized over speed-to-market
  - Even if no other services (RDP, FTP, SSH, LDAP, etc.) are exposed, web is almost always running

**Common web vulnerabilities for RCE:**
- **SQL Injection (SQLi)** — high impact
- **Local File Inclusion (LFI)** — high impact
- **XXE (XML External Entity)** — can lead to RCE
- **SSRF (Server-Side Request Forgery)** — can lead to RCE
- **Path Traversal** — high impact
- **XSS (Cross-Site Scripting)** — low impact (client-side, no direct shell)
- **CSRF** — lower impact
- **CORS misconfiguration**
- **IDOR (Insecure Direct Object References)**

> [!note]
> Not all web vulnerabilities give you a shell directly. XSS is client-side and won't grant RCE. But SQLi, LFI, XXE, and SSRF can potentially lead to direct RCE.

### 6. Other Techniques (Less Common)

| Technique | Limitation |
|---|---|
| **Wireless Exploitation** | Requires physical proximity |
| **IoT & Embedded Devices** | Not widely targeted yet |
| **Physical Media (USB)** | Requires physical presence |
| **Physical Intrusion** | Highly conditional |

These are less common in standard penetration tests and modern exams like OSCP.

---

## Related Modules

- **Privilege Escalation** — covered separately (differs for Windows vs Linux)
- **Lateral Movement & Maintaining Presence** — covered in the Active Directory (AD) course (most common in Windows/AD environments)
