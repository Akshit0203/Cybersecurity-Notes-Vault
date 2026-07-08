# UPI Transaction Fraud & the Parliamentary Debate

## Background: MP Radha Mohan Singh's Concerns

MP **Radha Mohan Singh** raised serious concerns in Parliament about UPI's growing risks. His main points:

1. **UPI has become extremely popular** — millions of Indians use it daily for everything from groceries to bills.
2. **As digital transactions increase, so do cyber frauds.** Ordinary people are losing money because:
   - They are unaware of online scams.
   - Fraudsters trick them into sharing OTPs or approving collect requests.
   - Fake customer-care numbers and phishing links are becoming common.
3. He questioned whether **India's digital payment ecosystem is sufficiently secure** for the average citizen, especially elderly people and those in rural areas.

### Solutions He Called For

- Better cybersecurity measures
- Stronger fraud prevention
- Public awareness campaigns about online scams
- Better protection for users who lose money through cyber fraud
- Greater monitoring of fraudulent digital transactions

---

## Is UPI Itself Unsafe?

**No.** UPI is generally regarded as one of the world's most secure and successful instant payment systems. The vast majority of transactions complete safely every day.

The problem is usually **not the technology** but **social engineering** — criminals exploiting trust rather than breaking the UPI system itself.

### Common Scam Techniques

| Technique | How It Works |
| --- | --- |
| Impersonation | Pretend to be bank officials, ask you to "verify" your account |
| Fake QR codes | Send a QR code that debits money instead of crediting it |
| Reversed collect requests | Ask you to approve a "Receive Money" request that actually *sends* money |
| Remote access apps | Trick users into installing screen-sharing apps (e.g., AnyDesk) |
| Phishing links | Fake customer-care numbers and malicious links |

> [!important] Key Insight
> In most fraud cases, the UPI system works exactly as designed — the criminal manipulates the **user** into authorizing the payment.

---

## How UPI Transactions Work

UPI has two types of transactions:

### 1. Push Transaction (Send Money)

The **sender** initiates the payment. **No approval needed from receiver.**

**Example:**
- Rahul opens Google Pay → enters Priya's UPI ID → types ₹500 → enters his UPI PIN.
- ₹500 is immediately credited to Priya. She is **not asked** "Do you accept this ₹500?"

This is exactly how cash works — if someone hands you ₹500, you don't approve receiving it.

### 2. Pull Transaction (Collect Request)

The **receiver** requests money. **Approval IS required from sender.**

**Example:**
- Rahul sends a Collect Request to Priya for ₹500.
- Priya receives: "Rahul is requesting ₹500."
- Priya must **approve** and **enter her UPI PIN** — only then does money leave her account.

> [!tip] Summary
> - **Sending money TO someone** → no receiver approval needed
> - **Taking money FROM someone** → always requires sender's approval + UPI PIN

---

## The Controversial Proposal: Consent for Incoming Payments

### What Exactly Did the MP Ask?

> **"क्या सरकार यूपीआई के इस पैसे ट्रांसफर के सिस्टम में यह प्रावधान लाने का निर्णय लेगी कि किसी भी व्यक्ति के अकाउंट में उसकी सहमति या उसकी जानकारी के बिना पैसा ट्रांसफर न किया जा सके?"**
>
> *"Will the government introduce a provision in the UPI money transfer system so that money cannot be transferred into a person's account without that person's consent or knowledge?"*

He questioned the **Push Transaction** model — why should anyone be able to credit money into another person's bank account without permission?

### Current System vs. Proposed System

**Current System:**
```
Rahul sends ₹1000
       ↓
Money arrives instantly in receiver's account
```

**Proposed System:**
```
Rahul sends ₹1000
       ↓
Notification: "Rahul wants to send you ₹1000."
       ↓
[Accept]  [Reject]
       ↓
Money arrives only after receiver presses Accept
```

Similar to accepting a file transfer or a friend request.

---

## Why Unsolicited Incoming Payments Are a Problem

### 1. "I Sent Money by Mistake" Scam

