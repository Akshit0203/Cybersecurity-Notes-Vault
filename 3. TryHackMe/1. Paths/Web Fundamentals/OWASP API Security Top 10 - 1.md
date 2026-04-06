## Introduction

Open Worldwide Application Security Project (OWASP) is a non-profit and collaborative online community that aims to improve application security via a set of security principles, articles, documentation etc.

## Understanding APIs - A refresher

An **API** is like a **messenger** that allows two different software programs to talk to each other.

- **Application** → any software or app (like Instagram, weather app, etc.)
    
- **Interface** → the connection or bridge that lets them exchange data

### ⚙️ Why is an API important?

- It **connects** different apps or systems easily.
    
- Helps developers **reuse code** instead of building everything from scratch.
    
- Makes it easy to **integrate** services (like payment gateways, weather data, or Google Maps).
    
- It’s a **building block** for modern software — without APIs, apps couldn’t talk to each other or share data efficiently.

API documentation is **not trivial** and is **very important even after development**.

It helps developers:

- Understand how to **use** the API (endpoints, parameters, responses).
    
- **Debug** issues or make updates later.
    
- Allow **other teams or third-party developers** to integrate with the API easily.

## Vulnerability I - Broken Object Level Authorisation (BOLA)

### What is BOLA (one line)
BOLA (a.k.a. IDOR) happens when an API lets you request objects (like `/users/{id}`) **without properly checking whether the requester is allowed to access that specific object**.
### Step-by-step: how it happens
1. API exposes endpoints that use object IDs (e.g., `/users/1`, `/invoices/42`).
    
2. The endpoint checks _that the request is authenticated_ (maybe) but **does not verify the requester is the owner** of the requested object.
    
3. An attacker changes the ID (e.g., `1 → 2 → 3`) and the API returns other users’ data because the server never checked ownership.
### Likely impact
- **Data leakage** (private user data shown to others).
    
- **Account takeover** if the API returns session tokens or sensitive info.
    
- **Reputation & legal damage** if customer/personal data is exposed.

![Pasted image 20251101110417.png](attachments/Pasted%20image%2020251101110417.png)

- In the VM, if you add a valid `Authorization-Token` and call `http://localhost:80/MHT/apirule1_s/user/1`, only then will you be able to get the correct results. Moreover, all API calls with an invalid token will show `403 Forbidden` an error message (as shown below).  
    

![Image for Secure Request BOLA](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/d7276bdd5c3d6fe7b6eea7731d261210.png)

**Mitigation Measures**

- An authorisation mechanism that relies on user policies and hierarchies should be adequately implemented. 
- Strict access controls methods to check if the logged-in user is authorised to perform specific actions. 
- Promote using completely random values (strong encryption and decryption mechanism) for nearly impossible-to-predict tokens.

## Vulnerability II - Broken User Authentication (BUA)

Broken User Authentication (BUA) reflects a scenario where an API endpoint allows an attacker to access a database or acquire a higher privilege than the existing one. 

The primary reason behind BUA is either **invalid implementation of authentication** like using incorrect email/password queries etc., or the absence of security mechanisms like authorisation headers, tokens etc.
### ⚙️ How it happens (in simple terms)
APIs usually ask for something like:

`{   "email": "user@example.com",   "password": "mypassword" }`

If the developer **forgets to check the password properly**, or **doesn’t use secure tokens**, then anyone who knows your email can log in as you.

💀 **Example mistake:**

`SELECT * FROM users WHERE email = 'user@example.com';`

⬆️ This query only checks the email, **not the password** — so the attacker can enter any password and still log in.


## Vulnerability III - Excessive Data Exposure

**Definition:**  
Excessive Data Exposure happens when an API **returns more information than necessary** — including sensitive data — instead of filtering it before sending it to the user.

---

**🧠 How it Happens:**

- Developers send **entire database objects** in API responses.
    
- They expect the **front-end** to hide unwanted or sensitive fields (like passwords, tokens, phone numbers).
    
- Attackers can intercept the raw API response and **see all hidden fields**.

![Image for Vulnerable Scenario](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/6733955d8ce9471ce57924fb77a8caf6.png)  

- What is the issue here? The API is sending more data than desired. Instead of relying on a front-end engineer to filter out data, only relevant data must be sent from the database.
- Bob realising his mistake, updated the endpoint and created a valid endpoint `/apirule3/comment_s/{id}` that returns only the necessary information to the developer (as shown below).

![Image for Secure Scenario](https://tryhackme-images.s3.amazonaws.com/user-uploads/62a7685ca6e7ce005d3f3afe/room-content/23e044cc3efe648691292fac6f6e4acf.png)  

**Mitigation Measures** 

- Never leave sensitive data filtration tasks to the front-end developer. 
- Ensure time-to-time review of the response from the API to guarantee it returns only legitimate data and checks if it poses any security issue. 
- Avoid using generic methods such as `to_string() and to_json()`. 
- Use API endpoint testing through various test cases and verify through automated and manual tests if the API leaks additional data.

❌ **Nay** — we **should not** rely on network-level devices to control excessive data exposure.

✅ **Reason:**  
Excessive data exposure happens at the **application (API) level**, where sensitive information is included in the response.  
Network devices (like firewalls or proxies) **cannot understand or filter business logic data** inside API responses.

🔹 The right approach is to **control it programmatically** — filter sensitive fields **in the API code itself** before sending the response.

## Vulnerability IV - Lack of Resources & Rate Limiting

This vulnerability happens when an **API doesn’t limit how often** users can send requests or **how much data** they can send.  
As a result, attackers can overload the system — causing it to slow down or even crash (a **Denial of Service – DoS**).

🛡️ **Mitigation Measures**
1. ✅ **Enable Rate Limiting** – restrict how many requests a user can make per minute/second.
    
    > Example: “A user can only request an OTP once every 2 minutes.”
    
2. ✅ **Use CAPTCHA** – stops bots or scripts from sending automated requests.
    
3. ✅ **Set resource limits** – limit file upload size, input length, and array elements.
    
4. ✅ **Add API response for limits** – e.g., show `429 Too Many Requests` when exceeded.
    
5. ✅ **Monitor and alert** – track unusual traffic spikes to detect DoS attempts.


## Vulnerability V - Broken Function Level Authorisation

### 🧠 **What It Means**

**Broken Function Level Authorisation (BFLA)** happens when an API **doesn’t properly check a user’s role or permissions** before allowing them to perform an action.

Broken Function Level Authorisation reflects a scenario where a low privileged user (e.g., sales) bypasses system checks and gets access to **confidential data by impersonating a high privileged user (Admin)**.

---

### ⚙️ **How It Happens**

- The API has **different functions** for different roles (e.g., admin functions vs user functions).
    
- The developer adds a simple flag like `isAdmin=1` or a hidden field to control access.
    
- The API **trusts the client** instead of checking the user’s real role in the database.
    
- So, a normal user can change `isAdmin=0` ➜ `isAdmin=1` and gain admin access.

