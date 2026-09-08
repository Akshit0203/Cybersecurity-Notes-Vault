# Course Introduction — Information Gathering

> Course overview, learning objectives, prerequisites, and ethical disclaimer for the eJPT Information Gathering module.
> **Instructor:** Alexis Ahmed — Senior Penetration Tester at HackerSploit & Offensive Security Instructor at INE.

---
## Course Outline

This course walks through the **information gathering** phase of a penetration test in three stages:

### 1. Introduction to Information Gathering
- What information gathering is and why it matters during a pentest.
- Understanding the critical differences between **active** and **passive** information gathering.

### 2. Passive Information Gathering
- Collecting information about a target **without directly interacting** with their systems.
- Uses **publicly available sources** — search engines (Google), online databases, OSINT tools.
- **Goal:** Learn as much as possible about the target company, individuals, or systems from public data before touching anything.

### 3. Active Information Gathering
- **Directly engaging** with the target systems to obtain more specific information.
- **Example:** After discovering an IP address during passive recon, performing a **port scan** on that IP to identify running services.
- Does **not** include exploitation — that comes after the enumeration course (next course).
- **Goal:** Get granular, system-level details that can only be obtained through direct interaction.

---
## Passive vs. Active — Key Distinction

| Aspect               | Passive                                     | Active                                         |
| --------------------- | ------------------------------------------- | ---------------------------------------------- |
| **Interaction**       | No direct contact with target               | Directly engages target systems                |
| **Sources**           | Google, public databases, OSINT             | Port scans, service probes, direct queries     |
| **Example**           | Looking up domain info on WHOIS             | Running `nmap` against a target IP             |
| **Risk of detection** | Very low                                    | Higher — target may log or detect your activity |
| **Output**            | IPs, domains, emails, org structure         | Open ports, services, versions, OS fingerprint |

> [!IMPORTANT]
> Beginners often mix up passive and active recon. Keep them **separate** — the information from each phase serves a different purpose and feeds into different stages of the pentest.

---
## Prerequisites

1. **Basic Linux familiarity**
   - Navigating the Linux file system
   - Using the Linux terminal to run commands
   - Kali Linux is the penetration testing distro used throughout the course

2. **Basic web technology knowledge**
   - Understanding of web protocols: **HTTP**, **HTTPS**
   - General familiarity with how websites and web applications work

---
## Learning Objectives

1. **Differentiate** between active and passive information gathering — understand when and why to use each.
2. **Perform passive information gathering** using various tools and publicly accessible online resources.
3. **Perform active information gathering** using tools and techniques that directly interact with target systems.

---
## ⚠️ Legal & Ethical Disclaimer

> [!CAUTION]
> This course demonstrates tools and techniques on **real-world websites and IP addresses**.
> 
> **Never** run any of these tools or techniques on systems you do not have **explicit, written authorization** to test.
> 
> As a penetration tester, you **must** have written permission from your client or employer **before** testing any systems. Without that authorization, what you are doing is **illegal**.