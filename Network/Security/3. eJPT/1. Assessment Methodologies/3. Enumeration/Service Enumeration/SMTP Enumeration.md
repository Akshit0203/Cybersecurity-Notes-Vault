![Pasted image 20250919224636.png](attachments/Pasted%20image%2020250919224636.png)


```
└─# service postgresql start
└─# msfconsole    
msf6 > workspace -a SMTP_ENUM
msf6 > setg RHOSTS demo.ine.local
msf6 > search type:auxiliary name:smtp

#WILL GIVE VERSION OF SMTP SERVER
msf6 > use auxiliary/scanner/smtp/smtp_version
msf6 auxiliary(scanner/smtp/smtp_version) > show options 

# WILL GIVE USERS LIST
msf6 auxiliary(scanner/smtp/smtp_version) > search type:auxiliary name:smtp
msf6 auxiliary(scanner/smtp/smtp_version) > use auxiliary/scanner/smtp/smtp_enum 
msf6 auxiliary(scanner/smtp/smtp_enum) > show options 
msf6 auxiliary(scanner/smtp/smtp_enum) > info

```


SMTP server name and banner.
**Answer:**
```
Server: Postfix
Banner: openmailbox.xyz ESMTP Postfix: Welcome to our mail server.
```
**Command:**
```
nmap -sV -script banner demo.ine.local
```
![Content Image](https://assets.ine.com/lab/learningpath/49a93cd264d434fe6e21440d21281b0626dcd35f8c9838d76fc4d4372950fc99.jpg)



