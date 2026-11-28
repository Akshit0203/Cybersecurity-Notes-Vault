# Key Learnings

---

## AI Standards — What Counts & What Does Not

| Category | Example | Verdict |
|----------|---------|---------|
| Independent AI certification | ISO/IEC 42001 | ✅ Counts |
| Information security certification | ISO 27001, SOC 2 | ❌ That's security, not AI governance |
| Vendor's own "Responsible AI" page | — | ❌ That's marketing |

---

## Rules or AI? — The Deciding Question

> **Can you write the correct answer down in advance, and will it stay true?**

| | Use Rules (if/then logic) | Use AI (learn pattern from data) |
|---|---|---|
| **Answer** | **Yes** — you can write it down | **No** — you cannot |
| Logic | Known and fixed | Relationships keep shifting |
| Variables | Only a few matter | Too many interacting variables |
| Inputs | Structured | Unstructured |

### Why Rules Are Underrated

- Cheaper to build and to run
- Explainable by reading them
- Identical result every time
- No drift — no monitoring, no retraining

> [!warning] Both wrong choices cost money and fail differently
> - **AI where a rule would do** → paying for complexity you don't need
> - **Rules where the pattern is complex** → brittle logic, endless exceptions

### Sounds Like AI, Only Needs Rules

| Argument | Reality |
|----------|---------|
| "It's automation" | Rules automate too |
| "The volume is huge" | Rules scale too |
| "The data sits in five systems" | That's an integration job |
| "Users want an explanation in plain English" | That's a UI feature |

> [!tip] Exam Tip
> Name the pattern the system must find. **No pattern to find → it's a rule.**

---

## Four Kinds of AI Solution

| Type | What It Does | Example |
|------|-------------|---------|
| **Assistant** | Gives an answer | "What is our refund policy?" |
| **Dashboard** | Gives a view | "How many refunds this week?" |
| **Predictive Model** | Gives a score | "Is this refund request fraudulent?" |
| **Agent** | Takes the action | "Process this refund" |

> [!important]
> Only the **agent** acts on its own, without a person approving each step.

---

## Shadow AI

> Shadow AI is a symptom of **missing governance**, not of bad employees.

---

## Personal Reflection

From a recent work experience — we had a situation where the team was confused whether to use automation or agentic AI. The team wanted agentic AI; the manager wanted automation.

This certification helped me understand that this is exactly where an **AI Business Strategist** comes into play — knowing exactly:

- **Where to use simple rule-based automation** → e.g., SOC alerts
- **Where to use generative AI** → e.g., report generation
- **When to use an assistant vs. a dashboard vs. an agent vs. a predictive model**

> [!note]
> This might seem like a small thing, but in day-to-day tasks we tend to forget the fundamentals.