
# Exam Proofs

The valid way to provide the contents of the proof files is in an interactive shell on the target machine with the `type` or `cat` command from **their original location**.

**Obtaining the contents of the proof files in any other way will result in zero points for the target machine; this includes any type of web-based shell.**

YOU NEED TO HAVE A INTERACTIVE SHELL 
EX, SSH ; reverse shell
SHELL IS WHERE WE CAN INTERACT


NOT A NON-INTERACTIVE SHELL 
EX. WEBSHELL
![446](4.%20OSCP/Exam%20Day/14.%20Preparing%20for%20OSCP%201/1.%20OSCP%20Exam%20Guide/Attachments/Pasted%20image%2020261016212649.png)
ex . even os command injection (RCE) 
![448](4.%20OSCP/Exam%20Day/14.%20Preparing%20for%20OSCP%201/1.%20OSCP%20Exam%20Guide/Attachments/Pasted%20image%2020261016212837.png)
even this is not a shell 


# Control Panel Submission

The exam control panel contains a section available to submit your proof files. The contents of the local.txt and proof.txt files obtained from your exam machines _must be submitted in the control panel before your exam has ended._

![](4.%20OSCP/Exam%20Day/14.%20Preparing%20for%20OSCP%201/1.%20OSCP%20Exam%20Guide/Attachments/Pasted%20image%2020261016205632.png)


# Screenshot Requirements

pour down as many screenshots as you can in your report

Each local.txt and proof.txt found must be shown in a screenshot that includes the contents of the file, as well as the **IP address** of the target by using `ipconfig`, `ifconfig` or `ip addr`. An example of this is shown below:

WITH THE CONTENTS OF THE LOCAL AND PROOF FLAG 
GIVE IP ADDRESS AS WELL OF MACHINE 
 `ipconfig`, `ifconfig`

![](4.%20OSCP/Exam%20Day/14.%20Preparing%20for%20OSCP%201/1.%20OSCP%20Exam%20Guide/Attachments/Pasted%20image%2020261016205822.png)

# Exam Restrictions

LMMNR Spoofing using Responder will not come

No nessus,OpenVAS also

Nmap Scripts should be only of recon and enumeration 

Allowed : 
Msfvenom , searchsploit , exploitdb

You cannot use any of the following on the exam:
- Spoofing (IP, ARP, DNS, NBNS, etc)
- Commercial tools or services (Metasploit Pro, Burp Pro, etc.)
- Automatic exploitation tools (e.g. db_autopwn, browser_autopwn, SQLmap, SQLninja etc.)
- Mass vulnerability scanners (e.g. Nessus, NeXpose, OpenVAS, Canvas, Core Impact, SAINT, etc.)
- AI Chatbots (OffSec KAI, ChatGPT, YouChat, etc.)
- Features in other tools that utilize either forbidden or restricted exam limitations

# Metasploit Restrictions

meterpreter shell only on 1 machine 

The usage of Metasploit and the Meterpreter payload are restricted during the exam. You may only use Metasploit modules (**Auxiliary, Exploit, and Post**) or the Meterpreter payload against **one** single target machine of your choice. Once you have selected your one target machine, you cannot use Metasploit modules ( Auxiliary, Exploit, or Post ) or the Meterpreter payload against any other machines.

Metasploit/Meterpreter **should not** be used to test vulnerabilities on multiple machines before selecting your one target machine ( this includes the use of **check** ) . You may use Metasploit/Meterpreter as many times as you would like against your one target machine.

If you decide to use Metasploit or Meterpreter on a specific target and the attack fails, then you **may not** attempt to use it on a second target. In other words, the use of Metasploit and Meterpreter becomes locked in as soon as you decide to use either one of them.

Metasploit **cannot** be used for **pivoting**, because it would thereby be used on more than one target.

You may use the following against all of the target machines with the exception that meterpreter payload could be used only against one target machine:

- multi handler (aka exploit/multi/handler)
- msfvenom



# Exam Connection

