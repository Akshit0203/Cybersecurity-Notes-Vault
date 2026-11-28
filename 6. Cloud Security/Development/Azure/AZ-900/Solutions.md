
# Multiple Choice Questions

## Question 1

### What can you use to automatically send an alert if an administrator stops an Azure virtual machine?

✅ **Answer: B. Azure Monitor**

### Explanation

Azure Monitor collects metrics and logs from Azure resources and can trigger alerts when specific events occur.

Example:

- VM stopped
- CPU > 90%
- Disk space low

Why others are wrong:

- Network Watcher → network troubleshooting
- Service Health → Azure service outages
- Advisor → recommendations

---

## Question 3

### Restrict administrators to creating resources only in specific regions.

✅ **Answer: A. Azure Policy**

### Explanation

Azure Policy can enforce rules such as:

- Allowed regions
- Allowed VM sizes
- Required tags

Example:  
Only allow:

- Central India
- South India

Any deployment outside those regions is denied.

---

## Question 5

### Track Azure resource costs.

✅ **Answer: D. Budgets**

### Explanation

Budgets allow:

- Cost tracking
- Spending thresholds
- Alerts

Example:  
Monthly budget = ₹50,000

Alert at:

- 80%
- 90%
- 100%

---

## Question 6

### Where does Azure Monitor store event data?

✅ **Answer: C. A Log Analytics workspace**

### Explanation

Azure Monitor sends logs and metrics to a Log Analytics Workspace for querying and analysis.

---

## Web App Management

### Manage Azure App Service from an iPhone.

✅ **Answers: C and D**

- C. Azure Portal
- D. Azure Cloud Shell

### Explanation

Azure Portal:

- Accessible via mobile browser.

Azure Cloud Shell:

- Browser-based Bash/PowerShell environment.

Why not:

- Storage Explorer → desktop application
- Windows PowerShell → not available natively on iPhone

---

## Resource Utilization Reports

### Generate utilization reports for each office.

✅ **Answer: B. Tags**

### Explanation

Apply tags such as:

```
Office = DelhiOffice = MumbaiOffice = Bangalore
```

Then filter reports by tag.

---

## Question 16

### Feature of Azure Virtual Network?

✅ **Answer: D. Isolation and Segmentation**

### Explanation

Azure Virtual Network (VNet):

- Private networking
- Network isolation
- Subnet segmentation

---

## Departmental Segmentation

### Segment Azure for departments.

✅ **Answers: B and D**

- Multiple subscriptions
- Multiple resource groups

### Explanation

Resource Groups:

- Logical grouping

Subscriptions:

- Separate billing and administration

---

## Operating System Installation

### Which cloud service allows OS installation?

✅ **Answer: A. Infrastructure as a Service (IaaS) only**

### Explanation

IaaS:

- Customer manages OS.

Examples:

- Azure VM
- AWS EC2

PaaS:

- OS managed by provider.

SaaS:

- No OS access.

---

## Question 26

### Only PaaS solutions allowed.

✅ **Answer: C. Azure App Service and Azure SQL Databases**

### Explanation

Both are PaaS services.

Why not others?

- Virtual Machines = IaaS

---

## Cloud Adaptation

### What allows cloud services to adapt quickly?

✅ **Answer: A. Agility**

### Explanation

Agility means rapid deployment and quick adaptation to changing business requirements.

---

## Public Cloud Characteristics

### Two characteristics

✅ **Answers: C and E**

- Metered pricing
- Self-service management

### Explanation

Public cloud:

- Pay-as-you-go
- Users provision resources themselves

---

## Question 33

### Cloud model with least customer management

✅ **Answer: C. SaaS**

### Explanation

Responsibility comparison:

|Model|Customer Responsibility|
|---|---|
|IaaS|Highest|
|PaaS|Medium|
|SaaS|Lowest|

Example SaaS:

- Microsoft 365
- Gmail

---

# Yes / No Questions

## Azure Policy

|Statement|Answer|
|---|---|
|Assign policy to VM|✅ Yes|
|Noncompliant resources removed|❌ No|
|Only compliant resources can be deployed|✅ Yes|

### Explanation

Policy enforces compliance but doesn't automatically delete resources.

---

## Azure Advisor

|Statement|Answer|
|---|---|
|Can list VMs protected by Backup|❌ No|
|Security recommendations decrease secure score|❌ No|
|Must implement within 30 days|❌ No|

