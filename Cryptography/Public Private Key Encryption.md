# Public-Key (Asymmetric) Encryption

> How public and private keys work, why open-source algorithms are safe, how keys are distributed, and how HTTPS ties it all together.

---

## 1 — Symmetric vs Asymmetric Encryption

### Symmetric (One Key)

The **same key** encrypts and decrypts.

```
Key ---------> Lock
Key <--------- Unlock
```

| Examples  | Used In                          |
| --------- | -------------------------------- |
| AES       | Wi-Fi, HTTPS sessions, VPNs     |
| ChaCha20  | WireGuard, mobile TLS            |

### Asymmetric (Two Keys)

You create **two mathematically related but non-identical keys**.

```
Public Key   ← share with everyone
Private Key  ← never leaves your machine
```

> Think of them as two puzzle pieces manufactured together — only one fits with the other.

---

## 2 — The Mailbox Analogy

Imagine a mailbox anyone can drop letters into, but only you hold the key to open.

```
 _______
|       |
|   📬  |
|_______|
```

- **Mail slot** = Public Key (anyone can lock messages inside)
- **Mailbox key** = Private Key (only you can unlock)

The slot and the key are **different objects**, yet they work together.

---

## 3 — Why Does This Work? One-Way & Trapdoor Functions

### One-Way Functions

Certain math operations are easy to compute forward but astronomically hard to reverse.

```
48392847239847239847239847239847239847
```

If this was produced via enormous primes and modular arithmetic, going **forward** is cheap — going **backward** without secret information is infeasible.

### Paint-Mixing Analogy

```
🎨 Secret Color + Blue  →  🟢 Green
```

Hand someone the green paint — they **cannot** separate out the exact secret color. Mixing is easy; un-mixing is practically impossible.

### Trapdoor Functions

Public-key cryptography relies on **trapdoor functions**:

1. Easy to compute in one direction.
2. Extremely hard to reverse — **unless** you hold a secret piece of information (the "trapdoor"), which is the private key.

```
Encrypt  → Easy (with public key)
Decrypt without private key  → Essentially impossible
```

---

## 4 — RSA Example (Simplified)

RSA's security rests on the difficulty of **factoring large numbers**.

### Toy Example

```
Prime 1 = 61
Prime 2 = 53
61 × 53 = 3233
```

- **Public key** is based on `3233` — everyone sees it.
- Nobody knows the factors `61` and `53`.
- Recovering them requires factoring `3233` — trivial here, but…

### Real-World Scale

```
61732984723984723984723984723984723984723984723984723984723
×
98723498723984723984723984723984723984723984723984723984711
```

These primes are hundreds or thousands of bits long. Factoring their product is **computationally infeasible** with current classical computers when appropriate key sizes are used.

---

## 5 — Why the Public Key Can't Decrypt

The public key contains enough information to **transform plaintext → ciphertext**, but **not** the secret math needed to reverse it. Only the private key does.

```
Plaintext
     │
     ▼
Public Key
     │
     ▼
Ciphertext
     │
     ▼
Private Key
     │
     ▼
Plaintext
```

### Why Can't Someone Derive the Private Key?

That would require solving a problem **designed** to be infeasible:

| Algorithm | Hard Problem                              |
| --------- | ----------------------------------------- |
| RSA       | Factoring a huge composite number         |
| ECC       | Elliptic Curve Discrete Logarithm Problem |

These problems are easy to **verify** once solved, but extraordinarily hard to **solve from scratch**.

### Common Misconception

Many people picture public and private keys as two copies of the same thing:

```
Public Key  ≠  Private Key
```

They are **different mathematical objects** generated together so they work as a complementary pair — one locks, the other unlocks.

### Padlock Analogy

- 🔓 **Padlock** = Public key — hand copies to everyone.
- 🔑 **Key** = Private key — never share it.

Anyone can snap the padlock shut. Only the owner has the key to open it.

---

## 6 — Why Open-Source Algorithms Are Not Weaker

> **The strongest encryption algorithms in the world are open source and publicly documented.**

### Kerckhoffs's Principle (1883)

> *"A cryptographic system should remain secure even if everything about the system is public except the key."*

Security comes from the **secrecy of the key**, not from hiding the algorithm.

### Algorithm (Public) vs Key (Secret)

