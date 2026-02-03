# 1. Novacore Financial's Contract (Windows command line)

WIndows machine
use CMD

Question 1
What is the hostname of the system?
OPS-WKS01

```
hostname
```

---

Question 2
What is the account type assigned to alex.reid? (Administrator/Standard)
Standard

```
net user alex.reid
```

Look for:
- “Local Group Memberships”
    
- If **Administrators** is listed → Administrator
    
- Otherwise → Standard

---

Question 3
Other than the alex.reid user account and the local groups, which user account holds Full Control permissions on C:\Users\alex.reid\Documents\system_overview.txt? 
noah.jones

```
icacls "C:\Users\alex.reid\Documents\system_overview.txt"
```

```
OPS-WKS01\noah.jones:(F)
OPS-WKS01\alex.reid:(F)
BUILTIN\Administrators:(F)
NT AUTHORITY\SYSTEM:(F)
```

---

Question 4
Which local group’s intended role involves system design?
Ops-Engineering

```
net localgroup
```

“System design” aligns with **Engineering**.
(usually something like Architects / Designers / Engineers)

---

Question 5
Which local group includes both alex.reid and noah.jones as members?
Ops-Compliance

We already know from earlier:

- alex.reid belongs to:
    

`Ops-Compliance Ops-Network Users`

Now we check which of those also includes **noah.jones**.

next:
`net localgroup "Ops-Compliance" net localgroup "Ops-Network"`


From outputs:
### Ops-Compliance:

- alex.reid
    
- noah.jones
    
### Ops-Network:

- alex.reid
    
- emma.clark
    

Only **Ops-Compliance** contains **both alex.reid and noah.jones**.

---

Question 6
What is the name of the service that starts with the prefix Ops and is currently stopped on the system?
OpsAuditService

```
sc query state= all | findstr /I "Ops"
```

```
C:\Users\Administrator>sc query state= all | findstr /I "Ops" 
SERVICE_NAME: CertPropSvc 
SERVICE_NAME: OpsAuditService
```

confirm its **state** (stopped).
Run:
`sc query OpsAuditService`

--- 

Question 7
What is the name of the scheduled task configured to perform the daily operations check?
Ops_DailyAudit

Open Task Scheduler:

`taskschd.msc`

Browse Task Scheduler Library.

Look for something like:

- Daily
    
- Operations
    
- Check

---

Question 8
What is the SHA256 hash of C:\Users\alex.reid\Documents\system_overview.txt?
114c6042a07df6cd5ce5970f72819bc38dcc4503f4f8e47728286b6a886cda0f

```
certutil -hashfile "C:\Users\alex.reid\Documents\system_overview.txt" SHA256
```

---

Question 9
What is the name of the custom shared folder configured on this system?
SharedData

```
net share
```

Ignore default shares "(C$, ADMIN $)."
Whatever custom name appears = answer.

---

Question 10
What is the creation time of the shadow copy configured for drive C:? (Format: MM/DD/YYYY HH:MM AM/PM)
11/14/2025 9:57 AM

```
vssadmin list shadows
```

From output:

`creation time: 11/14/2025 9:57:32 AM`

format:
**MM/DD/YYYY HH:MM AM/PM**

So ignore seconds:
**11/14/2025 9:57 AM**

# 2. Joy Candy Factory's Contract (Linux command line)

Question 1
What is the target machine’s operating system's PRETTY_NAME?
Ubuntu 24.04.1 LTS

```
cat /etc/os-release
```

Look for:
PRETTY_NAME="..."

---

Question 2
What is the full path of the home directory assigned to the user ops.audit?
/home/ops.audit

```
getent passwd ops.audit
```

```
ubuntu@ops-linux01:~$ getent passwd ops.audit
ops.audit:x:1001:1001::/home/ops.audit:/bin/bash
```


---

Question 3
Which group is assigned as the primary group for the user ops.audit?
**ops-users**

Primary group = GID **1001**.

convert GID → group name:

run:
`getent group 1001`

Primary group
From:
`ops-users:x:1001:`

Answer:
**ops-users**

---

