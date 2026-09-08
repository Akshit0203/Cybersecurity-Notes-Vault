## Firewall Detection & IDS Evasion

sA' or ACK scan tells if a port is filtered or not 
tells if firewall is present or not

```
└─# nmap -Pn -sA -p445,3389 demo.ine.local
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-07-30 19:52 IST
Nmap scan report for demo.ine.local (10.5.16.206)
Host is up (0.0022s latency).
PORT     STATE      SERVICE
445/tcp  unfiltered microsoft-ds
3389/tcp unfiltered ms-wbt-server
Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
```

unfiltered here shows that the firewall is not active

```
nmap -Pn -sS -sV -p80,445,3389 -f demo.ine.local
```

"-f" option fragments the packets
![Pasted image 20250731000611.png](attachments/Pasted%20image%2020250731000611.png)

MTU : Maximum transmitted unit
minimum 8 bytes
```
nmap -Pn -sS -sV -p80,445,3389 -f --mtu 8 demo.ine.local
```

![Pasted image 20250731001437.png](attachments/Pasted%20image%2020250731001437.png)


## use of decoy IPs

after -D , put gateway IP 
to spoof that traffic from that IP address
```
└─# ifconfig
eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.10.36.7  netmask 255.255.255.0  broadcast 10.10.36.255
        ether 02:42:0a:0a:24:07  txqueuelen 0  (Ethernet)
        RX packets 894  bytes 153540 (149.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1110  bytes 149931 (146.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
here , we use 10.10.36.7
and change the last digit to .1 to make it gateway ip i.e 10.10.36.1

```
nmap -Pn -sS -sV -p445,3389 -f --data-length 200 -D 10.10.36.1,10.10.36.2 <target ip>
```
![Pasted image 20250731002349.png](attachments/Pasted%20image%2020250731002349.png)

all SYN packets are being sent from the decoy IP 

## Spoof custom port

```
nmap -Pn -sS -sV -p445,3389 -f --data-length 200 -g 53 -D 10.10.36.1,10.10.36.2 <target ip>
```
![Pasted image 20250731002829.png](attachments/Pasted%20image%2020250731002829.png)
in this packet , the source port is 53


## Optimizing Nmap Scans

to slow down or speed up the scan
1. when dealing with an IDS , slowing down will reduce the amount of packets being sent and make network activity look less suspicious
2. if sending a lot of packets at once , may cause un-intended denial of service and may cause the routers or switches to crash

### Scan speed

Options which take <time> are in seconds, or append 'ms' (milliseconds), s' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g 30m).

-T<0-5>: Set timing template (higher is faster)
-T0 (paranoid)
-T1 (sneaky)
-T2 (polite)
-T3 (normal)
-T4 (aggresive)
-T5 (insane)

### host timeout

--host-timeout <time>: Give up on target after this long
```
└─# nmap -sS -sV -F --host-timeout 5s demo.ine.local

Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-08-02 17:56 IST
Nmap scan report for demo.ine.local (10.5.20.61)
Host is up (0.0025s latency).
*Skipping host demo.ine.local (10.5.20.61) due to host timeout*
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.27 seconds
```
### Scan delay 

--scan-delay/--max-scan-delay <time>: Adjust delay between probes

```
nmap -sS -sV -F --scan-delay 15s demo.ine.local
```
it will send packets after every 15 seconds to remain stealthy
![Pasted image 20250802180443.png](attachments/Pasted%20image%2020250802180443.png)


## nmap output format

'oN' - store in normal format , as shown on terminal
```
nmap -Pn -sS -F -T4 demo.ine.local -oN nmap_normal.txt
```



'-oX' - stores in XML format - conversion format , can later import results into metasploit 
```
nmap -Pn -sS -F -T4 demo.ine.local -oX nmap_xml.xml
```
![Pasted image 20250802204502.png](attachments/Pasted%20image%2020250802204502.png)

![Pasted image 20250802205053.png](attachments/Pasted%20image%2020250802205053.png)
![Pasted image 20250802205031.png](attachments/Pasted%20image%2020250802205031.png)
![Pasted image 20250802205258.png](attachments/Pasted%20image%2020250802205258.png)
![Pasted image 20250802205348.png](attachments/Pasted%20image%2020250802205348.png)

now we can run nmap from within metasploit
![Pasted image 20250802205609.png](attachments/Pasted%20image%2020250802205609.png)
this will update the database

![Pasted image 20250802205628.png](attachments/Pasted%20image%2020250802205628.png)
os name got updated

![Pasted image 20250802205644.png](attachments/Pasted%20image%2020250802205644.png)
service info also got updated

![Pasted image 20250802205748.png](attachments/Pasted%20image%2020250802205748.png)
our other workspace will remain empty

'-oS'- saves output in a "script kiddie" (stylized) format.



'-oG' - saves output in a greppable format
```
nmap -Pn -sS -F -T4 demo.ine.local -oG nmap_grep.txt
```
![Pasted image 20250802211104.png](attachments/Pasted%20image%2020250802211104.png)



'-oA' - Output in the three major formats at once (oN,oX,oG)


'-v' Increase verbosity level (use -vv or more for greater effect)


'--reason' Display the reason a port is in a particular state



