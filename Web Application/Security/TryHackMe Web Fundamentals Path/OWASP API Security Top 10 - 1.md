# OWASP API Security Top 10 — Part 1

> [!info] Topics Covered
> 1. [[#Task 1 Introduction|Introduction & API Refresher]]
> 2. [[#Task 2 API1 — Broken Object Level Authorisation (BOLA)|API1 — Broken Object Level Authorisation (BOLA)]]
> 3. [[#Task 3 API2 — Broken User Authentication (BUA)|API2 — Broken User Authentication (BUA)]]
> 4. [[#Task 4 API3 — Excessive Data Exposure|API3 — Excessive Data Exposure]]
> 5. [[#Task 5 API4 — Lack of Resources & Rate Limiting|API4 — Lack of Resources & Rate Limiting]]
> 6. [[#Task 6 API5 — Broken Function Level Authorisation (BFLA)|API5 — Broken Function Level Authorisation (BFLA)]]

---

# Task 1 Introduction

**Open Worldwide Application Security Project (OWASP)** is a non-profit, collaborative online community that aims to improve application security via security principles, articles, and documentation.

## Understanding APIs — A Refresher

An **API** (Application Programming Interface) is a messenger that allows two different software programs to talk to each other.

- **Application** → any software or app (like Instagram, a weather app, etc.)
- **Interface** → the connection or bridge that lets them exchange data

### Why Are APIs Important?

- **Connects** different apps or systems easily.
- Helps developers **reuse code** instead of building everything from scratch.
- Makes it easy to **integrate** services (payment gateways, weather data, Google Maps, etc.).
- It's a **building block** for modern software — without APIs, apps couldn't talk to each other or share data efficiently.

### API Documentation

API documentation is **not trivial** and is **very important even after development**. It helps developers:

- Understand how to **use** the API (endpoints, parameters, responses).
- **Debug** issues or make updates later.
- Allow **other teams or third-party developers** to integrate with the API easily.

---

# Task 2 API1 — Broken Object Level Authorisation (BOLA)

## What Is BOLA?

BOLA (a.k.a. **IDOR**) happens when an API lets you request objects (like `/users/{id}`) **without properly checking whether the requester is allowed to access that specific object**.

## How It Happens

1. API exposes endpoints that use object IDs (e.g., `/users/1`, `/invoices/42`).
2. The endpoint checks _that the request is authenticated_ (maybe) but **does not verify the requester is the owner** of the requested object.
3. An attacker changes the ID (e.g., `1 → 2 → 3`) and the API returns other users' data because the server never checked ownership.

## Likely Impact

- **Data leakage** — private user data shown to others.
- **Account takeover** — if the API returns session tokens or sensitive info.
- **Reputation & legal damage** — if customer/personal data is exposed.

## Practical Example

![Pasted image 20251101110417.png](attachments/Pasted%20image%2020251101110417.png)

In the VM, if you add a valid `Authorization-Token` and call `http://localhost:80/MHT/apirule1_s/user/1`, only then will you be able to get the correct results. All API calls with an invalid token will show `403 Forbidden` (as shown below).

![Image for Secure Request BOLA](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/d7276bdd5c3d6fe7b6eea7731d261210.png)

## Mitigation Measures

- Implement an authorisation mechanism that relies on **user policies and hierarchies**.
- Enforce **strict access controls** to check if the logged-in user is authorised to perform specific actions.
- Use **completely random, unpredictable tokens** (strong encryption/decryption mechanisms).

---

# Task 3 API2 — Broken User Authentication (BUA)

## What Is BUA?

Broken User Authentication reflects a scenario where an API endpoint allows an attacker to access a database or acquire a higher privilege than the existing one.

The primary cause is either **invalid implementation of authentication** (e.g., using incorrect email/password queries) or the **absence of security mechanisms** (authorisation headers, tokens, etc.).

## How It Happens

APIs usually authenticate with something like:

```json
{
  "email": "user@example.com",
  "password": "mypassword"
}
```

If the developer **forgets to check the password properly**, or **doesn't use secure tokens**, then anyone who knows your email can log in as you.

> [!warning] Example Mistake
> ```sql
> SELECT * FROM users WHERE email = 'user@example.com';
> ```
> This query only checks the email, **not the password** — so the attacker can enter any password and still log in.

---

# Task 4 API3 — Excessive Data Exposure

## What Is Excessive Data Exposure?

Excessive Data Exposure happens when an API **returns more information than necessary** — including sensitive data — instead of filtering it before sending it to the user.

## How It Happens

- Developers send **entire database objects** in API responses.
- They expect the **front-end** to hide unwanted or sensitive fields (like passwords, tokens, phone numbers).
- Attackers can intercept the raw API response and **see all hidden fields**.

## Practical Example

**Vulnerable scenario** — the API returns all fields from the database:

![Image for Vulnerable Scenario](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/6733955d8ce9471ce57924fb77a8caf6.png)

The issue: the API is sending more data than desired. Instead of relying on a front-end engineer to filter out data, **only relevant data must be sent from the database**.

**Secure scenario** — Bob updated the endpoint to `/apirule3/comment_s/{id}`, which returns only the necessary information:

![Image for Secure Scenario](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/23e044cc3efe648691292fac6f6e4acf.png)

## Mitigation Measures

- Never leave sensitive data filtration tasks to the front-end developer.
- Regularly review API responses to guarantee they return only legitimate data and check for security issues.
- Avoid using generic methods such as `to_string()` and `to_json()`.
- Use API endpoint testing through various test cases; verify through automated **and** manual tests if the API leaks additional data.

> [!caution] Network Devices Are NOT the Answer
> We **should not** rely on network-level devices (firewalls, proxies) to control excessive data exposure.
> 
> Excessive data exposure happens at the **application (API) level**, where sensitive information is included in the response. Network devices **cannot understand or filter business-logic data** inside API responses.
> 
> The right approach is to **control it programmatically** — filter sensitive fields **in the API code itself** before sending the response.

---

# Task 5 API4 — Lack of Resources & Rate Limiting

## What Is It?

This vulnerability happens when an API **doesn't limit how often** users can send requests or **how much data** they can send. Attackers can overload the system — causing it to slow down or crash (a **Denial of Service — DoS**).

## Mitigation Measures

1. **Enable Rate Limiting** — restrict how many requests a user can make per minute/second.
   > Example: "A user can only request an OTP once every 2 minutes."
2. **Use CAPTCHA** — stops bots or scripts from sending automated requests.
3. **Set resource limits** — limit file upload size, input length, and array elements.
4. **Return proper error codes** — e.g., show `429 Too Many Requests` when limits are exceeded.
5. **Monitor and alert** — track unusual traffic spikes to detect DoS attempts.

---

# Task 6 API5 — Broken Function Level Authorisation (BFLA)

## What Is BFLA?

**Broken Function Level Authorisation** happens when an API **doesn't properly check a user's role or permissions** before allowing them to perform an action.

A low-privileged user (e.g., sales) bypasses system checks and gets access to **confidential data by impersonating a high-privileged user (Admin)**.

## How It Happens

- The API has **different functions** for different roles (e.g., admin functions vs. user functions).
- The developer adds a simple flag like `isAdmin=1` or a hidden field to control access.
- The API **trusts the client** instead of checking the user's real role in the database.
- A normal user can change `isAdmin=0` → `isAdmin=1` and gain admin access.
