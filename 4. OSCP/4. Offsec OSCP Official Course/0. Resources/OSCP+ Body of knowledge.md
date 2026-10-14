# Only These Topics are In the Scope of Exam

|   |   |   |
|---|---|---|
|**Learning Module**|**Learning Units**|**Learning Objectives**|
|**Report Writing for Penetration Testers**|Understanding Note-Taking|- Review the deliverables for penetration testing engagements<br>- Understand the importance of note portability<br>- Identify the general structure of pentesting documentation<br>- Choose the right note-taking tool<br>- Understand the importance of taking screenshots<br>- Use tools to take screenshots|
||Writing Effective Technical Penetration Testing Reports|- Identify the purpose of a technical report<br>- Understand how to specifically tailor content<br>- Construct an Executive Summary<br>- Account for specific test environment considerations<br>- Create a technical summary<br>- Describe technical findings and recommendations<br>- Recognize when to use appendices, resources, and references|
|**Information Gathering**|The Penetration Testing Lifecycle|- Understand the stages of a Penetration Test<br>- Learn the role of Information Gathering inside each stage<br>- Understand the differences between Active and Passive Information Gathering|
||Passive Information Gathering|- Understand the two different Passive Information Gathering approaches<br>- Learn about Open Source Intelligence (OSINT)<br>- Understand Web Server and DNS passive information gathering|
||Active Information Gathering|- Learn to perform Netcat and Netmap port scanning<br>- Conduct DNS, SMB, SMTP, and SNMP Enumeration<br>- Understand Living off the Land techniques|
|**Vulnerability Scanning**|Vulnerability Scanning Theory|- Gain a basic understanding of the Vulnerability Scanning process<br>- Learn about the different types of Vulnerability Scans<br>- Understand the considerations of a Vulnerability Scan|
||Vulnerability Scanning with Nessus|- Install Nessus<br>- Understand the different Nessus components<br>- Configure and perform a vulnerability scan<br>- Understand and work with the results of a vulnerability scan with Nessus<br>- Provide credentials to perform an authenticated vulnerability scan<br>- Gain a basic understanding of Nessus plugins|
||Vulnerability Scanning with Nmap|- Understand the basics of the Nmap Scripting Engine (NSE)<br>- Perform a lightweight Vulnerability Scan with Nmap<br>- Work with custom NSE scripts|
|**Introduction to Web Applications**|Web Application Assessment Methodology|- Understand web application security testing requirements<br>- Learn different types and methodologies of web application testing<br>- Learn about the OWASP Top10 and most common web vulnerabilities|
||Web Application Assessment Tools|- Perform common enumeration techniques on web applications<br>- Understand Web Proxies theory<br>- Learn how Burp Suite proxy works for web application testing|
||Web Application Enumeration|- Learn how to debug Web Application source code<br>- Understand how to enumerate and inspect Headers, Cookies, and Source Code<br>- Learn how to conduct API testing methodologies|
||Cross-Site Scripting (XSS)|- Understand Cross-Site Scripting vulnerability types<br>- Exploit basic Cross-Site Scripting<br>- Perform Privilege Escalation via Cross-Site Scripting|
|**Common Web Application Attacks**|Directory Traversal|- Understand absolute and relative paths<br>- Learn how to exploit directory traversal vulnerabilities<br>- Use encoding for special characters|
||File Inclusion Vulnerabilities|- Learn the difference between File Inclusion and Directory Traversal<br>- vulnerabilities<br>- Gain an understanding of File Inclusion vulnerabilities<br>- Understand how to leverage Local File Inclusion (LFI) to obtain code<br>- Execution<br>- Explore PHP wrapper usage<br>- Learn how to perform Remote File Inclusion (RFI) attacks|
||File Upload Vulnerabilities|- Understand File Upload vulnerabilities<br>- Learn how to identify File Upload vulnerabilities<br>- Explore different vectors to exploit File Upload vulnerabilities|
||Command Injection|- Learn about command injection in web applications<br>- Use operating system commands for OS command injection<br>- Understand how to leverage command injection to gain system access|
|**SQL Injection Attacks**|SQL Theory and Database Types|- Refresh SQL theory fundamentals<br>- Learn different DB types<br>- Understand different SQL syntax|
||Manual SQL Exploitation|- Manually identify SQL injection vulnerabilities<br>- Understand UNION SQLi payloads<br>- Learn about Error SQLi payloads<br>- Understand Blind SQLi payloads|
||Manual and Automated Code Execution|- Exploit MSSQL Databases with xp_cmdshell<br>- Automate SQL Injection with SQLmap|
|**Client-Side Attacks**|Target Reconnaissance|- Gather information to prepare client-side attacks<br>- Leverage client fingerprinting to obtain information|
||Exploiting Microsoft Office|- Understand variations of Microsoft Office client-side attacks<br>- Install Microsoft Office<br>- Leverage Microsoft Word Macros|
||Abusing Windows Library Files|- Prepare an attack with Windows library files<br>- Leverage Windows shortcuts to obtain code execution|
|**Locating Public Exploits**|Getting Started|- Understand the risk of executing untrusted exploits<br>- Understand the importance of analyzing the exploit code before execution|
||Online Exploit Resources|- Access multiple online exploit resources<br>- Differentiate between various online exploit resources<br>- Understand the risks between online exploit resources<br>- Use Google search operators to discover public exploits|
||Offline Exploit Resources|- Access Multiple Exploit Frameworks<br>- Use SearchSploit<br>- Use Nmap NSE Scripts|
||Exploiting a Target|- Follow a basic penetration test workflow to enumerate a target system<br>- Completely exploit a machine that is vulnerable to public exploits<br>- Discover appropriate exploits for a target system<br>- Execute a public exploit to gain a limited shell on a target host|
|**Fixing Exploits**|Fixing Memory Corruption Exploits|- Understand high-level buffer overflow theory<br>- Cross-compile binaries<br>- Modify and update memory corruption exploits|
||Fixing Web Exploits|- Fix web application exploits<br>- Troubleshoot common web application exploit issues|
|**Antivirus Evasion**|Antivirus Evasion Software Key Components and Operations|- Recognize known vs unknown threats<br>- Understand AV key components<br>- Understand AV detection engines|
||AV Evasion in Practice|- Understand antivirus evasion testing best practices<br>- Manually evade AV solutions<br>- Leverage automated tools for AV evasion|
|**Password Attacks**|Attacking Network Services Logins|- Attack SSH and RDP logins<br>- Attack HTTP POST login forms|
||Password Cracking Fundamentals|- Understand the fundamentals of password cracking<br>- Mutate wordlists<br>- Explain the basic password cracking methodology<br>- Attack password manager key files<br>- Attack the passphrase of SSH private keys|
||Working with Password Hashes|- Obtain and crack NTLM hashes<br>- Pass NTLM hashes<br>- Obtain and crack Net-NTLMv2 hashes<br>- Relay Net-NTLMv2 hashes|
|**Windows Privilege Escalation**|Enumerating Windows|- Understand Windows privileges and access control mechanisms<br>- Obtain situational awareness<br>- Search for sensitive information on Windows systems<br>- Find sensitive information generated by PowerShell<br>- Become familiar with automated enumeration tools|
||Leveraging Windows Services|- Hijack service binaries<br>- Hijack service DLLs<br>- Abuse Unquoted service paths|
||Abusing Other Windows Components|- Leverage Scheduled Tasks to elevate our privileges<br>- Understand the different types of exploits leading to privilege<br>- escalation<br>- Abuse privileges to execute code as privileged user accounts|
|**Linux Privilege Escalation**|Enumerating Linux|- Understand files and users privileges on Linux<br>- Perform manual enumeration<br>- Conduct automated enumeration|
||Exposed Confidential Information|- Understand user history files<br>- Inspect user trails for credential harvesting<br>- Inspect system trails for credential harvesting|
||Insecure File Permissions|- Abuse insecure cron jobs to escalate privileges<br>- Abuse insecure file permissions to escalate privileges|
||Insecure System Components|- Abuse SUID programs and capabilities for privilege escalation<br>- Circumvent special sudo permissions to escalate privileges<br>- Enumerate the system's kernel for known vulnerabilities, then abuse them for privilege escalation|
|**Port Redirection and SSH Tunneling**|Port Forwarding with *NIX Tools|- Learn about port forwarding<br>- Understand why and when to use port forwarding<br>- Use Socat for port forwarding|
||SSH Tunneling|- Learn about SSH tunneling<br>- Understand how to perform SSH local port forwarding<br>- Understand how to perform SSH dynamic port forwarding<br>- Understand how to perform SSH remote port forwarding<br>- Understand how to perform SSH remote dynamic port forwarding|
||Port Forwarding with Windows Tools|- Understand port forwarding and tunneling with ssh.exe on Windows<br>- Understand port forwarding and tunneling with Plink<br>- Understand port forwarding with Netsh|
|**Advanced Tunneling**|Tunneling Through Deep Packet Inspection|- Learn about HTTP tunneling<br>- Understand how to perform HTTP tunneling with Chisel<br>- Learn about DNS tunneling<br>- Understand how to perform DNS tunneling with dnscat|
|**The Metasploit Framework**|Getting Familiar with Metasploit|- Setup and navigate Metasploit<br>- Use auxiliary modules<br>- Leverage exploit modules|
||Using Metasploit Payloads|- Understand the differences between staged and non-staged payloads<br>- Explore the Meterpreter payload<br>- Create executable payloads|
||Performing Post-Exploitation with Metasploit|- Use core Meterpreter post-exploitation features<br>- Use post-exploitation modules<br>- Perform pivoting with Metasploit|
||Automating Metasploit|- Create resource scripts<br>- Use resource scripts in Metasploit|
|**Active Directory Introduction and Enumeration**|Active Directory Manual Enumeration|- Enumerate Active Directory using legacy Windows applications<br>- Use PowerShell and .NET to perform additional AD enumeration|
||Manual Enumeration Expanding our Repertoire|- Enumerate Operating Systems Permissions and logged on users<br>- Enumerate Through Service Principal Names<br>- Enumerate Object Permissions<br>- Explore Domain Shares|
||Active Directory Automated Enumeration|- Collect domain data using SharpHound<br>- Analyze domain data using BloodHound|
|**Attacking Active Directory Authentication**|Understanding Active Directory Authentication|- Understand NTLM Authentication<br>- Understand Kerberos Authentication<br>- Become familiar with cached AD Credentials|
||Performing Attacks on Active Directory Authentication|- Use password attacks to obtain valid user credentials<br>- Abuse enabled user account options<br>- Abuse the Kerberos SPN authentication mechanism<br>- Forge service tickets<br>- Impersonate a domain controller to retrieve any domain user credentials|
|**Lateral Movement in Active Directory**|Active Directory Lateral Movement Techniques|- Understand WMI, WinRS, and WinRM lateral movement techniques<br>- Abuse PsExec for lateral movement<br>- Learn about Pass The Hash and Overpass The Hash as lateral movement techniques<br>- Misuse DCOM to move laterally|
||Active Directory Persistence|- Understand the general purpose of persistence techniques<br>- Leverage golden tickets as a persistence attack<br>- Learn about shadow copies and how can they be abused for persistence|
|**Assembling the Pieces**|Enumerating the Public Network|- Enumerate machines on a public network<br>- Obtain useful information to utilize for later attacks|
||Attacking WEBSRV1|- Utilize vulnerabilities in WordPress Plugins<br>- Crack the passphrase of a SSH private key<br>- Elevate privileges using sudo commands<br>- Leverage developer artifacts to obtain sensitive information|
||Gaining Access to the Internal Network|- Validate domain credentials from a nondomain-joined machine<br>- Perform phishing to get access to the internal network|
||Enumerating the Internal Network|- Gain situational awareness in a network<br>- Enumerate hosts, services, and sessions in a target network<br>- Identify attack vectors in a target network|
||Attacking the Web Application on INTERNALSRV1|- Perform Kerberoasting<br>- Abuse a WordPress Plugin function for a Relay attack|
||Gaining Access to the Domain Controller|- Gather information to prepare client-side attacks<br>- Leverage client fingerprinting to obtain information|

