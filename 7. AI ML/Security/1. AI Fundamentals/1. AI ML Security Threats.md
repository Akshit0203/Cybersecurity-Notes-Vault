# AI/ML Security Threats

> Foundations of AI & ML — key concepts, terminology, and how they relate to security.

---
## What is AI?

- **Artificial Intelligence** = machines carrying out tasks that normally require human reasoning, comprehension, problem-solving, or creativity
- The term dates back to the **1950s** — research on having machines simulate human intelligence
- AI is the **goal** — making systems intelligent

---
## What is Machine Learning?

- **ML is a subset of AI** — a computer's ability to learn from data without explicit instructions
- Comparable to how the human brain learns from experience
- With more data and time, ML algorithms improve in accuracy and decisions
- ML is the **method** — one way to achieve AI by learning from data

> **All ML is AI, but not all AI is ML.**
### AI vs ML — Simple Distinction

| Approach | How It Works                      | Example                           |
| -------- | --------------------------------- | --------------------------------- |
| **AI**   | Hardcoded rules (if-else logic)   | "If email has 'win money' → spam" |
| **ML**   | Learns patterns from labeled data | Trained on 10,000 labeled emails  |

| Feature    | AI                        | ML                        |
| ---------- | ------------------------- | ------------------------- |
| Scope      | Broad field               | Subset of AI              |
| Goal       | Mimic human intelligence  | Learn from data           |
| Approach   | Rules, logic, ML, etc.    | Data-driven learning      |
| Dependency | Can work without ML       | Needs data                |

---

## ML Lifecycle

```
Define Problem → Collect Data → Clean & Prepare → Feature Engineering → Train Model → Evaluate & Tune → Deploy → Monitor → Retrain
```

> The ML lifecycle is **iterative** — models require continuous improvement.

### 1. Define the Problem

- What should the model do? (e.g., classify emails as spam or not spam)
- This determines the type of problem: **classification**, **regression**, etc.

### 2. Collect Data

- The model learns from examples — without data, no learning happens
- Example: 50,000 emails, each labeled "spam" or "not spam"

### 3. Clean the Data

- Real-world data is messy — fix duplicates, empty entries, formatting issues
- `"WIN $$$ NOW!!!"` → cleaned → `"win now"`
- Messy data = confused model

### 4. Feature Engineering

- Convert raw data into **numbers** the model can understand
- Extract meaningful features from raw input

| Feature              | Example Value |
| -------------------- | ------------- |
| Number of links      | 3             |
| Contains word "free" | 1 (yes)       |
| Email length         | 250 chars     |
| Capital letter count | 10            |

> This is where **patterns are made visible** to the model.

### 5. Train, Evaluate & Deploy

- Train using a selected algorithm
- Evaluate performance, tune to optimize
- Deploy into production (e.g., classifying emails in real-time)
- **Monitor** ongoing accuracy — retrain when performance drops

---

## Overfitting

When a model **memorizes** training data instead of learning generalizable patterns.

- Works great on training data ✅ — fails on new/unseen data ❌

### Why It Happens

- Too much focus on training data
- Model too complex for the dataset
- Not enough variety in data

### Analogy

- **Overfitting** = student who memorized answers → fails new questions
- **Good model** = student who understands concepts → handles new problems

---

## ML Algorithm Categories

| Category               | Data Type                | How It Works                                              | Example Use Case          |
| ---------------------- | ------------------------ | --------------------------------------------------------- | ------------------------- |
| **Supervised**         | Labeled data             | Learns from input-output pairs for classification/regression | Spam detection, price prediction |
| **Unsupervised**       | Unlabeled data           | Discovers hidden patterns (clustering, association)        | Customer segmentation     |
| **Semi-supervised**    | Mix of labeled + unlabeled | Small labeled set guides learning on larger unlabeled data | Medical image analysis    |
| **Reinforcement**      | No dataset — trial & error | Agent learns by rewards/penalties over time                | Game-playing AI, robotics |

### Three Components of an ML Algorithm

1. **Decision process** — makes predictions/classifications from input
2. **Error function** — evaluates performance and provides feedback
3. **Model optimization** — fine-tunes to minimize errors iteratively

