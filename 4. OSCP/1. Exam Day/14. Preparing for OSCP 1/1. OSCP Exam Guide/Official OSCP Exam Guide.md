
### [Please read this entire document carefully before beginning your exam!](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#please-read-this-entire-document-carefully-before-beginning-your-exam)

This article provides information on:

- [Exam Structure](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#h_01GFTCV6YN1BFY0DBXQH6AWH81)
- [Exam Requirements](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-1-exam-requirements)
- [Exam Information](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-2-exam-information)
- [Submission Instructions](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-3-submission-instructions)
- [Additional Required Information](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#additional-required-information)
- [Results](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#results)

### [Scope Statement](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#introduction)

The Offensive Security Certified Professional (OSCP) certification, designed for cybersecurity professionals, validates practical, hands-on skills in ethical hacking and penetration testing. Successful candidates demonstrate proficiency in identifying vulnerabilities, exploiting systems, escalating privileges, and documenting their findings in a real-world environment. The certification is relevant to roles such as penetration testers, security analysts, and consultants, confirming their ability to conduct comprehensive security assessments.

### [Criteria for Certification](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#01JV9P13HPB2X8N1HHJPC6WM1P)

The Offensive Security Certified Professional credential will be awarded without prerequisites to individuals who pass a performance test described below.

### [INTRODUCTION](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#01JV9NY4ZW3K4YAVFDHWBC0P44)

This guide explains the objectives of the OffSec Certified Professional Plus (OSCP+) certification exam. Section 1 describes the requirements for the exam, Section 2 provides important information and suggestions, and Section 3 specifies instructions for after the exam is complete.

The OSCP+ certification exam simulates a live network in a private VPN, which contains a small number of vulnerable machines.

**You have 23 hours and 45 minutes to complete the exam.**

This means that if your exam begins at 09:00 GMT, your exam will end at 08:45 GMT the next day.

Once the exam is finished, you will have another 24 hours to upload your documentation. Details on how to submit your files are provided below.

#### [**All OSCP+ exams are proctored.**](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#all-oscp-exams-are-now-proctored)

Please make sure to read the proctoring tool learner manual and the proctoring FAQ at the following URL: [https://help.offsec.com/hc/en-us/sections/360008126631-Proctored-Exams](https://help.offensive-security.com/hc/en-us/sections/360008126631-Proctored-Exams)

### [Exam Structure](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#h_01GFTCV6YN1BFY0DBXQH6AWH81)

The OSCP+ exam machines structure:

- **3 stand-alone machines (60 points in total)**
    - 20 points per machine
        - 10 points for initial access
        - 10 points for privilege escalation

- **1 Active Directory (AD) set containing 3 machines (40 points in total)**
    - For the Active Directory exam set, learners will be provided with a username and password, simulating a breach scenario.
    - 10 points for machine #1
    - 10 points for machine #2
    - 20 points for machine #3

- Possible scenarios to pass the exam (70/100 to pass)
    - 40 points AD + 3 local.txt flags (70 points)
    - 40 points AD + 2 local.txt flags + 1 proof.txt flag (70 points)
    - 20 points AD + 3 local.txt flags + 2 proof.txt flag (70 points)
    - 10 points AD + 3 fully completed stand-alone machines (70 points)

#### [Point Allocation](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#point-allocation)

- The order in which the exam machines are documented in your exam report are the order in which the exam machines will be graded and valued
- For independent targets, points will be awarded for partial and complete administrative control of each machine
- Each machine has a specific set of objectives that must be met in order to receive full points
- You must achieve a minimum score of 70 points to pass the exam
- It is possible to achieve a maximum of 100 points on the exam
- Specific objectives and point values for each machine are located in your exam control panel

---

### [SECTION 1: EXAM REQUIREMENTS](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-1-exam-requirements) 

Specific instructions for each target will be located in your Exam Control Panel, which will only become available to you once your exam begins.

#### [Documentation Requirements](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#documentation-requirements)

You are required to write a professional report describing your exploitation process for each target. You must document all of your attacks including all steps, commands issued, and console output in the form of a penetration test report. Your documentation should be thorough enough that your attacks can be replicated step-by-step by a technically competent reader.

**The documentation requirements are very strict and failure to provide sufficient documentation will result in reduced or zero points being awarded.** **Please note that once your exam report is submitted, your submission is final.** **If any screenshots or other information is missing, you will not be allowed to send them and we will not request them.**

---

#### [Exploit Code](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exploit-code)

If you have not made any modifications to an exploit, you should only provide the URL where the exploit can be found. Do not include the full unmodified code, especially if it is several pages long.

If you have modified an exploit, you should include:

- The modified exploit code
- The URL to the original exploit code
- The command used to generate any shellcode (if applicable)
- Highlighted changes you have made
- An explanation of why those changes were made

---

#### [Exam Proofs](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exam-proofs)

Your objective is to exploit each of the target machines and provide proof of exploitation. Each target machine contains at least one proof file (local.txt or proof.txt), which you must retrieve, submit in your control panel, and include in a screenshot with your documentation. **Failure to provide the appropriate proof files in a screenshot for each machine will result in zero points being awarded for the target.**

The valid way to provide the contents of the proof files is in an interactive shell on the target machine with the `type` or `cat` command from **their original location**.

**Obtaining the contents of the proof files in any other way will result in zero points for the target machine; this includes any type of web-based shell.**

On all Windows targets, you must have a shell running with the permissions of one of the following to receive full points:

- SYSTEM user
- Administrator user
- User with Administrator privileges

On all Linux targets, you must have a root shell in order to receive full points.

---

#### [Control Panel Submission](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#control-panel-submission)

The exam control panel contains a section available to submit your proof files. The contents of the local.txt and proof.txt files obtained from your exam machines _must be submitted in the control panel before your exam has ended._ Note that the control panel will not indicate whether the submitted proof is correct or not. An example of this is provided below:

![control-panel.png](https://help.offsec.com/hc/article_attachments/4415465949716)

---

#### [Screenshot Requirements](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#screenshot-requirements)

Each local.txt and proof.txt found must be shown in a screenshot that includes the contents of the file, as well as the **IP address** of the target by using `ipconfig`, `ifconfig` or `ip addr`. An example of this is shown below:

![proof-text.png](https://help.offsec.com/hc/article_attachments/16273700915860)

---

#### [Exam Restrictions](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exam-restrictions)

You cannot use any of the following on the exam:

- Spoofing (IP, ARP, DNS, NBNS, etc)
- Commercial tools or services (Metasploit Pro, Burp Pro, etc.)
- Automatic exploitation tools (e.g. db_autopwn, browser_autopwn, SQLmap, SQLninja etc.)
- Mass vulnerability scanners (e.g. Nessus, NeXpose, OpenVAS, Canvas, Core Impact, SAINT, etc.)
- AI Chatbots (OffSec KAI, ChatGPT, YouChat, etc.)
- Features in other tools that utilize either forbidden or restricted exam limitations

You are not required to disable tools with built-in AI features like Notion or Google AI Overview.   
However, using LLMs and AI chatbots (OffSec KAI, ChatGPT, Deepseek, Gemini, etc.) is strictly prohibited. This is considered receiving third-party help and sharing exam information, both of which violate our Academic Policy. For more information, please refer to [AI Usage Policy in OffSec Exams](https://help.offsec.com/hc/en-us/articles/35549468971156-AI-Usage-Policy-in-OffSec-Exams).

Any tools that perform similar functions as those above are also prohibited. You are ultimately responsible for knowing what features or external utilities any chosen tool is using. The primary objective of the OSCP+ exam is to evaluate your skills in identifying and exploiting vulnerabilities, not in automating the process.

You may however, use tools such as Nmap (and its scripting engine), Nikto, Burp Free, DirBuster etc. against any of your target systems.

**NOTE:** While you may use Discord as a resource for searching for information during the exam, under no circumstances are you permitted to seek or receive assistance from others on the platform.

For more information regarding the allowed tools, please visit our [**OSCP+ Exam** **FAQ article**](https://help.offensive-security.com/hc/en-us/articles/4412170923924).

**Please note that we will not comment on allowed or restricted tools, other than what is included inside this exam guide.**

Downloading any applications, files or source code from the exam environment to your local machine is strictly forbidden unless they're necessary for you to compromise the exam machine, and make sure to delete it after completing the exam objectives. For more information, please refer to the [https://www.offsec.com/legal-docs/](https://www.offsec.com/legal-docs/)

---

#### [Metasploit Restrictions](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#metasploit-restrictions)

The usage of Metasploit and the Meterpreter payload are restricted during the exam. You may only use Metasploit modules (**Auxiliary, Exploit, and Post**) or the Meterpreter payload against **one** single target machine of your choice. Once you have selected your one target machine, you cannot use Metasploit modules ( Auxiliary, Exploit, or Post ) or the Meterpreter payload against any other machines.

Metasploit/Meterpreter **should not** be used to test vulnerabilities on multiple machines before selecting your one target machine ( this includes the use of **check** ) . You may use Metasploit/Meterpreter as many times as you would like against your one target machine.

If you decide to use Metasploit or Meterpreter on a specific target and the attack fails, then you **may not** attempt to use it on a second target. In other words, the use of Metasploit and Meterpreter becomes locked in as soon as you decide to use either one of them.

Metasploit **cannot** be used for **pivoting**, because it would thereby be used on more than one target.

You may use the following against all of the target machines with the exception that meterpreter payload could be used only against one target machine:

- multi handler (aka exploit/multi/handler)
- msfvenom

All the above limitations also apply to different interfaces that make use of Metasploit (such as Armitage, Cobalt Strike, Metasploit Community Edition, etc).

---

### [SECTION 2: EXAM INFORMATION](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-2-exam-information)

#### [Exam Connection](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exam-connection)

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

---

#### [Exam Control Panel](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exam-control-panel)

The exam control panel is available via a link provided in your exam email. Through the exam control panel you will be able to:

- Submit proof files
- Revert target machines
- View specific target objectives and point values

---

#### [Machine Reverts](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#machine-reverts)

You have a limit of 24 reverts. This limit can be reset once during the exam. All of the machines have been freshly reverted at the start of your exam so you will not be required to revert the machines when you begin. Please wait patiently for the machine to revert and only click the button once per attempt. Note that reverting a target machine will cause it to return to its original state and any changes you have made to the machine will be lost.

---

#### [Exam Proof File names](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#exam-proof-filenames)

- proof.txt - This file is only accessible to the root or Administrator user and can be found under the **/root/** directory or the **Administrator Desktop****.** 
- local.txt - This file is accessible to an un-privileged user account.

Note that the targets containing these files are detailed in your exam control panel.

---

#### [Point Disqualification](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#point-disqualification)

You will receive no points for a specific target for the following:

- Using a restricted tool
- Using Metasploit Auxiliary, Exploit, or Post modules on multiple machines
- Using the Meterpreter payload on multiple machines
- Failure to provide the local.txt and proof.txt file contents in both the control panel and in an interactive shell screenshot
- Lack of documentation

---

#### [Suggested Documentation Templates](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#suggested-documentation-templates)

Ideally, one of the following templates should be used for the penetration test report:

- [Microsoft Word](https://www.offsec.com/pwk-online/OSCP-Exam-Report.docx)
- [OpenOffice/LibreOffice](https://www.offsec.com/pwk-online/OSCP-Exam-Report.odt)

You may use your own template as long as the information is presented in a structured, professional manner and follows all other requirements outlined above.

---

#### [Guidelines for Handling Unforeseen Factors during the Exam](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#internet-connection-issues)

This subsection of the exam guide documents what you should do in case you are unable to complete your exam due to severe external factors. Please make sure to read and understand it carefully.

The exam lab is a dedicated environment with no learners connected other than yourself. The total allotted time of 23:45 hours _does_ take life and its situations into consideration:

- You are expected to take rest breaks, eat, drink, and sleep
- You are also expected to have a contingency plan in the event that there is an issue outside your control. (e.g. ensure you have access to a backup Internet connection, Kali Virtual Machine, power etc)

If you have a legitimate issue, please send an email with your OSID to **"challenges AT offsec DOT com"** immediately. Make sure to include all the necessary details and supporting information such as a letter from your power company, ISP, or any other relevant documentation.

Please note we are only able to extend the exam time if the issues are present on our side and only when the exam subnet is not immediately in use by another learner following your exam. In the event of an issue on our side and the exam subnet is scheduled immediately following your exam we will provide a free exam retake attempt. We work very hard to ensure our environments are highly available and issues are very rare.

---

#### [Contact Protocol](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#contact-protocol)

If you encounter any connectivity problems with the VPN or target machines, inform us immediately, directly in the proctoring chat. Should you not be able to access the proctoring tool, please contact us via the live chat available at [**https://chat.offsec.com/**](https://chat.offsec.com/) or via email to **"help AT offsec DOT com"**.

Please note that we will not be able to assist with, or give hints on, any exam objectives and will only be available for technical problems during the exam.

---

### [SECTION 3: SUBMISSION INSTRUCTIONS](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#section-3-submission-instructions)

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

---

#### [Acknowledgement of Receipt](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#acknowledgement-of-receipt)

Once the report is uploaded successfully, **a confirmation email** will be sent immediately acknowledging the receipt. If you have not received the email, please ensure that you uploaded your report and clicked the **Submit File** button on the final page of [https://upload.offsec.com](https://upload.offsec.com/) after verifying your MD5 hash. We also recommend you to check your email spam and junk folders in case the confirmation email has been flagged as spam.

---

#### [Additional Required Information](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#additional-required-information)

In the unlikely event that we require additional clarification on your exam report, we will get in contact with you via email. You must submit the requested information within **24 hours** from the time we have requested it.

---

#### [Results](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide#results)

You will receive an email with your certification exam results (pass/fail) within ten (10) business days after submitting your documentation.



