
```
nmap demo.ine.local
```
if we don't specify any option , the default nmap command will first do host discovery and port scan using SYN 
this will result in ping packet drop if there is a firewall present

```
nmap -Pn demo.ine.local #sent to 1000 most common ports
nmap -Pn -p 80 demo.ine.local #if you want to scan only 1 port
nmap -Pn -p- 80 demo.ine.local #if you want to scan all 65,535 TCP ports
nmap -Pn -T5 -p- 80 demo.ine.local #increase speed
```
we use this when we want to scan windows devices 
the "-pn" option will skip ping scans and directly do port scans
thus avoiding ping packet drop by firewall

![Pasted image 20250726191447.png](attachments/Pasted%20image%2020250726191447.png)
if it says 'filtered' - it means firewall is blocking request
if it says 'closed' - no firewall is present

```
nmap -Pn -F demo.ine.local
```
the '-F' option performs a fast port scan , scanning only the top 100 ports

```
nmap -Pn -sS -F demo.ine.local
```
we write -Pn if we are a privileged user
if we are not a privileged user , we have to additionally use '-sS' option for a SYN scan

```
nmap -Pn -sT <target ip> #TCP connect scan : SYN,ACK,SYN-ACK
```
not recommended as it creates a lot of logs on network of 3-way handshakes
this is the type of scan nmap will run by default if you are not a privileged user

```
nmap -sU <target ip>
nmap -Pn -sU -p53,137,138,139 <target ip> #to skin host discovery
```
does a UDP port scan
we can also specify specific ports here



