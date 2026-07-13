
# FunboxEasyEnum

## About this lab

Employ enumeration and web enumeration techniques to identify vulnerabilities. Engage in bypassing file uploads, along with implementing privilege escalation strategies. Additionally, harness the abuse of sudo permissions to enhance your access. This lab is designed to capitalize on your skills in vulnerability exploitation.

## Learning Objectives

**After completion of this lab, learners will be able to:**

- Perform service discovery and hidden directory enumeration using tools like nmap and gobuster.
- Exploit a file upload vulnerability in a custom web shell to upload a PHP reverse shell.
- Enumerate system users and successfully guess a valid password to log in via SSH.
- Leverage sudo permissions on the mysql binary to execute root-level commands and escalate privileges.
- Validate root access and retrieve the final flag to complete the lab.

## Lab Description

In this lab, access is gained by exploiting a file upload vulnerability in a web shell, leading to remote code execution. Privilege escalation is performed through password guessing and abusing misconfigured sudo permissions on the mysql binary to execute commands as root. HINTS: Enum without sense, costs you too many time. Use "Daisys best friend" for information gathering. Visit "Karla at home". John and Hydra loves only rockyou.txt Enum/reduce the users to brute force with or brute force the rest of your life. This works better with VirtualBox rather than VMware


---------------

WALKTHROUGH

frist well run nmap scans on the target mahcine ip 

geegranl nmap command like 

```
nmap -p- 192.168.186.132
```
tells **Nmap** to scan **all TCP ports** on the host `192.168.186.132`.
will take up a lop of time 

so o increase the speed of nmap scan , 
either we can incearse the threads or we can increase the packets speed
## 1. Increase parallelism ("threads")

Nmap doesn't expose a simple "threads" option, but it uses **parallel probe groups** internally.

Increasing parallelism means Nmap can scan more ports or hosts simultaneously.

Related options:

```
--min-parallelism
--max-parallelism
```

Conceptually:

```
Without parallelism:

Port 22  ───────► Wait
Port 80  ───────► Wait
Port 443 ───────► Wait

With parallelism:

22 ─┐
80 ─┼──► Sent together
443─┘
```

More parallelism usually means a faster scan, provided the network and target can handle it.

---

## 2. Increase packet transmission rate

You can also make Nmap send probes more aggressively.

Common options include:

```
-T4
-T5
```

or more advanced controls such as:

```
--min-rate
--max-rate
```

Conceptually:

```
Normal

Packet
     1 second
Packet
     1 second
Packet

Fast

Packet Packet Packet Packet Packet
```

Higher rates reduce scan time but can:

- Increase packet loss
- Cause inaccurate results
- Trigger intrusion detection systems (IDS/IPS)
- Overload slower targets

------------

so now well run the command : 

```bash
nmap 192.168.186.132 --min-rate 10000
```

```bash
└─$ nmap 192.168.186.132 --min-rate 10000
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-12 15:43 -0400
Nmap scan report for 192.168.186.132
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.51 seconds
```

now we can run the ocmmand 

```bash
nmap 192.168.186.132 --min-rate 10000 -sV
```

to see what all versions are runnign on it 

```bash
└─$ nmap 192.168.186.132 --min-rate 10000 -sV
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-12 15:46 -0400
Nmap scan report for 192.168.186.132
Host is up (0.12s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.77 seconds
```

so noweve found that which all services are runnign in which all ports

now we can also run nmap scripts ont he tsame tager t machien like 

```
nmap 192.168.186.132 --min-rate 10000 -sV -sC
```

or we can even write it shorter like 

```
nmap 192.168.186.132 --min-rate 10000 -sVC
```

```bash
└─$ nmap 192.168.186.132 --min-rate 10000 -sVC
Starting Nmap 7.99 ( https://nmap.org ) at 2026-07-12 15:49 -0400
Nmap scan report for 192.168.186.132
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9c:52:32:5b:8b:f6:38:c7:7f:a1:b7:04:85:49:54:f3 (RSA)
|   256 d6:13:56:06:15:36:24:ad:65:5e:7a:a1:8c:e5:64:f4 (ECDSA)
|_  256 1b:a9:f3:5a:d0:51:83:18:3a:23:dd:c4:a9:be:59:f0 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 72.34 seconds
```