Your connection to the exam is to be done with Kali Linux using OpenVPN. We are unable to provide any VPN connectivity support if you choose to use another setup. Your exam connection pack and details will be sent by email at the exact start time of your exam and not in advance.

1) Download the exam-connection.tar.bz2 file from the link provided in the exam email to your Kali machine.

2) Extract the file:

```auto
┌──(kali㉿kali)-[~]
└─$ tar xvfj exam-connection.tar.bz2
OS-XXXXXX-OSCP.ovpn
troubleshooting.sh
```

3) Initiate a connection to the exam lab with OpenVPN:

```auto
┌──(kali㉿kali)-[~]
└─$ sudo openvpn OS-XXXXXX-OSCP.ovpn 
```

4) Enter the username and password provided in the exam email to authenticate to the VPN:

```auto
┌──(kali㉿kali)-[~]
└─$ sudo openvpn OS-XXXXXX-OSCP.ovpn 1 ⨯
[sudo] password for kali: 
2022-01-11 04:15:50 Note: Treating option '--ncp-ciphers' as '--data-ciphers' (renamed in OpenVPN 2.5).
2022-01-11 04:15:50 OpenVPN 2.5.0 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] built on Oct 28 2020
2022-01-11 04:15:50 library versions: OpenSSL 1.1.1g 21 Apr 2020, LZO 2.10
🔐 Enter Auth Username: OS-XXXXXX
🔐 Enter Auth Password: *********** 
2022-01-11 04:16:01 TCP/UDP: Preserving recently used remote address: [AF_INET]x.x.x.x:1194
2022-01-11 04:16:01 UDP link local (bound): [AF_INET][undef]:1194
2022-01-11 04:16:01 UDP link remote: [AF_INET]x.x.x.x:1194
2022-01-11 04:16:01 WARNING: this configuration may cache passwords in memory -- use the auth-nocache option to prevent this
2022-01-11 04:16:02 [offensive-security.com] Peer Connection Initiated with [AF_INET]x.x.x.x:1194
2022-01-11 04:16:03 TUN/TAP device tun0 opened
2022-01-11 04:16:03 net_iface_mtu_set: mtu 1500 for tun0
2022-01-11 04:16:03 net_iface_up: set tun0 up
2022-01-11 04:16:03 net_addr_v4_add: 192.168.xx.xx/24 dev tun0
2022-01-11 04:16:03 Initialization Sequence Completed
```

# Exam Control Panel

The exam control panel is available via a link provided in your exam email. Through the exam control panel you will be able to:

- Submit proof files
- Revert target machines
- View specific target objectives and point values

# Machine Reverts

You have a limit of 24 reverts. This limit can be reset once during the exam.

You can use it to revert for documentation purposes

# Exam Proof File names

