
SYSTEM HACKING
Modern Exploitation Techniques
Modern Exploitation
2

Modern Exploitation
▸ Also known as initial access
▸ First stage in a cyber attack chain
▸ Foothold establishment over a network link
▸ Followed by privilege escalation and lateral movement
3
Techniques
▸ Phishing
▹ Sending deceptive emails or messages to trick individuals into
revealing sensitive information, such as usernames and passwords
4
Techniques
▸ Password Guessing and Brute Force
▹ Trying different combinations of usernames and passwords until
they find a valid login credential
▹ Can be automated using tools
5
Techniques
▸ Public Software Exploits
▹ Unpatched or outdated software
▹ Vulnerabilities in third-party services or vendors
▹ E.g., old versions of Wordpress, vsFTPd, etc.
6
Techniques
▸ Client Side Attacks
▹ Exploit vulnerabilities in software running on a user's device
▹ Triggered when user visits a website or opens a document
▹ E.g., Microsoft office macros, browser plugins
7
Techniques
▸ Web Application Attacks
▹ Most common attack vectors
▹ Testing for SQLi, XSS, CORS, IDOR
8
Techniques
▸ Other Techniques
▹ Wireless Exploitation
▹ IoT and embedded devices
▹ Physical Media (USB)
▹ Physical Intrusion
9


**Part 1: Introduction to Modern Exploitation and Module Revamp**

Hello friends, I am Ansh and I am back again with a new topic. This is a very important topic in this system hacking module. So, this is a new revamped version of mine in this course which I had created a long time ago. In 2020, I created this course, and there are some topics that are going to be useful for you in the future. Like **initial access**, which is the entire penetration testing methodology, right? I am going to complete that in this course.

So, when I made this course in 2020, at that time, I did not have as much experience as I have today. Although at that time, I did have a lot of experience—I had studied penetration testing and had done it practically as well. But there were some topics that I couldn't make back then and which cover the entire penetration testing workflow. So, in the upcoming courses, I am going to tell you the complete penetration testing methodology and workflow, which are **modern techniques**. What we have studied so far are some outdated topics and some scattered pieces, like how to use WordPress or different web attacks.

**Part 2: Exploitation Objectives and the Shifting Workflows**

This will be a bonus section where I will show you how the entire initial access or initial foothold is established in any system. We have studied information gathering, scanning, and enumeration in the entire hacking course. Now, in the exploitation course, our goal is to get access to the system. The objective of exploitation is to **get a shell on the system**, to get its access, and to be able to run arbitrary commands on the target system. So, this access is our objective.

Basically, I have shown you Metasploit before, which is the same thing, but that was a public exploit that we used to compromise a system—like perhaps an SMB issue, an SMB CVE that we exploited on Windows 10. But that is only about 10% of our entire initial compromise process and the techniques involved. Besides that, there are many things in modern modules that we do and need to learn. What I taught earlier was incomplete, and we will complete it in this bonus section.

**Part 3: Modern Exploitation Techniques & The TryHackMe Recon Stage**

In this section, we are going to study **modern exploitation techniques**. It won't come under the system hacking module; it is a bonus section of the exploitation course itself. So, what are the different techniques in modern exploitation for initial access? Basically, I have picked up this diagram from TryHackMe, so we have to explain this entire workflow.

First of all, you have to do **initial recon** to find out about the system and about the target—which software is running, which ports are open, which software is on which port, what their versions are, fully enumerate them, and search for exploits. Once you find a starting point, after that, you perform an initial compromise on the system. The meaning of compromise is the same: you find some vulnerability in their service. For example, if there is a web application, and it has some WordPress issue, or some CVE in WordPress, or SQL injection, or any OWASP Top 10 web attack is possible, then you plan a compromise—meaning you will exploit that issue to compromise the target system.

**Part 4: Establishing a Foothold and RCE Vectors**

After that comes the **foothold**, which we are going to study in this bonus section. Establishing a foothold means getting an **RCE (Remote Code Execution)** or shell access on the system through a web shell or by running something that we saw in the previous step of initial compromise so that we can exploit it.