```
Algorithm = Lock design   → everyone knows it
Key       = 4e9f7b12a...  → only you know it
```

### Example — AES

```
Encrypted = AES(Data, Key)
```

Everyone knows exactly how AES works, even an attacker. But without the correct key (`mysecretkey123`), knowing the algorithm is not enough.

### Real Encryption Example

```
Plaintext:  Hello
Key:        (secret)
Ciphertext: A7F92C88B19E...
```

An attacker knows the AES algorithm ✅, the source code ✅, the ciphertext ✅ — but **not** the key. Without it, the ciphertext looks like random data.

### Brute-Force Is Infeasible

For AES-256 there are **2²⁵⁶** possible keys:

```
115,792,089,237,316,195,423,570,985,
008,687,907,853,269,984,665,640,
564,039,457,584,007,913,129,639,936
```

Even checking billions of keys per second would take far longer than the age of the universe.

### Security Through Obscurity vs Open Review

| Approach                        | Trust Level |
| ------------------------------- | ----------- |
| "We won't show how it works."   | Lower       |
| "Here's the blueprint. Experts have tried 20 years to break it." | Higher |

Open code means:

- Thousands of researchers inspect it
- Bugs are found and fixed
- Backdoors are harder to hide
- Independent experts verify the implementation matches the spec

### Common Open-Source Algorithms

AES · RSA · ECC · ChaCha20 · GnuPG/OpenPGP

---

## 7 — Key Distribution: How Keys Actually Get Exchanged

### Symmetric Key Problem

Both parties need the **same** secret key.

```
Alice  <------ Secret Key ------>  Bob
```

If Alice sends the key in the clear, an attacker steals it. This is the **Key Distribution Problem**.

### Asymmetric Solution

The private key **never** leaves your machine. You only share the public key.

#### GPG Example

```bash
gpg --full-generate-key
```

This creates a key pair. The **public key** can be uploaded anywhere (GitHub, key servers, your website, email). The **private key** stays local.

#### Sending an Encrypted Message

Alice downloads Bob's public key and encrypts:

```
Message
     │
     ▼
Bob's Public Key
     │
     ▼
Encrypted Message
```

Only Bob's **private key** can decrypt it.

### How Keys Are Generated

Keys are created locally using a **Cryptographically Secure Random Number Generator (CSPRNG)**.

Entropy sources:

- Mouse movement
- Keyboard timing
- CPU events
- Hardware RNG
- OS entropy pool

```
Randomness
     │
     ▼
Private Key
     │
     ▼
Public Key  (mathematically derived)
```

The reverse (public → private) is designed to be computationally infeasible.

---

## 8 — How HTTPS Ties It All Together

When you visit `https://google.com`:

### Step 1 — Client Hello

Your browser says: *"Hi Google."*

### Step 2 — Server Sends Public Key

Google responds with its **certificate** (containing its public key).

### Step 3 — Browser Generates a Session Key

A brand-new random symmetric key, just for this connection:

```
8f3a91d2...
```

### Step 4 — Encrypt the Session Key

Browser encrypts the session key with Google's public key:

```
Session Key
      │
      ▼
Google Public Key
      │
      ▼
Encrypted Session Key
```

### Step 5 — Server Decrypts

Google decrypts with its private key. Now **both sides** know the session key; nobody else does.

### Step 6 — Switch to Symmetric Encryption

From here on, all data is encrypted with **AES** (or another fast symmetric cipher) using the session key.

> **Why switch?** Symmetric encryption is **much faster** than public-key encryption. Public-key crypto is mainly used to **securely establish a shared secret**; symmetric crypto handles the rest.

---

## 9 — The Three Kinds of Keys

| Key Type        | Lifespan                       | Who Knows It | Purpose                                     |
| --------------- | ------------------------------ | ------------ | -------------------------------------------- |
| **Private Key** | Long-lived (keep secret forever) | Only you     | Decrypt data / sign messages                 |
| **Public Key**  | Long-lived (share freely)      | Everyone     | Encrypt data for the owner / verify signatures |
| **Session Key** | Ephemeral (one connection)     | Both endpoints | Fast symmetric encryption of actual traffic  |

> **The big "aha!" moment:** Public-key cryptography is usually used to **exchange or establish a secret symmetric key**, rather than encrypting all data directly.