---

## Neural Networks

Inspired by the human brain's interconnected neurons and synapses.

### Structure

```
Input Layer → Hidden Layer(s) → Output Layer
```

| Layer           | Role                                                              |
| --------------- | ----------------------------------------------------------------- |
| **Input layer** | Receives raw data (e.g., 4×4 pixel image = 16 nodes)             |
| **Hidden layers** | Process and refine data, extract features progressively         |
| **Output layer** | Produces final prediction (e.g., 10 nodes for digits 0–9)       |

- Each **node** = neuron, each **connection** = synapse
- Each connection has a **weight** determining its importance
- Example: in email classification, body text may carry more weight than the subject line

### How Recognition Works (Digit Example)

- Early layers detect **edges and curves**
- Deeper layers combine patterns to form **complete shapes**
- Output layer selects the digit with the **highest prediction value**

---

## Deep Learning

DL is a subset of ML that uses neural networks with **more than 3 layers**.

| Feature              | ML                                    | Deep Learning                          |
| -------------------- | ------------------------------------- | -------------------------------------- |
| Data requirements    | Needs **labeled** data                | Can work with **unlabeled** raw data   |
| Feature extraction   | Manual (feature engineering)          | **Automatic** (self-learning)          |
| Human intervention   | Required for labeling                 | Not required                           |
| Scalability          | Limited by labeling effort            | "Scalable ML" — handles massive datasets |
| Network depth        | Shallow models                        | 3+ layers (deep neural networks)       |

### Why DL Exploded Recently

- Mass **digitization of information** → huge datasets became available
- More data + deep neural networks = unlocking new AI capabilities

> DL doesn't need labeled data → no human intervention required → **self-learning** → can process much larger datasets than traditional ML.

---

## Quick Reference

| Concept                | Definition                                                     |
| ---------------------- | -------------------------------------------------------------- |
| **AI**                 | Machines performing tasks requiring human intelligence         |
| **ML**                 | Subset of AI — learning from data without explicit programming |
| **Deep Learning**      | Subset of ML — neural networks with 3+ layers, self-learning  |
| **Neural Network**     | Interconnected nodes mimicking brain neurons and synapses      |
| **Overfitting**        | Model memorizes training data, fails on unseen data            |
| **Feature Engineering** | Converting raw data into meaningful numerical features        |
| **Supervised Learning** | Trained on labeled data                                       |
| **Unsupervised Learning** | Finds patterns in unlabeled data                           |

---

## Large Language Models (LLMs)

**LLMs** = deep learning-based AI models that process and generate text by **predicting the next word** in a sequence.

- Powered by **transformer neural networks** and trained on massive text corpora
- Examples: ChatGPT, LLaMA, DeepSeek

### How LLMs Work

```
Pre-training → Fine-tuning (Backpropagation) → RLHF → Deployment
```