But after exploiting, how you gain access to the system is a major concern. You might get RCE on the system, most commonly through SQL injection, or it could be through XXE, LFI, or SSRF. Through all these techniques, you can directly get RCE on the system. There are some techniques through which you cannot, so that is only one part of the techniques or vectors. But there are other parts as well, like public software exploits, known exploits, password cracking, and guessing. So, whatever services are open on that target, you have to enumerate all of them and apply all the techniques that we can use to compromise it.

**Part 5: Complete Methodology, Privilege Escalation, and Career Pathways**

So, this is basically a part of network penetration testing, not just web penetration testing. It has a much wider scope; it has a very huge scope. I am going to tell you about the complete **network penetration testing** and infrastructure in this module. After that, we will study about **Privilege Escalation** in another course. We will complete up to this part, and the part about privilege escalation will be covered in another course because it will be different for Windows and different for Linux.

After that, for lateral movement and maintaining presence, I have already created a course. I have covered the Active Directory (AD) part in my AD course, so you can study that from there. **Lateral movement** basically happens most commonly in Windows when AD is being used, and I have covered that in my AD course, so you can study it from there. The part about completing the mission is also fully covered there.

What I am trying to do here—as you might have figured out—is that I am covering the entire modern-day infrastructure penetration testing methodology (like in OSCP) right here. For anyone wanting to build a career in VAPT, penetration testing, or red teaming, these courses will be extremely useful. You should definitely do them, and you will learn everything from them. In the future, I will also let you know which other courses you should study besides this. But the process of establishing a foothold is what I am going to tell you in this module.

**Part 6: Initial Access and Low-Privilege Service Accounts**

Let us move forward and look at initial access—what actually is it? If you perform any cyber attack, or if you want to compromise any system—I am not talking about illegal things, I am talking about legal security assessments, like penetration testing done legally in every company for their assets—their first step is to gain initial access to some system that is a part of the network. Then from that network, you go to a second system, then a third system, and so on.

When you get the first access to any system, it is not necessary that you will get the highest-level access at that time. As you know, there are different user levels: guest user, normal user, service account, and then root user or admin user. Generally, when you gain initial access, you will get it through a **service account** because if you got it through a website, the web service runs under a service account—like `www-data` or similar. These service accounts have very low privileges on the system. So, generally, when you get initial access, you will have low-privileged access on the system. Your goal is to get the highest privilege, like a higher user level, for which you perform privilege escalation using different techniques that we will study later.

**Part 7: Publicly Exposed Systems and WannaCry Analogy**

But for now, understand that any compromise is the first stage of any cyber attack chain. Before moving forward, you have to establish yourself somewhere. Generally, if an external attacker wants to compromise a company, they will take initial access on an **internet-facing or publicly exposed system** so that they can discover the network interface, find other systems on that network, perform scanning, and move forward by executing further attacks, eventually gaining the highest domain access on that system. This is foothold establishment on any network.

For example, if we talk about the WannaCry attack analogy and SMB, to enter a network, it first had to compromise one system. It spreads through SMB, but SMB will only work when you can establish a foothold on a system first; you have to get onto that system first where SMB is running.

**Part 8: Landing on a Target and Local Enumeration**

You can go to other systems only after that. If an attacker wants to attack via SMB, propagate or spread it, you first have to establish that worm or malware on at least one system. That could happen through phishing—mostly it was phishing where an email came, they clicked on it, something got downloaded, and an executable ran. So it happened through phishing.

Similarly, you have to do the same here: first, establish your footing on one system. After establishing your footing, when you are inside the system, you can perform further enumeration, look at the source code of the web application or other services, check the network interfaces, check which ports are open locally on localhost, and see which other systems are connected to it. There are many enumeration steps that we can discuss. Basically, this is very important; without this, you cannot move forward in any attack chain.

**Part 9: Social Engineering and Phishing Templates (The Appraisal Trap)**