Question 4
Who is the owner of /home/ops.audit/documents/system_overview.txt?
ops.maint

```
ls -l /home/ops.audit/documents/system_overview.txt
```

```
ubuntu@ops-linux01:~$ sudo ls -l /home/ops.audit/documents/system_overview.txt
-rwxr-x--- 1 ops.maint ops-users 616 Jan  9 12:54 /home/ops.audit/documents/system_overview.txt
```

```
-rwxr-x--- 1 ops.maint ops-users ...
```

---

Question 5
What are the permissions set on /home/ops.audit/documents/system_overview.txt? Provide the numeric value.
750

```
stat -c "%a" /home/ops.audit/documents/system_overview.txt
```

That number (e.g. 640 / 644 / 600) = answer.

---

Question 6
Read the system_overview.txt file. How many service accounts (usernames containing svc) are listed in the authorised users file?
2

```
sudo cat /home/ops.audit/documents/system_overview.txt
```

From the file, authorised users list is at:
`/opt/joycandy/config/authorised_users.list`

Now run:
`sudo cat /opt/joycandy/config/authorised_users.list`

Then:
`sudo cat /opt/joycandy/config/authorised_users.list | grep svc | wc -l`

That number = Q6.

Service accounts (containing `svc`):
`svc.monitor svc.patch`

Count: **2**

---

Question 7
What is the name of the running process owned by ops.audit that is not attached to a terminal?
/usr/local/ops/ops-report.sh

Run:
`ps -u ops.audit -o pid,tty,cmd`

Look for:
`?`
under TTY.

Process name = answer.

```
ubuntu@ops-linux01:~$ ps -u ops.audit -o pid,tty,cmd
    PID TT       CMD
    610 ?        /bin/bash /usr/local/ops/ops-report.sh
   1279 ?        sleep 60
```

---

Question 8
Read the system_overview.txt file. What is the full target path of the symbolic link mentioned there?
/opt/joycandy/releases/1.0.0

We already saw in `system_overview.txt` that the symbolic link is:
`/opt/joycandy/live`

Now need to **resolve that symlink to its real target**.

terminal, run:
`readlink -f /opt/joycandy/live`

That will print something like:
`/some/full/path/here`

👉 Whatever full path it outputs = **Question 8 answer**.

```
ubuntu@ops-linux01:~$ readlink -f /opt/joycandy/live
/opt/joycandy/releases/1.0.0
```

---

Question 9
How many lines does /home/ops.maint/logs/auth/auth.log.1 have?
2398

```
wc -l /home/ops.maint/logs/auth/auth.log.1
```

First number = answer.

---

Question 10
Which command should be used to view the manual page for the ps command?
man ps

# 3. TryMapMe's Contract (Nmap)

Question 1
How many hosts are up in the network 192.168.8.0/24?
11

```
sudo nmap -sn 192.168.8.0/24
```

---

Question 2
Which protocol is running on the host with IP 192.168.8.10?
dns

```
sudo nmap -sS -sV -p- 192.168.8.0/24
```

---

Question 3
What is the name and version of the service running on the host that has port 8080 open?
SimpleHTTPServer 0.6 (Python 3.10.12)

---

Question 4
What is the OS version of the host 192.168.8.60? Provide the full value of the "OS details" field.
Linux 4.15 - 5.8

```
sudo nmap -O 192.168.8.60
```

---

Question 5
How many UDP ports are open on the host with IP 192.168.8.91? Use the flag --min-rate 5000 to speed up the scan.
1

```
sudo nmap -sU --min-rate 5000 192.168.8.91
```

Everything else is **closed** or **open|filtered**.

---

Question 6
How many TCP ports are open on the host with IP 192.168.8.50?
3

---

Question 7
What is the MAC address of the host with IP 192.168.8.20?
76:4D:85:6B:98:44

---

Question 8
How many well-known TCP ports are open on the host with IP 192.168.8.60?
1

8080 is NOT well-known.

---

Question 9
On which IP address is the DHCP service active?
192.168.8.90

```
sudo nmap -sU -p 67 192.168.8.0/24
```

