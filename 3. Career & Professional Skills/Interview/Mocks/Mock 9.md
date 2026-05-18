
## INTRO / BACKGROUND

1. Why cybersecurity?
2. Why are you interested in security compared to other domains?

---

## AI / SYSTEM DESIGN SCENARIO

## How will you secure AI Agents ?

3. What are the threats of having an AI system deployed internally?
4. What would be the attack surface in such a system?
5. What kind of threats can arise from such a setup?
6. What kind of sensitive data could be exposed?
7. How would you fix these issues?
8. How would you design protections for such a system?
9. What kind of access control would you implement?
10. How would you prevent privilege escalation (vertical and horizontal)?
11. What other security mechanisms would you add?
12. How would you handle logging and monitoring?
13. How would you validate outputs from the system?

---

## DATA SECURITY / ARCHITECTURE

14. What are the risks when sending data to cloud systems?
15. How will you protect sensitive data before sending it?
16. What is better — local deployment or cloud deployment? Why?

---

## IAM / ACCESS CONTROL

17. How will you implement access control practically?
18. How will IAM (Identity & Access Management) work in your system?
19. How will the system authenticate and authorize itself?

---

## ATTACK METHODOLOGY / STEALTH

20. How would you perform reconnaissance in a stealthy way?
21. What techniques will you use to avoid detection during scanning?
22. Why do you need stealth in scanning?
23. What are some less noisy attack techniques?

---

## DEFENSIVE THINKING

24. How would you prevent DoS/DDoS attacks?

---

## EXPLOITATION / VULNERABILITIES

25. If a service like MySQL is running, what attacks would you try?
26. What attacks would you try on SSH?
27. What is directory traversal and how would you exploit it?

---

## AUTHENTICATION / AUTHORIZATION

28. What is faulty authentication?
29. How does improper authorization lead to vulnerabilities?
30. How will you prevent unauthorized access?

---

## SQL INJECTION

31. How does SQL injection work?
32. How will you prevent SQL injection?

---

## XSS (CROSS-SITE SCRIPTING)

33. What is XSS?
34. What are different types of XSS?
35. What is the impact of XSS?
36. How would you exploit XSS?
37. How would you protect against XSS?

---

## SESSION / TOKEN SECURITY

38. How would you protect session tokens?
39. How would you prevent session hijacking?

---

## CODING QUESTION

40. Given logs of IP and ports, how will you identify IPs connecting to multiple ports?
41. How will you parse and process such data?
42. What data structures will you use?
43. How will you count connections per IP?

**Coding Exercise (Netflow Analysis)**
- read netflow.txt, split “src:port -> dst:port” lines
- store destination ports per (source IP, destination IP) in a set
- print source IPs with ≥ 3 unique ports to same destination