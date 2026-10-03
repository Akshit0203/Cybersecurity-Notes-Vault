## IP: 
___
## Nmap TCP

```bash

```
## Nmap UDP

```bash

```

___
# Initial Access
### Ports Open:

### 80
#### Nikto:

```bash

```
#### Wappalyzer:

```

```


#### Source Code:
#### Directories Fuzzing 

**Cheatsheet:**

```
===DIRECTORY FUZZING:
gobuster dir -u $URL -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt -k -t 30 --random-agent --exclude-length 6765

===DIRECTORY FUZZING:
ffuf -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v

===AUTHENTICATED FUZZING DIRECTORIES:
wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt --hc 404 -d "SESSIONID=value" "$URL"

===FUZZ Directories:
wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-large-directories.txt --hc 404 "$URL"

Also try: /opt/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt
/opt/SecLists/Discovery/Web-Content/common.txt
```

**Result:**

```bash
```
#### Files Fuzzing (add extensions)

**Cheatsheet:**

```
===AUTHENTICATED FILE FUZZING:
wfuzz -c -z file,/opt/SecLists/Discovery/Web-Content/raft-medium-files.txt --hc 404 -d "SESSIONID=value" "$URL"


===FILE FUZZING:
gobuster dir -u $URL -w /opt/SecLists/Discovery/Web-Content/raft-medium-files.txt -k -t 30 -x php,html,htm --random-agent --exclude-length 6765
```

**Result:**

```bash
```

**Fuzz Request:**
`ffuf -request ~/boxes/aoc/brute -request-proto http -w numbers`
# Privilege Escalation

### Linux:

Penelope: 
`script https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh`
Leave pspy64 running while reviewing linpeas output
Penelope: `run upload_privesc_scripts`

Look for "Unknown SUID binary!" @ winpeas output

On .git directory, need to check commits `git log`

Look for white files on crontab section @ winpeas output

Hunting for Passwords:

```
# navigate to common folders where we normally find interesting files, such as /var/www, /tmp, /opt, /home, etc. and then execute the following command:

grep --color=auto -rnw -iIe "PASSW\|PASSWD\|PASSWORD\|PWD\|DB_" --color=always 2>/dev/null
```

whoami; hostname; ifconfig; cat /home/user/local.txt
whoami; hostname; ifconfig; cat /root/proof.txt