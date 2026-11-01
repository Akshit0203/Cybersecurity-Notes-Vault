
The commands are used to find and exploit misconfigurations in Active Directory Certificate Services (AD CS).

## 1. First, understand the concept

### What is AD CS?

Active Directory is Microsoft's system for managing users, computers, groups, and permissions in a Windows domain.

AD CS is a Windows Server role that allows an organization to issue digital certificates to users and computers.

Think of a certificate as a digital identity card.

![](Pasted%20image%2020261028113045.png)

The security problem occurs when a certificate template is configured so that an ordinary user can obtain a certificate representing a more privileged account.

For example, a low-privileged user might be able to request a certificate identifying themselves as `Administrator`. If the domain accepts that certificate for authentication, the user may gain administrator-level access.

This is the general idea behind AD CS privilege escalation.

## 2. Learn the important terminology

|Term|Simple meaning|
|---|---|
|CA (Certificate Authority)|The service that issues certificates.|
|Certificate template|A reusable set of rules defining who can request a certificate and what it can be used for.|
|Enrollment rights|Which users or groups are allowed to request certificates.|
|UPN|User Principal Name, often formatted like `administrator@corp.local`.|
|PFX file|A file that can contain a certificate and its private key.|
|NT hash|A Windows password-derived hash used in certain authentication mechanisms.|
|ESC1|An AD CS misconfiguration that can allow a requester to obtain a certificate for another identity.|
|Certipy|A tool for discovering and assessing AD CS configurations and vulnerabilities.|

The key distinction: being allowed to request a certificate is not the same as being allowed to request a certificate for any identity. The latter is where dangerous misconfigurations can arise.

## 3. Understand each command in your cheatsheet

### A. Find vulnerable certificate templates

```
certipy-ad find -u 'test@test.local' -p 'test' \
  -dc-ip $target -vulnerable -stdout
```

What it does: Connects to the domain and searches AD CS for certificate templates that Certipy identifies as potentially vulnerable.

- `find` — enumerate AD CS.
    
- `-u` — domain username.
    
- `-p` — user's password.
    
- `-dc-ip` — IP address of the domain controller.
    
- `-vulnerable` — focus on templates with recognized vulnerability conditions.
    
- `-stdout` — print results in the terminal.
    

What you're looking for: A template that ordinary domain users can enroll in and that has a dangerous combination of identity and certificate settings.

This is your discovery stage, not exploitation itself.

### B. Save the enumeration results

Your screenshot contains this command:

```
certipy-ad find -u test@test.local -p 'test' \
  -dc-ip $target -text > output_certs
```

The intention is to save the enumeration output to a file so you can review it.

The `>` symbol is shell redirection: it writes command output to a file instead of displaying it normally.

You can then search the saved results:

```
cat -n output_certs
```

The next command in the screenshot uses `grep` to search around lines containing `enrollment rights`.

Important: Certipy command-line options differ between versions. Check `certipy-ad find -h` if `-text` isn't accepted by your installed version.

### C. Understand enrollment rights

Suppose your output says:

```
Enrollment Rights:
  Domain Users
```

This means members of Domain Users may request certificates using that template, subject to its other restrictions.

That alone does not prove a vulnerability.

For an ESC1 assessment, examine whether the template:

- Allows low-privileged users to enroll.
    
- Allows the requester to supply an alternative subject identity or UPN.
    
- Supports authentication through the issued certificate.
    
- Has the other conditions required for the attack.
    

The combination of settings matters more than any single line.

## 4. What does “Forge certificate” mean?

The command in your screenshot is:

```
certipy req -u 'test@test.local' -p 'test' \
  -dc-ip '10.0.0.100' \
  -target 'CA.TEST.LOCAL' \
  -ca 'TEST-CA' \
  -template 'UserTemplate' \
  -upn 'Administrator@corp.local'
```

This requests a certificate through a certificate authority using a particular template and specifies the identity the certificate should represent.

Here's what each argument means:

|Argument|Purpose|
|---|---|
|`req`|Request a certificate.|
|`-u` / `-p`|Credentials of the account making the request.|
|`-dc-ip`|Domain controller IP.|
|`-target`|Hostname of the certificate authority server.|
|`-ca`|Certificate authority name.|
|`-template`|Certificate template to request.|
|`-upn`|UPN identity to place in the request, when the template permits it.|

The sample names are placeholders. They must match the actual domain, CA, and template you discover.

Why is the UPN important?

Normally, your certificate should identify you. If the template allows you to request a certificate representing another account, and the CA accepts that request, the resulting certificate could authenticate as that account.

This is the central identity-misconfiguration issue behind ESC1.

## 5. What happens when Certipy authenticates with a PFX?

```
certipy auth -pfx 'administrator.pfx' -dc-ip '10.0.0.100'
```

This uses the certificate and private key in the PFX file to attempt certificate-based authentication.

Conceptually, the process is:

1. PFX file

Contains the certificate and private key.

2. Certificate authentication

The domain validates the certificate and its identity.

3. Authentication result

Depending on the environment, Certipy may obtain the account's NT hash.

A successful certificate authentication does not automatically guarantee that Certipy can retrieve an NT hash; that depends on the domain's configuration and authentication flow.

## 6. What does “get shell with psexec next” mean?

Impacket's `psexec.py` can provide a remote command shell when the supplied account has the necessary administrative privileges and the target permits the required SMB and service operations.

The general syntax is:

```
impacket-psexec 'DOMAIN/Administrator'@TARGET_IP -hashes ':NT_HASH'
```

Here, `NT_HASH` is the recovered NT hash. This technique uses pass-the-hash rather than a plaintext password.

It is a separate stage from AD CS exploitation: first obtain valid authentication material, then establish a remote session using an account with sufficient privileges.

## 7. Memorize the workflow

1. Find

Enumerate AD CS and identify suspicious templates.

2. Analyze

Check enrollment permissions, identity controls, and authentication settings.

3. Request

Assess whether the template improperly permits certificates for other identities.

4. Authenticate

Test whether the issued certificate can authenticate as the intended identity.

5. Verify access

Confirm the effective privileges and document the impact.

The most important takeaway for OSCP preparation: don't memorize only the commands. Learn to recognize why a certificate template is vulnerable, what evidence confirms the misconfiguration, and how certificate-based authentication differs from password-based authentication.

Official reference: [Certipy Usage](https://github.com/ly4k/Certipy/wiki/05-%E2%80%90-Usage?utm_source=chatgpt.com) · [Certipy Privilege Escalation](https://github.com/ly4k/Certipy/wiki/06-%E2%80%90-Privilege-Escalation?utm_source=chatgpt.com)

