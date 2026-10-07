
#### 🚫 GitHub Account Safety Checklist

##### <span style="color:rgb(255, 0, 0)">If banned : </span> 
1. Open a support ticket (follow up on single one only dont open multiple tickets) ; Follow up promptly in the same original ticket
2. tweet it : at @github or @githubhelp ; delete the tweet Link with ticket numbers
3. Check sub gitub subreddit ; delete reddit comment on pinned post [Link](https://www.reddit.com/r/github/comments/1er6iwo/was_your_account_suspended_deleted_or/?sort=new)

Reddit comment : 
```
Username: xxxxxx  
Ticket ID: #xxxx

My account was flagged on September 21, 2026, with no email or stated reason. I can still log in, but my public profile is hidden/returns 404 to others, and Code Search shows:

“Your user account has been flagged, and cannot search code.”

I submitted an appeal through the official GitHub Support form, but I haven't received a further human response. The ticket is still **Open as of October 5**, with no update.

I use GitHub for professional software development, cybersecurity projects, research, authorized CTFs/labs, and technical documentation. I have also enabled 2FA and reviewed my account security activity.

Would really appreciate a manual review if any GitHub staff see this. Thank you.
```
##### <span style="color:rgb(255, 0, 0)">Personal Checklist : </span>
1. Don't put a lot of commits in a single day
2. Don't use the GitHub copilot ai or github actions Inside GitHub
3. Do not use Github 3rd party authentication
4. Don't sponsor anyone
5. 1 project only daily - hard limit
##### 🤖 Automation & AI
- [ ] Don't let an AI agent make **mass changes across your repositories** using your personal GitHub token.
- [ ] Don't let automation generate huge bursts of commits/pushes.
- [ ] Don't run bots that continuously interact with GitHub.
- [ ] Don't accidentally expose your personal GitHub token to an automated tool.
- [ ] Review what an AI agent is going to modify **before giving it write/push access**.
##### 🌐 Scraping & Web Automation
- [ ] Don't use **GitHub Actions to scrape/interact with third-party websites**.
- [ ] Don't run automated scrapers through GitHub Actions.
- [ ] Don't generate hundreds/thousands of requests in a short period.
- [ ] Don't repeatedly query external websites from scheduled workflows.
- [ ] Be particularly careful with workflows that run automatically several times per day.
- [ ] Don't assume that respecting `robots.txt` automatically makes GitHub Actions usage acceptable—the thread contains a case where it wasn't. Pasted text
##### 📦 Repositories & Content
- [ ] Don't upload **malware**.
- [ ] Don't fork suspicious repositories without checking their contents.
- [ ] Don't host or distribute **game cheats**.
- [ ] Don't host tools for **bypassing paid software licensing**.
- [ ] Don't host tools intended for **unauthorized commercial software use**.
- [ ] Don't create **privacy-invasive scraping/surveillance tools**.
- [ ] Don't create abusive automation tools.
- [ ] Don't create repositories that could reasonably be interpreted as spam.
- [ ] Be careful with repositories containing cracked-game/modding material.
##### 📈 Activity Patterns
- [ ] Avoid suddenly creating **hundreds of files/commits** in a short period.
- [ ] Avoid unusual bursts of automated repository activity.
- [ ] Don't accidentally create excessive API/request traffic.
- [ ] If you're testing automation, keep the activity controlled rather than generating a massive burst.
One user specifically reported that **800–900 small files committed over 3–4 days** may have contributed to their flagging. Pasted text
##### 👤 Account Rules
- [ ] Don't maintain multiple free GitHub accounts.
- [ ] Don't create a new account to get around a restriction/suspension.
- [ ] Don't use another account to evade enforcement.
- [ ] Keep your account/student information accurate.
- [ ] Complete GitHub Education/student verification when requested.

The thread specifically quotes GitHub's rule that one person/legal entity may maintain no more than one free account, and that additional accounts created around restrictions can be removed. Pasted text
##### 🔐 Account Security
- [ ] Keep **2FA enabled**.
- [ ] Protect your GitHub tokens.
- [ ] Don't give tokens to untrusted automation.
- [ ] Review account activity if something looks unusual.
- [ ] If an AI agent uses your token, restrict its permissions as much as possible.
- [ ] If your account/token may be compromised, secure it immediately.
##### 🛑 Things to be especially careful about

**The biggest red flags from the actual incidents were:**

> **Mass automation + scraping + unusual request volume + suspicious repository content + duplicate accounts + malware/cheats/licensing bypass tools.**

And one very important point: **don't assume that doing something normally as a developer means GitHub's automated systems cannot flag it.** The thread contains reports of ordinary CLI/desktop activity, repository cleanup, AI-agent activity, and other normal-looking workflows being flagged, sometimes with no confirmed reason. Pasted text

So for your normal use—**coding, cybersecurity labs, CTFs, personal projects, documentation, and normal Git operations**—the key is to avoid **mass automation, scraping through Actions, suspicious content, duplicate accounts, and uncontrolled token-based automation**.

----

