![Pasted image 20251023195849.png](attachments/Pasted%20image%2020251023195849.png)

![Pasted image 20251023200037.png](attachments/Pasted%20image%2020251023200037.png)

At tenant level, there are some layers to protect and that the customer is responsible for, such as:

- [AWS VPC](https://aws.amazon.com/products/security/network-application-protection/)
    
    - Network ACL - Subnet level
        
    - Security Group - EC2 level
        
    - [PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) - establish private connectivity between Virtual Private Clouds and supported services.
        
    
- [Azure Network Security](https://azure.microsoft.com/en-us/solutions/network-security)
    
    - Network Security Group - Subnet & Instance level
        
    - [Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)
        
    
- [Google Cloud Network Security](https://cloud.google.com/learn/what-is-cloud-network-security)
    
    - Firewall Rule - VPC, Subnet, VM Level
        
    - [VPC Service Controls](https://cloud.google.com/vpc-service-controls)
        
    

Additional network security services:

- _AWS_ - Shield, Web Application Firewall (WAF), GuardDuty
    
- _Azure_ - Firewall, App Gateway, FrontDoor
    
- _Google_ - Cloud Armor
    

📌 Best practices for cloud network protection:

- leverage cloud provider tools and limit **public** attack surface
    
    - check firewall rules and don't open ports globally
        
    
- monitor, setup alerts for abnormal usage and have a playbook for this kind of activity



