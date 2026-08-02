## Definition of System

Where do the banks store your cards, or where are your emails stored? The answer - on a system: a physical server, a virtual machine, or a cloud platform like Microsoft 365. Protecting such systems is crucial: if the attackers breach one user's mailbox via phishing, they compromise a single mailbox, but if they breach a mail server, they now control all thousands of mailboxes. Each system type can have a different value for threat actors, for example:

|Breached System|Attack Value|
|---|---|
|A personal laptop of a school student|Steal Steam profile and add the PC to a botnet|
|A laptop of the bank's senior IT administrator|Get access to the internal banking systems|
|A mail server of a criminal law company|Dump all mailboxes and blackmail the victim|
|A server at the heart of an industrial network|Encrypt the whole network with ransomware|
|A government website management panel|Damage the website content ([defacement](https://en.wikipedia.org/wiki/Website_defacement) / activism)|

## Attacks on Systems

### Human-Led Attacks

It's no surprise that system users are often those who start the attack: By inserting a malicious USB found on a street, downloading malware from pirated resources, or simply reusing a weak password everywhere. [81%](https://deepstrike.io/blog/password-statistics-2025) of breaches involve stolen or breached passwords - [check out](https://haveibeenpwned.com/Passwords) your passwords too!

![Two examples of how human-led attacks start: by using a weak "tryhackme" password seen in data breaches, and inserting a RubberDucky - a USB that runs malware commands.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1753218281339.svg)

### Vulnerabilities

Every piece of software can have security flaws. In 2024, [over 40,000](https://cyberpress.org/over-40000-cves-published-in-2024/) software vulnerabilities were published and [more than 300](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) were actively exploited in major attacks. Moreover, IT administrators often increase the risks by setting weak passwords and allowing unrestricted access to their systems.

![A screenshot from Shodan showing 100,000 Internet-exposed Windows XP / 2008 machines in 2025, and a chart showing 325 new critical vulnerabilities since 2024.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1753218271259.svg)

### Supply Chain

Your PC is home to hundreds of apps, including web browsers, messengers, development, and entertainment software. Every app depends on thousands of libraries. If threat actors manage to breach one of the apps or libraries and push an update to all its users, all of them will be compromised. This technique is called a supply chain attack. The most famous examples are the [SolarWinds](https://attack.mitre.org/campaigns/C0024/#:~:text=Victims%20of%20this%20campaign%20included%20government) and [3CX](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise) breaches which affected thousands of companies.

**Emerging Threat of Supply Chain**

It is hard to protect from supply chain attacks since you can't always control all the software present on your laptops, servers, and web apps. Even TryHackMe once [fell victim](https://tryhackme.com/room/supplychainattacks) to a supply chain in Lottie Player, a library used for room animations. As a SOC analyst, you must be ready for such scenarios and know how to respond!

## Misconfigurations

On the other hand, a misconfiguration isn't a bug in the software but a mistake in how the system was set up, often by the IT team. These errors happen frequently, usually to make things simpler, like using "1111" instead of typing a long password every time. Let's take a look at some real-world examples.

- How ["123456" password](https://www.bleepingcomputer.com/news/security/123456-password-exposed-chats-for-64-million-mcdonalds-job-chatbot-applications/) exposed chats for 64 million McDonald's job applications
- How a [misconfigured AWS cloud](https://www.bleepingcomputer.com/news/security/capital-one-data-breach-affects-106-million-people-suspect-arrested/#:~:text=intrusion%20occurred%20through%20a%20misconfigured%20web%20application%20firewall) resulted in a breach of 106 million bank customers
- How improperly configured [smart fridges](https://www.sectigo.com/resource-library/when-refrigerators-attack-how-cyber-criminals-infect-appliances-and-how-manufacturers-can-stop-them) are silently used in full-scale botnet attacks

Another common scenario is when the IT department unknowingly introduces new flaws into secure systems. Below is a simple example of how a critical database can be breached because of the insecure configuration:

![Pasted image 20251119192422.png](attachments/Pasted%20image%2020251119192422.png)

### Responding to Misconfigurations

Misconfigurations do not require a software update - just a better setup. As a SOC analyst, you'll often spot them only after threat actors exploit them. However, in smaller companies, you might also be responsible for a more proactive response, for example:

- **Penetration Testing**: Hire ethical "hackers" who simulate an attack and report on discovered security flaws
- **Vulnerability Scans**: Periodically run tools that can detect default passwords or outdated software
- **Configuration Audits**: Manually review the systems to match best practices like [CIS benchmarks](https://www.cisecurity.org/cis-benchmarks)

## Practice

Attackers don't see "human hacking" and "system hacking" as separate, so you should apply equal effort into protecting both humans and systems, combining **Mitigation** and **Detection**:

![Three threats aim to breach the company: the first is mitigated by an applied software patch, the second by an antivirus solution, and the remaining one is detected and stopped by the SOC analysts.](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1752599036221.svg)

Unlike humans, you can't train the system to spot the attack. However, you can train your IT department to configure the systems and explain how to avoid simple mistakes. Below are the most common mitigation measures to protect your systems:

|Mitigation|Description|
|---|---|
|**Patch Management**|A process of tracking and patching the vulnerable systems significantly reduces the chance of a successful attack|
|**Training for IT**|If your IT knows the risks of misconfigurations, they are less likely to leave the systems unprotected|
|**Network Protection**|The system is much harder to breach if access to it is restricted to trusted people or IP addresses|
|**Antivirus Protection**|Same as with attacks on humans, a good antivirus can stop or at least detect many different attacks|
