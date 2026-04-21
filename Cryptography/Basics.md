# Cryptography Basics

> Core cryptographic concepts — symmetric encryption, asymmetric encryption, and how they work together in practice.

---

## Core Terminology

| Term           | Definition                                                                                    |
| -------------- | --------------------------------------------------------------------------------------------- |
| **Plaintext**  | Readable message (e.g., `HELLO`, `Patient name: Alice Smith`)                                 |
| **Ciphertext** | Scrambled, unreadable version (e.g., `KHOOR`, `Sdwlhqw qdph: Dolfh Vplwk`)                    |
| **Key**        | Secret value that controls how encryption/decryption works                                    |
| **Algorithm**  | The public recipe — the set of steps for using the key. Security comes from the key, not this |

---

## Encryption & Decryption Flow

```
Encryption:  plaintext  + algorithm + key  →  ciphertext
Decryption:  ciphertext + algorithm + key  →  plaintext
```

> **Lockbox analogy:** The algorithm is how the lock works (public). The key is your specific metal key (secret). The plaintext is the letter inside. The ciphertext is the locked box travelling through the postal system.

---

## The Caesar Cipher

A simple substitution cipher — **not secure**, but useful for learning the concept of algorithm + key.

- Named after **Julius Caesar** (used ~2000 years ago for military messages)
- **Algorithm:** Shift each letter by a fixed number of positions in the alphabet
- **Key:** The shift amount

### Example (Key = 3)

| Plaintext | H | E | L | L | O |
| --------- | - | - | - | - | - |
| Ciphertext| K | H | O | O | R |

- Wraps around: `X` → `A`, `Y` → `B`, `Z` → `C`
- Decrypt by shifting **backwards** by the key

### Why It's Insecure

- Only **25 possible keys** (shifts 1–25)
- A computer brute-forces all of them in milliseconds
- **Never used in real systems** — purely educational

> Real algorithms like **AES** are vastly more complex but follow the same principle: algorithm + key + plaintext → ciphertext.

---

## Symmetric Encryption

**One key** is used for both encryption and decryption. Both sender and receiver must share the same secret key.

### Benefits

- **Fast** — can process huge amounts of data quickly
- **Efficient** — ideal for encrypting files, hard drives, and network traffic

### The Key Distribution Problem

- If you send the key in plaintext → attacker intercepts it
- If you encrypt the key → you need **another** key to encrypt that key → infinite regress
- This is symmetric encryption's **Achilles' heel** when used alone

> Solved by **asymmetric encryption** — uses two different keys instead of one.

---

## Asymmetric Encryption

Uses **two mathematically linked keys** to solve the key distribution problem.

| Key              | Who Has It     | Purpose                                           |
| ---------------- | -------------- | ------------------------------------------------- |
| **Public key**   | Anyone         | Used to **encrypt** messages to the key owner      |
| **Private key**  | Only the owner | Used to **decrypt** messages encrypted with the public key |

- Encrypting with someone's **public key** → only their **private key** can decrypt
- Encrypting with your **private key** → anyone with your **public key** can decrypt (used for **digital signatures**)
- Recovering the private key from the public key is **computationally infeasible** (hundreds to thousands of years)

> No secret key ever travels over the network. The only key shared publicly is the **public key**, which is not secret by design.

---

## HTTPS — Real-World Application

When you visit `https://example.com`:

1. Browser requests the website's **public key**
2. Website sends back its public key wrapped in a **certificate**
3. Browser and website use **asymmetric encryption** to agree on a shared **symmetric key**
4. Session continues with fast **symmetric encryption** using that shared key

> This is the **hybrid approach**: asymmetric encryption for key exchange, symmetric encryption for bulk data.

### Certificates

A certificate is a digital document containing:

- The server's **public key**
- Who the key belongs to (e.g., `example.com`)
- A digital signature from a trusted **Certificate Authority (CA)**

**Browser verification process:**

1. Check that a **trusted CA** signed the certificate
2. Check that it's **still valid** (not expired or revoked)
3. If valid → show padlock icon and trust the public key
4. If invalid → display a warning / refuse to connect

> Your browser and OS come **preloaded** with a list of trusted CAs.

### How to View a Certificate

1. Visit any HTTPS site
2. Click the **padlock icon** in the address bar
3. Look for "Certificate" or "Connection is secure"
4. View details: **Issued to**, **Issued by**, **Valid from/until**

---

## Symmetric vs Asymmetric — Comparison

| Feature             | Symmetric                                    | Asymmetric                                    |
| ------------------- | -------------------------------------------- | --------------------------------------------- |
| Number of keys      | **One** key (shared)                         | **Two** keys (public + private)               |
| Key sharing         | Both parties need the same secret key        | Public key shared openly                      |
| Speed               | **Very fast**                                | **Slower** (small data only)                  |
| Main use            | Encrypting bulk data (files, network traffic)| Key exchange, digital certificates            |
| Analogy             | One key locks and unlocks a box              | Mailbox: anyone posts, only owner retrieves   |

---

## Key Takeaways

- **Algorithm is public, key is secret** — security comes from the key, not obscurity of the method
- **Symmetric** = fast, one shared key, but has the key distribution problem
- **Asymmetric** = slower, two keys, solves key distribution
- **Real systems use both** (hybrid) — asymmetric for key exchange, symmetric for session data
- This hybrid approach powers **HTTPS, VPNs, and encrypted messaging apps**