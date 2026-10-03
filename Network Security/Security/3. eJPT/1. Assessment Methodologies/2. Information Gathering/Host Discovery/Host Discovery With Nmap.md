## using ping

![Pasted image 20250726072757.png](attachments/Pasted%20image%2020250726072757.png)

if ping takes a lot of time, add 
```
ping -c 5 demo.ine.local
```
this will send only 5 ping icmp packets to target thus will take less time (can set any number after -c)

## using ICMP 

```
nmap -sn <target ip>
```
sends icmp packets in network to identify which hosts are online 
```
ifconfig
10.0.1.0 subnet mask 255.255.0.0
```
then scan for nmap 10.0.1.0/24 (faster) or 10.0.1.0/16

if you want to scan targets from a text file 
```
vim targets.txt
nmap -sn -iL targets.txt
```


## using SYN (recommended)

if you want to send a SYN packet to port 80 (by default - changable) on target
```
nmap -sn -PS 192.168.253.129
nmap -sn -PS22 192.168.253.129 #send on port 22
nmap -sn -PS1-1000 192.168.253.129 #scans on all ports from 1 to 1000
nmap -sn -PS3389 192.168.253.129 #send on RDP port
nmap -sn -PS80,3389,445 192.168.253.129 #set individual ports
```
here , the -PS will override the -sn(ping send)

SYN scan is better and stealthier as it doesnt has to go through the SYN , SYN-ACK , ACK procedure

so -sn options tells nmap to not perform a port scan 
and just do host discovery

## using ACK
### not recommended

by default it will send an ACK flag to target Ip on port 80

if the host is not online/ip is not active , it will not respond to the request
if it is active then it will return an RST packet

```
nmap -sn -PA 10.4.23.227
```

## using ICMP echo requests 

```
nmap -sn -PE 10.4.23.227 --send-ip # if we are on ethernet
nmap -sn -PE 10.4.23.227 # if we not are on ethernet
```

windows firewall blocks icmp ping requests

Here’s the **core difference** in one line:

> 🔸 `-sn` = **Tells Nmap to skip port scan**  
> 🔸 `-PE` = **Tells Nmap to use ICMP Echo as a host discovery method**

---

### ✅ Why both exist:

They serve **different purposes**:

|Option|Purpose|
|---|---|
|`-sn`|Controls **what Nmap does** → “Don’t scan ports”|
|`-PE`|Controls **how Nmap discovers hosts** → “Use ICMP Echo”|

---

### ✅ Why you need both:

If you want Nmap to:

- **Only check if hosts are alive**, and
    
- **Only use ICMP pings** (no TCP/ACK/SYN, etc.)
    

Then you combine them:

`nmap -sn -PE 192.168.1.0/24`

---

### 🔚 Summary:

- `-sn`: disables port scanning.
    
- `-PE`: uses ICMP Echo to detect live hosts.
    
- You **combine** them to do an ICMP-only host discovery with no port scan.  
    That's why both are needed — different jobs.















