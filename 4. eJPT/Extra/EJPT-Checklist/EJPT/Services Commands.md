

### 📁 FTP Commands

- [ ] `ftp <ip>` → Connect to FTP server
    - 🔹 Try `anonymous` login if credentials are not provided
- [ ] `get <filename>` → Download file from FTP server

---

### 🐬 MySQL Commands

- [ ] `mysql -u root -p -h <ip>` → Connect to MySQL server
    - 🔹 `-u` → Username (e.g., root)
    - 🔹 `-p` → Prompt for password (try empty, `toor`, or check nmap script)
    - 🔹 `-h` → Host IP

**Inside MySQL prompt:**
- [ ] `SHOW DATABASES;` → List all databases

---

## 🗂️ SMB Commands Checklist

### 🔐 Connecting to SMB Server
- [ ] `smbclient //<ip>/share_name -U username`  
    - 🔸 Enter password when prompted

### 🔍 SMB Nmap Script Scan with Credentials
- [ ] `nmap -p445 --script=smb-snumsessions --script-args smbusername=administrator,smbpassword=smbserver_771 demo.ine.local`  
    - 🔸 Pass SMB creds directly to Nmap script

---

