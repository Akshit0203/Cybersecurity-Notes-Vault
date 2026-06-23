
**General Multiple Choice Questions**

- **Question 1:** What can you use to automatically send an alert if an administrator stops an Azure virtual machine?
    - A. Azure Network Watcher
    - B. Azure Monitor
    - C. Azure Service Health
    - D. Azure Advisor
- **Question 3:** Your company has an Azure subscription that contains resources in several regions. You need to ensure that administrators can only create resources in those regions. What should you use?
    - A. an Azure policy
    - B. a management group
    - C. a read-only lock
    - D. a reservation
- **Question 5:** Which Azure feature should you use to track the costs of Azure resources?
    - A. usage and quotas
    - B. tags
    - C. Azure Quickstart templates
    - D. budgets
- **Question 6:** Where does Azure Monitor store event data?
    - A. Azure Storage Queue
    - B. Azure SQL Database
    - C. a Log Analytics workspace
    - D. an Azure Blob Storage account
- **Web App Management:** You have an Azure App Service web app. You need to manage the settings of the web app from an iPhone. What are two Azure management tools that you can use? (Each correct answer presents a complete solution).
    - A. Azure Storage Explorer
    - B. Windows PowerShell
    - C. the Azure portal
    - D. Azure Cloud Shell
- **Resource Utilization:** Your company has 10 offices. You plan to generate several billing reports from the Azure portal. Each report will contain the Azure resource utilization of each office. Which Azure feature should you use before you generate the reports?
    - A. locks
    - B. tags
    - C. policies
    - D. templates
- **Question 16:** What is a feature of an Azure virtual network?
    - A. resource cost analysis
    - B. geo-redundancy
    - C. packet inspection
    - D. isolation and segmentation
- **Departmental Segmentation:** Your company plans to migrate to Azure. The company has several departments. All the Azure resources used by each department will be managed by a department administrator. What are two possible techniques to segment Azure for the departments? (Each correct answer presents a complete solution).
    - A. multiple regions
    - B. multiple subscriptions
    - C. multiple Microsoft Entra tenants
    - D. multiple resource groups
- **Operating System Installation:** To which type of cloud service can you install an operating system?
    - A. Infrastructure as a Service (IaaS) only
    - B. Platform as a Service (PaaS) only
    - C. Software as a Service (SaaS) only
    - D. Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) only
    - E. Platform as a Service (PaaS) and Software as a Service (SaaS) only
- **Question 26:** Your company plans to migrate all its data and resources to Azure. The company's migration plan states that only Platform as a Service (PaaS) solutions must be used in Azure. You need to deploy an Azure environment that meets the company's migration plan. What should you create?
    - A. Azure virtual machines, Azure SQL databases, and Azure Storage accounts
    - B. an Azure App Service and Azure virtual machines that have Microsoft SQL Server installed
    - C. an Azure App Service and Azure SQL databases
    - D. Azure storage accounts and web server in Azure virtual machines
- **Cloud Adaptation:** What enables a cloud service to adapt quickly to changing requirements?
    - A. agility
    - B. manageability
    - C. high availability
    - D. predictability
- **Public Cloud Characteristics:** What are two characteristics of the public cloud? (Each correct answer presents a complete solution).
    - A. unsecured connections
    - B. limited storage
    - C. metered pricing
    - D. dedicated hardware
    - E. self-service management
- **Question 33:** Which cloud service model minimizes the management responsibility of a customer?
    - A. infrastructure as a service (IaaS)
    - B. platform as a service (PaaS)
    - C. software as a service (SaaS)

**Yes/No Statement Questions**

- **Azure Policy Statements:** Select Yes if the statement is true. Otherwise, select No.
    - You can assign an Azure policy to a virtual machine.
    - If an Azure policy is assigned to a resource group, noncompliant resources are removed from the resource group.
    - If an Azure policy is assigned to a resource group, only compliant resources can be deployed to the resource group.
- **Azure Advisor Statements:** Select Yes if the statement is true. Otherwise, select No.
    - Azure Advisor can generate a list of Azure virtual machines that are protected by Azure Backup.
    - If you implement the security recommendations provided by Azure Advisor, your company's secure score will decrease.
    - To maintain Microsoft support, you must implement the security recommendations provided by Azure Advisor within a period of 30 days.
- **Question 9 (Azure Arc):** Select Yes if the statement is true. Otherwise, select No.
    - Azure Arc can manage physical servers that run Linux.
    - Azure Arc can manage Azure Kubernetes Service (AKS) clusters at scale.
    - Azure Arc can manage a third-party database solution hosted outside of Azure.
- **Question 10 (Tags):** Select Yes if the statement is true. Otherwise, select No.
    - You can use Azure Policy to apply tags to resources.
    - You can add multiple tags to the same Azure resource.
    - An Azure resource inherits tags from the resource group to which the resource is deployed.
