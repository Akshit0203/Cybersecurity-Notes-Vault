![image1](../../attachments/207c6e2f22d84a409780e2848aed143f.png)

DNS Record Types

DNS isn't just for websites though, and multiple types of DNS record exist. We'll go over some of the most common ones that you're likely to come across.

A Record

These records resolve to IPv4 addresses, for example 104.26.10.229

AAAA Record

These records resolve to IPv6 addresses, for example 2606:4700:20::681a:be5

CNAME Record

These records resolve to another domain name, for example, TryHackMe's online shop has the subdomain name store.tryhackme.com which returns a CNAME record shops.shopify.com. Another DNS request would then be made to shops.shopify.com to work out the IP address.

MX Record

These records resolve to the address of the servers that handle the email for the domain you are querying, for example an MX record response for tryhackme.com would look something like alt1.aspmx.l.google.com. These records also come with a priority flag. This tells the client in which order to try the servers, this is perfect for if the main server goes down and email needs to be sent to a backup server.

TXT Record

TXT records are free text fields where any text-based data can be stored. TXT records have multiple uses, but some common ones can be to list servers that have the authority to send an email on behalf of the domain (this can help in the battle against spam and spoofed email). They can also be used to verify ownership of the domain name when signing up for third party services.

GET Request

This is used for getting information from a web server.

POST Request

This is used for submitting data to the web server and potentially creating new records

PUT Request

This is used for submitting data to a web server to update information

DELETE Request

This is used for deleting information/records from a web server.
![image2](../../attachments/4568901182eb46d1a99360083646ec17.png)

![image3](../../attachments/ce93b308cc824f398251fe7e8ca91bd9.png)

![image4](../../attachments/95dc3530ef454b1d91b6d0f48a587961.png)

![image5](../../attachments/01d435cc59c8485da13b792df900da96.png)

![image6](../../attachments/088687e35a8f41f3a18ecf9f4726cb59.png)

![image7](../../attachments/08ca95a0690348a5bb119d4f517aeb3c.png)

![image8](../../attachments/8bdbfd528f8a4d3094ea02b5f14d474d.png)

![image9](../../attachments/7bf585ff623944aa9ba6b7eaf094625c.png)

![image10](../../attachments/7a5982cc72b74600bcb5e744cf5e2ba7.png)

![image11](../../attachments/db46a1cb423b47158b50412c8c6db35f.png)

![image12](../../attachments/a8be43a332d64c6288f5094d2a0871f2.png)

![image13](../../attachments/9d00a4b26fc74c6f870e428beffab017.png)

![image14](../../attachments/283b0ed4b74d4f5ca840533f79e503be.png)

![image15](../../attachments/20553b2a3dac42cf99fc3b85e9851680.png)

![image16](../../attachments/8bc1d187e76a47ca853127776bc9e26b.png)

![image17](../../attachments/f2bd1113736e431da9f11b2bd6356ee6.png)

![image18](../../attachments/eb34cfcad13e4540a1d859fb2e83315d.png)

![image19](../../attachments/8a7beb98ec334a35aaafed4d891f0725.png)

![image20](../../attachments/09a964e1e03341cca660cbd3eef38658.png)

![image21](../../attachments/87af7767e83b47819e58b02de983b196.png)

