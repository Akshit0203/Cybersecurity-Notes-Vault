
---

Enumeration > Exploitation (every single time)_\

Avoid the habit of randomly throwing exploits at a target.

Proper enumeration:
•	Builds a mental model of the system
•	Narrows realistic attack paths
•	Saves time by eliminating guesswork

Poor enumeration leads to rabbit holes, repeated loops, and unnecessary stress.

Take notes for every enumeration step, even findings that look boring. Many exploitation paths only become clear when small details are connected later. And sometimes, once you step back and review your notes, you realize the solution is actually simpler than it first appeared.

**Enumeration is not a step — it’s the whole exam.** Miss a UDP port, miss a service, miss the foothold that was sitting right there. Most rabbit holes exist because you didn’t enumerate thoroughly enough at the start. Go back to basics before you decide the machine is just hard.

**Build a checklist, not just notes.** Notes are for learning. Checklists are for performing under pressure. There’s a real difference — build both.

---

Don’t only understand how to exploit a vulnerability, but also understand how the underlying technologies work (e.g how AD works, how relational databases store data, how APIs work)

Learn concepts, not just tools
Tools help, but they don’t replace understanding.

•	Don’t depend on one tool
•	Learn what the tool is doing underneath
•	Know when, why, and with which options to use it

Blindly running commands rarely works unless enumeration already pointed you there.

As the saying goes _"If you can't explain it simply, you don't understand it well enough_".

---

It’s really about focusing on learning and making sure you do a lot of boxes/labs.
note making was always more important than just solving machines. Including the writeups of all the boxes you have solved

For eg, if I am learning Windows Privesc, I will side by side get hands on by solving Windows Boxes. 
I also made a write up kind of notes for all the boxes I have solved for my personal reference and get skill of solving & documenting at the same time. 
This is also VERY important as in future , if you encounter a same service in any other box, you can easily search through it and use the same commands and steps.

In the starting of your HTB solving, if you fail to solve the complete boxes, it is completely fine, all of us do. But also keep in mind the steps when you are not able to solve boxes, check write up for those boxes (0xdf preferred) and understand the steps or see ippsec.rocks walk through videos to understand not just the steps taken to solve but also **WHY** was that step taken. The WHY is really important to make sure you progress further. After understanding, try again to solve them on your own based on the things you have understood from resources.

----

Notes are non-negotiable (during prep and the exam)

<span style="color:rgb(255, 0, 0)">A common mistake:<br>“I’ll solve a few machines first and organize notes later.”</span>
Avoid this.

Why? 
• You forget why you ran a command
•	You repeat the same dead ends
•	You lose time rebuilding context

Instead:
•	<span style="color:rgb(255, 0, 0)">Take notes while solving</span>
•	Record commands, outputs, assumptions, failures, and conclusions
•	Write why you ran something, not just what you ran

---




