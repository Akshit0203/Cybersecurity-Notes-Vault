# Kerbrute, AS-REP Roasting & Kerberoasting

## Kerbrute

Kerbrute is a tool used to enumerate Active Directory usernames and test authentication against Kerberos. It communicates with the Domain Controller over Kerberos, typically **TCP/UDP port 88**.

### How it works

1. **Provide a username list** — e.g. `users.txt`.
2. **Kerbrute sends Kerberos requests** — the Domain Controller responds to each request.
3. **Interpret responses** — depending on the response, Kerbrute can identify valid usernames or report authentication results.

### Main modes

| Mode | Purpose |
|---|---|
| `userenum` | Find valid domain usernames |
| `passwordspray` | Test one password against multiple users |
| `bruteuser` | Test multiple passwords against one user |
| `bruteforce` | Test username/password combinations |

### Example: username enumeration

```
kerbrute userenum --dc <DC_IP> -d thm.red users.txt
```

- `userenum` — enumerate usernames.
- `--dc <DC_IP>` — specify the Domain Controller's IP address.
- `-d thm.red` — specify the domain.
- `users.txt` — candidate usernames.

> Use this only in your authorized lab environment.

### How Kerbrute decides a username is valid (without a password)

Kerbrute checks whether a username is valid by sending Kerberos authentication requests to the Domain Controller and interpreting its responses. It doesn't need to log in successfully to identify many valid usernames.

**Step by step, behind the scenes** — suppose your wordlist contains:

```
alice
bob
charlie
```

1. **Kerbrute sends a Kerberos request** — it sends an `AS-REQ` for the candidate username to the Domain Controller, commonly on port 88.
2. **The Domain Controller responds** — the response contains a Kerberos result code that can help distinguish a recognized account from an unknown one.
3. **Kerbrute interprets the result:**
   - `alice` — account recognized.
   - `bob` — account not found.
   - `charlie` — account recognized, depending on the response.

   *(These usernames and results are illustrative.)*

### The technical detail: Kerberos error codes

| Response | Meaning |
|---|---|
| `KDC_ERR_C_PRINCIPAL_UNKNOWN` | The requested client principal (username) is unknown to the KDC. |
| `KDC_ERR_PREAUTH_REQUIRED` | Pre-authentication is required; this indicates the KDC recognizes the principal. |
| `KDC_ERR_PREAUTH_FAILED` | Pre-authentication failed; the cause depends on the request and context. |

The important distinction: Kerbrute is analyzing **protocol responses**, not guessing from the username's format.

**Why does this work without a password?** Kerberos must process the requested account before it can determine what authentication requirements apply. Differences in the resulting responses can reveal whether an account exists.

> **Limitation:** Network errors, domain configuration, account policies and other conditions can make results ambiguous. A timeout does **not** mean the username is invalid.

---

## AS-REP Roasting

AS-REP Roasting is an Active Directory attack that lets an attacker obtain password-cracking material for certain domain users **without knowing their passwords first**. It works because some AD accounts have Kerberos pre-authentication disabled (`DONT_REQUIRE_PREAUTH`).

### How it works

1. **Find vulnerable users** — identify accounts with Kerberos pre-authentication disabled (`DONT_REQUIRE_PREAUTH`).
2. **Request authentication data** — send an `AS-REQ` to the Domain Controller without first proving knowledge of the user's password.
3. **Receive the AS-REP response** — the DC returns a response containing encrypted data usable for offline password guessing.
4. **Crack the hash offline** — use tools such as John the Ripper or Hashcat to guess the password without repeatedly contacting the DC.

### Why does it work?

Normally, Kerberos pre-authentication requires a user to prove knowledge of their password before the DC issues the AS-REP response. If pre-authentication is disabled for an account, the DC can return the response *without* that initial proof, and the encrypted portion can then be attacked offline.

AD allows pre-authentication to be disabled for compatibility with certain legacy applications or systems. If an account is configured this way unnecessarily, it creates an opportunity for AS-REP Roasting.

> The vulnerability is **not** that Kerberos encryption is broken. It's that disabling pre-authentication allows an attacker to obtain password-cracking material without first authenticating as that user. The attacker does **not** automatically get the plaintext password — it must usually be recovered through guessing, and a strong password may resist cracking.

### Lab commands

1. Find users without pre-authentication enabled:

```
impacket-GetNPUsers thm.red/ -usersfile users.txt -dc-ip <DC_IP>
```

2. Save the returned `$krb5asrep$23$...` hash into `hash.txt`.

3. Crack it with John:

```
john --wordlist=/usr/share/wordlists/rockyou.txt --format=krb5asrep hash.txt
```

4. Show any recovered password:

```
john --show --format=krb5asrep hash.txt
```

> If John reports `0g`, it means no password was cracked in that run. It doesn't necessarily mean the hash is invalid.

---

## Kerberoasting

**Kerberoastable users** = AD accounts whose service-ticket encryption can be used to try guessing their passwords offline.

Think of it like this:

1. A user account runs a service, such as SQL Server.
2. That account has an **SPN** (Service Principal Name).
3. An authenticated domain user can request a Kerberos service ticket (TGS) for that service.
4. The ticket contains encrypted data that can be used to crack the service account's password offline.
5. If the password is weak, it might be recovered.

**Why does BloodHound show them?** It identifies accounts with SPNs that could be targeted for Kerberoasting.

> **Kerberoastable** doesn't mean the account is already hacked. It means its ticket may be *targeted* for password cracking.

---

## AS-REP Roasting vs Kerberoasting

| Feature | AS-REP Roasting | Kerberoasting |
|---|---|---|
| Target | Users with pre-authentication disabled | Accounts with SPNs |
| Requires valid domain credentials? | Not necessarily | Usually yes |
| What is attacked? | AS-REP response | Service-ticket (TGS) response |
| Main weakness | Pre-authentication disabled | Weak service-account password |

> AS-REP Roasting targets a specific Kerberos configuration weakness. The main defense is to enable Kerberos pre-authentication for accounts wherever possible and enforce strong passwords.

---

## Kerbrute vs AS-REP Roasting (workflow)

- **Kerbrute:** helps discover valid usernames and test Kerberos authentication.
- **AS-REP Roasting:** targets accounts with Kerberos pre-authentication disabled to obtain material for offline password cracking.

**Typical lab workflow:** Enumerate usernames with Kerbrute → identify accounts configured without pre-authentication → test for AS-REP roasting with Impacket's `GetNPUsers`.
