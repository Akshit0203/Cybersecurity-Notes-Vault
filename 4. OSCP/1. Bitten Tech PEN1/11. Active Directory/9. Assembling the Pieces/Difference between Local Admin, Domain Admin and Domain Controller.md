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

## OSCP Active Directory Attack Path — In Order

1. Enumeration — Discover domain, users, groups, computers and services.
    
2. Initial Foothold — Obtain initial access or valid credentials.
    
3. Credential Attacks — AS-REP Roasting, Kerberoasting, password reuse.
    
4. Privilege Escalation — Exploit Windows misconfigurations, services or permissions.
    
5. Credential Dumping — Find credentials, hashes and tickets.
    
6. BloodHound Analysis — Identify AD attack paths and excessive permissions.
    
7. Lateral Movement — Access other domain computers using discovered credentials.
    
8. AD Privilege Escalation — Abuse ACLs, delegation, GPOs or other misconfigurations.
    
9. Domain Compromise — Obtain the required high-level access, potentially Domain Admin or control of a Domain Controller.
    
10. Proof / Reporting — Collect required proof and document the attack path.
    

Remember: These steps aren't always strictly linear. Enumeration and credential discovery repeat throughout the assessment. You do not always need Domain Admin or Domain Controller compromise to complete an OSCP objective.

1. Initial Foothold
    
2. Local Privilege Escalation → Local Admin / SYSTEM
    
3. Credential Dumping
    
4. Lateral Movement → Other machines
    
5. AD Enumeration → BloodHound
    
6. Domain Privilege Escalation → ACLs, GPOs, Delegation
    
7. Domain Admin / DC Compromise
    
8. Capture Proofs

The difference is simple: Domain Privilege Escalation is the process; Domain Admin / DC Compromise is the result.

### 1. Domain Privilege Escalation

You exploit misconfigured AD permissions to gain more privileges.

Examples:

- ACL abuse — exploit excessive permissions on AD objects.
    
- GPO abuse — modify a policy that affects domain computers.
    
- Delegation abuse — misuse Kerberos delegation permissions.
    

You might go from a normal domain user to controlling a server or gaining powerful domain privileges.

### 2. Domain Admin / DC Compromise

You've reached the high-privilege outcome.

- Domain Admin: You have administrative privileges across the domain.
    
- DC compromise: You obtain high-level control of a Domain Controller.
    

### Simple example

`Initial foothold → Local Admin → Find exploitable GPO → Abuse GPO → Domain Admin privileges or control of the DC`

Remember: ACLs, GPOs and delegation are possible ways to escalate. Domain Admin or DC compromise is a possible end result—but not every escalation leads to it.

Yes, that's the basic flow for many OSCP Active Directory labs, but there can be extra steps.

1. Initial Foothold → Gain access as a normal user.
    
2. Local Privilege Escalation → Become Local Admin / SYSTEM on the first machine.
    
3. Lateral Movement → Access another machine using discovered credentials or attack paths.
    
4. Domain Privilege Escalation → Abuse AD permissions, GPOs, or delegation.
    
5. Domain Admin / DC Compromise → Reach the required domain-level objective.
    

Remember: Local Admin on the first machine is not always necessary. Sometimes you can move laterally directly from a normal domain user.

The difference is Step 4 is how you gain more privileges; Step 5 is the final level of access you achieve.

### Step 4 — Domain Privilege Escalation

You exploit an Active Directory weakness to gain higher privileges.

Examples:

- Abuse ACL permissions
    
- Modify a vulnerable GPO
    
- Exploit Kerberos delegation
    
- Obtain credentials for a privileged domain account
    

You might gain Domain Admin privileges during this step.

### Step 5 — Domain Admin / DC Compromise

You have achieved the high-level objective.

- Domain Admin: You have administrative privileges across the domain.
    
- DC compromise: You have high-level control over the Domain Controller.
    

### Simple analogy

`Step 3: Access another machine → Step 4: Exploit AD permissions → Step 5: Achieve domain-level control`

Remember: Step 4 is the attack process; Step 5 is the result. You don't necessarily need separate steps if your exploitation immediately grants Domain Admin access.

Yes, you've got it! Step 4 can be the last step. Step 5 is just the outcome, not necessarily a separate step.

Your OSCP AD flow can simply be:

1. Initial Foothold → Normal user access
    
2. Local Privilege Escalation → Local Admin / SYSTEM
    
3. Lateral Movement → Access another machine
    
4. Domain Privilege Escalation → Gain Domain Admin or compromise the Domain Controller
    

That's it. You stop when you've achieved the required exam objective. You don't always need Domain Admin; the required proof and target determine when you're done.

