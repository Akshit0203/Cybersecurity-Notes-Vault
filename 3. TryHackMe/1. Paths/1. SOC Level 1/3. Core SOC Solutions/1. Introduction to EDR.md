
## Task 2 What is an EDR?

To ensure these endpoint devices are protected even out of the network, we need a security solution that guards all devices in different areas and is capable of fighting advanced threats. Endpoint Detection and Response (EDR) is a security solution that offers deep-level protection for endpoints. No matter where the endpoints are, the EDR will make sure they are monitored constantly and threats are detected.

Below are some of the EDR solutions in the market:

- [**CrowdStrike Falcon**](https://www.crowdstrike.com/wp-content/uploads/2022/03/crowdstrike-falcon-insight-data-sheet.pdf)
- [**SentinelOne ActiveEDR**](https://sentinelone.com/resources/datasheets/assets/usecase/sentinel-one-active-#page=1)
- [**Microsoft Defender for Endpoint**](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-endpoint)
- [**OpenEDR**](https://www.openedr.com/)
- [**Symantec EDR**](https://docs.broadcom.com/doc/endpoint-detection-and-response-atp-endpoint-en)

### Features of EDR

There are three main features of an EDR, which can also be referred to as the three pillars of an EDR solution.  
![Pillars of EDR.|700x377](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1754897179751.png)


### Visibility 

A good analysis often depends on the available level of visibility of the activity. This is one of the features of **EDR** that makes it unique from other endpoint security solutions. The level of visibility EDR provides is impressive. It collects detailed data from the endpoints, which includes process modifications, registry modifications, file and folder modifications, user actions, and much more. It then presents this information in a very structured format to the analyst. The analyst can see the whole process tree with a complete activity timeline of the sequence of actions. The analyst can also access the historical data of any endpoint for threat hunting or any other purpose. Any detections in the EDR land with a whole context.

| Process Modifications | Registry Modifications | File And Folder Modifications | User Actions | And Much More |
| --------------------- | ---------------------- | ----------------------------- | ------------ | ------------- |

The following screenshot shows graphical representation of a process tree. We can see which processes were spawned on the endpoint. Each node represents a process. The lines connecting them represents their relationship. If we click on the `+` icon given with each process, we will be able to see all the network connections, registry changes, file changes etc. associated with that process. 
 ![CrowdStrike Falcon EDR's Process Tree.|700x219](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1755242793089.png)

Along with the process trees, there are many other features available in the EDRs which maximize the visibility.
### Detection 

The detection feature of EDR wins over traditional detection capabilities. It incorporates signature-based detections as well as behavior-based detections, such as unexpected user activities. With modern machine learning capabilities, it identifies any deviation from the baseline behavior and instantly flags it. It can also detect fileless malware that resides in memory. It also allows us to feed custom IOCs for threat detections.

The following screenshot shows a dashboard of all the detections happening on the different endpoints. Each detection is represented by a row with different fields including the severity of the detection, time, triggering file, hostname, username, and more. The Tactic via Technique field maps the detection with MITRE. Any detection when clicked will show us rich details which helps a SOC analyst during the analysis.

![CrowdStrike Flacon EDR's detections page.](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1755242793208.png)

### Response 

EDR also empowers analysts to take action on detected threats. These actions can be taken at any endpoint within the central EDR console. Imagine getting a detection on the EDR with full-fledged details on when, where, and what happened, and you have to opt for the best possible action for that detection. As an analyst, you may decide to isolate a complete endpoint, terminate a process, or quarantine some files. You can also connect to the host remotely and execute actions independently. You can do this all from within the EDR console.

The following screenshot shows the actions available that can be taken on the host after connecting to it. 

![CrowdStrike Falcon EDR's RTR (Real Time Response) console.](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1755242797142.png)

There are several other actions that the analyst can take during the investigation.


**With advanced visibility, detection, and response, EDR becomes a very powerful tool. However, it's also important to remember that an EDR is a host-only security solution and does not detect network-level threats.**

## Task 3 Beyond the Antivirus

we need an EDR. Unlike antivirus software's basic signature-based detection, it monitors and records the behaviors of the endpoint. An EDR also provides organization-wide visibility of any activity. For example, if a suspicious file is detected on one endpoint, the EDR will also check it across all the other endpoints.

### Scenario Breakdown

- **Step #1:** A user receives a phishing email with a Word document embedded with a malicious macro (VBA script)
- **Step #2:** The user downloads the document and opens it
- **Step #3:** The malicious macro is silently executed, and it spawns PowerShell
- **Step #4:** The malicious macro runs an obfuscated PowerShell command to download a sophisticated second-stage payload
- **Step #5:** The payload is injected into a legitimate svchost.exe
- **Step #6:** The attacker gains remote access to the system

![Antivirus vs EDR Scenario.](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1755532607648.png)

|   |   |   |
|---|---|---|
|**Attack Steps**|**AV's Response**|**EDR's Response**|
|Step #1|Does nothing if the downloaded file has no previous signature in the database|Logs the file download activity and monitors it|
|Step #2|Does nothing upon the opening of the document since winword.exe is a legitimate utility|Records the execution of winword.exe and keeps monitoring|
|Step #3|Does nothing if the executed macro has no previous signature|Detects and flags the macro execution due to the unusual parent-child relationship of winword.exe and PowerShell.exe processes|
|Step #4|Typically, AVs will not detect obfuscated PowerShell scripts|Flags the obfuscated script execution|
|Step #5|Will not flag malicious injection into svchost.exe since it does not monitor the memory injections|Detects Process Injection in svchost.exe|
|Step #6|Lacks Network Level Visibility|Flags the unexpected behaviour of svchost.exe, making an outbound connection|
|Final Action|May be marked as clean|Generates an alert with the full attack chain and enables the analyst to take actions from within the EDR|

**Note:** Some modern AVs may have more enhanced visibility and detection. However, an EDR is ahead as it levels up the detection and response in an endpoint.

## Task 4 How an EDR works?

### EDR Console

All the detailed data sent by the EDR agents is correlated and analyzed through complex logic and machine learning algorithms. The threat intelligence information is matched with the collected data. The EDR is just like the brain connecting all the dots. These dots connect to form a detection, often called an alert. 

The following screenshot shows the dashboard of an EDR console. All the data from the endpoint agents is coming into this console, and the detections are happening here. This dashboard gives a holistic view of the current status of detections in all the endpoints. 

![CrowdStrike Falcon EDR Console.](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1752566212394.png)

### What happens after Detection?

When a detection comes, it's a SOC analyst's responsibility to acknowledge the alert and prioritize it. The prioritization is made easy by the EDR itself. It gives severities to all the alerts (Critical, High, Medium, Low, Informational). The alert with the highest severity is investigated as a priority. For the investigation, once the alert is clicked, the analyst can see all the details of the detection. This includes any files executed, processes executed, network connection attempts, registry modifications, and much more. Based on the available data, the analyst's job is first to use their expertise to determine if the alert is a false positive or a true positive. In case of a true positive, the analyst can take actions from within the EDR console.

### EDR with Other Tools

As a SOC Analyst, it is essential to understand that although a standalone EDR provides enough information to detect and respond to threats in an endpoint, it works alongside other security solutions to form a larger security ecosystem. Within a network, you will see Firewalls, DLPs, Email Security Gateways, IAMs, EDRs, and other security solutions protecting the different components of the network. To minimize the effort and maximize the efficiency, all these security solutions are integrated with a SIEM solution that becomes the central point of investigation for the analysts. 

## Task 5 EDR Telemetry

### What is Telemetry?

In the previous task, we learned about EDR agents, which collect different data from their endpoints and push it to the EDR console. This data is known as Telemetry. Telemetry is the black box of an endpoint with everything necessary for detection and investigation.

### Collected Telemetry

Usually, many activities are going on in the endpoints, most of which are legitimate. It is often difficult to differentiate between regular and malicious activity. The more data is collected, the better judgments can be made. EDR collects detailed telemetry from the endpoints. Let's take a brief look at some of the telemetry that it collects:

- **Process Executions and Terminations**  
    It keeps track of all the running and idle processes, which helps to identify suspicious child-parent process relationships, suspicious executables initiating a process, malware payload, etc.
- **Network Connections**  
    All the endpoints' network connections are monitored, which helps identify any connection to a C2 server, unusual port usage, data exfiltration, or lateral movement within the network.
- **Command Line Activity**  
    It captures all the commands executed on the endpoints in CMD, PowerShell, etc., which helps to identify malicious command execution, obfuscated PowerShell script executions, which are often missed by a traditional antivirus.
- **Files and Folders Modifications**  
    Threat actors modify different files and folders during data staging, ransomware executions, and malicious file dropping. The EDR tracks this.
<span style="color:rgb(255, 0, 0)">- <b>Registry Modifications</b>  <br>    The registry is a goldmine of information about the configurations in a Windows system. There are many registry modifications that occur during a malicious activity, and most of these are monitored by the EDR.</span>

EDR collects much more than this data from an endpoint. It uses complex logic and machine learning algorithms to assess the activities. Advanced threats keep most of their activities stealthy, using legitimate utilities during execution. Individually, their activities may seem harmless, but when observed through detailed telemetry, they tell a different story. This detailed telemetry not only helps the EDR detect advanced threats and make better judgments on the legitimacy of the activities, but it is also very helpful for the analysts during the investigations. The analysts can understand the full chain of events, identify the root cause, and reconstruct the attack timeline.

## Task 6 Detection And Response Capabilities

### Detection

Based on the telemetry received from the endpoints, some advanced detection techniques are applied to this data. Some of these techniques include:

- **Behavioral Detection**  
    Instead of just matching the signatures with known threats, it observes the complete behavior of a file. Advanced threats craft their malware to look clean and use legitimate processes to carry out their attack. EDR catches this behavior.  
    **Example:** A process winword.exe spawning PowerShell.exe will be flagged by the EDR due to the behavior. A Word document spawning a PowerShell is an unusual parent-child relationship.
- **Anomaly Detection**  
    With time, EDR understands the baseline behavior of the endpoints. Any activity that deviates from this behavior will be flagged. During any malicious activity, the endpoint's behavior deviates from normal. EDR picks it up. Sometimes, this can generate false positives as well. However, with the full context it gives, the analyst can identify its legitimacy.  
    **Example:** On one of the endpoints, a process modifies an auto-start registry key, which is not a common behavior on the endpoint.
- **IOC matching**  
    EDRs have some strong threat intelligence field integrations. Except for zero-day attacks, most of the attacks have indicators published in the threat intelligence feeds. EDR flags any activity that matches any known IOC.  **Example:** A user downloads a file that drops an executable. The executable is often used in a specific attack. The hash of this executable will get matched with the threat intelligence feed and instantly flagged by the EDR.
- **MITRE ATT&CK Mapping**  
    Any activity flagged by the EDR is not only marked as malicious or suspicious but also mapped with the MITRE Tactic and Technique (attack stage) that the particular activity was on. This proves to be very helpful for the analysts.  
    **Example:** If the EDR flags the creation of a scheduled task for any reason, it will likely map this activity to the following:
    - Tactic: Persistence
    - Technique: Scheduled Task/Job

- **Machine Learning Algorithms**  
    Advanced threat actors try to evade defenses as much as possible, and their activities may sometimes bypass advanced detection techniques. Modern EDRs have machine learning models trained by a large dataset of normal and malicious behaviors. This can detect complex patterns of an attack.  
    **Example:** Attacks in which the individual actions are not inherently malicious, but the ML algorithm identifies the whole chain of activities as malicious. Fileless attacks and multi-staged intrusions are often detected through this.

### Response

The next step after any detection is the response. EDR offers both automated and manual responses. You can make policies to block known malicious behaviors automatically. However, manual response gives you a wide range of response capabilities. Let's discuss some of them.

- **Isolate Host**  
    During any malicious activity on an endpoint, you can isolate that endpoint from the network through EDR. This is a very effective function for containing malicious activity. Most attacks start from a single endpoint and move laterally to other endpoints to compromise the whole network. Isolating the infected endpoint on time can stop this from happening.
- **Terminate Process**  
    Not every malicious activity requires host isolation. Some hosts run the core business operations, and isolating them can cause more loss than the malicious activity. In such cases, terminating a process is enough to neutralize the malicious activity. The analysts get this option in the EDR. They can terminate any process at any time. This action should be taken consciously since terminating a legitimate process can disrupt the endpoint.
- **Quarantine**  
    If a malicious file comes into the endpoint, it can be quarantined. Quarantine ensures that the file is moved to an isolated location where it can not be executed. The analysts can then review the file to restore or permanently remove it. 
- **Remote Access**  
    Analysts can also remotely access the shell of any endpoint. This is often done when the EDR's built-in response is not enough to take action on a specific activity. Through remote access, analysts can gain deeper visibility into the system or take custom actions within the endpoints. The analysts can also run scripts or collect their desired data from the host through remote access.  
    Below is an example of CrowdStrike Falcon EDR's RTR (Real Time Response) console, which allows analysts to remotely access the shell of any endpoint and run commands and scripts.

![CrowdStrike Falcon EDR's RTR (Real Time Response) console.](https://tryhackme-images.s3.amazonaws.com/user-uploads/6645aa8c024f7893371eb7ac/room-content/6645aa8c024f7893371eb7ac-1755242797142.png)

- **Artefacts Collection**  
    Sometimes, the analysts may need to extract some data from the endpoints for detailed forensic investigation or reporting for legal actions. Analysts can extract important artefacts from the endpoints without physically accessing the device. The most commonly extracted artefacts include:
    - Memory Dump
    - Event Logs
    - Specific Folder Contents
    - Registry Hives

