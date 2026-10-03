# Burpsuite Not Starting : 

#### Reason : outdated Burp package

error : 
```
└─$ burpsuite
[warning] /usr/bin/burpsuite: No JAVA_CMD set for run_java, falling back to JAVA_CMD = java
Could not start Burp: java.lang.NullPointerException: Cannot invoke "burp.Zcie.ZA()" because the return value of "burp.Zdnd.Zw()" is null
```

Solution : 

Update Kali's package lists
Run:
```
sudo apt update
```

Upgrade Burp
```
sudo apt install --only-upgrade burpsuite
```

Then launch:
```
burpsuite
```


# Websites not authenticating/loading : 

| Option                    | What it is                                                         | Use it?                                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Firefox on Kali**    | Your normal Firefox browser                                        | ❌ Not for this setup                                                                                                                                                                                                                                                                |
| **2. Chromium on Kali**   | Chromium you launch yourself from Kali                             | ✅ **Yes**                                                                                                                                                                                                                                                                           |
| **3. Burp's own browser** | Chromium launched from **Burp → Proxy → Intercept → Open Browser** | ❌ Not what we're configuring ; authentication wont work here ; why ? - The site's authentication flow uses redirects/cookies that don't behave correctly in Burp's embedded browser.<br>- A login provider or anti-bot mechanism may behave differently in an instrumented browser. |
Browser choice: Chromium ≈ Firefox for our current task.
Both can do:

```
Browser → 127.0.0.1:8080 → Burp → Website
```

I was preferring **Chromium only because you already have Chromium available and we're already discussing a Chromium-based workflow**. There is **no special Burp advantage** to Chromium over Firefox here.

Cloudflare is blocking the proxied login request.