### Explanation

Implementing recommendations increases Secure Score.

---

## Azure Arc

|Statement|Answer|
|---|---|
|Manage physical Linux servers|✅ Yes|
|Manage AKS clusters at scale|✅ Yes|
|Manage third-party databases outside Azure|✅ Yes|

### Explanation

Azure Arc extends Azure management to:

- On-premises
- Multi-cloud
- Edge environments

---

## Tags

|Statement|Answer|
|---|---|
|Policy can apply tags|✅ Yes|
|Multiple tags per resource|✅ Yes|
|Resource inherits tags automatically|❌ No|

### Explanation

Tag inheritance isn't automatic.

---

## ExpressRoute

|Statement|Answer|
|---|---|
|Uses BGP|✅ Yes|
|Uses Internet|❌ No|
|Multiple circuits supported|✅ Yes|

### Explanation

ExpressRoute uses private dedicated connectivity.

---

## Resource Groups

|Statement|Answer|
|---|---|
|Resource group inside another resource group|❌ No|
|VM in multiple resource groups|❌ No|
|Resource group contains resources from multiple regions|✅ Yes|

---

## Storage

|Statement|Answer|
|---|---|
|Premium file shares|✅ Yes|
|Premium block blob storage|✅ Yes|
|Premium StorageV2|❌ No|

---

## Identity

|Statement|Answer|
|---|---|
|AD identities synchronized to Entra ID|✅ Yes|
|Third-party identities can access Azure|✅ Yes|
|Azure provides authentication and authorization|✅ Yes|

---

## Cloud Service Responsibility

|Statement|Answer|
|---|---|
|Customer updates OS in PaaS|❌ No|
|Network control in IaaS is Microsoft's responsibility|❌ No|
|Identity management in SaaS is shared|✅ Yes|

---

## Cloud Models

|Statement|Answer|
|---|---|
|Private cloud gives complete control|✅ Yes|
|Hybrid cloud allows choosing location|✅ Yes|
|Public cloud scaling requires CapEx|❌ No|

### Explanation

Public cloud uses OpEx.

---

## Question 34 (Expenditure)

|Statement|Answer|
|---|---|
|Building data center = OpEx|❌ No|
|Salaries = OpEx|✅ Yes|
|Leasing software = OpEx|✅ Yes|

### Explanation

Building a data center = Capital Expenditure (CapEx).

---

# Selection / Drop-down Questions

## Accidental Deletion

✅ **Answer: Locks**

### Explanation

Use:

```
Delete Lock
```

Prevents accidental deletion.

---

## Cloud Deployment Solutions

|Service|Model|
|---|---|
|Azure Virtual Machines|✅ IaaS|
|Azure SQL Database|✅ PaaS|

---

## Question 13

### Azure Region

✅ **Answer: Contains one or more data centers connected by a low-latency network.**

### Explanation

Official Azure definition.

---

## Azure File Sync

✅ **Answer: File Share**

### Explanation

Azure File Sync synchronizes on-premises file servers with Azure Files.

---

## Domains

### Update Domain / Fault Domain

✅ **Answer: Availability Sets**

### Explanation

Availability Sets organize VMs into:

- Fault Domains
- Update Domains

---

## User Verification

✅ **Answer: Authentication**

### Explanation

Authentication = Verify identity.

Authorization = Determine permissions.

---

## Reader Role

✅ **Answer: Access Control (IAM)**

### Explanation

Role assignments are managed through IAM.

---

## Uptime Comparison

✅ **Answer: Availability**

### Explanation

99.999% uptime provides higher availability than 99.9%.

---

## Virtual Machine Recovery

✅ **Answer: Disaster Recovery**

### Explanation

Azure Site Recovery replicates workloads and enables failover during disasters.

---

# Matching Questions

## Cloud Computing Benefits

|Benefit|Description|
|---|---|
|Scalability|Increase compute capacity of apps in the cloud|
|High Availability|Provide continuous user experience with no apparent downtime|
|Geo-distribution|Deploy applications close to users worldwide|
|Disaster Recovery|Recover systems and data after an outage/disaster|

### Final Matching

|Description|Benefit|
|---|---|
|Increase compute capacity of apps in cloud|✅ Scalability|
|Continuous user experience with no downtime|✅ High Availability|
|Deploy apps to regions where users are|✅ Geo-distribution|
|Restore operations after failure/disaster|✅ Disaster Recovery|