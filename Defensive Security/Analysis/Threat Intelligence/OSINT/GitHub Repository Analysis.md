
- You’re analyzing **public data (GitHub)** → OSINT
- Looking for leaks/secrets → Threat Intelligence
- Large-scale analysis → Analysis domain

# GitHub Repository Analysis (Large Scale)

## Goal
Analyze thousands of repositories to find:
- Secrets
- Sensitive data
- Employee patterns

## Workflow

### 1. HTTP Status Check
- Check if repo is active / accessible
- Python script to send requests

### 2. Secret Scanning
- Tools:
  - gitleaks
  - trufflehog (faster)
- Detect:
  - API keys
  - Tokens
  - Credentials

### 3. Email / Identity Analysis
- Check commits for:
  - Employee emails
  - Internal domains

### 4. Deduplication
- Remove repeated repos / forks
- Avoid duplicate findings

## Tools
- Python (requests, multiprocessing)
- gitleaks
- trufflehog

## Real Use Case
- Bug bounty recon
- Data leak detection
- Threat intelligence collection