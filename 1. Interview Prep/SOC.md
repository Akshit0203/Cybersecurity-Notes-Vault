
Q1. How would you investigate failed logins/brute force attacks on Windows/Linux:  
Ans: Start with volume and pattern. Is it just one account or multiple accounts? Same source IP or distributed? Failed then succeeded, or just failed? This would tell you whether it’s a user, a lockout loop, or password spraying.  
  
Q2: How do you decide if an alert is FP?  
Ans: Compare against baseline. Does this user do this regularly? Does this process normally run from this path? Always see the context, alert JSON before even running queries.  
  
Q3: Whats the difference between detection and investigation?  
Ans: Detection is the tool telling you something happened. Investigation is you figuring out what actually happened.  
  
Q4: How do you investigate an alert/Scenario based question/Hardest incident you worked?  
Ans: Use STAR(Situation Task Action Result) format, always mention a process improvement/learning from the incident.  
If your only answer is a TryHackMe room, build a home lab this week. Do one real investigation. Document it. That story is worth more than three certifications in an interview room.