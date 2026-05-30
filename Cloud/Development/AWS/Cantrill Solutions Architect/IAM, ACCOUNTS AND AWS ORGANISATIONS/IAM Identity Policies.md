![image1](../../attachments/af1a34c35a544fa8b8db4f571f71b3a2.png)

Identity Policies are attached to AWS identities and either ALLOW or DENY access to AWS resources.

![image2](../../attachments/1ed59657d5c64853892a05ae69b25a4f.png)

There are two effects here

Allow and deny

The deny always wins
It takes more priority

![image3](../../attachments/f63b3c92fab54dfeaafd559ad1187562.png)

![image4](../../attachments/6461339161ff4fff90687d2d77e44dff.png)

If a person is in different groups and those groups also have different policies

Then aws combines them altogether

Deny wins
Then allow

![image5](../../attachments/e1060c4b84ec4cc6bd7103d4e00d851a.png)

Inline policies are given to each individual individually
So we have to edit for everyone

![image6](../../attachments/129c50facf5944758481051d11cc4cd9.png)

We use managed policies when we want to assign policies to a large group

Inline policies are used only in special circumstances
When we want to give an individual more rights or deny some rights

