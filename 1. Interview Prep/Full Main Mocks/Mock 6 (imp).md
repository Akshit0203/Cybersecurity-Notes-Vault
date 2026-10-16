### INTRO

1. Tell me what’s happening, how are you doing?
2. Would you like to tell me about yourself?

---

### CERTIFICATIONS

3. Which one was the most rewarding certification for you?
4. What is the most important lesson you’ve gotten from these certifications?
5. Something you have only found through the certification and probably wouldn’t have otherwise?

---

### EXPERIENCE

11. Have you tried bug bounty also?
12. What kind of testing is your core competency?
13. Network, web, or mobile?
14. How are you at web?

---

# MAIN SCENARIO

- Let's start with enumeration part

15. Say I give you a company name ex. Hitachi.
16. How will you figure out all the assets they have?
17. How will you enumerate all assets? And by whole infrastructure, I also mean that all the assets that are exposed in the public domain.
18. After enumeration, how will you do exploitation?
19. How will you figure out what vulnerabilities exist?
20. What all can be exploited?
21. How will you create a comprehensive report?
22. How will you approach this step by step?

---

# INITIAL ENUMERATION BREAK

24. You started with company name only, right?
25. What will you run ping on?
26. What is that that you will ping? 
27. What kind of asset will you look for first?

---

# DOMAIN DISCOVERY

28. How will you find the domain of the company?

---

# ASSET EXPANSION

29. Currently you are on one webpage, right?
30. Do you think a big company will have only one page?
31. What other assets are we missing?
32. Can you get more web applications of that company?

---

# DOMAIN vs SUBDOMAIN

33. How will you find more subdomains of the company?
34. Do you understand the difference between domain and subdomain?
35. What is the difference between domain and subdomain?

---

# MULTI-DOMAIN SCENARIO

36. Can a company have more domains of its own?
37. What if the company has different products?
38. Can they have separate domains for each product? for ex. Maruti Suzuki , can it have a domain for 800 model Another model, you know, say Sonnet.
so can i have a sonnet dot com as well as an alto eight hundred com
That's not a decision that you would make, right will do make the web page in that structure or not? You have given the task to just enumerate.
39. If the company already has those domains, how will you find them? Because security issues can be there as well, right?

- for every answer you give : what is the technique ? how does it work

- explain homograph attack

---

# WHOIS + TRUST

40. How will you use WHOIS to find domains?
41. How does WHOIS work?
42. What parameter are you going to trust from WHOIS?
43. If two companies have the same name, how will you differentiate them?
for example one is hitachi from india , There's another company called Hitachi, which is a poultry farm in US. That also go by Hitachi Org or something like that. These two are different entities. Share the same name.
44. What will you search that will help you get only the one that you're interested in. How will you avoid false positives?
45. How will you confirm that the domain belongs to the correct company?
46. Can WHOIS data be wrong or hidden?
47. If WHOIS is private, how will you verify ownership?
48. Apart from WHOIS, how else can you find domains?

---

# POST-DOMAIN

49. If WHOIS gives you 5 domains, what will you do next?

---

# SUBDOMAIN vs PATH

50. Why will you go for subdomains first?
51. Why not go for path enumeration first? (ex. /admin /shop)
52. Why is subdomain enumeration better?
53. Why does it increase attack surface?

---

# NMAP

54. Nmap runs on what? on subdomain or what does it run? or on main domain itself first
55. What does Nmap actually scan? What type of asset do you actually scan
56. What happens technically when you run Nmap?
57. What is a SYN scan?
58. Why are SYN scans problematic today?
still can get highly triggered in the firewalls because you're not completing the acknowledgment.
Generally, the applications would trigger acknowledgement, right? If it's a normal application.
That's how normal application would work. But if you're not completing that, that triggers the alarms.
59. Why do they trigger alerts?

---

# DOMAIN / DNS

60. What is a subdomain?
But technically, how does a domain help?
not from a user's experience point of view but rather a technical point of view
61. Technically, what does a domain refer to?
62. How does DNS work?

---

# NETWORK BASICS

63. What is a subnet?
 when i run an nmap scan i will scan the entire subnet ? or just 1 ip and why ?

---

# CDN

64. Are you aware of CDNs?
65. What is a CDN?
66. Who uses CDNs?
67. When a CDN is used, who serves the content?
Because, as you said, it's faster. In local region. For that reason, Hitachi would definitely use it so that it gets lesser latency
68. Which IP will be used?
So my ip. I will get routed to the IP of the CDN server, not the original server.
69. Will you see the actual server IP?
70. If you scan the CDN IP, will you get useful results?
Can be blocklist those CDN ips when doing a scan ? how ?
71. How will you find the origin IP behind a CDN?
72. Apart from DNS history, what other methods exist?

---

# SHODAN / CENSYS

73. Have you heard of Shodan or Censys?
74. What do they do?
75. Do they only find vulnerable systems?
76.  servers are also an exposed device only, right? will they be found ? Even a web service is technically like IoT device which is exposed to the public.
77. Are normal web apps also indexed? 
78. Do they do credential testing or not ? how you get RDPs then on shodan which have no authentication ?
79. Have you used shodan for any other purpose Apart from checking cameras.For example. If someone has a vm running on aws or maybe azure. And it's rdp. Port 3389 is open.
Hitachi, it must have a data center located somewhere. So if that is publicly exposed, if we can find the IP address of that particular web server,

