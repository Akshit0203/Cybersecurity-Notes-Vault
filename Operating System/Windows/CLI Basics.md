## Navigation Commands

| Command                     | Purpose                                              |
| --------------------------- | ---------------------------------------------------- |
| `cd`                        | Print current working directory (no arguments)       |
| `cd <dir>`                  | Change directory                                     |
| `cd ..`                     | Go up one level                                      |
| `cd \`                      | Jump to root of current drive                        |
| `D:`                        | Switch to another drive (just type the drive letter)  |
| `dir`                       | List files & folders in current directory             |
| `dir /a`                    | Include hidden and system files                      |
| `tree`                      | Display directory structure as a visual tree          |
| `tree /f`                   | Include files in the tree output                     |

> In CMD, `cd` alone prints the current path — equivalent to `pwd` in Linux.

---

## File & Folder Management

| Command                          | Purpose                                          |
| -------------------------------- | ------------------------------------------------ |
| `type <file>`                    | Print file contents to terminal (like `cat`)     |
| `more <file>`                    | Display file contents page by page               |
| `copy <src> <dest>`             | Copy a file                                      |
| `move <src> <dest>`             | Move or rename a file                            |
| `del <file>`                     | Delete a file                                    |
| `mkdir <dir>`                    | Create a new directory                           |
| `rmdir <dir>`                    | Remove an empty directory                        |
| `rmdir /s <dir>`                 | Remove a directory and all its contents           |
| `ren <old> <new>`               | Rename a file or folder                          |
| `find "text" <file>`            | Search for a string inside a file                |
| `where <filename>`              | Locate a file in the system PATH                 |

> Use `/?` after any command (e.g. `dir /?`) to see all available flags and usage.

---

## System Information Commands

| Command              | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| `hostname`           | Print computer name                                        |
| `whoami`             | Print current username (domain\user format)                |
| `systeminfo`         | Full OS, hardware & network details                        |
| `ver`                | Print Windows version                                      |
| `set`                | List all environment variables                             |
| `echo %USERNAME%`    | Print a specific environment variable                      |
| `cls`                | Clear the terminal screen                                  |

### `systeminfo` Key Fields

```
Host Name:           DESKTOP-ABC123
OS Name:             Microsoft Windows 11 Pro
OS Version:          10.0.22631
System Manufacturer: HP
Total Physical Memory: 16,192 MB
```

- **OS Version** — build number, useful for identifying patch level
- **System Boot Time** — when the machine was last restarted
- **Hotfix(s)** — installed Windows updates / patches
- **Network Card(s)** — lists all adapters with IP addresses

---

## Networking Commands

| Command                      | Purpose                                              |
| ---------------------------- | ---------------------------------------------------- |
| `ipconfig`                   | Show IP address, subnet mask, default gateway        |
| `ipconfig /all`              | Full network details — MAC, DHCP, DNS servers        |
| `ping <host>`               | Test connectivity to a host                          |
| `tracert <host>`            | Trace the route packets take to a destination        |
| `nslookup <domain>`         | Query DNS — resolve domain to IP                     |
| `netstat`                    | Show active network connections                      |
| `netstat -an`               | All connections with numeric addresses & ports       |
| `netstat -ab`               | Show which program owns each connection              |

### `ipconfig` vs `ipconfig /all`

- `ipconfig` — quick check: IP, subnet, gateway
- `ipconfig /all` — detailed: adds MAC address, DHCP lease info, DNS servers, adapter type

---

## Process Management Commands

| Command                         | Purpose                                           |
| ------------------------------- | ------------------------------------------------- |
| `tasklist`                      | List all running processes (like Task Manager)    |
| `tasklist /fi "imagename eq notepad.exe"` | Filter for a specific process           |
| `taskkill /pid <PID>`          | Kill a process by its Process ID                  |
| `taskkill /im <name> /f`      | Force kill a process by name                      |

### `tasklist` Output Breakdown

```
Image Name          PID   Session Name   Mem Usage
───────────────────────────────────────────────────
svchost.exe         892   Services       12,340 K
explorer.exe       4216   Console        98,512 K
chrome.exe         7840   Console       210,448 K
```

- **Image Name** — the executable's filename
- **PID** — unique Process ID (use this with `taskkill`)
- **Mem Usage** — RAM consumed by the process

---

## Useful Tips

- **Tab completion** — press `Tab` to auto-complete file/folder names
- **Command history** — press `↑` / `↓` arrows to cycle through previous commands
- **Pipe output** — `command | more` to paginate long output
- **Redirect output** — `command > file.txt` saves output to a file
- **Append output** — `command >> file.txt` appends instead of overwriting
- **Chain commands** — `command1 && command2` runs second only if first succeeds