Now, what are the techniques for this? I will give you a high-level overview, but after that, we will study these techniques in detail. The very first technique, as I mentioned, is **phishing**—sending deceptive emails to someone. Nowadays, it's not just emails; SMS is sent (smishing), and you can even get physical notes, or calls (vishing), impersonation, and many other creative ways of social engineering have emerged.

This can be the first step of getting an initial foothold—sending an email to a company employee, pretending to be their manager, and telling them, for example: _"Your appraisal cycle is about to start, and I have created your performance review. You can click on this link to view it."_ There will be a link in it, and when they click on that link, a portal will open. It will look exactly like the company's actual performance review portal, but you have built a fake portal, and on that, you will ask for their username and password.

**Part 10: Credential Harvesting and Urgent Scenarios**

Because the email is so well-targeted, and their manager is saying they've completed the performance review—and a performance review means if they get a good rating, they will get a good hike—this is an **incredibly juicy email template** that people, especially employees, will fall for. If this email is received right during the performance review cycle (like December, or whenever their cycle runs), they will particularly want to click on it and might even enter their username and password to log in, which will then come to you.

If they enter their username and password, most commonly that username will belong to their AD (Active Directory) account or domain account. Using those credentials, you can log into other systems to access the company's internal network. So, this phishing is a common method for credential leakage or **credential harvesting**. You can also create templates like _"It's Diwali time, accept your gift, go to this link and enter your email/password or other details to receive it."_ You have to think with a calm mind about how an individual can be tricked.

You can create a sense of urgency, or target their family members, like a child or an elderly father who needs money or is stuck somewhere and asking for funds. You can craft such emails or SMS. There are many such ways, and they are highly effective because we know that **humans are the weakest link in the security chain**. This targets humans and is most commonly successful.

**Part 11: Brute-forcing, Online/Offline Dynamics, and Crackers**

The second technique is **password guessing and brute force**. You have often seen login portals on websites or other services like FTP and SSH where authentication is required. If their login details are very trivial, like default usernames and default passwords, we can extract them with simple guessing.

Guessing means trying different combinations online. If it is FTP, you have to try online because you won't get a hash there, so you cannot try offline—it has to be done online, meaning you try combinations by sending requests to the service every time. The more combinations you try, the more requests go to FTP, which might even cause a lockout. These are the problems with online attacks, but if you know the username, it becomes much easier to crack the password. If the password is simple and present in a wordlist, it will be caught, and you can log in. That is why it is recommended to keep strong passwords, very long passphrases, and try combinations of lower case, upper case, special characters, and numbers.

Brute forcing can always be done. You know that if you get someone's hash from a database, or extract it during exploitation, cracking it is easy because it is offline, and **offline cracking is extremely fast**. Another good thing is that password guessing and brute-forcing can be automated using many tools available to us like **Hydra, Medusa, John the Ripper, and Hashcat**. These are very popular tools.

**Part 12: Public Software Exploits, CVEs, and Exploit-DB**

The third method is **public software exploits**. We have done this previously with Windows 7, where we exploited the SMB MS17-010 vulnerability (EternalBlue)—I think that was its number—using Metasploit, and maybe manually as well. Public exploits are those found in unpatched software. For example, if you are using a very old version of a software, there are issues found in it like buffer overflows or injection issues. Bugs are discovered, and then they are patched via updates. However, on some systems or assets, they are not updated. If they are not updated, they continue running the old, vulnerable version. We can exploit and enumerate that to gain access to the system and get RCE if it is a critical or high-severity vulnerability.

In third-party services, vendor software is very common. If you are using open-source software, you must update it because a CVE was found in the previous version. The most common CVEs are found in third-party software or old versions of services like SSH, OpenSSH, VSFTPD, WordPress, Drupal, etc. These are third-party software programs that you haven't coded yourself in-house but have outsourced from a vendor. Issues in their software are exposed by the community and then fixed. But if they are not fixed, and you are using the old version, your software can be compromised.

So, as a penetration tester, we will search for CVEs. First, we need to extract the version of the running service. If the version is identified, we can search on **Exploit-DB** to see if exploits exist for this version. We will get the exploit code, run it, and get access to the system. This is why outdated software should not be used; all software should be updated. If no fix is available for a particular exploit, you can apply firewalls, disable it, or apply temporary fixes.