- proof.txt - This file is only accessible to the root or Administrator user and can be found under the **/root/** directory or the **Administrator Desktop****.** 
- local.txt - This file is accessible to an un-privileged user account.

Note that the targets containing these files are detailed in your exam control panel.

# Point Disqualification

You will receive no points for a specific target for the following:

- Using a restricted tool
- Using Metasploit Auxiliary, Exploit, or Post modules on multiple machines
- Using the Meterpreter payload on multiple machines
- Failure to provide the local.txt and proof.txt file contents in both the control panel and in an interactive shell screenshot
- Lack of documentation

# Suggested Documentation Templates

Ideally, one of the following templates should be used for the penetration test report:

- [Microsoft Word](https://www.offsec.com/pwk-online/OSCP-Exam-Report.docx)

# Contact Protocol

If you encounter any connectivity problems with the VPN or target machines, inform us immediately, directly in the proctoring chat. Should you not be able to access the proctoring tool, please contact us via the live chat available at [**https://chat.offsec.com/**](https://chat.offsec.com/) or via email to **"help AT offsec DOT com"**.

Please note that we will not be able to assist with, or give hints on, any exam objectives and will only be available for technical problems during the exam.

# SECTION 3: SUBMISSION INSTRUCTIONS

**Submission Checklist:**

- Your exam report is in PDF format
- You have used the following format for the PDF file name "OSCP-OS-XXXXX-Exam-Report.pdf", where "OS-XXXXX" is your OSID
- Your PDF has been archived into a .7z file (Please do NOT archive it with a password)
- You have used the following format for the .7z file name "OSCP-OS-XXXXX-Exam-Report.7z", where "OS-XXXXX" is your OSID
- You have made sure that your archive is not more than 200MB
- You have uploaded your .7z file to [https://upload.offsec.com](https://upload.offsec.com/) 

Note that the filename is case-sensitive. Learners must submit their exam file following the exact filename format structure above. If your file does not follow the exact filename format and structure, the application will not accept it.

The following subsections provide details on each of these requirements.

#### [Submission Format and Name](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#submission-format-and-name)

Your exam report must be submitted in PDF format archived into a .7z file. Please make sure to include all your scripts or any PoCs as text inside the exam report PDF file itself. No other file formats will be accepted within the .7z file other than PDF file format.  
If you submit your report in any other file format, we will not request or remind you to send a PDF report archived into a .7z file and your exam report will not be scored.

Before submitting your exam report, please review the PDF document to ensure the format and content appear as it did in your original edition document and that there are no formatting errors.  
After uploading your exam file to upload.offsec.com, the site will provide you with the MD5 hash of your uploaded file.  
Please make sure to verify that you have uploaded your report correctly by checking and comparing the MD5 hashes of your uploaded exam file and the file you have locally.

If the values do not match, that means your file did not upload successfully. Click on "Select a new file" and upload your archive again.

```auto
┌──(kali㉿kali)-[~]
└─$ sudo md5sum OSCP-OS-XXXXX-Exam-Report.7z
f7feecea01ac1eca9ee522906b087d5e OSCP-OS-XXXXX-Exam-Report.7z
```

---

#### [Archive File](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#archive-file)

Please do not archive your .7z and PDF(s) files with a password. Our system will not accept should you upload a password-protected file.

You must submit your documentation in a .7z file. Please use your Kali machine to create your .7z file.

```auto
┌──(kali㉿kali)-[~]
└─$ sudo 7z a OSCP-OS-XXXXX-Exam-Report.7z OSCP-OS-XXXXX-Exam-Report.pdf

7-Zip 9.20 Copyright (c) 1999-2010 Igor Pavlov 2010-11-18 p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,2 CPUs)

Scanning

Updating archive OSCP-OS-XXXXX-Exam-Report.7z


Everything is Ok
```

---

#### [Submission Upload](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#submission-upload)

Please submit your .7z file via [https://upload.offsec.com](https://upload.offsec.com/) within 24 hours of completion of the exam and follow the provided instructions in order to upload your archived exam report.

The maximum allowable size for uploading your archive file is 200MB. If the size constraints are not met, you would not be able to upload your archive. If you are unable to meet the size constraints, we suggest looking at ways to reduce your file size using techniques such as image compression.

After the file has been uploaded, you will be presented with a "**Submit File**" button where a MD5 hash of your exam report will be displayed. Make sure to click the "**Submit File**" button after verifying your MD5 hash to submit your files successfully.

If you do not upload your exam-report via [https://upload.offsec.com](https://upload.offsec.com/) , it will not be graded.

**IMPORTANT NOTE:** Please note that some Windows 11 users have encountered an issue while trying to upload their exam files to [https://upload.offsec.com](https://upload.offsec.com/) , and received **file is not a proper format** error. This issue may be related to compatibility concerns with Windows 11, and we'd like to provide a solution to ensure a smooth upload process.

To resolve this problem, we recommend using a Kali Virtual Machine (VM) to upload your exam files securely and without any compatibility issues.  
For more information about Kali VM, please visit: [https://help.offsec.com/hc/en-us/articles/360049796792-Kali-Linux-Virtual-Machine](https://help.offsec.com/hc/en-us/articles/360049796792-Kali-Linux-Virtual-Machine)


