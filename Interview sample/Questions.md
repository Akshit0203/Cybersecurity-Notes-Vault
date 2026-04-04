
Question : If HTTPS is secure, how do attackers still steal data?
Answer : - SSL Stripping → Enforce HSTS + redirect HTTP → HTTPS
- TLS Downgrade → Disable old protocols (TLS 1.0/1.1)
- Rogue CA → Certificate pinning
- BGP Hijack → DNSSEC + monitoring
- CRIME/BREACH → Disable TLS compression
- Phishing → Domain awareness + user education
- XSS → Input sanitization + CSP
- Supply Chain → Subresource Integrity (SRI)
- Response Splitting → Validate headers
- HSTS bypass → Preload your domain

---




