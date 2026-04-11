# Linux CLI Basics

> Source: TryHackMe — *Linux CLI Basics* room

---

## Navigation Commands

| Command                    | Purpose                                          |
| -------------------------- | ------------------------------------------------ |
| `pwd`                      | Print working directory — shows current location |
| `ls`                       | List files & folders in current directory        |
| `ls -l`                    | Long listing — shows permissions, size, dates    |
| `ls -al`                   | Includes hidden files (names starting with `.`)  |
| `cd <dir>`                 | Change directory                                 |
| `cd ..`                    | Go up one level                                  |
| `find <path> -name <file>` | Search for a file by name recursively            |
| `cat <file>`               | Print file contents to terminal                  |

---

## System Information Commands

| Command | Purpose |
|---|---|
| `whoami` | Print current username |
| `uname` | Print OS name |
| `uname -a` | Full system info — kernel, hostname, architecture |
| `df -h` | Disk usage in human-readable format |
| `cat /etc/os-release` | Distribution name, version & codename |

### `uname -a` Output Breakdown

```
Linux  tryhackme  6.8.0-aws  x86_64  GNU/Linux
 │        │          │          │        │
 OS    hostname   kernel    arch    OS type
```

### `df -h` Key Columns

- **Filesystem** — device or mount name
- **Size / Used / Avail** — space stats
- **Use%** — percentage full
- **Mounted on** — where it's accessible (e.g. `/`)

---

## Quick Reference Workflow

```bash
pwd                          # Where am I?
ls -al                       # What's here (incl. hidden)?
cd Documents                 # Move into a folder
cd ..                        # Go back
find ~ -name "file.txt"      # Search home dir for a file
cat file.txt                 # Read a file
whoami                       # Current user
uname -a                     # System & kernel info
df -h                        # Disk space
cat /etc/os-release          # Distro details
```

---

## Key Takeaways

- **Terminal** = text-based interface; faster & more powerful than GUI.
- Hidden files start with `.` — use `ls -a` to reveal them.
- `/etc` stores system config & info files.
- `find` searches recursively from a given starting point.
- `-h` flag on `df` converts bytes → human-readable sizes (G, M, K).