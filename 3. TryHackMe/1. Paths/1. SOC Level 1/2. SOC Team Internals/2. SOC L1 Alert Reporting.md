
## Task 2 Alert Funnel

![Pasted image 20251123144514.png](attachments/Pasted%20image%2020251123144514.png)

Alert Reporting
Before closing or passing the alert to L2, you might have to report it. Depending on team standards and alert severity, instead of a short alert comment, you can be required to document your investigation in detail, ensuring all relevant evidence is included. This is especially important for True Positives, which require escalation.

Alert Escalation
If the True Positive alert requires additional actions or deeper investigation, escalate it to the L2 analyst for further review following the agreed procedures. That's where your alert report comes in handy since L2 will use it to get the initial context and spend less on the analysis from scratch.

Communication
You may also need to communicate with other departments during or after the analysis. For example, ask the IT team if they confirm granting administrative privileges to some users or contact HR to get more information about the newly hired employee.


## Task 3 Reporting Guide

Having L1 analysts write alert reports serves several key purposes:

|   |   |
|---|---|
|**Alert Report Purpose**|**Explanation**|
|Provide context for escalation|- A well-written report saves lots of time for L2 analysts<br>- Also, it helps them quickly understand what happened|
|Save findings for the records|- Raw SIEM logs are stored for 3-12 months, but alerts are kept indefinitely<br>- As a result, it's better to keep all the context inside the alert, just in case|
|Improve investigation skills|- If you can't explain it simply, you don't understand it well enough<br>- Report writing is a great way to boost L1 skills by summarising alerts|

Report Format

![An example of good, structured report following the 5Ws approach](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1743611080297.svg)

Imagine yourself as an L2 analyst, a DFIR team member, or an IT professional who needs to understand the alert. What would you want to see in the report? We recommend you follow the **[Five Ws](https://en.wikipedia.org/wiki/Five_Ws)** approach and include at least these items in the report:

- **Who**: Which user logs in, runs the command, or downloads the file
- **What**: What exact action or event sequence was performed
- **When**: When exactly did the suspicious activity start and ended
- **Where**: Which device, IP, or website was involved in the alert
- **Why**: The most important W, the reasoning for your final verdict

## Task 4 Escalation Guide

You should escalate the alerts if:

1. The alert is an indicator of a major cyberattack requiring deeper investigation or DFIR
2. Remediation actions like malware removal, host isolation, or password reset are required
3. Communication with customers, partners, management, or law enforcement agencies is required
4. You just do not fully understand the alert and need some help from more senior analysts

### Escalation Steps

To escalate the alert, in most cases, all you have to do is to **reassign the alert to the L2 on shift** and ping them in corporate chat or in person. In some teams though, you may be required to create a formal written escalation request with dozens of required fields.

![L1 escalates phishing alert to L2, and L2 rotates user's credentials](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1743520297119.svg)

No matter what the agreements are, L2 will eventually receive the ticket from you, read your report, and contact you in case of any questions. Once everything is clear, the L2 analyst will typically research the alert details further, validate if the alert is indeed a True Positive, communicate with other departments if needed, and, for major incidents, start a formal Incident Response process.

### Requesting L2 Support

It is generally fine for L1 to request senior support if something is unclear. Especially in your first months, it's always better to discuss the alert and clarify SOC procedures than to blindly close the alert you don't understand yourself. The procedures for requesting support may differ, but the flow generally looks like this:

![L1 asks L2 to support with the investigation, L2 accepts and provides a knowledge sharing session](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1743520519371.svg)


## Task 5 SOC Communication

### Communication Cases

- **You need to escalate an urgent, critical alert, but L2 is unavailable and does not respond for 30 minutes.**  
    Ensure you know where to find emergency contacts. First, try to call L2, then L3, and finally your manager.
    
- **The alert about Slack/Teams account compromise requires you to validate the login with the affected user.**  
    Do not contact the user through the breached chat - use alternative contact methods like a phone call.
    
- **You receive an overwhelming number of alerts during a short period of time, some of which are critical.**  
    Prioritise the alerts according to the workflow, but inform your L2 on shift about the situation.
    
- **After a few days, you realise that you misclassified the alert and likely missed a malicious action.**  
    Immediately reach out to your L2 explaining your concerns. Threat actors can be silent for weeks before impact.
    
- **You can not complete the alert triage since the SIEM logs are not parsed correctly or are not searchable.**  
    Do not skip the alert - investigate what you can and report the issue to your L2 on shift or SOC engineer.
    

### Communication By L2

![L1 escalates data leak alert to L2, and L2 initiates DFIR and contacts legal and PR departments](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1743610529685.svg)

