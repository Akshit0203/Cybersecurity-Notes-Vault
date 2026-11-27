
for my oscp interview answer what is the diff bw pivoting and lateral movement

---

**"Walk me through your methodology for a black-box web app start to finish."**

I almost said "I run Nmap first" and stopped myself. They don't want to hear about tools. They want to hear that you have a process. Passive recon before you touch anything( crtsh, Shodan, Wayback Machine, Google dorks). Build your target profile first. Then enumerate. Then test manually before you even think about automation. Methodology over tools, every time.

**"What's the first thing you do after getting a shell on a Windows box?"**

Not "open Meterpreter." Situational awareness. whoami /all. systeminfo. netstat -ano. tasklist. You need to know your privilege level, the network around you, and what security tooling is running before you breathe wrong. This answer alone apparently filters out a huge chunk of candidates.

**"Walk me through Kerberoasting. Why does it actually work?"**

Don't just say "you request tickets and crack them offline." They want the WHY — any authenticated domain user can request a TGS for any SPN. The ticket is encrypted with the service account's password hash. Weak password = cracked offline with hashcat, zero lockout risk. The mechanism matters more than the tool name.

**"What are Metasploit's limitations?"**

This is a trap and most people walk straight into it. "It gets caught by AV" is not the answer they want. The real answer: default payloads are heavily signatured, staged payloads need network callbacks that firewalls often block, and running modules you don't understand is a genuine liability on a real engagement. Know the edges of your tools.

**The thing that actually got me the offer (or at least what I think):**

I brought a redacted lab report. Not a cert. Not a list of HTB machines. An actual professionally written pentest report from a lab environment with CVSS scores, reproduction steps, and executive summary. Nobody else did that probably because they looked hella shocked.

--------


