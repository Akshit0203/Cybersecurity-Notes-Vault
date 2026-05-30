# Practice Questions — AI Fundamentals

> TryHackMe recap quiz questions from the AI Fundamentals learning path.

---

## AI in DFIR — Legal Admissibility

**Q: What combination of factors makes ML models particularly challenging for legal admissibility in court proceedings?**

**A: Black box nature, probabilistic behavior, and lack of explainability**

Courts need evidence that is understandable, explainable, reliable, reproducible, and challengeable. ML models conflict with these requirements because:

- **Black box nature** → hard to explain how a decision was made
- **Probabilistic behaviour** → may not give the same result twice
- **Lack of explainability** → weakens expert testimony and trust

> These issues can conflict with evidentiary standards like the **Daubert Standard**.

---

## AI in Digital Forensics — Primary Purpose

**Q: What is the primary purpose of using AI in digital forensics investigations?**

**A: To process large amounts of data and identify patterns that guide investigators**

---

## PCAP Files

**Q: What is the primary purpose of network packet capture (PCAP) files in cybersecurity investigations?**

**A: To store network traffic data for analysis and forensic examination**

PCAP files capture and store network packets, allowing analysts to examine communications, identify threats, and reconstruct attack sequences during incident response.

---

## Zeek in Network Forensics

**Q: What is the primary purpose of Zeek in network forensics / security analysis?**

**A: To parse network traffic and generate structured logs**

Zeek analyses network packets and creates structured logs (`http.log`, `dns.log`, `conn.log`) for easier investigation.

---

## Ransomware Investigation — Zeek Logs

**Q: In a ransomware investigation, which Zeek log field combination is most useful for identifying data exfiltration patterns?**

**A: `host` and `uri`**

These fields show **where** data is being sent (host) and the **specific endpoints** (uri), revealing exfiltration patterns.

---

## DFIR Workflow Order

**Q: What is the correct order for DFIR investigation steps?**

| Step | Action |
| ---- | ------ |
| 1 | **Run AI classification scripts** to identify suspicious artifacts (automated heavy lifting) |
| 2 | **Validate AI findings** using human expertise and domain knowledge (filter false positives) |
| 3 | **Correlate validated findings** to reconstruct the attack timeline (connect the dots) |
| 4 | **Document conclusions** with proper chain of custody for legal proceedings (ensure admissibility) |
