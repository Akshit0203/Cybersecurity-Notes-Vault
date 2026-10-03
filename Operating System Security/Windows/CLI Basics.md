## Navigation & File Discovery

The **terminal** is a text-based interface for interacting with Windows. Instead of clicking through folders, you type commands that tell the system exactly what to do.

| Command                      | Purpose                                             |
| ---------------------------- | --------------------------------------------------- |
| `cd`                         | Print current working directory (no arguments)      |
| `cd <folder>`               | Move into the specified folder                      |
| `cd ..`                      | Go back one level                                   |
| `dir`                        | List files & folders in current directory            |
| `dir /a`                     | Include hidden & system files in the listing        |
| `dir /s <filename>`         | Search all subfolders for a file recursively         |
| `type <file>`               | Print file contents to terminal                      |

> `cd` alone prints your current path — equivalent to `pwd` in Linux.

### Finding a File You Don't Know the Location Of

1. **Check your location** — `cd` to see your current directory
2. **Look around** — `dir` to list visible contents
3. **Check for hidden items** — `dir /a` reveals hidden files/folders (hidden ≠ secret, just not shown by default)
4. **Navigate into folders** — `cd <folder>` to explore, `cd ..` to go back
5. **Search recursively** — `dir /s <filename>` searches all subfolders from your current location and returns the full path
6. **Navigate to the file** — `cd <path>` using the path from the search result
7. **Read the file** — `type <filename>` to display its contents

---

## System Information

Before fixing a problem or investigating an incident, the first step is gathering information about the system — who's logged in, what machine this is, and how it's connected.

| Command      | Purpose                                                            |
| ------------ | ------------------------------------------------------------------ |
| `whoami`     | Print current username (different users = different permissions)   |
| `hostname`   | Print the computer's name (used to identify machines on a network) |
| `systeminfo` | Full OS, hardware & network details                                |
| `ipconfig`   | Show network config — IPv4 address, default gateway                |

### `systeminfo` — Key Fields to Focus On

- **OS Name** — which Windows edition (e.g. Windows 10 Pro)
- **OS Version** — build number, identifies patch level
- **System Type** — 32-bit or 64-bit architecture

### `ipconfig` — Key Fields to Focus On

- **IPv4 Address** — the machine's IP on the network
- **Default Gateway** — the router it connects through
