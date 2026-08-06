# Who is Werner Koch?

Werner Koch is a German software engineer who created **GnuPG (GNU Privacy Guard)**, one of the most important pieces of open-source cryptographic software ever written.

Millions of people have used it without ever realizing it.

If you've ever:

- Verified software downloads
- Signed Git commits
- Used encrypted email
- Installed Linux packages
- Verified cryptographic signatures

...there's a good chance GnuPG was involved.

---

# Why did he build GnuPG?

To understand this, you need to understand the "Crypto Wars."

## The Internet in the 1990s

Imagine sending every email as a postcard.

Anyone who handled it could read it.

There was no WhatsApp end-to-end encryption.  
No Signal.  
No HTTPS everywhere.

Strong encryption existed...

...but governments didn't like ordinary people having it.

---

# Why was the US against encryption?

The U.S. government considered strong cryptography strategically important.

During the 1990s:

- Encryption software was treated under export regulations similarly to military technology.
- Strong cryptographic software couldn't always be freely exported.
- Governments argued criminals and foreign adversaries could hide communications.
- Privacy advocates argued ordinary people also needed protection.

So there was a long political and legal battle over whether everyone should have access to strong encryption.

This period became known as the **Crypto Wars**.

---

# What was PGP?

PGP = Pretty Good Privacy

Created by Phil Zimmermann in 1991.

It allowed people to:

- Encrypt files
- Encrypt emails
- Digitally sign messages

using public-key cryptography.

It became extremely popular.

---

## But there was a problem

Although PGP was revolutionary:

- commercial versions existed
- licensing was complicated
- export restrictions affected distribution
- not everyone could freely integrate it into other software

Developers wanted something completely free and open.

---

# Werner Koch's solution

In 1997, Koch began writing:

**GNU Privacy Guard (GnuPG)**

Released in 1999.

It was:

✅ Free

✅ Open source

✅ No licensing fees

✅ Could be audited

✅ Could be modified

✅ Anyone could use it

It implemented the OpenPGP standard, making strong encryption broadly accessible.

---

# How does GPG actually work?

Suppose Alice wants to send Bob a secret message.

Instead of sharing one password...

Bob creates two keys:

**Public Key**

Anyone can have it.

**Private Key**

Only Bob has it.

---

Alice encrypts using Bob's public key.

The encrypted message becomes unreadable gibberish.

Only Bob's private key can decrypt it.

Even if someone intercepts the message...

they cannot read it without the private key.

This is called **public-key cryptography**.

---

# Digital signatures

GPG also proves who wrote a message.

Bob signs a document using his private key.

Anyone can verify that signature using Bob's public key.

This provides:

- authenticity
- integrity
- non-repudiation

This is why software packages are signed.

When Linux says:

> Verified

GPG is often involved somewhere in that trust chain.

---

# Why was open source important?

Imagine a bank says:

> Trust us.

But won't show how the vault works.

That's closed source.

Now imagine:

Everyone can inspect the vault.

Experts worldwide continuously test it.

That's open source.

If someone finds a weakness...

they can report or fix it.

This transparency helps build trust in cryptographic software.

---

# Did Edward Snowden use GPG?

Yes.

Edward Snowden used GPG to encrypt communications with journalists during the 2013 NSA disclosures.

This helped protect messages from interception.

It's one reason GPG became widely known outside technical circles.

---

# Did the NSA fail to break GPG?

This statement needs nuance.

The post says:

> The encryption held.

That does **not** mean:

> The NSA tried every possible way to crack GPG itself and failed.

Instead:

Modern public-key algorithms (such as RSA with sufficiently large keys or ECC when properly implemented) are considered computationally infeasible to brute-force with current publicly known capabilities.

In practice, intelligence agencies often target:

- endpoints (the user's computer)
- malware
- stolen keys
- weak passwords
- implementation bugs
- metadata
- operational mistakes

rather than mathematically breaking well-implemented encryption.

So the security of GPG generally comes from the strength of the underlying cryptography when used correctly.

---

# "$50 billion a year"

This is one of the more misleading parts.

The post implies:

> NSA spent $50B trying to crack GPG.

That isn't accurate.

The NSA's overall budget supports many missions, including:

- signals intelligence
- cybersecurity
- infrastructure
- personnel
- research
- operations

It is **not** a budget dedicated solely to breaking GPG.

The comparison is rhetorical.

---

# Why was Werner Koch poor?

This is one of the saddest parts.

GnuPG became global infrastructure.

But it was free.

Nobody had to pay.

Companies relied on it.

Governments relied on it.

Millions relied on it.

Yet almost nobody funded its maintenance.

By around 2013–2014:

- Koch earned roughly €2,000 per month (about €24,000/year before expenses), an amount widely cited in reporting.
- He struggled to sustain development.
- He had to let employees go.
- He considered stopping work.

This illustrates a common problem with open-source infrastructure: software can become essential while remaining chronically underfunded.

---

# What happened in 2015?

A ProPublica article highlighted Koch's financial situation.

The story spread quickly.

Within about a day:

- over €100,000 was donated
- thousands of people contributed
- companies stepped in

Organizations such as Facebook and Stripe committed recurring financial support.

This allowed continued development.

---

# Why is GPG so important today?

Even if you've never run the `gpg` command, it underpins many security workflows.

It is commonly used for:

- Linux package verification
- Git commit signing
- Email encryption
- Software release verification
- Cryptographic identity verification
- Secure file encryption

It is one of the foundational building blocks of today's software supply chain.

---

# The deeper lesson

The final paragraph says:

> He almost lost everything because he wasn't visible.

There's some truth here, but it's only part of the story.

A broader lesson is that **critical digital infrastructure often depends on small teams or even individuals**, and society has historically underinvested in maintaining that infrastructure. Koch's case became a powerful example of why sustainable funding for open-source projects matters.

Building an audience can certainly help attract users, contributors, and funding. But the more fundamental issue wasn't a lack of visibility—it was that the internet increasingly relied on free software without consistently supporting the people maintaining it.

---

## In one sentence

Werner Koch built GnuPG—a free, open-source implementation of strong encryption that became a cornerstone of internet security, was trusted by journalists and activists (including Edward Snowden), nearly disappeared due to lack of funding despite its global importance, and ultimately survived after public attention led to renewed financial support.





