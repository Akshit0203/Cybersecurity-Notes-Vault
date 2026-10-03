# GitHub License Types

When you create a public GitHub repository, the **license determines what other people are legally allowed to do with your code**. Without a license, **nobody has permission to copy, modify, or distribute your code**, even if it's public on GitHub.

---

## Quick Comparison

| Feature                       | MIT         | Apache 2.0      | BSD 3-Clause | MPL 2.0          | GPL v3                   |
| ----------------------------- | ----------- | --------------- | ------------ | ---------------- | ------------------------ |
| Commercial use                | ✅           | ✅               | ✅            | ✅                | ✅                        |
| Modify code                   | ✅           | ✅               | ✅            | ✅                | ✅                        |
| Private use                   | ✅           | ✅               | ✅            | ✅                | ✅                        |
| Distribute                    | ✅           | ✅               | ✅            | ✅                | ✅                        |
| Patent protection             | ❌           | ✅               | ❌            | Limited          | Limited                  |
| Must open-source changes?     | ❌           | ❌               | ❌            | Only modified files | Entire derivative work |
| Can make it closed source?    | ✅           | ✅               | ✅            | Partially        | ❌                        |
| Enterprise-friendly           | ⭐⭐⭐⭐      | ⭐⭐⭐⭐⭐         | ⭐⭐⭐⭐        | ⭐⭐⭐              | ⭐⭐                      |
| Simplicity                    | ⭐⭐⭐⭐⭐    | ⭐⭐⭐            | ⭐⭐⭐⭐        | ⭐⭐⭐              | ⭐⭐                      |

| Question                      | MIT         | Apache       | GPL     | MPL       |
| ----------------------------- | ----------- | ------------ | ------- | --------- |
| Easy to understand            | ⭐⭐⭐⭐⭐    | ⭐⭐⭐         | ⭐⭐     | ⭐⭐⭐      |
| Widely used                   | ⭐⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐      | ⭐⭐⭐⭐  | ⭐⭐⭐      |
| Enterprise adoption           | ⭐⭐⭐⭐      | ⭐⭐⭐⭐⭐      | ⭐⭐     | ⭐⭐⭐      |
| Protects contributors         | ⭐⭐         | ⭐⭐⭐⭐⭐      | ⭐⭐⭐⭐  | ⭐⭐⭐⭐    |
| Forces sharing improvements   | ❌           | ❌            | ✅       | Partial   |
| Best for portfolios           | ⭐⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐      | ⭐⭐⭐    | ⭐⭐⭐      |

---

## 1. MIT License (Most Popular)

> **Philosophy:** "Do whatever you want with my code. Just keep my copyright notice."

**Allows people to:**
- ✅ Use your code
- ✅ Modify it
- ✅ Sell it
- ✅ Include it in proprietary software

**They only need to:**
- Keep your copyright notice
- Include the MIT license

### Example

You make an Nmap automation script. Someone can improve it, sell it, and use it inside their company's product. They **don't** have to release their changes publicly.

### Pros
- Extremely short (~170 words)
- Most popular license on GitHub — everyone understands it
- Companies love it → maximum adoption
- Great for GitHub portfolios

### Cons
- No patent protection
- Someone can take your code, improve it, sell it, and never contribute back — this is perfectly legal

### Used By
- jQuery, Rails, Express.js, React, Node.js, VS Code
- Thousands of Python libraries

### Best For
- Personal projects, portfolios, scripts, learning projects, CTF tools

---

## 2. Apache License 2.0

> **Philosophy:** "Use my code however you want, but everyone gets patent rights too."

Does everything MIT does, **plus** patent protection.

**Allows:**
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ✅ Patent license included

**Extra benefits:**
- Better legal protection for contributors
- Preferred by many companies

### Patent Grant — Why Apache Exists

Imagine you invent a completely new way of detecting malware:

```
AI Malware Detection Algorithm
```

You open-source it.

- **Without Apache** — someone could theoretically sue users claiming patent infringement
- **With Apache** — everyone automatically gets a patent license from contributors, making enterprise adoption much safer

### Pros
- Patent protection
- Large company friendly
- Clear legal framework

### Cons
- Longer than MIT
- More legal language

### Used By
- Apache HTTP Server, Kubernetes, TensorFlow, Android (many components)

### Best For
- Professional software, security tools, large projects, enterprise software

---

## 3. GPL v3 (Strong Copyleft)

> **Philosophy:** "If you improve my work and distribute it, everyone should benefit."

GPL forces openness. If someone modifies your code and distributes it, they **must** release their modified version under GPL too. This prevents companies from making your project closed source.

### Example

