
Security control is what you place between the system and people who are trying to get into the system

Conceptually it is important to have as many layers of security as you practically can

![Pasted image 20251022013541.png](attachments/Pasted%20image%2020251022013541.png)

![Pasted image 20251022013634.png](attachments/Pasted%20image%2020251022013634.png)

[Defense in depth](https://www.cloudflare.com/learning/security/glossary/what-is-defense-in-depth/) (layered security) is a principle and strategy in cloud security that involves implementing multiple layers of security controls and measures to protect cloud resources from various threats and attacks.

- Robust and resilient posture
    
- Mitigate the risk of a single security control
    

Public Network (Perimeter)

- Public **firewall**, DDos Prevention, IDS/IPS, etc
    

Local Network

- nACL, Device **Hardening**, Monitoring, etc
    

Operating System (Endpoint)

- Hardening, **Patching**, Endpoint Protection, **Monitoring**, etc
    

Service (Application)

- **Hardening**, Patching, Monitoring, Vuln Scanning, Testing, etc
    

Workload

- Authentication, Authorization, Auditing, Data access control, Monitoring, **Encryption** (in transit & at rest), MFA, etc