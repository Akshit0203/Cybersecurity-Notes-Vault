
[OSCP+ Exam Guide](https://help.offsec.com/hc/en-us/articles/360040165632-OSCP-Exam-Guide)

FIRST COMPLETE THE OFFICIAL COURSE AND ALL PROVING GROUNDS

https://whop.com/pro-hack-academy/pro-hack-academy/?trackingLinkRoute=learn-oscp-fast&trackingLinkId=trk_5yyuiCtTRm5kbu
can buy his checklist

https://docs.google.com/spreadsheets/d/1FBzafhtRXI9ngXIdVRpyoMndKJ-v6JgWqIKZfr1xBNA/edit?gid=1162211700#gid=1162211700


Also, don’t only understand how to exploit a vulnerability, but also understand how the underlying technologies work (e.g how AD works, how relational databases store data, how APIs work)

It’s really about focusing on learning and making sure you do a lot of boxes/labs.

notemaking was always more important than just solving machines.

https://www.youtube.com/watch?v=mac3HaJN2EI

https://rana-khalil.gitbook.io/hack-the-box-oscp-preparation/

Rooms list : 
https://docs.google.com/spreadsheets/d/18weuz_Eeynr6sXFQ87Cd5F0slOj9Z6rt/htmlview
(combined)
tj null sheet
https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview
https://docs.google.com/spreadsheets/d/18weuz_Eeynr6sXFQ87Cd5F0slOj9Z6rt/htmlview


portswigger



 automating reconnaissance - [https://github.com/Tib3rius/AutoRecon](https://github.com/Tib3rius/AutoRecon)


Privilege Escalation : 
1. TCM Windows Privesc: [https://academy.tcm-sec.com/p/windows-privilege-escalation-for-beginners](https://academy.tcm-sec.com/p/windows-privilege-escalation-for-beginners)
2. TCM Linux Privesc: [https://academy.tcm-sec.com/p/linux-privilege-escalation](https://academy.tcm-sec.com/p/linux-privilege-escalation)
3. Tryhackme Privilege Escalation path: [https://tryhackme.com/module/privilege-escalation](https://tryhackme.com/module/privilege-escalation)

### Active Directory Pentesting
1. Video by CyberMentor: [https://www.youtube.com/watch?v=VXxH4n684HE](https://www.youtube.com/watch?v=VXxH4n684HE)
2. Compromising Active Directory: [https://tryhackme.com/module/hacking-active-directory](https://tryhackme.com/module/hacking-active-directory)
3. Internet All Things (AD): [https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adcs-certificate-services/](https://swisskyrepo.github.io/InternalAllTheThings/active-directory/ad-adcs-certificate-services/)


HTB Boxes from TJNull List ( [https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview#) ) 

For eg, if I am learning Windows Privesc, I will side by side get hands on by solving Windows Boxes. I also made a write up kind of notes for all the boxes I have solved for my personal reference and get skill of solving & documenting at the same time. This is also VERY important as in future , if you encounter a same service in any other box, you can easily search through it and use the same commands and steps.

In the starting of your HTB solving, if you fail to solve the complete boxes, it is completely fine, all of us do. But also keep in mind the steps when you are not able to solve boxes, check write up for those boxes (0xdf preferred) and understand the steps or see ippsec.rocks walk through videos to understand not just the steps taken to solve but also **WHY** was that step taken. The WHY is really important to make sure you progress further. After understanding, try again to solve them on your own based on the things you have understood from resources.


---

_1. Enumeration > Exploitation (every single time)_

Avoid the habit of randomly throwing exploits at a target.

Proper enumeration:

•	Builds a mental model of the system

•	Narrows realistic attack paths

•	Saves time by eliminating guesswork

Poor enumeration leads to rabbit holes, repeated loops, and unnecessary stress.

Take notes for every enumeration step, even findings that look boring. Many exploitation paths only become clear when small details are connected later. And sometimes, once you step back and review your notes, you realize the solution is actually simpler than it first appeared.

_2. Notes are non-negotiable (during prep and the exam)_

A common mistake:

“I’ll solve a few machines first and organize notes later.”

Avoid this.

Why? • You forget why you ran a command

•	You repeat the same dead ends

•	You lose time rebuilding context

Instead:

•	Take notes while solving

•	Record commands, outputs, assumptions, failures, and conclusions

•	Write why you ran something, not just what you ran


_3. Learn concepts, not just tools_

Tools help, but they don’t replace understanding.

•	Don’t depend on one tool

•	Learn what the tool is doing underneath

•	Know when, why, and with which options to use it

Blindly running commands rarely works unless enumeration already pointed you there.

_4. Community resources worth using (responsibly)_

These were genuinely helpful during preparation:

•	Lainkusanagi

•	TJ Null

  •	Offsec Discord

•	s1ren & IppSec: walkthroughs with strong emphasis on reasoning and note-taking

---

## 🚫 What NOT to Study

Offensive security is big and you can be overwhelmed at the amount of material. Focus on what's in PEN-200. Skip these:

- **Advanced AD attacks** (stay with the basics)
- **Phishing** (not on the exam)
- **EDR/AV evasion** (boxes won't have EDR or AV)
- **Network attacks** (Responder, ARP poisoning, bettercap)
- **Metasploit deep dives** (you don't need modules beyond basics)

**Rabbit hole warning:** If you are modifying an exploit beyond changing your IP address, you are in a rabbit hole. Move on.




---

## ⚠️ Exam Restrictions

[](https://github.com/jeffaf/oscp-prep-checklist#%EF%B8%8F-exam-restrictions)

**Metasploit Rules:**

- `msfvenom` + `multi/handler` = OK on ALL machines
- Modules (Auxiliary/Exploit/Post) + Meterpreter = ONE machine only
- Once you use modules on a target, you're locked to that target
- Can't use for pivoting (would touch multiple targets)

**Banned Tools:**

- SQLmap, SQLninja, auto-exploitation tools
- Mass scanners (Nessus, OpenVAS, etc.)
- AI chatbots (ChatGPT, OffSec KAI, etc.)
- Commercial tools (Burp Pro, Metasploit Pro, etc.)



