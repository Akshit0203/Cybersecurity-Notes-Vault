
# Task 1 Introduction

categories that are related to failures in how Identity, Authentication, Authorisation, and Accountability (IAAA) is implemented in the application.

1. A01: Broken Access Control
2. A07: Authentication Failures
3. A09: Logging & Alerting Failures

# Task 2 What is IAAA?

IAAA is a simple way to think about how users and their actions are verified on applications.

if a previous item isn't being performed, you cannot perform the later times. The four items are:
- **Identity** - the unique account (e.g., user ID/email) that represents a person or service.
- **Authentication** - proving that identity (passwords, OTP, passkeys).
- **Authorisation** - what that identity is allowed to do.
- **Accountability** - recording and alerting on who did what, when, and from where.

# Task 3 A01: Broken Access Control

Broken Access Control happens when the server doesn’t properly enforce **who can access what** on every request. A common occurence of this is **IDOR** (Insecure Direct Object Reference): if changing an ID (like `?id=7 → ?id=6`) lets you see or edit someone else’s data, access control is broken.

this shows up as horizontal privilege escalation (same role, other user’s stuff) or vertical privilege escalation (jumping to admin-only actions)

# Task 4 A07: Authentication Failures

Authentication Failures happen when an application can’t reliably verify or bind a user’s identity. Common issues include:

- username enumeration
- weak/guessable passwords (no lockout/rate limits)
- logic flaws in the login/registration flow
- insecure session or cookie handling

break into the `admin` user's account. We know that their username is `admin`, so let's try to fool the application by registering a user with the name of `aDmiN`. Start the static site attached to this task. register your account and log into the admin user's account

# Task 5 A09: Logging & Alerting Failures

When applications don’t record or alert on security-relevant events, defenders can’t detect or investigate attacks.

In practice, failures look like missing authentication events, vague error logs, no alerting on brute-force or privilege changes, short retention, or logs stored where attackers can tamper with them.

# Task 6 Conclusion

- **A01 Broken Access Control:** Enforce server-side checks on **every** request
- **A07 Authentication Failures:** Enforce unique indexes on the canonical form, rate-limit/lock out brute force, and rotate sessions on password/privilege changes.
- **A09 Logging & Alerting Failures:** Log the full auth lifecycle (fail/success, password/2FA/role changes, admin actions), centralise logs off-host with retention, and alert on anomalies (e.g., brute-force bursts, privilege elevation).

