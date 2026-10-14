In Active Directory, Local Administrator, Domain Admin, and Domain Controller are three different things. Understanding their differences is extremely important for OSCP Active Directory labs.

The most important distinction is:

- Local Admin = Administrative control over one computer.
    
- Domain Admin = Administrative control over most of the AD domain.
    
- Domain Controller (DC) = The server that manages Active Directory and authentication.
    

## 1. Difference between Local Admin, Domain Admin and Domain Controller

|Term|What is it?|Access|
|---|---|---|
|Standard Domain User|AD user account|Resources permitted to that user|
|Local Administrator|Privileged account or group membership on a computer|Administrative control over that computer|
|Domain Admin|Member of the AD Domain Admins group|Broad administrative control across the domain|
|Domain Controller|Windows server running Active Directory Domain Services|Hosts AD database and authentication services|
|Enterprise Admin|Highly privileged group in an AD forest|Administrative control across domains in the forest|

## 2. Example AD environment

Imagine your OSCP lab has three machines:

CLIENT01 — Workstation

You compromise a local Administrator account. You control CLIENT01, but not automatically the other machines.

Further enumeration and lateral movement

SERVER01 — Member Server

You obtain another privileged session. You might discover credentials or AD permissions that lead to higher privileges.

Domain privilege escalation

DC01 — Domain Controller

You gain administrative control over the DC, potentially compromising the entire domain.

## 3. What is the difference between Domain Admin and Domain Controller?

This is where people often get confused.

Domain Admin is a privilege level, whereas Domain Controller is a machine role.

For example:

`THM\Administrator` could be a Domain Admin account.

`DC01.thm.local` could be the Domain Controller.

If you compromise the Domain Admin account, you generally have enough privileges to administer the DC.

But compromising a normal domain user does not make you a Domain Admin, even if that user can log in to a domain-joined computer.

## 4. What does SYSTEM mean?

You may have seen:

```
whoami
```

Output:

```
nt authority\system
```

This means your process is running as LOCAL SYSTEM, one of the highest privilege levels on that Windows machine.

However:

SYSTEM on a workstation is not automatically Domain Admin.

|What you obtained|What it means|
|---|---|
|`CLIENT01\Administrator`|Local admin on CLIENT01|
|`NT AUTHORITY\SYSTEM` on CLIENT01|Very high local privileges on CLIENT01|
|`THM\DomainAdminUser` with Domain Admin membership|Domain-wide administrative privileges|
|`NT AUTHORITY\SYSTEM` on DC01|Extremely sensitive control over the Domain Controller|

SYSTEM on a Domain Controller is especially powerful because the DC hosts the Active Directory database and critical authentication secrets.

## 5. What is the final goal in OSCP Active Directory?

For many traditional AD attack-path labs, the progression looks like this:

Initial foothold

Low-privileged user or shell

Local privilege escalation

Local Administrator / SYSTEM

Lateral movement

Access another domain computer

Domain privilege escalation

Obtain powerful AD permissions or credentials

Domain Controller compromise

Administrative control of the DC, when that is the lab's objective

Important for OSCP: The actual exam objective is to obtain the required proof and meet the specific machine or challenge requirements. You should not assume that obtaining Domain Admin membership is always required, or that it automatically completes every AD challenge.

For example, a lab might require you to gain a privileged shell on the Domain Controller and retrieve a proof file.

## 6. Which one is the highest?

For a typical single-domain AD environment:

|Level|Scope|
|---|---|
|Domain User|Normal domain access|
|Local Administrator|One computer|
|SYSTEM on member server|Very high control over that server|
|Domain Admin|Broad domain administration|
|SYSTEM on Domain Controller|Direct high-privilege control over a critical domain server|

This isn't a strict universal ranking. Domain Admin and SYSTEM on a DC represent different types of control, and an Enterprise Admin can have broader forest-level authority.

Remember for OSCP:

- Local Admin: I control this computer.
    
- SYSTEM: I have very high privileges on this computer.
    
- Domain Admin: I have administrative privileges across the domain.
    
- Domain Controller: This is the server that runs AD.
    
- DC compromise: I control a critical server that stores and manages domain authentication information.
    

The key distinction is privileges versus machines: Domain Admin is a privileged group membership, while Domain Controller is a server role.

