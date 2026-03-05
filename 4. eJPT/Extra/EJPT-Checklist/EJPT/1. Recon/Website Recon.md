

### 🔍 Passive Recon Checklist

- [ ] Identify IP address of the website  
  - [ ] Run `host hackersploit.com`  
    - [ ] Check if multiple IPs (Firewall/Proxy?)  
    - [ ] Note mail server, IPv6 address

- [ ] Perform Whois lookup (Domain)  
  - [ ] Run `whois hackersploit.org`  
    - [ ] Record registrar name  
    - [ ] Record organization info  
    - [ ] Record owner contact info

- [ ] Perform Whois lookup (IP Address)  
  - [ ] Extract IP from `host` command  
  - [ ] Run `whois <ip-addr>`  
    - [ ] Identify IP block and organization owner

- [ ] Use Netcraft site report  
  - [ ] Visit [Netcraft Site Report](https://sitereport.netcraft.com/)  
    - [ ] Check registrar details  
    - [ ] Check nameservers  
    - [ ] Identify OS and web technologies  
    - [ ] Check for SSL vulnerabilities

- [ ] Check for hidden directories  
  - [ ] Visit `hackersploit.com/robots.txt`

- [ ] Check sitemap for listed URLs  
  - [ ] Visit `hackersploit.com/sitemap.xml`

- [ ] Identify web technologies  
  - [ ] Use [BuiltWith](https://builtwith.com)  
  - [ ] Use [Wappalyzer extension](https://www.wappalyzer.com)  
  - [ ] Run `whatweb hackersploit.org`

- [ ] Collect contact & location info (OSINT)  
  - [ ] Look for phone numbers  
  - [ ] Look for email addresses  
  - [ ] Look for physical address

- [ ] Mirror/download the website  
  - [ ] Use HTTrack to clone site to local directory

---

### 🌐 DNS Recon Checklist

- [ ] Run DNSRecon  
  - [ ] `dnsrecon -d hackersploit.org`  
    - [ ] Collect A, AAAA, TXT, MX records  
    - [ ] Identify name servers

- [ ] Use DNSDumpster  
  - [ ] Visit [dnsdumpster.com](https://dnsdumpster.com/)  
    - [ ] Identify DNS servers and locations  
    - [ ] Attempt zone transfer  
    - [ ] Check owner of IP block  
    - [ ] Find other websites using same DNS server

---

### 🛡️ WAF Detection Checklist

- [ ] View supported WAFs  
  - [ ] Run `wafw00f -l` to list all detectable WAFs

- [ ] Detect WAF on target domain  
  - [ ] Run `wafw00f hackersploit.org`  
    - [ ] Note if any WAF is in use

- [ ] Run full WAF analysis  
  - [ ] Run `wafw00f nec.edu.in -a`  
    - [ ] List all WAFs detected on the domain

---

### 🌐 Subdomain Enumeration Checklist

- [ ] Use Sublist3r  
  - [ ] Run `sublist3r -d hackersploit.org -e google,yahoo` (specific search engines)  
  - [ ] Run `sublist3r -d hackersploit.org` (comprehensive scan)

---

### 🔍 Google Dorking Checklist

- [ ] Discover domains & subdomains  
  - [ ] `site:ine.com`  
  - [ ] `site:*.ine.com`

- [ ] Find admin panels  
  - [ ] `site:ine.com inurl:admin`  
  - [ ] `site:ine.com intitle:admin`

- [ ] Search for documents  
  - [ ] `site:ine.com filetype:pdf`

- [ ] Search for employee data  
  - [ ] `site:ine.com employees`

- [ ] Look for directory listing  
  - [ ] `intitle:index of`

- [ ] View cached content  
  - [ ] `cache:ine.com`

- [ ] Look for credential files  
  - [ ] `inurl:auth_user_file.txt`  
  - [ ] `inurl:passwd.txt`

- [ ] Use Wayback Machine for historical snapshots

- [ ] Use GHDB (Google Hacking Database) for advanced dorks

---

### 📧 Email Harvesting Checklist
- [ ] Use theHarvester tool  
  - [ ] `theHarvester -d INE -b duckduckgo`  
  - [ ] `theHarvester -d INE -b duckduckgo,yahoo,bing`  
  - [ ] `theHarvester -d ine.com -b urlscan,baidu`  
    - [ ] Collect email addresses  
    - [ ] Collect subdomains  
    - [ ] Identify IP blocks

---

### 🔓 Leaked Password Databases Checklist
- [ ] Check for data breaches  
  - [ ] Visit [haveibeenpwned.com](https://haveibeenpwned.com)  
    - [ ] Search for email addresses or domains with known breaches

---

## 🚧 Active Information Gathering

### ✅ DNS Zone Transfer

- [ ] Check `/etc/hosts` file for internal DNS records
- [ ] Identify domain name servers
- [ ] Attempt zone transfer using `dnsenum`
  - [ ] `dnsenum zonetransfer.me`
- [ ] Attempt zone transfer using `dig`
  - [ ] `dig axfr @nsztm1.digi.ninja zonetransfer.me`
- [ ] Attempt zone transfer using `fierce`
  - [ ] `fierce -dns zonetransfer.me`


---

## ✅ Nmap Scanning

### 🔎 Host Discovery
- [ ] Identify active hosts in subnet  
  - [ ] `sudo nmap -sn 192.168.2.0/24`
- [ ] Discover hosts using Netdiscover  
  - [ ] `sudo netdiscover -i wlp3s0 -r 192.168.29.0/24`

### 🚪 Port Scanning
- [ ] Perform default TCP port scan (Top 1000 ports)  
  - [ ] `nmap 192.168.2.29`
- [ ] Scan all 65535 TCP ports  
  - [ ] `nmap -p- <ip>`
- [ ] Scan specific ports (e.g., 80 and 443)  
  - [ ] `nmap -p 80,443 <ip>`
- [ ] Perform fast scan (Top 100 common ports)  
  - [ ] `nmap -F <ip>`
- [ ] Perform UDP scan  
  - [ ] `nmap -sU <ip>`
- [ ] Combine TCP & UDP scan  
  - [ ] `nmap -sS -sU <ip>`

### 🛠️ Advanced Options
- [ ] Full detailed scan  
  - [ ] `nmap -sS -sV -sC -O -T4 -Pn <ip>`
- [ ] All TCP ports with service detection  
  - [ ] `nmap -p- -sV -T4 <ip>`

---
## 🧠 Important Tips

- [ ] Check `robots.txt` to see what search engines are allowed/blocked from indexing
- [ ] Use Nmap version scan to see what's running on the website and its version
- [ ] Use directory traversal tools like Gobuster if asked to look for directories
- [ ] Check for `.bak` files when asked to find backup files on the web
  - [ ] Tailor your search based on web technology (e.g., `wp-config.bak` for WordPress)
- [ ] Use HTTrack to mirror/download a website’s source code
- [ ] On WordPress sites, check for presence of `xmlrpc.php`
- [ ] Use Gobuster with `-x` flag to search for backup files
  - [ ] `gobuster dir -u <url> -w <wordlist> -x .bak`
- [ ] Always perform **recursive scanning** during directory traversal
  - [ ] `dirb <url>` (recursive by default)
- [ ] If you find multiple folders, **inspect each one**—hidden clues might be inside