**Part 13: Client-Side Attack Methodology and MS Office Macros**

Now let's come to **client-side attacks**. This is another technique that can give you an initial foothold. In client-side attacks, what happens is that you are not attacking the server directly, but you are exploiting the user's device. For example, software running on their device, like their web browser or browser applications. It could be that their browser has some issues or vulnerabilities that we exploit.

If not the browser, it can be other things like Microsoft Office. If we create a document and send it to the client, and when they open it on their system, our code gets executed. This kind of functionality is called **Macros**. Microsoft Office has this Macros functionality, particularly in MS Word, where you can include it.

Through this, you can run certain codes like VBA scripts (Visual Basic for Applications). This is basically used to automate repetitive tasks, handle complex functionalities, or for cross-platform usage. The general definition of macros is to automate repetitive tasks—like automating a data flow, mouse clicks, keystrokes, or things you do repeatedly like filling, adding, deleting, or updating data. These code snippets are used for regular tasks by people handling accounts or data entry. In these code snippets, you also have the functionality to run shell commands.

So, if you embed a macro inside a Word document that opens a shell and gives you a reverse shell, opens another program, or deletes files, you can save it in `.docm` format (macro-enabled document) and send it to the client.

**Part 14: Client-Side Efficacy and Prompt Warnings**

Nowadays, Microsoft has disabled macros by default and a prompt appears: _"Do you want to view the content or run the script?"_ This notifies them that there are macros, adding an extra step of verification. If the client is not security-aware, they might click through the warning, running your macro on their system. This gives you access from the client's system.

However, sometimes this doesn't work, so client-side attacks are not always fully reliable. But they can work, and if you have no other choice, you can use them to eventually gain access to the company's servers because their local systems often contain valuable information like usernames, passwords, or sensitive data that you can use for further enumeration. Browser plugins can also be vulnerable, and you can exploit outdated plugins through client-side attacks.

**Part 15: Web Application Attack Vectors (The Mainstream Threat)**

Now, let's look at a very obvious technique: **web application attacks**. These are the most common attack vectors. Even if no other services are running on a system like RDP, FTP, SSH, LDAP, RPC bind, or NetBIOS, which are common services on systems, the web is the most common because other services are deliberately set up by technically competent people and don't directly serve a business objective or generate revenue.

The most common entry points are web applications because businesses earn revenue through them. Their main concern is to deploy web apps quickly, and they often do not focus much on how securely they are deployed if they lack security awareness. That is why they are the most common targets for exploitation.

We already know what web vulnerabilities are—like SQL injection, LFI, RCE, etc. If we find these in a web application, we can potentially gain RCE and establish a foothold. This is not always a sure-shot because you might not have write access, or some attacks might be client-side (like XSS) which won't directly grant you a shell. Nevertheless, web applications are the most common attack vectors.

We will discuss these techniques in detail—how initial access is obtained through them. I will show you practical examples, solve some labs on TryHackMe, study each technique individually, and explain how to gain an initial foothold. This will help you understand how practical penetration testing is performed in modern examinations and the industry. You will do the exact same things in **OSCP** and other modern, up-to-date exams.

**Part 16: Modern VAPT Exams & Less Common Techniques**

There are some other techniques too, like wireless exploitation, IoT devices, or physical media (like plugging a USB into their system, which is a highly conditional physical intrusion technique), but these techniques are less common. Very less common.

For wireless, you need to be within physical range. IoT devices are still not very widely targeted in this context, and physical media requires physical presence, which is very conditional. You can still read and learn about them if you are interested, but we won't be discussing them in this course. We will focus entirely on the widely-used, mainstream techniques.

So, that's all for this video. This was just a theoretical introduction to what we are going to study in Modern Exploitation, and in the upcoming videos, we will perform hands-on practicals and look at how to gain initial access on any system. So, stay tuned, keep watching, keep learning, and goodbye.

