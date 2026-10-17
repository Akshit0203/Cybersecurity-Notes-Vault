# Responder

> **Responder pretends to be a service on the network so Windows computers accidentally talk to _you_ instead of the real machine. Then it grabs their login hashes.**

## How It Works

### Real-World Analogy
Imagine an office. Someone shouts:

> "Hey, where's the printer server?"

The real printer hasn't answered yet. You quickly yell:

> "I'm the printer server!"

They believe you, walk over, and hand you their ID badge to log in. You copy the badge details. That's basically Responder.

### On a Windows Network

1. Victim machine tries to find `\\fileserver` but doesn't know where it is.
2. Windows asks the network:
   > "Anyone know FILESERVER?"
3. Responder hears it and says:
   > "Yep—that's me."
4. Victim connects to you.
5. Windows automatically tries to authenticate with NTLM.
6. Responder captures the credentials:

```
username::domain:hash
```

Now you have the **username**, **domain**, and **NTLM hash** — which you can then **crack**, **relay**, or use to **identify users**.

## Why It Works — Broadcast Protocols

The victim talks to you because of insecure broadcast name resolution protocols:

| Protocol   | Full Name                          |
| ---------- | ---------------------------------- |
| **LLMNR**  | Link-Local Multicast Name Resolution |
| **NBT-NS** | NetBIOS Name Service               |
| **mDNS**   | Multicast DNS                      |

When DNS fails to resolve a hostname, Windows falls back to these protocols and asks everyone nearby:

> "Who is this?"

Responder lies faster than the real answer arrives.

## Attack Flow

```
Victim:     "Who is FILESERVER?"
Responder:  "Me!"
Victim:     "Cool. Here's my NTLM login."
Responder:  "Thanks 😄"
```

## Usage

```bash
sudo responder -I eth0
```

| Flag       | Meaning                    |
| ---------- | -------------------------- |
| `sudo`     | Run as root (required)     |
| `responder` | The tool itself           |
| `-I eth0`  | Listen on this network interface |

Then it waits. When someone asks for something on the network:

```
[SMB] NTLMv2 hash captured
```

## Quick Recall

> **Responder = "Windows asks the network for a machine → Responder lies → victim authenticates → you capture the hash."**
