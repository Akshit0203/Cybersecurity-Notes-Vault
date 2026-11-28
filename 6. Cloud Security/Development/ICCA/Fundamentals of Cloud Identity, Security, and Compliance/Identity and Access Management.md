- _  
    Users_ - Cloud User, Guest User, External/Hybrid User (_Federated Systems_)
    
    - minimize privileged `admin`/`root` (cloud subscription account) user access
        
    - create groups and use **dynamic management**
        
    - security assessments and **auditing** user configuration
        
    - apply _**least required rights**_ concept ([POLP](https://www.crowdstrike.com/cybersecurity-101/principle-of-least-privilege-polp/))
        
    
- _Resources_
    
    - apply least privileges and **audit** resource access & review
        
    - use dynamic access policies ( # TEMPORARILY ELEVATED PERMISSIONS)
        
    - **separate control plane and data plane access**
        
    

`e.g.` It can be useful to organize user identities into a flow like this:

User identity/credentials (Access management)
⬇️
Group
⬇️
Role
⬇️
Resource

Resource

![](https://blog.syselement.com/ine/~gitbook/image?url=https%3A%2F%2F1996978447-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FlhjuckuLbvBn36EoFL7P%252Fuploads%252Fgit-blob-bcb06facb4f30cb0be257cc2118651719f7729ec%252Fimage-20230530230320832.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=92e764be&sv=2)

Azure AD User

> 📌 CSPs Identity Management
> 
> 🔗 [AWS IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
> 
> - Users, Roles, Policies
>     
> 
> 🔗 [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis)
> 
> - Users, Service Principals, Managed Identities, Roles
>     
> 
> 🔗 [Google Cloud IAM](https://cloud.google.com/iam/docs/overview)
> 
> - Google Account, Service Account, Role, Policy


