**Infrastructure compute protection** involves

- _patch management_
    
    - IaaS - automated OS patching (AWS, Azure) & service
        
    
- _resource protection_
    
- _OS hardening_ (run only required services, with most secure settings)
    
- _monitoring_ (logs)
    
- _attack surface minimization_ (block ports).
    
- _availability_ (multiple instances)
    

**Platform compute protection** involves the cloud provider to secure the services and operating system of the running application

- custom options can also be set up by the customer
    
- PaaS - always patched by the CSP


![Pasted image 20251023220058.png](attachments/Pasted%20image%2020251023220058.png)
![Pasted image 20251023220108.png](attachments/Pasted%20image%2020251023220108.png)
![Pasted image 20251023220122.png](attachments/Pasted%20image%2020251023220122.png)


![Pasted image 20251023220517.png](attachments/Pasted%20image%2020251023220517.png)

**Confidential computing** enables the execution of workloads while _keeping the data and code confidential_, protecting them from the cloud service provider, other tenants and potential attackers, unauthorized data access, inside a trusted isolated execution environment (application **enclave**).

- Confidential compute requires specific compute instance sizes and hardware
    

> 🔗 [Azure Confidential Computing](https://azure.microsoft.com/en-us/solutions/confidential-compute/)
> 
> - `e.g.` [Azure - Confidential computing on a healthcare platform](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/confidential/healthcare-inference#architecture)
>     

**Monitoring** is a built-in feature into the cloud platform.

- 3rd party agent monitoring can also be used
    

> 🔗 [Azure Monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/overview)

![](https://blog.syselement.com/ine/~gitbook/image?url=https%3A%2F%2F1996978447-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FlhjuckuLbvBn36EoFL7P%252Fuploads%252Fgit-blob-96ea11ec04dafa8922660065d239d3ee3147c965%252Fazure-monitor.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=5ce07edc&sv=2)
Azure Monitor