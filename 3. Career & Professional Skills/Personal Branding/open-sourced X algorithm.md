
The latest open-sourced X (“For You”) algorithm is basically a massive real-time AI recommendation pipeline that decides:

- which posts to fetch,
- which ones you are most likely to engage with,
- and in what exact order they appear.

The main public repos are:

- [twitter/the-algorithm GitHub repo](https://github.com/twitter/the-algorithm?utm_source=chatgpt.com)
- [xai-org/x-algorithm GitHub repo](https://github.com/xai-org/x-algorithm?utm_source=chatgpt.com)

The newer one is the important one because it shows the newer “Phoenix” transformer-based architecture.

---

# High-Level Architecture

The pipeline works like this:

```
1. User opens X2. System gathers user context3. Retrieve candidate tweets/posts4. AI ranks all candidates5. Filters remove bad/duplicate/spam content6. Feed mixer assembles final timeline7. Timeline served in <200ms
```

The key idea:

X does NOT evaluate all posts on Earth.

That would be impossible.

Instead it progressively narrows:

```
500M+ daily posts      ↓~100k possible candidates      ↓~1500 shortlisted candidates      ↓~100 final ranked posts
```

---

# Core Components

## 1. Query Hydration (Understanding YOU)

Before ranking anything, X builds a “user state”.

It gathers:

- Accounts you follow
- Your likes
- Retweets
- Replies
- Watch time
- Click behavior
- Communities joined
- Spaces listened to
- Topics interacted with
- Time spent on posts
- Posts you ignored
- Block/mute history

This becomes a giant embedding vector.

Think of it like:

```
user_embedding = [   politics_interest,   startup_interest,   cybersecurity_interest,   meme_interest,   ai_interest,   ...]
```

This vector is the “digital personality” used by the model.

---

# 2. Candidate Retrieval

This is the MOST important scaling trick.

Instead of ranking millions of tweets directly, X first retrieves likely-good candidates.

It uses TWO major sources:

---

## A) In-Network Retrieval (“Thunder”)

Posts from:

- people you follow
- people followed by your network
- replies inside your network

This is safer and more predictable.

Example:

If you follow:

- cybersecurity people
- AI researchers
- startup founders

Thunder fetches recent tweets from those circles.

---

## B) Out-of-Network Retrieval (“Phoenix Retrieval”)

This is where viral discovery happens.

AI searches across the ENTIRE platform to find posts similar to your interests.

This uses:

- embeddings
- vector similarity
- transformer retrieval models

Example:

You never followed someone posting about:

- SDR
- HackRF
- OSCP

But if your behavior resembles users who engage with those topics, Phoenix retrieves those tweets.

This is how unknown accounts suddenly explode.

---

# 3. Embeddings System

This is the heart of modern recommendation systems.

Everything becomes vectors:

- users
- posts
- hashtags
- communities
- topics
- creators

Example:

```
You:[0.9 cybersecurity, 0.8 AI, 0.2 football]Tweet:[0.95 cybersecurity, 0.7 AI, 0.1 football]
```

Cosine similarity becomes high:

```
=> show this tweet
```

This replaces old manual rules.

Old Twitter:

```
if likes > 100:   boost()
```

New X:

```
if embedding_similarity(user, post) high:   boost()
```

Huge difference.

---

# 4. Transformer Ranking Model (Phoenix)

This is the biggest change.

The old system used:

- gradient boosted trees
- manually engineered features

The new system uses:

- transformer architectures
- Grok-inspired ranking models
- sequence understanding

---

## What the Transformer Predicts

The model predicts probabilities for:

- Like
- Reply
- Retweet
- Profile click
- Follow
- Long dwell time
- Video completion
- Share
- Conversation quality

Example:

```
tweet_score =   0.3 * like_probability +   0.5 * reply_probability +   0.8 * repost_probability +   1.2 * follow_probability
```

Not exact weights — but conceptually similar.

---

# 5. Conversation-Centric Ranking

One huge discovery from the code:

Replies and conversations matter MUCH more now.

Likes are weaker than before.

Why?

Because likes are cheap.

Replies indicate:

- emotional reaction
- debate
- engagement depth

This is why ragebait often spreads.

The algorithm often confuses:

- outrage  
    with
- interest

Even Musk admitted this publicly.

---

# 6. Dwell Time Tracking

X tracks:

- how long you stop scrolling
- how long you watch
- whether you expand replies
- whether you read thread continuation

Even WITHOUT liking.

Example:

```
If you stare at a post for 12 seconds:algorithm thinks:"interesting"
```

This is extremely important.

Modern recommendation systems heavily weight passive engagement.

---

# 7. Social Graph Amplification

The algorithm heavily uses graph relationships.

If many people similar to you engage with a post:

```
your_probability_of_liking ↑
```

This is collaborative filtering.

Same principle used by:

- TikTok
- YouTube
- Netflix
- Instagram Reels

---

# 8. Real-Time Feedback Loops

The system constantly updates rankings.

A tweet can suddenly explode because:

```
small early engagement spike       ↓boosted to more users       ↓more engagement       ↓boosted harder       ↓viral cascade
```

This is why:

- first 30 minutes matter heavily
- replies matter massively
- repost chains matter

---

# 9. Filtering Layer

After ranking, X applies filters.

These include:

- NSFW filtering
- spam filtering
- deduplication
- engagement bait detection
- block/mute enforcement
- author fatigue limits
- diversity balancing

Example:

Even if 10 Elon tweets rank highly:

- system may intentionally reduce repetition.

---

# 10. Feed Mixer

Final stage.

The Home Mixer combines:

- ads
- in-network posts
- out-of-network posts
- videos
- trends
- replies
- threads

Then constructs final order.

This is basically orchestration logic.

---

# Technologies Used

From the repo:

|Component|Tech|
|---|---|
|Core services|Rust|
|ML pipelines|Python|
|ML framework|JAX|
|Embeddings|Vector retrieval|
|Ranking|Transformer models|
|Messaging|Kafka|
|APIs|gRPC|
|Feature store|Internal infra|

---

# Biggest Shift vs Old Twitter Algorithm

Old Twitter:

```
Manual features+heuristics+engagement counters
```

New X:

```
Transformer AI+embedding similarity+behavior understanding+sequence modeling
```

This is VERY similar to TikTok now.

---

# Why Some Posts Go Viral Now

The new algorithm strongly rewards:

- replies
- controversy
- long reading time
- quote tweets
- discussion chains
- emotional engagement
- niche authority

Weak signals:

- hashtags
- follower count alone
- pure likes

This is why small accounts can suddenly explode.

---

# Why Open-Sourcing This Matters

This is rare.

Almost no major platform exposes:

- ranking pipelines
- retrieval architecture
- ML orchestration
- scoring systems

Researchers are now studying it heavily because it shows:

- production-scale recommender design
- transformer-based feed ranking
- real-world AI infrastructure

---

# Important Reality Check

Even though the repo is huge, it is STILL incomplete.

Missing pieces likely include:

- production model weights
- anti-abuse internals
- ad ranking details
- internal infrastructure
- some moderation systems

So the public repo is:

- very real,
- but not literally the entire production system.

---

# If You Want To Learn From It

The BEST things to study are:

1. Candidate retrieval architecture
2. Embedding systems
3. Ranking pipelines
4. Transformer recommenders
5. Feature hydration
6. Feed orchestration
7. Real-time inference systems

This repo is basically a masterclass in:

- large-scale recommender systems
- ML engineering
- distributed systems
- AI ranking pipelines

The architecture concepts are extremely useful for:

- AI security
- social media intelligence
- recommendation systems
- cyber threat prioritization
- SOC alert ranking
- autonomous agents

because all of those are fundamentally ranking/filtering problems.