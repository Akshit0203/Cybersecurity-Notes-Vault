## Task 2 Assets & Identities

Imagine having a night shift and looking into an alert saying that G.Baker logged into the HQ-FINFS-02 server. Then, the user downloaded the "Financial Report US 2024.xlsx" file from there and shared it with R.Lund. To correctly triage the alert and understand if the activity is expected, you will have to find answers to many questions:

- Who is G.Baker? What are their working hours and role in the company?
- What is the purpose and location of HQ-FINFS-02? Who can access it?
- Why could R.Lund need access to the corporate financial records?

### Identity Inventory

Identity inventory is a catalogue of corporate employees (user accounts), services (machine accounts), and their details like privileges, contacts, and roles within the company. For the scenario above, identity inventory would help you get context about G.Baker and R.Lund, and make it simpler to decide if the activity was expected or not.

**Example of Identities**

|Full Name|Username|Email|Role|Location|Access|
|---|---|---|---|---|---|
|Gregory Baker|G.Baker|g.baker@tryhatme.thm|Chief Financial Officer|Europe, UK|VPN, HQ, FINANCE|
|Raymond Lund|R.Lund|r.lund@tryhatme.thm|US Financial Adviser|US, Texas|VPN, FINANCE|
|Kate Danner|K.Danner|k.danner@tryhatme.thm|Chief Technology Officer|Europe, UK|VPN, DA, HQ, AWS|
|svc-veeam-06|svc-veeam-06|N/A|Backup Service Account|N/A|VEEAM, DMZ, HQ|
|svc-nginx-pp|svc-nginx-pp|N/A|Web App Service Account|N/A|DMZ|

**Sources of Identities**

|Solution|Examples|Description|
|---|---|---|
|Active Directory|On-prem AD, Entra ID|AD itself is an identity database, and it is commonly used by SOC|
|SSO Providers|Okta, Google Workspace|Cloud alternative for AD, an easy way to manage and search the users|
|HR Systems|BambooHR, SAP, HiBob|Limited to employees only, but usually provides full employee data|
|Custom Solution|CSV or Excel Sheets|It is common for IT or security teams to maintain their own solutions|

### Asset Inventory

Asset inventory, also called asset lookup, is a list of all computing resources within an organisation's IT environment. Note that while "asset" is a vague term and can also refer to software, hardware, or employees, this room emphasises servers and workstations only. For the scenario above, asset inventory would help you get context about the HQ-FINFS-02 server.

**Example of Assets**

|Hostname|Location|IP Address|OS|Owner|Purpose|
|---|---|---|---|---|---|
|HQ-FINFS-02|UK Datacenter|172.16.15.89|Windows Server 2022|Central IT|File server for financial records|
|HQ-ADDC-01|UK Datacenter|172.16.15.10|Windows Server 2019|Central IT|Primary AD domain controller|
|PC-891D|London Office|192.168.5.13|Windows 11 Pro|Tech Support|Stationary PC for accountants|
|L007694|Remote|N/A|MacOS 13|A.Kelly, DevOps|Corporate laptop|
|L005325|Remote|N/A|MacOS 13|J.Eldridge, HR|Corporate laptop|

**Sources of Assets**

|Solution|Examples|Description|
|---|---|---|
|Active Directory|On-prem AD, Entra ID|AD is not only an identity but also a solid asset inventory database|
|SIEM or EDR|Elastic, CrowdStrike|Some SIEM or EDR agents collect information about the monitored hosts|
|MDM Solution|MS Intune, Jamf MDM|A dedicated class of solutions created to list and manage assets|
|Custom Solution|CSV or Excel Sheets|Same as with the identity inventory, custom solutions are common|

## Task 3 Network Diagrams

1. **08:00**: An IP **103.61.240.174** is repeatedly connecting to a corporate firewall via port **TCP/10443**
2. **08:23**: Firewall logs show that the IP 103.61.240.174 was translated to an internal **10.10.0.53** IP
3. **08:25**: The IP 10.10.0.53 is scanning the **172.16.15.0/24** network range but does not find open ports
4. **08:32**: The same IP is now scanning the **172.16.23.0/24** network range, and the attack seems to be ongoing

### Network Diagrams

To investigate the case above, you will have to find out what service is running at the 10443 port and why anyone would connect there. Then, identify the subnet the 10.10.0.53 IP belongs to and why it would ever try to connect to other subnets. A **network diagram**, a visual schema presenting existing locations, subnets, and their connections, is an answer to your questions:

_![Network diagram for the explained scenario: a firewall exposing VPN on port 10443, and web service on HTTP ports. The firewall protects three corporate subnets: Office (172.16.23.0/24), Database (172.16.15.0/24), and VPN (10.10.0.0/16)](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1742848063212.png)_

1. Threat actor behind the 103.61.240.174 IP performed **VPN brute force**, targeting vpn.tryhatme.thm
2. After a successful brute force and VPN login, the threat actor was assigned an IP from the **VPN Subnet**
3. Then, the adversary tried to scan the **Database Subnet**, but was likely blocked by the firewall rules
4. Seeing no success, the threat actor switches to the **Office Subnet**, looking for their next target

## Task 4 Workbooks Theory

### SOC Workbooks

**SOC workbook**, also called playbook, runbook, or workflow, is a structured document that defines the steps required to investigate and remediate specific threats efficiently and consistently. Since L1 analysts are considered junior specialists and are not expected to triage every possible attack scenario perfectly, senior analysts often prepare workbooks to support their less experienced teammates. L1 analysts are recommended and sometimes even required to triage the alerts precisely according to workbooks to avoid mistakes and streamline the analysis.

### Workbook Example

**Unusual Login Location Workbook**

_![The flowchart showing the process from receiving a login alert through identity enrichment via BambooHR, Threat Intel usage, investigation using Splunk and escalation stages. It includes IP analysis, user behaviour checks, and conditions for escalating to L2 or closing alerts based on actions preceding or following the login](https://tryhackme-images.s3.amazonaws.com/user-uploads/678ecc92c80aa206339f0f23/room-content/678ecc92c80aa206339f0f23-1743455620681.svg)_

1. **Enrichment**: Use Threat Intelligence and identity inventory to get information about the affected user
2. **Investigation**: Using the gathered data and SIEM logs, make your verdict if the login is expected
3. **Escalation**: Escalate the alert to L2 or communicate the login with the user if necessaryTask 6Conclusion

## Task 6 Conclusion

Remember to use the existing lookups like asset inventory or network map to better understand the alerts, and push your team to implement and maintain workbooks to streamline and simplify SOC operations. Hope you enjoyed the room!

