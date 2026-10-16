In Active Directory, **Local Administrator**, **Domain Admin**, and **Domain Controller** are three different things. Understanding their differences is extremely important for OSCP Active Directory labs.

The most important distinction up front:

- **Local Admin** = Administrative control over *one computer*.
- **Domain Admin** = Administrative control over *most of the AD domain*.
- **Domain Controller (DC)** = The *server* that manages Active Directory and authentication.

---

## 1. The core terms

| Term | What is it? | Access |
|---|---|---|
| Standard Domain User | AD user account | Resources permitted to that user |
| Local Administrator | Privileged account or group membership on a computer | Administrative control over that computer |
| Domain Admin | Member of the AD Domain Admins group | Broad administrative control across the domain |
| Domain Controller | Windows server running Active Directory Domain Services | Hosts AD database and authentication services |
| Enterprise Admin | Highly privileged group in an AD forest | Administrative control across domains in the forest |

---

## 2. Example AD environment

Imagine your OSCP lab has three machines:

- **CLIENT01 — Workstation**
  You compromise a local Administrator account. You control CLIENT01, but not automatically the other machines.
  → *Further enumeration and lateral movement*

- **SERVER01 — Member Server**
  You obtain another privileged session. You might discover credentials or AD permissions that lead to higher privileges.
  → *Domain privilege escalation*

- **DC01 — Domain Controller**
  You gain administrative control over the DC, potentially compromising the entire domain.

---

## 3. Domain Admin vs Domain Controller

This is where people often get confused.

> **Domain Admin is a privilege level, whereas Domain Controller is a machine role.**

For example:

- `THM\Administrator` could be a Domain Admin account.
- `DC01.thm.local` could be the Domain Controller.

If you compromise the Domain Admin account, you generally have enough privileges to administer the DC.

But compromising a normal domain user does **not** make you a Domain Admin, even if that user can log in to a domain-joined computer.

---

## 4. What does SYSTEM mean?

You may have seen:

```
whoami
```

Output:

```
nt authority\system
```

This means your process is running as **LOCAL SYSTEM**, one of the highest privilege levels *on that Windows machine*.

However, SYSTEM on a workstation is **not** automatically Domain Admin:

| What you obtained | What it means |
|---|---|
| `CLIENT01\Administrator` | Local admin on CLIENT01 |
| `NT AUTHORITY\SYSTEM` on CLIENT01 | Very high local privileges on CLIENT01 |
| `THM\DomainAdminUser` with Domain Admin membership | Domain-wide administrative privileges |
| `NT AUTHORITY\SYSTEM` on DC01 | Extremely sensitive control over the Domain Controller |

SYSTEM on a Domain Controller is especially powerful because the DC hosts the Active Directory database and critical authentication secrets.

---

## 5. Which one is the highest?

For a typical single-domain AD environment:

| Level | Scope |
|---|---|
| Domain User | Normal domain access |
| Local Administrator | One computer |
| SYSTEM on member server | Very high control over that server |
| Domain Admin | Broad domain administration |
| SYSTEM on Domain Controller | Direct high-privilege control over a critical domain server |

This isn't a strict universal ranking. Domain Admin and SYSTEM on a DC represent *different types* of control, and an Enterprise Admin can have broader forest-level authority.

**Quick mental model for OSCP:**

- **Local Admin:** I control this computer.
- **SYSTEM:** I have very high privileges on this computer.
- **Domain Admin:** I have administrative privileges across the domain.
- **Domain Controller:** This is the server that runs AD.
- **DC compromise:** I control a critical server that stores and manages domain authentication information.

The key distinction is **privileges vs machines**: Domain Admin is a privileged group membership, while Domain Controller is a server role.

---

## 6. OSCP Active Directory attack path — in order

1. **Enumeration** — Discover domain, users, groups, computers and services.
2. **Initial Foothold** — Obtain initial access or valid credentials.
3. **Credential Attacks** — AS-REP Roasting, Kerberoasting, password reuse.
4. **Privilege Escalation** — Exploit Windows misconfigurations, services or permissions → Local Admin / SYSTEM.
5. **Credential Dumping** — Find credentials, hashes and tickets.
6. **BloodHound Analysis** — Identify AD attack paths and excessive permissions.
7. **Lateral Movement** — Access other domain computers using discovered credentials.
8. **AD / Domain Privilege Escalation** — Abuse ACLs, delegation, GPOs or other misconfigurations.
9. **Domain Compromise** — Obtain the required high-level access, potentially Domain Admin or control of a Domain Controller.
10. **Proof / Reporting** — Collect required proof and document the attack path.

> These steps aren't always strictly linear. Enumeration and credential discovery repeat throughout the assessment. Local Admin on the first machine is not always necessary — sometimes you can move laterally directly from a normal domain user. You do **not** always need Domain Admin or DC compromise to complete an OSCP objective; the required proof and target determine when you're done.

---

## 7. Domain Privilege Escalation vs Domain Admin / DC Compromise

The difference is simple: **Domain Privilege Escalation is the *process*; Domain Admin / DC Compromise is the *result*.**

### Domain Privilege Escalation (the process)

You exploit misconfigured AD permissions to gain more privileges. Examples:

- **ACL abuse** — exploit excessive permissions on AD objects.
- **GPO abuse** — modify a policy that affects domain computers.
- **Delegation abuse** — misuse Kerberos delegation permissions.
- **Obtain credentials** for a privileged domain account.

You might go from a normal domain user to controlling a server or gaining powerful domain privileges.

### Domain Admin / DC Compromise (the result)

You've reached the high-privilege outcome:

- **Domain Admin:** administrative privileges across the domain.
- **DC compromise:** high-level control of a Domain Controller.

### Simple example

```
Initial foothold → Local Admin → Find exploitable GPO → Abuse GPO → Domain Admin privileges or control of the DC
```

> ACLs, GPOs and delegation are *possible* ways to escalate. Domain Admin or DC compromise is a *possible* end result — but not every escalation leads to it, and the escalation step can be the last step if your exploitation immediately grants Domain Admin access. Stop when you've achieved the required exam objective.
