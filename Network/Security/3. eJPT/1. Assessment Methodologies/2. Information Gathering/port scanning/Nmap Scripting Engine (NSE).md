Nmap default script scan will run a script scan on the services running on the target machine(ip) regardless of port
it will select the relevant scripts from its entire database of scripts

```
ls -l /usr/share/nmap/scripts 
```
default location of all scripts

```
└─# ls -l /usr/share/nmap/scripts | grep -e "http"

-rw-r--r-- 1 root root  5149 Jun 20  2024 http-affiliate-id.nse
-rw-r--r-- 1 root root  1805 Jun 20  2024 http-aspnet-debug.nse
-rw-r--r-- 1 root root  3959 Jun 20  2024 http-auth-finder.nse
-rw-r--r-- 1 root root  3187 Jun 20  2024 http-auth.nse
```
specifying a protocol or word will list all scripts of that service

```
nmap -sS -sV -sC -p- -T4 demo.ine.local 
```
"-sC" to run default script scan 

```
ls -l /usr/share/nmap/scripts | grep -e "mongodb"

nmap --script-help=mongodb-databases.nse
```
![Pasted image 20250729191814.png](attachments/Pasted%20image%2020250729191814.png)
to get information about a script

```
nmap -sS -sV --script=mongodb-info -p- -T4 demo.ine.local
```
to run a specific script


```
nmap -sS -A -p- -T4 demo.ine.local
nmap -help
man nmap
```
-A: Enable OS detection, version detection, script scanning, and traceroute


