## Structure of InfoSec

penetration tester - a professional who finds and fixes security weaknesses in systems

A **risk** in the context of information security refers to the potential for a malicious event to occur, which could cause damage to an organization's assets, such as its data or infrastructure. This potential for damage is typically quantified in terms of its likelihood and the severity of its impact.

A threat, on the other hand, is a potential cause of an incident that could result in harm to a system or organization. It could be a person, like a cybercriminal or hacker, or it could be a natural event, like a fire or flood. Threats exploit vulnerabilities to compromise the security of a system.

A vulnerability is a weakness in a system that could be exploited by a threat. Vulnerabilities can exist in various forms, such as software bugs, misconfigurations, or weak passwords.

a risk represents the potential for damage, a threat is what can cause that damage, and a vulnerability is the weakness that allows the threat to cause damage. All three concepts are interconnected

| **Role**                                      | **Description**                                         | **Relevance to Penetration Testing**                                                                                                              |
| --------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Chief Information Security Officer` (`CISO`) | Oversees the entire information security program        | Sets overall security strategy that pen testers will evaluate                                                                                     |
| `Security Architect`                          | Designs secure systems and networks                     | Creates the systems that pen testers will attempt to breach                                                                                       |
| `Penetration Tester`                          | Identifies vulnerabilities through simulated attacks    | Actively looks for and exploits vulnerabilities within a system, legally and ethically. This is likely your target role.                          |
| `Incident Response Specialist`                | Manages and responds to security incidents              | Often works in tandem with pen testers by responding to their attacks, and sharing/collaborating with them afterwards to discuss lessons learned. |
| `Security Analyst`                            | Monitors systems for threats and analyzes security data | May use pen test results to improve monitoring                                                                                                    |
| `Compliance Specialist`                       | Ensures adherence to security standards and regulations | Pen test reports often support compliance efforts                                                                                                 |

## Principles of Information Security

1. `Non-repudiation`
    - Ensures that a party cannot deny the authenticity of their signature on a document or the sending of a message that they originated
    - Important in e-commerce and legal contexts
    - Implemented through measures like digital signatures and audit logs