it has foudn ssh keys which are of virtually no use to us 

then we can see that on port 80 there is http apache server runnign tso well copy th eip address 
`192.168.186.132` and paste it in our browser

```
http://192.168.232.132/
```

![](attachments/Pasted%20image%2020260713201618.png)

we can see that is no form and nothing 
this is justa default page on which there is not much onfiguration

we can rght lcick on the we b page and check the source code of the page as well

![](attachments/Pasted%20image%2020260713223242.png)

![](attachments/Pasted%20image%2020260713223558.png)


try to read the comments of the source code aswell 
al lot of times in comments hidden links migt be stored
now fromt he source code , we can only figure out one thing that the websote is running inside `/var/www/html/index.html` inside ubuntu using apapche 

we fromt he nmap results also have the apache version i.e `2.4.29 `


![](attachments/Pasted%20image%2020260713223822.png)


other information in the osurce code is not useful to us 




now we can try directory brute forcing since the link is just an ip address 
it is possible that tehre might be another wbsite hidden behind it 
We need to find out if there are hidden directories or files tucked behind this default page

now well use dirbuster to do directory brute ofrcing

To search for hidden folders, we can use directory brute-forcing tools [12]. The first tool is `dirb` [12]. You run it by entering `dirb <target-URL>` [12]. This tool will guess directories by appending words from a default wordlist located at `/usr/share/wordlists/dirb/common.txt` [12]. 

so well run run command 

```
dirb http://192.168.232.132/
```

However, `dirb` is extremely slow [12].

 Instead, we can use a much faster tool called **Gobuster** [12]. Gobuster is highly efficient, though it may not be installed by default on every basic Linux machine; you might have to install it [12]. To see its directory brute-forcing options, type `gobuster dir -h` [12].

```
└─$ gobuster
NAME:
   gobuster - the tool you love

USAGE:
   gobuster command [command options]

VERSION:
   3.8.2

AUTHORS:
   Christian Mehlmauer (@firefart)
   OJ Reeves (@TheColonial)

COMMANDS:
   dir      Uses directory/file enumeration mode
   vhost    Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)
   dns      Uses DNS subdomain enumeration mode
   fuzz     Uses fuzzing mode. Replaces the keyword FUZZ in the URL, Headers and the request body
   tftp     Uses TFTP enumeration mode
   s3       Uses aws bucket enumeration mode
   gcs      Uses gcs bucket enumeration mode
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --help, -h     show help
   --version, -v  print the version
```

we can see from its manual the ocmmand it reuires to run 

`dir` 

now we can even run manual for `dir` commandby 

```
gobuster dir -h
```