- Scammer sends you ₹100.
- Calls 10 minutes later: *"Sir, I accidentally sent ₹50,000. Please return it quickly."*
- Victim panics and sends real money.
- The first transfer was only used to start the scam.

### 2. Money Laundering (Money Mules)

- Criminals split ₹50 lakh of illegal money into small amounts (₹500, ₹1,000, ₹2,000, ₹5,000).
- Sent to hundreds of accounts.
- Recipients unknowingly become part of an investigation because illegal funds passed through their accounts.

### 3. Harassment

- Someone knows your UPI ID.
- Sends ₹1, ₹2, ₹5 daily with messages like "Call me", "Please respond", "Remember me?"
- While standard UPI transfers don't support arbitrary messages, repeated unsolicited payments can still be used to annoy or initiate unwanted contact.

### 4. Social Engineering Setup

- Fraudster intentionally sends you money.
- Claims: *"I accidentally paid you. Can you return it to another account?"*
- Many victims comply. The account they send to belongs to another criminal.

---

## Why UPI Was Designed This Way

UPI was built for:
- **Instant settlement**
- **Simplicity**
- **Very high transaction volume** (India processes **billions of UPI transactions every month**)

The core design philosophy:

> Anyone can **give** you money. Nobody can **take** your money without your authorization. That's why only **debits** require your UPI PIN.

Requiring recipients to approve every incoming payment would add friction and slow many legitimate payments.

---

## What Would Break If Consent Were Required?

| Scenario | Problem |
| --- | --- |
| **Salary** | Employer sends salary → Employee must approve before it's credited. Miss the notification → salary stays pending. |
| **Shopping** | You pay at a store → Store owner must approve receiving your payment. Customers wait at checkout. |
| **Hospital** | You pay fees → Hospital accountant has to approve. Queue becomes longer. |
| **Restaurant** | 10 customers pay → Staff must manually accept each payment. |
| **Online refund** | Amazon refunds ₹3,000 → Stays pending until you approve. |

---

## Realistic Solutions (Middle Ground)

Many experts prefer **optional controls** instead of mandatory approval for every payment:

| Option | How It Works |
| --- | --- |
| **Whitelist-only mode** | Accept money automatically only from saved contacts, family, merchants. Unknown senders go to a pending list. |
| **Block unknown senders** | User-enabled setting: "Block payments from unknown UPI IDs." |
| **Sender warnings** | Alerts like "This sender is new" or "This account has been reported for suspicious activity." |
| **Threshold-based approval** | Require approval only for payments above ₹10,000. Small payments remain instant. |
| **AI fraud detection** | Banks auto-flag unusual patterns (e.g., one account sending ₹1 to thousands of unrelated people) and stop/review those transactions. |

---

## Anti-Fraud Measures (What Actually Reduces UPI Fraud)

| Measure | How It Helps |
| --- | --- |
| Better scam detection by banks | Blocks suspicious transactions before money leaves the account |
| AI-based fraud detection | Identifies unusual payment patterns in real time |
| Transaction cooling-off periods for risky payments | Gives users time to cancel fraudulent transfers |
| Public education | Reduces success of phishing and impersonation scams |
| Faster reporting and fund freezing | Increases the chance of recovering stolen money |
| Stronger KYC for mule accounts | Makes it harder for criminals to receive stolen funds |

---

## Would the Proposal Eliminate Scams?

**Not entirely.** It could reduce scams that begin with unsolicited incoming payments, but **most UPI fraud today happens because victims themselves authorize outgoing payments** after being deceived. Criminals trick people into entering their UPI PIN, approving a collect request, or transferring money voluntarily. Recipient consent alone would not stop the majority of UPI frauds.

> [!note] The Core Question
> *"Should anyone in India be able to deposit money into my bank account without my consent or even my prior knowledge?"*
>
> This is less about a flaw in UPI's security technology and more about a **policy question**: should users have more control over who can send them money, or is the convenience of instant payments worth keeping the current model? Parliament and payment regulators would need to balance fraud prevention against the speed and ease that have made UPI so widely used.