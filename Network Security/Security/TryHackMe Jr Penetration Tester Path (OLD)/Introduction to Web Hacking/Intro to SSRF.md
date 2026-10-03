### **What is an SSRF?**

SSRF stands for Server-Side Request Forgery. It's a vulnerability that allows a malicious user to cause the webserver to make an additional or edited HTTP request to the resource of the attacker's choosing.

### **Types of SSRF**
There are two types of SSRF vulnerability; the first is a regular SSRF where data is returned to the attacker's screen. The second is a Blind SSRF vulnerability where an SSRF occurs, but no information is returned to the attacker's screen.

### What's the impact?
A successful SSRF attack can result in any of the following: 
- Access to unauthorised areas.
- Access to customer/organisational data.
- Ability to Scale to internal networks.
- Reveal authentication tokens/credentials.

### **Deny List**
A Deny List is where all requests are accepted apart from resources specified in a list or matching a particular pattern. A Web Application may employ a deny list to protect sensitive endpoints, IP addresses or domains from being accessed by the public while still allowing access to other locations. A specific endpoint to restrict access is the localhost, which may contain server performance data or further sensitive information, so domain names such as localhost and 127.0.0.1 would appear on a deny list. Attackers can bypass a Deny List by using alternative localhost references such as 0, 0.0.0.0, 0000, 127.1, 127.*.*.*, 2130706433, 017700000001 or subdomains that have a DNS record which resolves to the IP Address 127.0.0.1 such as 127.0.0.1.nip.io.

### **Allow List**

- **What it is:** The opposite of a deny list.  
    Only certain URLs or patterns are allowed — everything else is blocked.
    
- **Example:** The website might say:  
    _“Only URLs starting with `https://website.thm` are allowed.”_
    
**How attackers bypass it**

**Trick:** Use a **subdomain**.  
If the rule only checks that the URL _starts_ with `https://website.thm`, an attacker could use:

`https://website.thm.attackers-domain.thm`

The app sees it as matching the rule (starts with `https://website.thm`),  
but in reality, it belongs to `attackers-domain.thm`, which the attacker controls.


### **Open Redirect**

- **What it is:** A website feature that automatically sends you to another URL.
    
- **Example:**
    
    `https://website.thm/link?url=https://tryhackme.com`
    
    Here, `/link` redirects the user to whatever URL is given in the `url=` parameter.
    

---

**How attackers abuse it for SSRF**

If the app only allows URLs starting with `https://website.thm`,  
the attacker could first point to the open redirect endpoint:

`https://website.thm/link?url=https://attackers-site.com`

The app thinks it’s going to `website.thm` (allowed),  
but the open redirect immediately forwards the request to the attacker’s site.