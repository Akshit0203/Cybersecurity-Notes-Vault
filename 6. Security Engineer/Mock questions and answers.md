**Question 1**

**Explain how HTTPS works from the moment a user enters a URL in the browser**

Always explain in this order:

1️⃣ DNS resolution  
2️⃣ TCP connection  
3️⃣ TLS handshake  
4️⃣ Certificate validation  
5️⃣ Key exchange  
6️⃣ Encrypted communication

In interview, never jump randomly. Say:

I’ll explain this step by step starting from DNS to encrypted communication.

# ✅ Ideal Answer (learn this flow)

### 1️⃣ DNS Resolution
- Browser needs IP of the domain
- Checks:
    - browser cache
    - OS cache
    - DNS resolver
- Resolver queries:
    - root → TLD → authoritative DNS
- Gets IP address
### 2️⃣ TCP Connection
- Client establishes TCP connection with server (port 443)
3-way handshake:
Client → SYN    
Server → SYN-ACK    
Client → ACK
### 3️⃣ TLS Handshake Begins

Client sends:
ClientHello

Contains:
- TLS version
- cipher suites
- random number
### 4️⃣ Server Response

Server sends:
ServerHello

Includes:
- selected cipher suite
- server certificate
- server random

Q.1 Can you please Walk me through your C.V ?
Ans: Tell them about your experience in infosec, projects you have worked on, what kind of Applications you have tested. Your methodology or approach of testing those applications, tools you have worked on for both automated and manual testing.

For Freshers:
Tell them about your skills in Application Security, about the vulnerabilities you are aware of and if you have done any freelancing projects or bug bounties tell them your experience of that, your approach for testing applications and finding the Vulnerabilities, trainings and certifications you attended.