You create an `Awesome Pentest Tool`. A company modifies it. If they distribute their modified version, they **must** publish their source code under GPL.

### Pros
- Improvements stay open source — community always benefits
- Nobody can "steal" it into proprietary software

### Cons
- Many companies avoid GPL because they don't want to release their own source code
- Less adoption in commercial software

### Used By
- Linux kernel (GPLv2), GNU tools, GIMP

### Best For
- Projects where keeping derivatives open source is a priority

---

## 4. BSD 3-Clause

Almost identical to MIT, but adds a clause:

> "You can't use my name to promote your product without permission."

### Example

You create `CyberScanner`. Someone sells it. They **cannot** advertise:

> "Officially approved by Akshit"

…unless you actually approved it.

### Pros
- Simple, business friendly
- Slightly more protection than MIT

### Cons
- Still no patent protection

---

## 5. MPL 2.0 (Middle Ground)

> **Philosophy:** "Only the files you modify must stay open."

Other files in a larger project can remain proprietary.

### Example

Suppose your project has:

```
tool/
  scanner.py
  parser.py
  api.py
```

Someone modifies only `scanner.py`. Only that modified file must remain open source if distributed. Everything else in their larger application can stay closed source.

### Pros
- Balances openness and commercial use
- Encourages contributions to the original code

### Cons
- Not as widely used or understood as MIT or Apache

### Best For
- Libraries, SDKs, frameworks

---

## Documentation Licenses

Software licenses like MIT or Apache are **not ideal** for documentation. Use Creative Commons instead:

| Content       | Recommended License |
| ------------- | ------------------- |
| Documentation | CC BY 4.0           |
| Notes         | CC BY-SA 4.0        |
| Blog posts    | CC BY 4.0           |
| Images        | CC BY 4.0           |

---

## MIT vs Apache 2.0 — Deep Dive

The biggest confusion is that **MIT and Apache 2.0 give almost the same permissions to users**. The real difference is **what protections they give to _you_ and _your users_**.

### Side-by-Side

| Question                            | MIT | Apache 2.0 |
| ----------------------------------- | --- | ---------- |
| Can people use it?                  | ✅   | ✅          |
| Can they modify it?                 | ✅   | ✅          |
| Can they sell it?                   | ✅   | ✅          |
| Can they keep it closed source?     | ✅   | ✅          |
| Must they credit you?              | ✅   | ✅          |
| Patent protection?                  | ❌   | ✅          |
| Must modified files mention changes? | ❌   | ✅          |
| NOTICE file support?               | ❌   | ✅          |

**95% is identical.** The differences are in the last three rows.

---

### Difference 1: Patent Grant (The Biggest Difference)

This is the main reason Apache exists.

**Timeline scenario** — you create `AI-VulnScanner`, a Python vulnerability scanner:

- **Year 1** — you create and open-source it
- **Year 3** — Google, Microsoft, CrowdStrike, and thousands of companies use it
- **Year 5** — you say: "That detection algorithm is patented. Pay me $1 million." and sue everyone

**Under MIT:**
MIT never explicitly says users get patent rights. This situation can become legally complicated. Users may have to argue about implied licenses or defend themselves in court. Companies think: "Could the author sue us?" That uncertainty is why legal teams sometimes hesitate.

**Under Apache:**
You **already granted** everyone permission to use patents covering your contribution. You cannot later surprise users with a patent lawsuit over the code you contributed. This makes companies much more comfortable.

**What companies' lawyers ask:**

> "Can this developer sue us later over patents?"

- MIT → `Maybe.`
- Apache → `No.`

Guess which answer lawyers prefer? **Apache.**

---

### Difference 2: State Changes

Apache requires that if someone changes your code, they must clearly mention it:

**Original:** `scan.py`

Someone edits it. Apache requires something like:

```python
# Modified by ABC Corp
# Added AI Detection
```

MIT doesn't require that. Someone could completely rewrite the file and not explicitly mark what they changed (though they must still keep the original license and copyright notice).

---

### Difference 3: NOTICE File

Suppose your project contains:

```
NOTICE

Uses Google's tokenizer
Uses Microsoft's parser
Contains work from John Smith
```

Apache says: if someone redistributes your project, they must preserve these attribution notices. MIT has no NOTICE file concept.

---

### Difference 4: Patent Lawsuit Clause

One of Apache's smartest features.

You contribute an `AI Detection Engine`. Later you sue another company claiming your contribution infringes your patent.

Apache says:

```
If YOU start patent litigation,
YOU lose your patent license under Apache.
```

This discourages patent lawsuits among contributors. MIT doesn't include this mechanism.

---

### Contributor Patent Rights

Suppose another developer contributes `AI Ransomware Detection` to your project. Later that contributor owns a patent on the technique.

