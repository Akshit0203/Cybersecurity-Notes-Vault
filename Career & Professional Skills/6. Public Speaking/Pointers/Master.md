# Master — Session Content Guide

> **Topics to include:** Learnings, CTF, Interview tab

---

## General Career Advice

- Forget another cert; your new religion is GitHub. No recruiter in Bangalore or Hyderabad is going to be wowed by a Google cert, but they will 100% click a link to a repo where you've documented how you popped a box from VulnHub in your own home lab. The current meta isn't collecting certs — it's creating content. Spend your weekends grinding TryHackMe or Blue Team Labs Online, and for every box you finish, write a detailed post on a simple blog or a GitHub README.md. This portfolio is your golden ticket.
- Start networking on LinkedIn by referencing your projects, not your degree.
- Find your local Null Community or OWASP chapter — that's where the real internship opportunities are, not on some random job portal. End of the day, you need to show you're the kind of person who learns this stuff for fun on a Saturday night.

---

## Don't Put Borders in Cybersecurity

- Don't think in terms of "Red Team vs Pentester vs Blue Team" — these rigid labels don't matter.
- Never draw borders in cybersecurity like "I only want to do SOC" or "I only want to do Red Team."
- There are many domains — Cloud, IoT, AI/ML Security — explore all of them.

---

## Practical Tips

- Apply on LinkedIn jobs for internships — check their job descriptions to understand what's trending.
- Make notes for each topic — recommend Obsidian, show examples.
- Do things that are legal. You might see random Instagram ads claiming "I hacked Android 16 this way" or "I spoofed calls" — these things are interesting but there's no career future in them. Go the formal way — focus on titles like Web Application Security, Cloud Security, Mobile Application Security — because jobs come from these.
- Always think: **"Is the work I am doing scalable?"** For example, if tomorrow I want to start my own cybersecurity company or get a great job, will this work help me or not?

---

## Understand Things from the Ground Up

- Try to understand things from the ground up.
    - Example: If given a domain name (e.g., Hitachi), explain how you would track all the assets.
- Also try to understand how all the tools work from the ground up:
    - Example: How does Nmap check ports? TCP vs UDP? What message do you get if a port is closed in both? Does it use ARP or ICMP?
- Example — Digital Forensics:
    - How do tools like FTK Imager and Autopsy work?
    - After formatting, how does 2 GB of data go to 0 GB?
    - Finding patterns in data.

---

## Scaling Bug Bounty — GitHub Repo Analysis

Who has found bugs and got bounties by analysing GitHub repos?
Now the question is: **How do you scale it for real-world testing?**

If you have 2,000 GitHub repos, how will you analyse them?

1. Check HTTP status codes — write a Python script
2. Analyse for secrets using tools — use Gitleaks or TruffleHog (faster)
3. Keep only verified keys
4. Handle IP rate limiting — make a new script, add delay
5. Check which repos have employee email commits
6. Remove test keys
7. Remove duplicates

---

## Be a Builder, Not Just a Coder

In big companies and product-based companies, during appraisals they will ask:

**"Is this person a builder or not?"**

- Not just a coder
- Not just a developer
- But a **builder**

---

## AI in Cybersecurity — Focus on the Right Thing

- Instead of focusing on making your own AI agents that do AI pentesting, SOC automation, etc. — you will never be able to make agents at the level that companies are pouring billions of dollars into.
- So focus on **using AI** only after understanding it.
- If you focus on **building AI tools**, you will waste time and will get replaced.
- Focus instead on **building secure systems by design** — this won't be replaced in the near future.

---

## Resilient Systems in Cybersecurity

A **resilient system** is not just:

- ❌ "Secure" (no vulnerabilities)

It is:

- ✅ Able to **withstand attacks**
- ✅ Able to **detect and respond**
- ✅ Able to **recover quickly**
- ✅ Still functional even if something is compromised

### Example 1: Web Application

- **Not resilient:** One vulnerability → full system compromise
- **Resilient:**
    - WAF blocks malicious requests
    - App has input validation
    - Backend is isolated
    - Logs trigger alerts
    - → Attack happens, but system survives

### Example 2: Cloud Infrastructure

- **Not resilient:** One leaked credential → attacker gets everything
- **Resilient:**
    - IAM least privilege
    - Network segmentation
    - Monitoring + alerts
    - Auto-rotation of keys
    - → Breach attempt ≠ full compromise

---

## Courses

1. Red Team Leaders (free courses)
2. TryHackMe, HackTheBox, PicoCTF
3. [TCM Security Academy](https://tcm-sec.com/academy/) (Paid)
4. [500+ Free TryHackMe Rooms — GitHub](https://github.com/Hunterdii/tryhackme-free-rooms) (Free rooms list)
5. [PortSwigger Web Security Learning Paths](https://portswigger.net/web-security/learning-paths) (Free)

---

## Interviews

- **Bad answer:** "I use Nmap to scan ports."
- **Better answer:** "Port scanning works by initiating TCP connections to determine which services are exposed. Tools like Nmap optimize this using SYN scans and packet crafting."

---

## Projects

- [BittenTech YouTube Channel — Project Videos](https://www.youtube.com/@BittenTech/videos)

---

## Action Items

- Start with the Burp Suite TryHackMe module
- Make a mega note covering all phases from recon to access

---

## Future of Cybersecurity — Topics to Cover

- AI Security
- Cloud Security
- Threat Modelling
- Secure Code Review

---

## Modern Languages & AI

- Modern languages to learn: **Python, Go, Rust**
- AI — Learn it daily now. Otherwise, you will be left out.
- "Teach ML to security engineers now." — Big Basket CEO
- Traditional pentesting tools like Burp Suite, Kali Linux, Nexus, Nessus will be outdated/dead — if tools like Mythos make it.
- Learn **prompt engineering** as well.

---

## Presentation Logistics

- Add a QR code for LinkedIn and GitHub profile
- Add a QR code for anonymous feedback and rating
