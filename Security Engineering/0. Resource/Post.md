
https://www.linkedin.com/feed/update/urn:li:activity:7481018086754648065/

Jail >>>>>> Democracy (in the AI-world)  
  
I know that the above statement is silly, but jailing engineering teams is superior to collaboration in an AI-world. Consequences work better than incentives and that is the strategy that we used to fix a year’s worth of vulns in one month here at Rippling.  
  
Vulnerability management programs run like negotiations. Security teams chase Engineering teams to fix vulns, we track data and escalate when SLAs are missed. If a team falls behind, they’d ask for an extension and someone in their leadership chain would sign off on it. It has been a constant cycle of requests and approvals.  
  
I have seen this throughout the industry and product roadmaps always win the tug-of-war against Security. Security debt will accumulate and it is challenging to hold people accountable to fix issues.  
  
For the past two quarters, we stopped being accommodating and start jailing engineering teams 皿  
  
When there are no consequences to ignore security issues, engineers focus on areas where there are consequences (missing feature development deadlines). Security is a prioritization problem.  
  
What is Vulnerability Jail? If a vulnerability goes over SLA, engineers can no longer merge PRs into the main branch of their repository. Stakes are high, but it changed how engineers view vulns. Engineers realized they couldn’t ship features if their vuln queue was large and they started collaborating with us before hitting limits, not after.  
  
The result? We’re now fixing as much in four weeks as we used to fix in an entire year. Engineers realized that fixing a vulnerability today is a lot easier than dealing with a jail sentence tomorrow.  
  
This wasn't a technical fix (or an AI-fix), it was a cultural one and here’s how we made it stick:  
1️⃣ Leadership Buy-in: Most critical piece, I’ve been in DMs where engineers complain to their VPs about stopping feature work to fix vulns and the VPs stood their ground and told them to prioritize the security work. Without their support, the program would have failed.  
  
2️⃣ A Bulletproof Ownership Model: We’re pushing thousands of vulns to hundreds of engineers. We had to automate the ownership mapping to ensure we aren’t jailing the wrong teams by mistake.  
  
3️⃣ Quick reversals: Ownership model isn’t exactly bulletproof 😅, mistakes happen. We built a system to quickly revert the jailing of teams. We run the jail automation every few minutes.  
  
4️⃣ A "High-Response" Security Team: When a team gets jailed, we don't disappear. Our on-call Security engineers are ready to jump in immediately to help teams clear their queue and get back to shipping.  
  
When the entire world is moving so quickly, you can’t leverage relationships and persuasion to address security technical debt. You need clear goals and clear consequences to drive the right behaviors.  
  
If this seems interesting to you, I have opened up another role on my team, more information on that in the comments.

------------

