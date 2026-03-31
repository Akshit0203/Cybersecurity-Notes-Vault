![image1](../../attachments/81dbb5ecba6540cc8e5bf6b627089868.png)

The management account cannot be restricted

Service control policy
Are not permission givers
They just define the limit to which a service can be used
For ex. Size of an ec2 instance

![image2](../../attachments/aab11d9b7e0c4766a650aa7402a6acfa.png)

![image3](../../attachments/7712aed6b6db4f679d2ed4c8967375ef.png)

In this lesson I introduce service control policies - a feature of AWS Organizations which allow restrictions to be placed on MEMBER accounts in the form of boundaries.

SCPs can be applied to the organization, to OU's or to individual accounts.

Member accounts can be effected, the MANAGEMENT account cannot.

SCPs DON'T GIVE permission - they just control what an account CAN and CANNOT grant via identity policies.