```
└─$ gobuster dir -h
NAME:
   gobuster dir - Uses directory/file enumeration mode

USAGE:
   gobuster dir [command options] [arguments...]

OPTIONS:
   --url value, -u value                                    The target URL
   --cookies value, -c value                                Cookies to use for the requests
   --username value, -U value                               Username for Basic Auth
   --password value, -P value                               Password for Basic Auth
   --follow-redirect, -r                                    Follow redirects (default: false)
   --headers value, -H value [ --headers value, -H value ]  Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
   --no-canonicalize-headers, --nch                         Do not canonicalize HTTP header names. If set header names are sent as is (default: false)
   --method value, -m value                                 the password to the p12 file (default: "GET")
   --useragent value, -a value                              Set the User-Agent string (default: "gobuster/3.8.2")
   --random-agent, --rua                                    Use a random User-Agent string (default: false)
   --proxy value                                            Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
   --timeout value, --to value                              HTTP Timeout (default: 10s)
   --no-tls-validation, -k                                  Skip TLS certificate verification (default: false)
   --retry                                                  Should retry on request timeout (default: false)
   --retry-attempts value, --ra value                       Times to retry on request timeout (default: 3)
   --client-cert-pem value, --ccp value                     public key in PEM format for optional TLS client certificates]
   --client-cert-pem-key value, --ccpk value                private key in PEM format for optional TLS client certificates (this key needs to have no password)
   --client-cert-p12 value, --ccp12 value                   a p12 file to use for options TLS client certificates
   --client-cert-p12-password value, --ccp12p value         the password to the p12 file
   --tls-renegotiation                                      Enable TLS renegotiation (default: false)
   --interface value, --iface value                         specify network interface to use. Can't be used with local-ip
   --local-ip value                                         specify local ip of network interface to use. Can't be used with interface
   --wordlist value, -w value                               Path to the wordlist. Set to - to use STDIN.
   --delay value, -d value                                  Time each thread waits between requests (e.g. 1500ms) (default: 0s)
   --threads value, -t value                                Number of concurrent threads (default: 10)
   --wordlist-offset value, --wo value                      Resume from a given position in the wordlist (default: 0)
   --output value, -o value                                 Output file to write results to (defaults to stdout)
   --quiet, -q                                              Don't print the banner and other noise (default: false)
   --no-progress, --np                                      Don't display progress (default: false)
   --no-error, --ne                                         Don't display errors (default: false)
   --pattern value, -p value                                File containing replacement patterns
   --discover-pattern value, --pd value                     File containing replacement patterns applied to successful guesses
   --no-color, --nc                                         Disable color output (default: false)
   --debug                                                  enable debug output (default: false)
   --status-codes value, -s value                           Positive status codes (will be overwritten with status-codes-blacklist if set). Can also handle ranges like 200,300-400,404
   --status-codes-blacklist value, -b value                 Negative status codes (will override status-codes if set). Can also handle ranges like 200,300-400,404. (default: "404")
   --extensions value, -x value                             File extension(s) to search for
   --extensions-file value, -X value                        Read file extension(s) to search from the file
   --expanded, -e                                           Expanded mode, print full URLs (default: false)
   --no-status, -n                                          Don't print status codes (default: false)
   --hide-length, --hl                                      Hide the length of the body in the output (default: false)
   --add-slash, -f                                          Append / to each request (default: false)
   --discover-backup, --db                                  Upon finding a file search for backup files by appending multiple backup extensions (default: false)
   --exclude-length value, --xl value                       exclude the following content lengths (completely ignores the status). You can separate multiple lengths by comma and it also supports ranges like 203-206
   --force                                                  Continue even if the prechecks fail. Please only use this if you know what you are doing, it can lead to unexpected results. (default: false)
   --help, -h                                               show help
```


we can see it says 

```
OPTIONS:
   --url value, -u value                                    The target URL
```

and 

```
--wordlist value, -w value                               Path to the wordlist. Set to - to use STDIN.
```



well also use the `-x` option to specify the extensions like `txt` and `php`
so that we get those results also 

we can choose fromt he vaaibale options 

```
└─$ ls /usr/share/wordlists/dirb                                           
big.txt     euskera.txt            mutations_common.txt  spanish.txt
catala.txt  extensions_common.txt  others                stress
common.txt  indexes.txt            small.txt             vulns
```

so our cmmand will become 
we'll usse `big.txt` here


```
gobuster dir -u http://192.168.232.132/ -w /usr/share/wordlists/dirb/big.txt -x php,txt
```

```
┌──(kali㉿kali)-[~/Desktop]
└─$ gobuster dir -u http://192.168.232.132/ -w /usr/share/wordlists/dirb/big.txt -x php,txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.232.132/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.htpasswd.php        (Status: 403) [Size: 280]
.htpasswd            (Status: 403) [Size: 280]
.htaccess.php        (Status: 403) [Size: 280]
.htaccess.txt        (Status: 403) [Size: 280]
.htaccess            (Status: 403) [Size: 280]
.htpasswd.txt        (Status: 403) [Size: 280]
javascript           (Status: 301) [Size: 323] [--> http://192.168.232.132/javascript/]
mini.php             (Status: 200) [Size: 3828]
phpmyadmin           (Status: 301) [Size: 323] [--> http://192.168.232.132/phpmyadmin/]
robots.txt           (Status: 200) [Size: 21]
robots.txt           (Status: 200) [Size: 21]
server-status        (Status: 403) [Size: 280]
Progress: 61407 / 61407 (100.00%)
===============================================================
Finished
===============================================================
```

