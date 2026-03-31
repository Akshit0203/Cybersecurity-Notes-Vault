
**difference between Hybrid users and Federated users** in **Azure AD (now Microsoft Entra ID)**:

---

## ⚙️ **1. Hybrid Users (Synchronized Users)**

### 🔹 **Definition:**

A **hybrid user** is an account that **originates in on-premises Active Directory (AD)** and is **synchronized to Azure AD** using **Azure AD Connect**.

### 🔹 **How Authentication Works:**

There are 3 main authentication models for hybrid users:

|Authentication Method|Description|Auth Process|
|---|---|---|
|**Password Hash Synchronization (PHS)**|On-prem password hash (not actual password) is synced to Azure AD.|User authenticates **directly in Azure AD** using cloud password hash.|
|**Pass-Through Authentication (PTA)**|Azure AD forwards authentication request to an on-prem agent.|Authentication happens **on-premises AD** via agent, but sign-in is cloud-based.|
|**Federation (AD FS)**|Azure AD redirects authentication to on-prem federation server.|User authenticates via **AD FS** using on-prem credentials.|

So, hybrid users **can** be federated too — federation is just one of the authentication options.

### 🔹 **Example:**

- Your organization has `user@company.local` in on-prem AD.
    
- Azure AD Connect syncs it to cloud as `user@company.com`.
    
- The identity source = _Windows Server AD_ (Hybrid).
    

---

## 🌐 **2. Federated Users**

### 🔹 **Definition:**

A **federated user** is one whose **authentication happens through a federation service**, such as:

- **Active Directory Federation Services (AD FS)**
    
- **PingFederate**
    
- **Okta**
    
- **Shibboleth**
    
- **Other SAML/OAuth providers**
    

The federation service acts as a **trusted Identity Provider (IdP)**. Azure AD **redirects** login requests to that IdP, which validates credentials and returns a security token.

### 🔹 **How Authentication Works:**

1. User tries to sign in to Azure AD.
    
2. Azure AD detects the domain is federated.
    
3. The user is redirected to the on-premises AD FS (or other IdP).
    
4. AD FS validates the credentials and returns a SAML token.
    
5. Azure AD issues its own token based on the trusted assertion.
    

### 🔹 **Example:**

- Domain `company.com` is configured as _federated_ in Azure AD.
    
- Login goes through `https://adfs.company.com`.
    
- Azure AD **trusts AD FS** to validate users.
    

---

## 🔍 **Key Differences Summary**

|Feature|**Hybrid User**|**Federated User**|
|---|---|---|
|**Identity Source**|On-prem AD (synced via Azure AD Connect)|On-prem AD or external IdP (trusted)|
|**Authentication Location**|Can be Azure AD (PHS/PTA) or on-prem (if federated)|Always via external IdP (e.g., AD FS)|
|**Dependency on Internet/AD FS**|PHS/PTA works even if AD FS down|Requires federation service availability|
|**Setup Complexity**|Easier (Azure AD Connect setup only)|Complex (requires federation trust setup)|
|**SSO (Single Sign-On)**|Cloud or seamless SSO|Full SSO through federation|
|**Example Tool**|Azure AD Connect|AD FS, PingFederate, Okta, etc.|


All the CSPs have identity protection services like

- AWS CloudTrail, Trusted Advisor
    
- Azure Identity Protection and AD Logs
    
- Google Cloud Identity, Advanced Protection Program, Security Key
    

### 

[](https://blog.syselement.com/ine/courses/icca/cloud-sec#vulnerabilities)

Vulnerabilities

`e.g.` Account & Login vulnerabilities:

- weak passwords, leaked credentials, threat intelligence
    
- location/IP anomalies, password spraying, brute force attacks
    

📌 Best practices for accessing and managing cloud resources and users:

- use strong authentication (**MFA**) & enforce strong **password policies**
    
- implement **role-based/conditional access** control
    
- **monitor** user activities & review user permissions/config
    
- use secure connection protocols & data encryption
    
- implement network segmentation
    
- regular systems patching & users training
    
- **audit** unused accounts


![Pasted image 20251022163305.png](attachments/Pasted%20image%2020251022163305.png)

![Pasted image 20251022163317.png](attachments/Pasted%20image%2020251022163317.png)

![Pasted image 20251022163326.png](attachments/Pasted%20image%2020251022163326.png)

![Pasted image 20251022163610.png](attachments/Pasted%20image%2020251022163610.png)

