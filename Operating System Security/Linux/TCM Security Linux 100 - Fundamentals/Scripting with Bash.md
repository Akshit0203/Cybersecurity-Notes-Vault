# Scripting with Bash — IP Sweep Script

## The Script

A simple Bash IP sweeper that pings every IP from `.1` to `.254` in a `/24` subnet and prints the ones that respond.

```bash
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
```

### Usage

```bash
./ipsweep.sh 192.168.1
```

It checks `192.168.1.1` through `192.168.1.254` and outputs only the IPs that respond.

### Example Output

```
192.168.1.1
192.168.1.5
192.168.1.10
192.168.1.20
192.168.1.254
```

---

## Line-by-Line Breakdown

### Shebang

```bash
#!/bin/bash
```

Tells Linux to execute the script using **Bash**.

### Input Validation

```bash
if [ "$1" == "" ]
```

`$1` = the **first argument** supplied to the script.

```bash
./ipsweep.sh 192.168.1    →    $1 = 192.168.1
./ipsweep.sh               →    $1 = "" (empty — show usage)
```

If empty, print usage instructions:

```
$ ./ipsweep.sh
You forgot an IP address!
Syntax: ./ipsweep.sh 192.168.1
```

### The Loop

```bash
for ip in `seq 1 254`; do
```

`seq 1 254` produces `1, 2, 3, ..., 254`. Each number is assigned to variable `ip`.

`$1.$ip` combines them:

```
$1 = 192.168.1,  ip = 10  →  192.168.1.10
```

### The Pipeline

```bash
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
```

Each stage:

| Stage | Command | What it does |
|---|---|---|
| **1. Ping** | `ping -c 1 192.168.1.10` | Send **one** ICMP ping |
| **2. Filter** | `grep "64 bytes"` | Keep only lines with a successful response |
| **3. Extract** | `cut -d " " -f 4` | Split by spaces, take field 4 (`192.168.1.10:`) |
| **4. Clean** | `tr -d ":"` | Remove trailing colon → `192.168.1.10` |
| **5. Background** | `&` | Run in background (concurrent pings = faster sweep) |

Visual flow:

```
         ping
           ↓
    Is there a response?
           ↓
    grep "64 bytes"
           ↓
    extract field #4
           ↓
       remove :
           ↓
       print IP
```

### How `cut` splits the line

```
64 | bytes | from | 192.168.1.10: | icmp_seq=1 | ttl=64 ...
1      2       3          4
```

`-d " "` = delimiter is space, `-f 4` = field number 4.

---

## Saving Ping Output to a File

```bash
ping 192.168.60.138 -c 1 > ip.txt
```

```
┌──(kali㉿kali)-[~]
└─$ cat ip.txt       
PING 192.168.60.138 (192.168.60.138) 56(84) bytes of data.
64 bytes from 192.168.60.138: icmp_seq=1 ttl=64 time=0.484 ms

--- 192.168.60.138 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.484/0.484/0.484/0.000 ms
```

---

## The Whole Script in Plain English

```
Take the subnet prefix from the user
        ↓
If no prefix was supplied → Show usage
        ↓
Otherwise → Generate numbers 1–254
        ↓
Append each number to the prefix
        ↓
Ping each resulting IP once
        ↓
If "64 bytes" is found → Extract and print the IP
```

---

## Important Limitation

This is an **ICMP host discovery script**, not a full network scanner. If a machine is alive but **blocks ICMP/ping**, this script won't detect it.

---

## Key Bash Concepts Reference

| Code | Meaning |
|---|---|
| `$1` | First command-line argument |
| `if` | Conditional |
| `for` | Loop |
| `seq 1 254` | Generate numbers 1–254 |
| `ping -c 1` | Send one ping |
| `\|` | Pipe output to next command |
| `grep` | Filter text |
| `cut` | Extract fields |
| `tr -d` | Delete characters |
| `&` | Run in background |