Q.2 Owasp 2017 top 10 attacks & Variation Between Owasp 2013 & 2017 ?
Ans: Below is the List of both Owasp 2013 & 2017. and the Variation is that, they added [**XML External Entities (XXE),**](https://www.owasp.org/index.php/Top_10-2017_A4-XML_External_Entities_\(XXE\)) [**Insecure Deserialization,**](https://www.owasp.org/index.php/Top_10-2017_A8-Insecure_Deserialization) [**Insufficient Logging&Monitoring**](https://www.owasp.org/index.php/Top_10-2017_A10-Insufficient_Logging%26Monitoring)**.** and for the rest you can compare below lists
Ans: [https://www.owasp.org/index.php/Top_10_2013-Top_10](https://www.owasp.org/index.php/Top_10_2013-Top_10) ( Owasp 2013)
[https://www.owasp.org/index.php/Top_10-2017_Top_10](https://www.owasp.org/index.php/Top_10-2017_Top_10) (Owasp 2017).

Q.3 What is XXE ?
Ans: An XML External Entity (XXE) attack (sometimes called an XXE injection attack) is based on [Server Side Request Forgery (SSRF)](https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/). This type of attack abuses a widely available but rarely used feature of XML parsers. Using XXE, an attacker is able to cause Denial of Service (DoS) as well as access local and remote content and services. In some cases, XXE may even enable port scanning and lead to remote code execution.
Reference: [https://www.acunetix.com/blog/articles/xml-external-entity-xxe-vulnerabilities/](https://www.acunetix.com/blog/articles/xml-external-entity-xxe-vulnerabilities/)

Q.4 what are the Diffrent types of XXE ? and Recommendations ?
Ans: There are basically two types of XXE attacks
1. In Band XXE: In-band XXE attacks are more common and let the attacker receive an immediate response to the XXE payload.
2. Out Of Band XXE (Blind XXE): in the case of out-of-band XXE attacks (also called blind XXE), there is no immediate response from the web application.
Reference: [https://www.acunetix.com/blog/articles/xml-external-entity-xxe-vulnerabilities/](https://www.acunetix.com/blog/articles/xml-external-entity-xxe-vulnerabilities/)
Recommendations (Reference): [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.md)

Q.5 What is Insecure Deserialization, How to Detect them in Black box & white box Testing and Recommendations ?
Ans: Insecure Deserialization is a vulnerability which occurs when untrusted data is used to abuse the logic of an application, inflict a denial of service (DoS) attack, or even execute arbitrary code upon it being **deserialized.**
www.acunetix.com
(https://www.acunetix.com/blog/articles/what-is-insecure-deserialization/?source=post_page-----ed1f74ce41b8---------------------------------------)

Detection in Black Box & White Box Testing:
(https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Deserialization_Cheat_Sheet.md?source=post_page-----ed1f74ce41b8---------------------------------------)

Recommendations:
(https://resources.infosecinstitute.com/10-steps-avoid-insecure-deserialization/?source=post_page-----ed1f74ce41b8---------------------------------------#gref)
https://www.contrastsecurity.com/security-influencers/java-serialization-vulnerability-threatens-millions-of-applications

Q.6 What is SQL Injection, Types of SQL Injection and Recommendations ? What is stored procedure are they secure against SQL Injection ?

Ans: SQL Injection (SQLi) is a type of an [injection attack](https://www.acunetix.com/blog/articles/injection-attacks/) that makes it possible to execute malicious SQL statements. These statements control a database server behind a web application. Attackers can use SQL Injection vulnerabilities to bypass application security measures. They can go around authentication and authorization of a web page or web application and retrieve the content of the entire SQL database. They can also use SQL Injection to add, modify, and delete records in the database.
References: [https://www.acunetix.com/websitesecurity/sql-injection/](https://www.acunetix.com/websitesecurity/sql-injection/)

Types of SQL Injection:
(https://www.acunetix.com/websitesecurity/sql-injection2/?source=post_page-----ed1f74ce41b8---------------------------------------)

Recommendations:
- Option 1: Use of Prepared Statements (with Parameterized Queries)
- Option 2: Use of Stored Procedures
- Option 3: Whitelist Input Validation
- Option 4: Escaping All User Supplied Input
- Also: Enforcing Least Privilege
- Also: Performing Whitelist Input Validation as a Secondary Defense

References:
(https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.md?source=post_page-----ed1f74ce41b8---------------------------------------)

Stored Procedure (Reference): https://www.paladion.net/blogs/are-stored-procedures-safe-against-sql-injection

Q.7 What is XSS ? Types of XSS ? Difference between DOM Based XSS & Reflected XSS ? What is DOM in DOM Based XSS ? Recommendations for XSS ?
Ans: Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.
Reference: [https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\))

Types of XSS:
1. Reflected XSS
2. Stored XSS
3. DOM Based XSS
Reference: [https://www.owasp.org/index.php/Types_of_Cross-Site_Scripting](https://www.owasp.org/index.php/Types_of_Cross-Site_Scripting)

Difference Between Ordinary XSS and DOM Based XSS:
[Reference: https://security.stackexchange.com/questions/51994/what-is-the-difference-between-ordinary-xss-and-dom-xss-vulnerabilities](https://security.stackexchange.com/questions/51994/what-is-the-difference-between-ordinary-xss-and-dom-xss-vulnerabilities)

DOM In DOM Based XSS:
Reference: [https://www.w3schools.com/js/js_htmldom.asp](https://www.w3schools.com/js/js_htmldom.asp)

Recommendations: There are some libraries which can help to protect against XSS.
Antixss in .NET, ESAP for Java, .NET and php
References: [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md)

Q.8 What is CORS ? How to Exploit Missconfigured CORS? they may ask you about the headers like “Origin”, “Access Control Allow Origin” etc.
Ans: CORS: Cross-Origin Resource Sharing(CORS) is a mechanism that enables web browsers to perform cross-domain requests using the XMLHttpRequest API in a controlled manner. These cross-origin requests have an Origin header, that identifies the domain initiating the request. It defines the protocol to use between a web browser and a server to determine whether a cross-origin request is allowed.
Exploit References: [https://www.we45.com/blog/3-ways-to-exploit-misconfigured-cross-origin-resource-sharing-cors](https://www.we45.com/blog/3-ways-to-exploit-misconfigured-cross-origin-resource-sharing-cors)

Q.9 What is SSRF ? What can be accomplished by exploiting SSRF ? Recommendations ?
Ana : Server Side Request Forgery (SSRF) is a type of attack that can be carried out to compromise a server. The exploitation of a SSRF vulnerability enables attackers to send requests made by the web application, often targeting internal systems behind a firewall.
References: [https://blog.detectify.com/2019/01/10/what-is-server-side-request-forgery-ssrf/](https://blog.detectify.com/2019/01/10/what-is-server-side-request-forgery-ssrf/)
[https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/](https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/)

Q.10 What is CSRF ? Recommendations ? What is Double Submit Cookie in CSRF ? is it possible to exploit CSRF in JSON request if yes then how ?

Ans: CSRF Attack: Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

References: [https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_\(CSRF\))

Recommendations References: [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md)

Double Submit Cookie (Reference): [https://medium.com/@munsifmusthafa03/csrf-protection-episode-2-double-submit-cookie-pattern-195824e53d42](https://medium.com/@munsifmusthafa03/csrf-protection-episode-2-double-submit-cookie-pattern-195824e53d42)

Bypass of Double Submit cookie (Reference) : [https://www.owasp.org/images/3/32/David_Johansson-Double_Defeat_of_Double-Submit_Cookie.pdf](https://www.owasp.org/images/3/32/David_Johansson-Double_Defeat_of_Double-Submit_Cookie.pdf)

CSRF in JSON request: yes it is possible to exploit CSRF in JSON request.

References: [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.md)

Q.11 What is IDOR ? Diffrence between IDOR and Missing Function Level access control ? Recommendations ?

Ans: IDOR: Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability attackers can bypass authorization and access resources in the system directly, for example database records or files.

Insecure Direct Object References allow attackers to bypass authorization and access resources directly by modifying the value of a parameter used to directly point to an object. Such resources can be database entries belonging to other users, files in the system, and more. This is caused by the fact that the application takes user supplied input and uses it to retrieve an object without performing sufficient authorization checks.

References: [https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)](https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_\(OTG-AUTHZ-004\))

Difference Between IDOR and Missing function Level access control:

( This Answer is From a quora user, i am not sure about this)

The IDOR is something in which the objects/ resources on the back-end are directly mapped to their names/identifier on the front-end. This mapping allows an adversary to access the objects/ resources by knowing or guessing the names/ identifier value. Now, being able to access the resource is IDOR but what kind of access is available is omething to do with missing access level control. Say if there would have been a acces control in picture, the access on resources would have been like read, read/write, no access to different set of users present on the system.

On the other hand, missing function level access control is much of an authorization issue (in broad terms) where the application just check for the user being authorized or not. And it does not have a proper authorization mechanism in place i.e. it checks if user A is logged into the application while user A makes a request to access resource C. But it does not checks whether user A is allowed to access resource C or not. _Although, this is just one of the example it may also mean certain APIs which just allows access to all resources to all users and does not have a access control mechanism implemented._ Another example can be authentication & authorization present on the directory structure but no authentication& authorization in the granular resources say folders and files in a cloud storage.

Recommendations (References): [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.md)

Q.12 What is session fixation attack ? Recommendations ?

Ans : Session Fixation Attack (Reference): [https://www.owasp.org/index.php/Session_fixation](https://www.owasp.org/index.php/Session_fixation)

Recommendation (Reference): [https://www.owasp.org/index.php/Session_Fixation_Protection](https://www.owasp.org/index.php/Session_Fixation_Protection)

Q.13 common flags on a cookie ? what is httponly flag ? what is the diffrence between httponly flag and secure httponlyflag

Ans: References: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

Q.12 What is Clickjacking attack ? Recommendations ?

Ans : Clickjacking Attack: Clickjacking, also known as a “UI redress attack”, is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the the top level page. Thus, the attacker is “hijacking” clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

References: [https://www.owasp.org/index.php/Clickjacking](https://www.owasp.org/index.php/Clickjacking)

Recommendations (References): [https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Clickjacking_Defense_Cheat_Sheet.md](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Clickjacking_Defense_Cheat_Sheet.md)

Q.13 What is Content Security Policy (CSP) ? and common use cases of CSP ?

Ans : **Content Security Policy** ([CSP](https://developer.mozilla.org/en-US/docs/Glossary/CSP)) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting ([XSS](https://developer.mozilla.org/en-US/docs/Glossary/XSS)) and data injection attacks. These attacks are used for everything from data theft to site defacement to distribution of malware.

References: [https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

Q.14 What is the difference between SSL and TLS ? Explain the process of SSL/TLS hamdshake ?

Ans: Differences between SSL and TLS.
1. The TLS protocol does not support Fortezza/DMS cipher suites while SSL supports Fortezza. Also, the TLS standardization process makes it much easier to define new cipher suites.
2. In SSL to create a master secret, the message digest of the pre-master secret is used. In contrast, TLS uses a pseudorandom function to generate master secret.
3. The SSL record protocol adds MAC (Message Authentication Code) after compressing each block and encrypts it. As against, TLS record protocol uses HMAC (Hash-based Message Authentication Code).
4. The “No certificate” alert message is included in SSL. On the other hand, TLS removes alert description (No certificate) and adds a dozen other values.
5. SSL message authentication unites key information and application data in an ad-hoc manner, created just for the SSL protocol. Whereas, the TLS protocol just relies on a standard message authentication code known as HMAC.
6. In the TLS certificate verify the message, the MD5 and SHA-1 hashes are computed only over handshake messages. On the contrary, in SSL the hash calculation also include the master secret and pad.
7. As with the finished message in TLS, created by applying the PRF to the master key and handshake messages. Whereas in SSL, it’s constructed by applying message digest to the master key and handshake messages.

SSL/TLS Handshake process (Reference): [https://medium.com/@kasunpdh/ssl-handshake-explained-4dabb87cdce](https://medium.com/@kasunpdh/ssl-handshake-explained-4dabb87cdce)

Q.15 what is the difference between Asymmetric and symmetric encryption ?
Ans: Symmetric encryption uses a single key that needs to be shared among the people who need to receive the message while asymmetrical encryption uses a pair of public key and a private key to encrypt and decrypt messages when communicating.
- Symmetric encryption is an old technique while asymmetric encryption is relatively new.
- Asymmetric encryption was introduced to complement the inherent problem of the need to share the key in symmetrical encryption model, eliminating the need to share the key by using a pair of public-private keys.
- Asymmetric encryption takes relatively more time than the symmetric encryption.

Q.17 What is the difference between encryption,encoding and Hashing ?
Ans: Encryption trades with keys which are using encrypt and decrypt the data. These keys are used to change a simple text into a cypher text and the vice versa.

Encryption is used to Security of data
Encoding:
The message is encoded by using an algorithm in encoding. However, one cipher text is produced for each plain text. The strategy used for change is not kept secret like in the case of encryption.
Encoding is used to Protection of integrity of data
Hashing:  
Data is converted to a message digest or hash, which is a number generated from a string of text. These digests are important as one can effortless match the hash of sent and received messages to ensure that both are the same and no tempering is done with the data.
Hashing is used to Verification of data

Q.18 What is Server SIde template Injection ?
Ans: Reference: [https://portswigger.net/blog/server-side-template-injection](https://portswigger.net/blog/server-side-template-injection)

Q.19 What is Http Parameter Pollution Attack ?
Ans: Supplying multiple HTTP parameters with the same name may cause an application to interpret values in unanticipated ways. By exploiting these effects, an attacker may be able to bypass input validation, trigger application errors or modify internal variables values. As HTTP Parameter Pollution (in short _HPP_) affects a building block of all web technologies, server and client side attacks exist.
Reference: [https://www.owasp.org/index.php/Testing_for_HTTP_Parameter_pollution_(OTG-INPVAL-004)](https://www.owasp.org/index.php/Testing_for_HTTP_Parameter_pollution_\(OTG-INPVAL-004\))

Q.20 What is CRLF Injection ?
Ans: The term CRLF refers to **C**arriage **R**eturn (ASCII 13, \r) **L**ine **F**eed (ASCII 10, \n). They’re used to note the termination of a line, however, dealt with differently in today’s popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. In the HTTP protocol, the CR-LF sequence is always used to terminate a line.

A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.

Reference: [https://www.owasp.org/index.php/CRLF_Injection](https://www.owasp.org/index.php/CRLF_Injection)

Q.21 What is the Difference between OS command Injection and Remote Code execution ?

Ans: In Remote Code Execution You are only limited to execute code on the server, if the application doesn’t control the uses of dangerous functions then it is possible to execute OS command on the system

In OS command Execution you are only limited to run system commands but it depends on the situation, if you are able to execute commands with high privileged user and can write the data into web server’s directory then you can write and run your code on server.

Q.22 How you can bypass restricted file uploads ?
Ans: Content-Type —>Change the parameter in the request header using Burp, ZAP etc.
Put server executable extensions like file.php5, file.shtml, file.asa, file.cert
Changing letters to capital form file.aSp or file.PHp3
Using trailing spaces and/or dots at the end of the filename like file.asp… … . . .. .. , file.asp , file.asp.
Use of semicolon after the forbidden extension and before the permitted extension example: file.asp;.jpg (Only in IIS 6 or prior)
Upload a file with 2 extensions—> file.php.jpg
Use of null character—> file.asp%00.jpg
Create a file with a forbidden extension —> file.asp:.jpg or file.asp::$data

Q.23 What is HSTS Header ?
Ans: If a website accepts a connection through HTTP and redirects to HTTPS, visitors may initially communicate with the non-encrypted version of the site before being redirected, if, for example, the visitor types [http://www.foo.com/](http://www.foo.com/) or even just foo.com. This creates an opportunity for a man-in-the-middle attack. The redirect could be exploited to direct visitors to a malicious site instead of the secure version of the original site.
The HTTP Strict Transport Security header informs the browser that it should never load a site using HTTP and should automatically convert all attempts to access the site using HTTP to HTTPS requests instead.
Reference: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security

Q.24 What you will Look in Manifest.xml file in Security Testing of Android Apps ?
Ans: Reference: [https://pentestlab.blog/2017/01/24/security-guidelines-for-android-manifest-files/](https://pentestlab.blog/2017/01/24/security-guidelines-for-android-manifest-files/)

Q.25 What is SSL Pinning in Android & how it can be bypassed?
Ans: Reference: [https://nileshsapariya.blogspot.com/2017/02/how-to-bypass-ssl-pinning.html](https://nileshsapariya.blogspot.com/2017/02/how-to-bypass-ssl-pinning.html)

Q.26 Tools to Perform Android App Security Testing ?
Ans: You can use below reference to Understand Android Application’s Security Testing
(https://manifestsecurity.com/android-application-security/?source=post_page-----ed1f74ce41b8---------------------------------------)

Q.27 Common Ports and services running on them ?
Ans: Reference: [https://www.utilizewindows.com/list-of-common-network-port-numbers/](https://www.utilizewindows.com/list-of-common-network-port-numbers/)

Q.28 What is DNS Zone Transfer Attack ?

Ans: Reference:[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=21&ved=2ahUKEwiN_NX8w4TiAhWo7HMBHep2CpEQFjAUegQIAhAB&url=http%3A%2F%2Fcolesec.inventedtheinternet.com%2Fhacking-and-information-gathering-with-dns-zone-transfer-attacks%2F&usg=AOvVaw3eJy-aexS2ibmTlsw-ERz-](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&cd=21&ved=2ahUKEwiN_NX8w4TiAhWo7HMBHep2CpEQFjAUegQIAhAB&url=http%3A%2F%2Fcolesec.inventedtheinternet.com%2Fhacking-and-information-gathering-with-dns-zone-transfer-attacks%2F&usg=AOvVaw3eJy-aexS2ibmTlsw-ERz-)

Q.29 What is SMTP Relay attack ?
Ans: Reference: [http://www.anonhack.in/2015/12/smtp-relay-attacks/](http://www.anonhack.in/2015/12/smtp-relay-attacks/)

Q.30 What is SMB Relay ?
Ans: Reference: [https://cqureacademy.com/blog/penetration-testing/smb-relay-attack](https://cqureacademy.com/blog/penetration-testing/smb-relay-attack)

Q.31 What is Pivoting ?
Ans: Pivoting is the unique technique of using an instance (also referred to as a ‘plant’ or ‘foothold’) to be able to move around inside a network. Basically using the first compromise to allow and even aid in the compromise of other otherwise inaccessible systems. In this scenario we will be using it for routing traffic from a normally non-routable network.

References: [https://www.offensive-security.com/metasploit-unleashed/pivoting/](https://www.offensive-security.com/metasploit-unleashed/pivoting/)

Q.32 What is the difference Between Telnet & SSH ?
Ans: Reference: [https://techdifferences.com/difference-between-telnet-and-ssh.html](https://techdifferences.com/difference-between-telnet-and-ssh.html)

Q.33 What is Pass The Hash Attack ?
Ans: Reference: [https://pentestlab.blog/2012/04/08/pass-the-hash-attack/](https://pentestlab.blog/2012/04/08/pass-the-hash-attack/)

Q.34 What is the difference between TCP & UDP ?
Ans: Reference: [https://www.geeksforgeeks.org/differences-between-tcp-and-udp/](https://www.geeksforgeeks.org/differences-between-tcp-and-udp/)

Q.35 What is Attack, Threat & Vulnerability?
Ans: **Threat** — A negative effect or undesired event. A potential occurrence, often best described as an effect that might damage or compromise an asset or objective. It may or may not be malicious in nature.
- **Vulnerability** — A weakness in some aspect or feature of a system that makes an exploit possible. Vulnerabilities can exist at the network, host, or application levels and include operational practices.
- **Attack** (or exploit) — An action taken that uses one or more vulnerabilities to realize a threat. This could be someone following through on a threat or exploiting a vulnerability.

Q.36 What is the Difference between Nmap’s TCP SYN scan & TCP connect Scan ?
Ans: Reference: [https://medium.com/@avirj/nmap-tcp-syn-scan-50106f818bf1](https://medium.com/@avirj/nmap-tcp-syn-scan-50106f818bf1)

Q.37 What is TCP idle scan ?
Ans: Reference: [https://nmap.org/book/idlescan.html](https://nmap.org/book/idlescan.html)

Q.38 What is Decoy in nmap ?
Ans: Reference: [https://www.cyberciti.biz/tips/nmap-hide-ipaddress-with-decoy-ideal-scan.html](https://www.cyberciti.biz/tips/nmap-hide-ipaddress-with-decoy-ideal-scan.html)
**And the last but not least**

Q.39 Do you have any question ?
Ans: _“This part is depend on you”,_ but I always ask a question in my interviews _“_**_Do you have any suggestions for me on the basis of this interview, and what are the things I need to work on for the next interviews”._**

Adding New Refrences: ( 2019 )

Q.1 Are you aware about OWASP top 10 api attacks ?
Ans: Referece: https://www.owasp.org/index.php/OWASP_API_Security_Project

Q.2 what is mass assigntment attack ?
Ans: Reference: https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html

Q.3 what Oauth & how to exploit a misconfigured Oauth ?
Ans: Reference: https://dhavalkapil.com/blogs/Attacking-the-OAuth-Protocol/

Q.4 What is SAML ? attacks & Recommandations ?
Ams: Reference: https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html

https://developer.okta.com/blog/2018/02/27/a-breakdown-of-the-new-saml-authentication-bypass-vulnerability

Q.5 What is Openid & SSO in Web applications ?
Ans: Reference:
https://www.darkreading.com/authentication/oauth-openid-flaw-7-facts/d/d-id/1251127

Q.6 What is HTP Request Smuggling ( HTTP Dsync ) attack ?
Ans: Reference: https://portswigger.net/web-security/request-smuggling

Q.7 What is web cache poisioning attack ?
Ans: Reference: https://portswigger.net/research/practical-web-cache-poisoning

Q.8 What is Web cache deception attack ?
Ans: Reference: http://omergil.blogspot.com/2017/02/web-cache-deception-attack.html?m=1

Q.9 What is HTTP Response splitting attack ?
Ans: Reference: https://www.owasp.org/index.php/HTTP_Response_Splitting

Q.10 What is host header Injection ?
Ans: Reference: https://www.acunetix.com/blog/articles/automated-detection-of-host-header-attacks/