1. **Pre-training** — model processes vast amounts of text (GPT-3's training data would take a human ~2,600 years to read)
2. **Next-word prediction** — model predicts the next word, compares against actual, adjusts **billions of parameters** via **backpropagation**
3. **RLHF** (Reinforcement Learning from Human Feedback) — humans review outputs, flag unhelpful/harmful predictions, parameters adjusted accordingly
4. **Deployment** — query is fed in, model predicts response word by word

> LLMs don't use labeled data — they use billions of parameters fine-tuned automatically based on prediction accuracy.

### Transformer Neural Networks

- Introduced in Google's **2017 paper** — *"Attention is All You Need"*
- Enabled **parallel text processing** instead of sequential word-by-word analysis
- **Attention mechanism** — assigns importance scores to key words for better contextual understanding
- Solves ambiguity — e.g., in *"The bank approved the loan because it was financially stable"*, correctly identifies "it" = "the bank"

### Generative AI

- LLMs power generative AI products (ChatGPT, LLaMA) that create **original text-based content** from user prompts
- Generative AI extends beyond text — images, music, code, etc.
- The AI boom is the result of **decades of research**, not overnight development

### How It All Connects

| Layer | Role |
| ----- | ---- |
| **AI** | Overarching field — systems that mimic human intelligence |
| **ML** | Subset of AI — learns patterns from data without explicit programming |
| **DL** | Subset of ML — neural networks processing data without human intervention (scalable ML) |
| **LLMs** | Advanced DL models built on **transformers** — understand and generate human-like text |

---

## AI Security Threats

AI security threats fall into two categories:
1. **Vulnerabilities in AI models** — new threats introduced by AI adoption
2. **Enhanced attacks** — existing attacks amplified by AI capabilities

> **MITRE ATLAS** framework — built on top of ATT&CK, specifically focused on AI cyber threats → [atlas.mitre.org](https://atlas.mitre.org/matrices/ATLAS)

### Vulnerabilities in AI Models

| Vulnerability | Description | Example |
| ------------- | ----------- | ------- |
| **Prompt Injection** | Overriding a model's original instructions to make it disclose information or generate harmful content | Bypassing an RPG chatbot's system prompt to extract training details |
| **Data Poisoning** | Manipulating training data so the model produces incorrect or biased outputs | Poisoning spam filter training data so attacker's spam emails bypass detection |
| **Model Theft** | Gaining unauthorized access to an AI model to steal IP or replicate behavior | Querying a model's API repeatedly, using outputs to train a clone model |
| **Privacy Leakage** | Model inadvertently reveals sensitive information from its training data | Medical AI leaking patient records to users |
| **Model Drift** | Model performance degrades over time as data/environment changes | Historical model failing on new data patterns — requires retraining |

### Enhanced Attacks

**AI-Enhanced Malware**
- Generative AI enables attackers to **generate malware code instantly**
- Lowers the skill barrier — attackers no longer need deep programming knowledge

**Deepfakes**
- AI generates a person's **voice or likeness** with high accuracy
- Undermines **authentication** — attackers impersonate trusted individuals
- Real-world examples: deepfaked video interviews, fraudulent voice calls to extract confidential info

**AI-Enhanced Phishing**
- Generative AI produces **fluent, context-specific phishing emails** — harder to spot than traditional broken-language attempts
- Attackers bypass GPT-style safety mechanics using **prompt injection** techniques
- Traditional "look for bad grammar" training is no longer sufficient

---

## Defensive AI

AI is not just a threat — it's a powerful **defensive tool** when adopted and secured properly.

### Impact (IBM Cost of a Data Breach Report)

| Metric | Value |
| ------ | ----- |
| Average cost of a data breach | **$4.88M** |
| Average savings with AI adoption | **$2.2M** |
| Reduction in breach identification + containment time | **108 days** |

### How AI Enhances Defence

**Analysis**
- ML excels at recognizing **patterns and anomalies** in data (e.g., network traffic)
- Enables faster **intrusion detection** at scale
- Products leveraging this: **Microsoft Defender for Endpoint**, **Splunk**

**Prediction & Automation**
- AI models trained on phishing examples can **recognize and block** phishing emails before they reach users
- Automates security workflows — "if-then" logic enhanced by ML predictions
- Core to **DevSecOps** automation methodologies

**Summarisation**
- AI summarises **incident reports, documents, and artefacts** in minutes
- Can draw **correlations between incidents** that humans might miss
- Massive time savings in incident response

**Investigation**
- Feed logs into an LLM → get **diagnostic queries and triage assistance** in natural language
- Assists **threat hunting** — AI can propose attack vectors humans wouldn't think of
- Augments human imagination in security scenario planning

### Securing AI (Secure AI Adoption)

> Only **24%** of generative AI initiatives are currently secured (IBM report).

| Practice | Details |
| -------- | ------- |
| **Access Control** | Enforce strict access with **RBAC** and **MFA** — limit who can interact with AI models |
| **Privacy Protection** | Encrypt training data — treat it as sensitive data (patient records, PII, etc.) |
| **Security Standards** | Implement frameworks like **ISO/IEC 27090** across development, deployment, and maintenance |
| **Model Monitoring** | Detect performance drops, unexpected behavior, biases, and anomalies — use explainability tools like **SHAP** and **LIME** |