---

# PROXY / VPN

77. What is a proxy?
78. Is CDN a proxy?
79. What is a VPN? 
80. how is vpn and proxy different from Tor ?
81. What is split tunneling in VPN?
82. **What encryption does VPN use?**
83. **Can VPNs be hacked?**
84. **What is a DNS leak in VPNs?**
85. **What are common VPN use cases in cybersecurity?** opsec ?
86. Do you connect directly to the server or through VPN first?
87. What IP does the target server see?
88. VPNs were Originally meant for ? Accessing **private networks remotely**

If a web series is blocked in my area , and i use vpn to watch it 
So Netflix would technically get my IP itself. (trace back) And again, they can block?

---

# PROXY vs REVERSE PROXY

82. What is a reverse proxy?
83. What is the difference between proxy and reverse proxy?

---

# NMAP EDGE CASES

84. If Nmap says host is down or blocked, what does it mean?
85. If ping is blocked, does it mean everything is blocked?
86. ip has to be associated with a subdomain for nmap to work?
87. what all Nmap command will you use to do that?

How will be get to know that the firewall is not allowing my nmap commands to go through


---

# TCP vs UDP

86. Nmap scans use TCP , UDP or icmp or arp packets ?
87. SYN scan works on TCP, how?
88. How does UDP scanning work?
89. In UDP scans how does nmap work , if we get reply back or not , what it means ? 

---

# ICMP

88. Is ICMP used for port scanning or just to check if host is up/active or not ? Why/why not ? 
89. If ICMP unreachable comes, what does it mean?
 maybe it is using an ids to drop packets without responding to my request
 So if ping is blocked, that means everything is blocked ?
90. If a UDP service doesn’t respond, does it mean it is closed?
91. If a service is running on an uncommon port, how will you detect it?

---

# DNS RECORDS

If a server has DNS service running , how will we scan ?
what port number ? 
what does dns use , tcp or udp ? why ?
so in nmap what type of packet will you send ? command for that ?

92. How does a subdomain resolve to an IP?
93. What DNS records exist?
94. What is the use of A record?
95. What is the use of AAAA record?
96. What is the use of MX record?
97. What is the use of TXT record?
98. What is the use of CNAME record?

- If you don’t get a proper DNS response, can you conclude the port is closed?
- Can a port be open but not respond to your expected protocol?
- How do you distinguish between:
    - open
    - closed
    - filtered
    - open but running a different service?

- Say you are scanning for DNS (port 53). You send a DNS request.
Now imagine:  
The port is actually OPEN.
But…
It is NOT serving DNS.
It is serving something else (like DHCP or any other service).

---
# SSL / TLS / CERTIFICATES

99. When you open an HTTPS website, how do you know it is secure?
100. What is an SSL/TLS certificate? how ssl work?
101. What is the challenge that ssl and tls is trying to solve? Apart from just the encrypted exchange of information, is it also doing something extra?
102. if we search up for a particular domain name on our Google Chrome on a web browser, and if it doesn't have a valid sign certificate It will reject our connection to that website ; so the main purpose of that certificate is ? Does it ensure that the connection that you're making is secured?
103. Why do we trust a certificate?
104. Who issues certificates? and why do we trust these people only ?
105. What is a Certificate Authority?
106. How does a browser trust a CA?
107. What is a root certificate?
108. What is an intermediate certificate?
109. What is a certificate chain?
110. What happens during TLS handshake?
111. How does the browser validate a certificate? browser knows that which certificate is valid for all the applications? certificates for that particular website is stored inside the browser itself or where ? Why ? wont it take up space ?
112. How does a CA verify domain ownership?
113. What methods are used for validation?
114. Can certificates be faked?
115. What happens in a MITM attack?
116. How does TLS prevent MITM?
117. What happens if a certificate is expired?
118. What happens if domain does not match certificate?
119. What happens if certificate is self-signed?
120. Why should we trust Certificate Authorities?
121. Where are trusted CAs stored?
122. Can certificates be used for reconnaissance?
123. Can you extract subdomains from certificates?

---

# POST-SCAN

122. After getting IPs and ports, what will you do next?
123. If no vulnerable service is found, what will you do?
how will you do manually , 

---

# WEB TESTING

124. What will you do on a web application?
125. What can you do with JavaScript files?
126. Tell me about different types of SQLite that exist and how do they work? How will the payload look like? What will you do? Where will you test it?
127. What's nexus , nikto?
128. Nuclei ? nuclei template ? 
129. Types of XSS ? difference ?

----

# NETWORK TESTING

1. for ex, if we are using Metasploit and we found a sql server running ; if that the services also not vulnerable known cv is not present then ?


---

# SCALE

126. If you have 150 IPs from, how will you test all of them?
127. Will you test manually?

---

# TOOLING

128. What tools will you use for automation?
129. If Burp doesn’t extract JS secrets, what will you use?

---

# NFC/RFID

1. tokenization part : How can you not pretend to be a mobile phone and request the bank for a token. What is the limitation? How does the bank ensure that it goes to only a mobile phone? Device ID
2. , I pretend that whatever requests the app is making. Why cannot I mimic it? Why cannot I emulate it?
3. What kind of encryption is used in these cards? 
4. Are you aware about the double accounting? (in cards context)