---

Question 10
What service is running on port 161 on the host with IP 192.168.8.50?
snmp

```
sudo nmap -sU -p 161 192.168.8.50
```


# 4. AstraVault's Contract (*web application testing)

- username: pentest_user
- password: password123

The application can be accessed at http://10.xx.xx.xx/

Question 1
What is the email of an employee that can be found in the HTML source?
eg.first.last@mail.com
james.smith@astravault.com

Right at the top of HTML:
`<!-- For banking inquiries, contact james.smith@astravault.com -->`

---

Question 2
What is the API key that can be obtained from the loaded JavaScript file?
av_health_9d2f1cbe12

At the bottom of HTML, :
`<script src="/js/healthcheck.js"></script>`
So the API key is inside that JS file.

Open it in browser:
Go to:
`http://10.49.136.36/js/healthcheck.js`

---

Question 3
What two additional login portals could be found through directory enumeration? (Answer in alphabetical order: E.g., /dir1, /dir2)
/admin, /employee

```
gobuster dir -u http://10.49.136.36 -w /usr/share/wordlists/dirb/common.txt -t 40
```

the **additional login-related portals** are:
/admin 
/employee

(we ignore `/css`, `/js`, `/includes` since those aren’t login portals)

---

Question 4
Exploit the Transactions page to access Jane Smith’s transaction details. What is the description of the $1,000.00 deposit in her account?
Cheque Deposit

IDOR
http://10.49.136.36/transactions.php?id=1
Change the `id` value (try `2`, `3`, etc.) until you land on **Jane Smith**.

---

Question 5
What is the incident ID that appears in the Offers page when you inject a simple alert dialogue?
INC-2025-117384

1. Click **Offers**
    
2. input field
    
3. Inject:
    

`<script>alert(1)</script>`

---

Question 6
What code must be submitted to bypass the employee password-reset MFA?
112233

1. Open the employee portal:
    

`http://10.49.136.36/employee/`

2. Click **Forgot Password** (or Password Reset).
    
3. When asked for email, enter:
    

`james.smith@astravault.com`

4. Submit.
    

You’ll now see a page asking for a **verification / MFA code**.

First try **blank**:

- Leave the MFA field empty
    
- Click Submit
    

If that fails, try:

`000000`

If that fails, try:

`123456`

One of these will succeed and the application will display a **code on screen**

Invalid MFA code. ### DEBUG CODE - REMOVE AFTER DEPLOYMENT: 112233 ###

112233

---

Question 7
What diagnostic token is found in CHANGELOG.md v0.7.3 after exploiting command-injection in File Search?

Step 1 — Go to employee reset again

Open:

`http://10.49.136.36/employee/`

Click **Forgot Password**.

Enter:

`james.smith@astravault.com`

Submit.

Step 2 — MFA prompt

When asked for MFA code, enter:

`112233`

(This is the debug code you already found.)

Step 3 — Set a new password

It will now let you set a **new password** for James Smith.

Set something simple, for example:

`Password123!`

(remember it)
Password has been reset for james.smith@astravault.com. New password: 2bc03844

Step 4 — Login as employee

Now go to:

`http://10.49.136.36/employee/`

Login with:

- **Username / Email:** james.smith@astravault.com
    
- **Password:** (whatever you just set)

In the **File to read** box, enter **exactly** this:

`offers.txt; cat CHANGELOG.md`



---

Question 8
What is the service token that is retrieved from the database after exploiting Customer Search?

Question 9
What message is displayed in the administrator portal upon gaining superuser access?

eg.WRN-1122: Message.

Question 10
What is the global token that can be retrieved from the database?


# 5. BrightCart Retail's Contract (SOC)

🎯 Objective
Investigate a security incident at BrightCart e-commerce platform. You'll analyze alerts, examine HTTP logs, decode malicious payloads, implement firewall rules, and identify vulnerabilities that led to the breach.

Investigation Workflow
1
Dashboard - Identify the Threat
Review the charts and statistics to understand the HTTP traffic patterns.