- **MIT** — the contributor might later argue about patent rights because MIT doesn't explicitly grant them
- **Apache** — by contributing under Apache 2.0, they automatically grant patent rights needed to use their contribution. Everyone is safer.

---

## Why Companies Prefer What They Prefer

**Why huge companies love Apache:**
Imagine you're Google — 20,000 developers, thousands of patents, billions of dollars. You want legal certainty. Apache gives lawyers a clear framework. MIT is intentionally minimalist.

**Why individuals love MIT:**
Because it's tiny. The entire license fits on one screen. No complicated legal wording. Just:

> Here's my code. Don't sue me. Keep my copyright notice.

Done.

### What Large Organizations Choose

| Organization | Typical License                     |
| ------------ | ----------------------------------- |
| Google       | Apache 2.0                          |
| Microsoft    | MIT (many repos)                    |
| Meta         | MIT / Apache 2.0 (varies)          |
| Kubernetes   | Apache 2.0                          |
| TensorFlow   | Apache 2.0                          |
| React        | MIT                                 |
| Node.js      | MIT                                 |
| VS Code      | MIT                                 |

**Why Google chose Apache:** Without Apache, a developer contributes code → legal team asks "Can they sue us later?" → Nobody knows. With Apache, developer contributes code → patent rights granted → legal team says "Approved." That's why Kubernetes and many Apache Foundation projects use Apache 2.0.

**Why Microsoft often chooses MIT:** Maximum adoption, projects don't always involve patent-sensitive technology, MIT is extremely simple and widely understood.

---

## Which License for What — Cybersecurity Guide

### Offensive Security Tools
Enumeration tools, recon tools, OSINT utilities, automation scripts, CTF helpers
→ **Apache 2.0 or MIT**

### Libraries
Python packages, Go modules, security SDKs
→ **Apache 2.0**

### Research Code
Malware analysis, exploit research, AI security experiments
→ **Apache 2.0**

### Community-First Projects
If your goal is to ensure improvements remain open source
→ **GPL v3**

---

## Practical Examples

### Example 1 — Small Project

```
python-port-scanner
```

100 lines. Anyone can use it.
→ ✅ **MIT** — nobody cares about patents for a small educational script

### Example 2 — Large Security Framework

```
AI-XDR
```

50,000 lines. 100 contributors. Companies use it. People build products on top of it.
→ ✅ **Apache 2.0** — patents matter, contributors matter, companies need legal certainty

### Example 3 — Research Platform (e.g., Wi-Fi CSI)

Researchers start using it. Universities cite it. Companies integrate it.
→ ✅ **Apache 2.0** — research-oriented, reusable platform with potential commercial adoption

### Example 4 — Documentation (e.g., Obsidian Notes)

No patents. No algorithms being commercialized.
→ ✅ **MIT** (for code snippets) or **CC BY 4.0** (for the notes themselves)

---

## Per-Repository Recommendations

| Project                        | License     | Why                                                  |
| ------------------------------ | ----------- | ---------------------------------------------------- |
| HTB/THM writeups               | CC BY 4.0   | Documentation, not software                          |
| Small Python scripts           | MIT         | Simple, permissive, easy for others to use           |
| Bash utilities                 | MIT         | No meaningful patent concerns                        |
| Recon tools                    | MIT         | Lightweight utilities                                |
| Security automation platform   | Apache 2.0  | Better legal protection as the project grows         |
| AI security tools              | Apache 2.0  | Patent grant can matter for novel algorithms         |
| Wi-Fi CSI framework            | Apache 2.0  | Research-oriented, potential commercial adoption      |
| Reusable Python libraries      | Apache 2.0  | Patent protection matters with broad adoption        |
| Portfolio website              | MIT         | Simple personal project                              |
| Obsidian vault                 | MIT or CC BY 4.0 | MIT if code-heavy, CC BY 4.0 if notes-heavy     |

---

## TL;DR — Simple Rules

- **MIT** = "Here's my code. Use it however you want. Just keep my copyright notice."
- **Apache 2.0** = "Here's my code. Use it however you want. Keep my notices, mark your changes, and everyone gets clear patent rights."
- **GPL v3** = "If you modify and distribute this, you must open-source your version too."

For **95% of hobby and portfolio repositories**, either MIT or Apache works. The reason many professional organizations default to **Apache 2.0** isn't because it restricts users more — it doesn't. It's because it provides additional legal certainty around patents, which becomes valuable when software is widely adopted or commercialized.

> [!tip] One default license for all code repos?
> **Apache License 2.0** — permissive like MIT but adds patent protection. Widely trusted in professional and enterprise environments.