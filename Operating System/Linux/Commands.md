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

| Command               | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| `whoami`              | Print current username                            |
| `uname`               | Print OS name                                     |
| `uname -a`            | Full system info — kernel, hostname, architecture |
| `df -h`               | Disk usage in human-readable format               |
| `cat /etc/os-release` | Distribution name, version & codename             |

Linux stores configuration and informational files in the `/etc` directory.

### `uname -a` Output Breakdown

```
Linux  tryhackme  6.8.0-aws  x86_64  GNU/Linux
 │        │          │          │        │
 OS    hostname   kernel    arch    OS type
```

### `df -h` Key Columns

The `-h` flag means **human-readable** — sizes display as `2G`, `500M` instead of raw byte counts.

- **Filesystem** — device or mount name
- **Size / Used / Avail** — space stats
- **Use%** — percentage full
- **Mounted on** — where it's accessible (e.g. `/`)

### `df -h` Output Breakdown

| Filesystem | Type | Description |
| --- | --- | --- |
| `/dev/root` | Physical disk | Main system disk — holds the OS and all user data |
| `tmpfs` | RAM-based | Temporary filesystem stored in RAM, not on physical disk; cleared on reboot |
| `/dev/shm` | Shared memory | RAM area for inter-process communication (e.g. 1.9G available, 0 used) |
| `/run/user/<id>` | Per-user tmpfs | Temporary runtime storage for a specific user session (e.g. 387M total, mostly empty) |

> **Example reading:** `/dev/root` with 70G total, 12G used, 55G free, 17% full — this is the real disk. The `tmpfs` entries are virtual and live only in memory.