2
Alerts - Find the Critical Alert
Navigate to the Alerts tab. Search and identify the High severity alert. Click on the alert row to expand details. Use the copy button next to the Source IP to copy the attacker's IP address.

3
Events - Analyze HTTP Logs
Go to the Events tab and click "View HTTP Events". Paste the attacker IP in the filter or use the "Malicious IP" quick filter button. Examine the suspicious requests, especially POST requests to admin endpoints.

4
Payloads - Decode the Attack
Switch to the Payloads tab. Find the malicious payload from the attacker IP. Decode the command the attacker tried to execute.

5
Firewall - Block the Attacker
Navigate to the Firewall tab. Click "Add Rule" to add a blocking rule for the attacker IP. Review the scan results to verify the block is effective.

6
Vuln Scan - Identify Root Cause
Go to the Vuln Scan tab and click "Start Scan". Review the vulnerability report. Click on the High severity vulnerability to understand how the attacker gained initial access and what needs to be patched.

---

Question 1
What is the name of the alert rule that originally detected suspicious activity against BCRT-WEB-01?
Suspicious Web Shell Upload

go to alerts tab

![](./attachments/image.png)

---

Question 2
What is the source IP address of the suspicious activity?
158.94.210.88

---

Question 3
What is the requested URI path used in the suspicious HTTP request made by the attacker?
/admin/upload.php

1. Click **Events** tab
    
2. Click **View HTTP Events**
    
3. Use the filter (or “Malicious IP”) and paste:
    

`158.94.210.88`

4. Look for the **suspicious POST request** (to `/admin/upload.php`).

---

Question 4
What is the decoded value of the suspicious request contained in the cmd parameter?
nmap -sV 127.0.0.1

Click the **Payloads** tab.

There you’ll see payload entries for source IP:

`158.94.210.88`

Find the one tied to `/admin/upload.php`. It will show something like:

- `cmd=...` (URL/Base64 encoded)

The encoded value:

`bm1hcCAtc1YgMTI3LjAuMC4x`

is Base64. Decoded, it becomes:

`nmap -sV 127.0.0.1`

---

Question 5
You decide to block the attacker’s IP address. What is the state of port 80/tcp after the firewall rule is applied?
filtered

- Click the **Firewall** tab.
    
- Add a rule to **block IP `158.94.210.88`** (they usually provide an “Add Rule” button).
    
- After applying, the console will show a **port scan / test result**.

- **Rule ID:** R5 (or leave auto)
    
- **Name:** Block_Attacker
    
- **Description:** Block malicious IP
    
- **Source IP:** `158.94.210.88`
    
- **Target IP:** BCRT-WEB01 (or `10.10.50.20`)
    
- **Port:** `80`
    
- **Action:** Block
    
- **Status:** Enabled

From the message:

> **Port 80/tcp is now filtered**

---

Question 6
A vulnerability scan report for BCRT-WEB01 has been provided to you. What is the CVE number of the highest severity vulnerability affecting the web server? (Answer format: CVE-XXXX-XXXXX)
CVE-2021-41773

Click the **Vuln Scan** tab.
Then:

1. Click **Start Scan** (if not already started).
    
2. Open the **High severity vulnerability**.



---

Question 7
Based on the vulnerability description, what type of vulnerability would this be categorised as? (Answer format: Answer1 and Answer2 vulnerability)
Path Traversal and Remote Code Execution vulnerability

---

Question 8
According to the scan report, what is the primary remediation action recommended for this vulnerability?
Upgrade Apache HTTP Server to a patched version

---

Question 9
Given that directory listing is enabled in multiple locations on the server, which year was the associated vulnerability published?
2022

---

Question 10
Which directories were confirmed to expose directory listings due to the vulnerability? (Answer in alphabetic order: /dir1/, /dir2/, /dir3/)

click **Directory Listing Enabled**

From the scan:

- `/images/`
    
- `/uploads/`
    
- `/backup/`
    

Alphabetical order:

