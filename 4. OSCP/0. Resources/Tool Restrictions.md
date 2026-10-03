
You may however, use tools such as Nmap (and its scripting engine), Nikto, Burp Free, DirBuster etc. against any of your target systems.

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

<span style="color:rgb(11, 142, 224)">You may however, use tools such as Nmap (and its scripting engine), Nikto, Burp Free, DirBuster etc. against any of your target systems.</span>

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