- **ExpressRoute Statements:** Select Yes if the statement is true. Otherwise, select No.
    - ExpressRoute uses Border Gateway Protocol (BGP).
    - ExpressRoute uses the internet to connect an on-premises network to Azure.
    - You can configure multiple ExpressRoute circuits to connect an on-premises datacenter to Azure.
- **Question 15 (Resource Groups):** Select Yes if the statement is true. Otherwise, select No.
    - You can create a resource group inside of another resource group.
    - An Azure virtual machine can be in multiple resource groups.
    - A resource group can contain resources from multiple Azure regions.
- **Question 20 (Storage):** Select Yes if the statement is true. Otherwise, select No.
    - Premium storage accounts can be configured as Azure file shares.
    - Premium storage accounts can be configured as block blobs storage.
    - Premium storage accounts can be configured as StorageV2 storage.
- **Question 21 (Identity):** Select Yes if the statement is true. Otherwise, select No.
    - Identities stored in an on-premises Active Directory can be synchronized to a Microsoft Entra tenant.
    - Identities stored in a Microsoft Entra tenant, third-party cloud services, and on-premises Active Directory can be used to access Azure resources.
    - Azure has built-in authentication and authorization services that provide secure access to Azure resources.
- **Cloud Service Responsibility:** Select Yes if the statement is true. Otherwise, select No.
    - For the platform as a service (PaaS) cloud service, updating the operating system is the responsibility of the customer.
    - For the infrastructure as a service (IaaS) cloud service, network control is the responsibility of Microsoft.
    - For the software as a service (SaaS) cloud service, identity management is a shared responsibility between the customer and Microsoft.
- **Cloud Model Statements:** Select Yes if the statement is true. Otherwise, select No.
    - A company has complete control of the resources and security for its private cloud.
    - A hybrid cloud solution enables a company to control whether its applications run on-premises or in the cloud.
    - Companies are responsible for capital expenditure when they scale up a virtual machine hosted in a public cloud.
- **Question 34 (Expenditure):** Select Yes if the statement is true. Otherwise, select No.
    - Building a data center infrastructure is an example of operational expenditure (OpEx) costs.
    - Monthly salaries for technical personnel are an example of operational expenditure (OpEx) costs.
    - Leasing software is an example of operational expenditure (OpEx) costs.

**Selection/Drop-down Questions**

- **Accidental Deletion:** From the Azure portal, you create a resource group named RG1. You need to prevent the accidental deletion of the resources in RG1. Which setting should you use?
    - Options: Quickstart, Resource costs, Deployments, Policies, Properties, **Locks**, Export template.
- **Cloud Deployment Solutions:** Which cloud deployment solution is used for Azure virtual machines and Azure SQL databases?
    - Azure virtual machines: [Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS)]
    - Azure SQL databases: [Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS)]
- **Question 13 (Azure Regions):** Select the answer that correctly completes the sentence: An Azure region...
    - ...contains one or more data centers that are connected by using a low-latency network.
    - ...is found in each country where Microsoft has a subsidiary office.
    - ...can be found in every country in Europe and the Americas only.
    - ...contains one or more data centers that are connected by using a high-latency network.
- **Azure File Sync:** Select the answer that correctly completes the sentence: You can use the Azure File Sync agent to sync on-premises data to an Azure...
    - ...blob container.
    - ...Data Lake Storage container.
    - ...file share.
    - ...queue.
- **Domains:** Select the answer that correctly completes the sentence: When using [availability sets / availability zones / Azure Load Balancer / Azure Virtual Machine Scale Sets] you can group virtual machines into an update domain or a fault domain.
- **User Verification:** Select the answer that correctly completes the sentence: [Authorization / Authentication / Federation / Ticketing] is the process of verifying a user's credentials.
- **Reader Role:** Which node in the Azure portal should you use to assign a user the Reader role for a resource group?
    - Options: Overview, Activity log, **Access control (IAM)**, Tags, Resource visualizer, Events, Settings (Resource costs, Deployments, Security, Policies, Properties, Properties).
- **Uptime Comparison:** Select the answer that correctly completes the sentence: A service that has an uptime of 99.999% has higher [availability / elasticity / manageability / scalability] than a service that has an uptime of 99.9%.
- **Virtual Machine Recovery:** Select the answer that correctly completes the sentence: Azure Site Recovery provides [fault tolerance / disaster recovery / elasticity / high availability] for virtual machines.

**Matching Questions**

- **Cloud Computing Benefits:** Match the benefit to its description:
    - **Benefits:** Disaster recovery, Geo-distribution, High availability, Scalability.
    - **Descriptions:**
        1. Increase the compute capacity of apps in the cloud.
        2. Provide a continuous user experience with no apparent downtime.
        3. Ensure that users always have the best experience by deploying apps to all the regions where there are users.