👉 **/backup/, /images/, /uploads/**

# 6. Rute Bay University's Contract (*network + web testing)

Question 1
What is the name of the FTP server? eg.filezilla
vsftpd

```
sudo nmap -sS -sV -p 1-10000 10.48.132.234
```

From this line:

`21/tcp   open  ftp   vsftpd 3.0.3`

FTP server name
👉 **vsftpd**

---

Question 2
What is the time returned by the daytime service at TCP port number 13? Format: HH:MM:SS.
eg.17:08:29
13:38:37

```
nc 10.48.132.234 13
```

---

Question 3
What is the numeric version number of the listening MongoDB service?
eg.3.9.1
5.0.8

⚠️ **MongoDB (27017/tcp) is NOT in this scan range.**
MongoDB usually runs on **27017**, which is **outside 1–10000**.

```
sudo nmap -sV -p 27017 10.48.132.234
```

---

Question 4

There is a hidden login page used by faculty instructors for authentication. For example, http://10.48.132.234:3000/path. What is the path?
eg.faculty
admin

```
gobuster dir -u http://10.48.132.234:3000 -w /usr/share/wordlists/dirb/common.txt -t 40
```

---

Question 5

There is a hidden login page used by IT personnel as a restricted entry point. For example, http://10.48.132.234:3000/path. What is the path?
eg.it_admin
`debug`

Among what we found, the restricted IT-style entry point is:
`/debug`

This is the separate technical/admin access page.

---

Question 6
At the main page accessible via http://10.48.132.234:3000, students can log in to check their courses. What is the password of the student student009?
eg.pass1234



---

Question 7

What is the grade of student057 in the course QM400?

eg.95

---

Question 8
At http://10.48.132.234:3000/files, there is an encrypted archive that contains an invoice details-b.txt. What is the total amount due in USD? The answer should be 3 digits.
eg.425

Now unzip:
`unzip details-b.zip`

(use the cracked password) - From Q10

Then:

`cat details-b.txt`

You’ll see:

`Total Amount Due: NNN USD`

👉 That **3-digit number = Q8**

---

Question 9
It seems that an IT personnel has left valuable information at http://10.48.132.234:3000/notes. What is the password for the user peter?
eg.pass1234

freedom

👉 First, visit:

`http://10.48.132.234:3000/notes`

this `/notes` page is exactly what Q9 is referring to 👍  
got **real `/etc/passwd` + `/etc/shadow` entries**, which means the intended path is:

👉 **offline password cracking**
```
peter:$6$nSNbeDclzgtYkw5r$Uxu.SkEn4d8vi4P/JpZPPSu7zFSPt39WCBdoEk419uuYLEcuvd8RExeqMibfOhRPoIp4we9vr6bW3Gj/xi2fp0
```

That `$6$` means **SHA-512 crypt**.

 1️⃣ Save Peter’s hash

`nano peter.hash`

Paste ONLY this line:
`peter:$6$nSNbeDclzgtYkw5r$Uxu.SkEn4d8vi4P/JpZPPSu7zFSPt39WCBdoEk419uuYLEcuvd8RExeqMibfOhRPoIp4we9vr6bW3Gj/xi2fp0`

Crack with john

`john peter.hash --wordlist=/usr/share/wordlists/rockyou.txt`

Then:

`john --show peter.hash`

👉 Whatever appears after `peter:` is your **Q9 answer**.

---

Question 10
At http://10.48.132.234:3000/files, there is an encrypted Zip archive, details-m.zip. What is the decryption password?
eg.pass1234
1q2w3e4r5t


🔓 Crack the ZIP password (details-b.zip / details-m.zip)

You already have:

`details-b.zip details-m.zip`

We’ll use `zip2john`.

1️⃣ Generate hash from the ZIP
`zip2john details-b.zip > zip.hash`
Verify:
`cat zip.hash`

2️⃣ Crack with rockyou

`john zip.hash --wordlist=/usr/share/wordlists/rockyou.txt`

Then show result:

`john --show zip.hash`

You’ll get something like:

`details-b.zip:XXXXX`

👉 That `XXXXX` is:

- **Q10 (ZIP decryption password)**

1q2w3e4r5t

# 7. TryPayMe Solutions's Contract


