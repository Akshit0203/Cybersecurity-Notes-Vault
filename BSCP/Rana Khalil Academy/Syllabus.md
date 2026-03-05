**The course covers the following server-side vulnerabilities:**
1. SQL Injection
2. Authentication Vulnerabilities
3. Directory Traversal
4. Command Injection
5. Business Logic Vulnerabilities
6. Information Disclosure
7. Access Control Vulnerabilities
8. File Upload Vulnerabilities
9. Server-Side Request Forgery (SSRF)
10. XXE Injection

**The course covers the following client-side vulnerabilities:**
1. Cross-Site Scripting (XSS)
2. Cross-site request forgery (CSRF)
3. Cross-origin resource sharing (CORS)
4. Clickjacking
5. DOM-based Vulnerabilities
6. WebSocket Vulnerabilities

**The course covers the following advanced vulnerabilities:**
1. JWT Attacks
2. HTTP Host Header Attacks
3. OAuth 2.0 Vulnerabilities

---

Introduction
- [Introduction to the Web Security Academy Series(11:52)Preview](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34258700)
- [Course Slides and ScriptsStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47992126)

Getting Help
- [Answering Your Questions(3:11)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47993220)
- [Join the Discord ServerStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34396145)

Lab Environment Setup
- [Lab Environment Setup(7:21)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47992124)
- [Step-by-Step GuideStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47993743)

SQL Injection
- [SQL Injection | Complete Guide(65:41)Preview](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34252111)
- [Lab #1 SQL injection vulnerability in WHERE clause allowing retrieval of hidden data(29:06)Preview](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259687)
- [Lab #2 SQL injection vulnerability allowing login bypass(33:17)Preview](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259735)
- [Lab #3 SQLi UNION attack determining the number of columns returned by the query(33:59)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259773)
- [Lab #4 SQL injection UNION attack, finding a column containing text(29:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259780)
- [Lab #5 SQL injection UNION attack, retrieving data from other tables(24:45)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259807)
- [Lab #6 SQL injection UNION attack, retrieving multiple values in a single column(29:24)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259833)
- [Lab #7 SQL injection attack, querying the database type and version on Oracle(26:50)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259848)
- [Lab #8 SQLi attack, querying the database type and version on MySQL & Microsoft(22:16)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259867)
- [Lab #9 SQL injection attack, listing the database contents on non Oracle databases(45:18)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259872)
- [Lab #10 SQL injection attack, listing the database contents on Oracle(40:24)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259889)
- [Lab #11 Blind SQL injection with conditional responses(48:38)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259903)
- [Lab #12 Blind SQL injection with conditional errors(44:58)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259911)
- [Lab #13 Blind SQL injection with time delays(19:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259929)
- [Lab #14 Blind SQL injection with time delays and information retrieval(35:37)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34259989)
- [Note - Changes to Burp CollaboratorStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47993978)
- [Lab #15 Blind SQL injection with out-of-band interaction(10:19)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34260015)
- [Lab #16 Blind SQL injection with out of band data exfiltration(8:17)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34260041)
- [Lab #17 SQL injection with filter bypass via XML encoding(7:14)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45725351)
- [Lab #18 Visible error-based SQL injection(14:46)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/47861142)

Authentication Vulnerabilities
- [Authentication Vulnerabilities | Complete Guide(29:35)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273752)
- [Lab #1 Username enumeration via different responses(6:02)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273754)
- [Lab #2 2FA simple bypass(11:46)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273758)
- [Lab #3 Password reset broken logic(13:10)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273759)
- [Lab #4 Username enumeration via subtly different responses(9:23)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273762)
- [Lab #5 Username enumeration via response timing(13:58)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273764)
- [Lab #6 Broken brute-force protection, IP block(14:20)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273767)
- [Lab #7 Username enumeration via account lock(9:41)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273770)
- [Lab #8 2FA broken logic(9:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273810)
- [Lab #9 Brute-forcing a stay-logged-in cookie(17:13)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273814)
- [Lab #10 Offline password cracking(11:59)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273815)
- [Lab #11 Password reset poisoning via middleware(8:28)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273818)
- [Lab #12 Password brute-force via password change(25:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273819)
- [Lab #13 Broken brute-force protection, multiple credentials per request(16:46)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273821)
- [Lab #14 2FA bypass using a brute-force attack(9:54)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45273825)

Directory Traversal
- [Directory Traversal | Complete Guide(21:05)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691833)
- [Lab #1 File path traversal, simple case(13:58)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691834)
- [Lab #2 File path traversal, traversal sequences blocked with absolute path bypass(10:55)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691836)
- [Lab #3 File path traversal, traversal sequences stripped non-recursively(14:26)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691839)
- [Lab #4 File path traversal, traversal sequences stripped with superfluous URL-decode(12:19)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691842)
- [Lab #5 File path traversal, validation of start of path(10:28)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691844)
- [Lab #6 File path traversal, validation of file extension with null byte bypass(9:54)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44691846)

OS Command Injection
- [Command Injection | Complete Guide(29:58)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308201)
- [Lab #1 OS command injection, simple case(18:03)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308204)
- [Lab #2 Blind OS command injection with time delays(19:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308241)
- [Lab #3 Blind OS command injection with output redirection(25:51)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308244)
- [Note - Changes to Burp CollaboratorStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/48160736)
- [Lab #4 Blind OS command injection with out-of-band interaction(6:35)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308246)
- [Lab #5 Blind OS command injection with out-of-band data exfiltration(7:33)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/38308248)

Business Logic Vulnerabilities
- [Business Logic Vulnerabilities | Complete Guide(17:30)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961554)
- [Lab #1 Excessive trust in client-side controls(24:40)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961556)
- [Lab #2 High-level logic vulnerability(25:55)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961563)
- [Lab #3 Inconsistent security controls(6:34)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961564)
- [Lab #4 Flawed enforcement of business rules(29:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961565)
- [Lab #5 Low-level logic flaw(14:10)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961567)
- [Lab #6 Inconsistent handling of exceptional input(15:20)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961569)
- [Lab #7 Weak isolation on dual-use endpoint(22:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961575)
- [Lab #8 Insufficient workflow validation(20:04)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961578)
- [Lab #9 Authentication bypass via flawed state machine(17:59)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961581)
- [Lab #10 Infinite money logic flaw(41:17)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961584)
- [Lab #11 Authentication bypass via encryption oracle(18:47)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/44961596)

Information Disclosure
- [Information Disclosure | Complete Guide(29:12)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248222)
- [Lab #1 Information disclosure in error messages(9:41)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248224)
- [Lab #2 Information disclosure on debug page(11:20)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248258)
- [Lab #3 Source code disclosure via backup files(11:18)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248260)
- [Lab #4 Authentication bypass via information disclosure(10:56)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248263)
- [Lab #5 Information disclosure in version control history(4:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45248266)

Access Control Vulnerabilities
- [Broken Access Control | Complete Guide(38:05)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215086)
- [Lab #1 Unprotected admin functionality(15:06)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215088)
- [Lab #2 Unprotected admin functionality with unpredictable URL(22:56)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215090)
- [Lab #3 User role controlled by request parameter(23:42)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215091)
- [Lab #4 User role can be modified in user profile(21:39)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215092)
- [Lab #5 URL-based access control can be circumvented(15:23)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215105)
- [Lab #6 Method-based access control can be circumvented(17:23)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215107)
- [Lab #7 User ID controlled by request parameter(21:24)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215094)
- [Lab #8 User ID controlled by request parameter, with unpredictable user IDs(29:18)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215095)
- [Lab #9 User ID controlled by request parameter with data leakage in redirect(21:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215097)
- [Lab #10 User ID controlled by request parameter with password disclosure(27:13)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215099)
- [Lab #11 Insecure direct object references(22:44)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215102)
- [Lab #12 Multi-step process with no access control on one step(16:25)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215108)
- [Lab #13 Referer-based access control(14:15)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/42215111)

File Upload Vulnerabilities
- [File Upload Vulnerabilities | Complete Guide(26:12)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478922)
- [Lab #1 Remote code execution via web shell upload(27:53)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478926)
- [Lab #2 Web shell upload via Content-Type restriction bypass(23:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478929)
- [Lab #3 Web shell upload via path traversal(26:54)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478933)
- [Lab #4 Web shell upload via extension blacklist bypass(30:11)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478934)
- [Lab #5 Web shell upload via obfuscated file extension(23:42)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478935)
- [Lab #6 Remote code execution via polyglot web shell upload(7:29)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478936)
- [Lab #7 Web shell upload via race condition(13:15)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45478938)

Server-Side Request Forgery (SSRF)
- [Server-Side Request Forgery (SSRF) | Complete Guide(45:31)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225426)
- [Lab #1 Basic SSRF against the local server(21:31)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225429)
- [Lab #2 Basic SSRF against another back-end system(26:53)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225563)
- [Lab #3 SSRF with blacklist-based input filter(20:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225571)
- [Lab #4 SSRF with whitelist-based input filter(21:04)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225594)
- [Lab #5 SSRF with filter bypass via open redirection vulnerability(18:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225610)
- [Note - Changes to Burp CollaboratorStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/48160847)
- [Lab #6 Blind SSRF with out-of-band detection(6:01)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225616)
- [Lab #7 Blind SSRF with Shellshock exploitation(12:41)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/35225627)

XXE Injection
- [XXE Injection | Complete Guide(48:12)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336689)
- [Lab #1 Exploiting XXE using external entities to retrieve files(10:28)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336691)
- [Lab #2 Exploiting XXE to perform SSRF attacks(11:33)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336769)
- [Note - Changes to Burp CollaboratorStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/48160950)
- [Lab #3 Blind XXE with out-of-band interaction(5:53)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336770)
- [Lab #4 Blind XXE with out-of-band interaction via XML parameter entities(6:35)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336771)
- [Lab #5 Exploiting blind XXE to exfiltrate data using a malicious external DTD(16:54)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336774)
- [Lab #6 Exploiting blind XXE to retrieve data via error messages(12:14)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336775)
- [Lab #7 Exploiting XInclude to retrieve files(12:41)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336776)
- [Lab #8 Exploiting XXE via image file upload(23:48)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336777)
- [Lab #9 Exploiting XXE to retrieve data by repurposing a local DTD(23:51)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/45336785)

Cross-Site Scripting (XSS)
- [Cross-Site Scripting (XSS) | Complete Guide(40:03)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/48182636)
- [Lab #1 Reflected XSS into HTML context with nothing encoded(3:47)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178909)
- [Lab #2 Stored XSS into HTML context with nothing encoded(5:06)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178915)
- [Lab #3 DOM XSS in document.write sink using source location.search(7:46)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179356)
- [Lab #4 DOM XSS in innerHTML sink using source location.search(6:03)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179358)
- [Lab #5 DOM XSS in jQuery anchor href attribute sink using location.search source(7:09)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179361)
- [Lab #6 DOM XSS in jQuery selector sink using a hashchange event(10:14)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179366)
- [Lab #7 Reflected XSS into attribute with angle brackets HTML-encoded(5:05)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179369)
- [Lab #8 Stored XSS into anchor href attribute with double quotes HTML-encoded(5:50)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179370)
- [Lab #9 Reflected XSS into a JavaScript string with angle brackets HTML encoded(5:54)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179374)
- [Lab #10 DOM XSS in document.write sink using source location.search inside a select element(8:18)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179376)
- [Lab #11 DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded(4:30)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179379)
- [Lab #12 Reflected DOM XSS(7:46)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179380)
- [Lab #13 Stored DOM XSS(8:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179381)
- [Lab #14 Exploiting cross-site scripting to steal cookies(9:21)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179382)
- [Lab #15 Exploiting cross-site scripting to capture passwords(10:01)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179383)
- [Lab #16 Exploiting XSS to perform CSRF(12:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179384)
- [Lab #17 Reflected XSS into HTML context with most tags and attributes blocked(10:57)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179386)
- [Lab #18 Reflected XSS into HTML context with all tags blocked except custom ones(10:23)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179387)
- [Lab #19 Reflected XSS with some SVG markup allowed(6:34)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179388)
- [Lab #20 Reflected XSS in canonical link tag(7:26)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179389)
- [Lab #21 Reflected XSS into a JavaScript string with single quote and backslash escaped(4:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179391)
- [Lab #22 Reflected XSS into a JavaScript string with angle brackets and double quotes HTML-encoded and single quotes escaped(5:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179392)
- [Lab #23 Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped(7:40)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179394)
- [Lab #24 Reflected XSS into a template literal with angle brackets, single, double quotes, backslash and backticks Unicode-escaped(3:19)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46179397)

Cross-Site Request Forgery (CSRF)
- [Cross-Site Request Forgery (CSRF) | Complete Guide(47:02)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34179716)
- [Note - Changes to Python Simple ServerStart](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/48192434)
- [Lab #1 CSRF vulnerability with no defenses(22:22)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251197)
- [Lab #2 CSRF where token validation depends on request method(20:33)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251251)
- [Lab #3 CSRF where token validation depends on token being present(14:29)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251255)
- [Lab #4 CSRF where token is not tied to user session(18:01)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251259)
- [Lab #5 CSRF where token is tied to non-session cookie(27:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251268)
- [Lab #6 CSRF where token is duplicated in cookie(21:05)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251273)
- [Lab #7 CSRF where Referer validation depends on header being present(19:53)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251274)
- [Lab #8 CSRF with broken Referer validation(18:14)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34251278)
- [Lab #9 SameSite Lax bypass via method override(7:51)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46326651)
- [Lab #10 SameSite Strict bypass via client-side redirect(12:45)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46326670)
- [Lab #11 SameSite Strict bypass via sibling domain(24:10)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46326671)
- [Lab #12 SameSite Lax bypass via cookie refresh(18:29)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46326673)

Cross-origin Resource Sharing (CORS)
- [Cross-Origin Resource Sharing (CORS) | Complete Guide(50:49)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/37578579)
- [Lab #1 CORS vulnerability with basic origin reflection(15:13)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/37578582)
- [Lab #2 CORS vulnerability with trusted null origin(19:08)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/37578586)
- [Lab #3 CORS vulnerability with trusted insecure protocols(23:32)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/37578592)
- [Lab #4 CORS vulnerability with internal network pivot attack(35:21)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/37578594)

Clickjacking
- [Clickjacking | Complete Guide(33:15)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178907)
- [Lab #1 Basic clickjacking with CSRF token protection(9:42)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178894)
- [Lab #2 Clickjacking with form input data prefilled from a URL parameter(10:04)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178900)
- [Lab #3 Clickjacking with a frame buster script(8:38)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178902)
- [Lab #4 Exploiting clickjacking vulnerability to trigger DOM-based XSS(11:27)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178905)
- [Lab #5 Multistep clickjacking(10:27)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46178906)

DOM-based Vulnerabilities
- [DOM-Based Vulnerabilities | Complete Guide(39:09)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503659)
- [Lab #1 DOM XSS using web messages(6:09)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503660)
- [Lab #2 DOM XSS using web messages and a JavaScript URL(5:59)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503661)
- [Lab #3 DOM XSS using web messages and JSON.parse(6:42)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503662)
- [Lab #4 DOM-based open redirection(7:56)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503671)
- [Lab #5 DOM-based cookie manipulation(9:14)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503672)
- [Lab #6 Exploiting DOM clobbering to enable XSS(31:53)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503674)
- [Lab #7 Clobbering DOM attributes to bypass HTML filters(16:34)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46503675)

WebSockets Vulnerabilities
- [WebSockets Vulnerabilities | Complete Guide(45:39)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46337417)
- [Lab #1 Manipulating WebSocket messages to exploit vulnerabilities(5:49)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46337420)
- [Lab #2 Manipulating the WebSocket handshake to exploit vulnerabilities(8:31)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46337422)
- [Lab #3 Cross-site WebSocket hijacking(16:03)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/46337426)

JWT Attacks
- [JWT Attacks | Complete Guide(57:24)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769756)
- [Lab #1 JWT authentication bypass via unverified signature(35:55)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769758)
- [Lab #2 JWT authentication bypass via flawed signature verification(38:05)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769766)
- [Lab #3 JWT authentication bypass via weak signing key(14:10)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769770)
- [Lab #4 JWT authentication bypass via jwk header injection(9:38)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769773)
- [Lab #5 JWT authentication bypass via jku header injection(10:20)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769774)
- [Lab #6 JWT authentication bypass via kid header path traversal(10:41)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769776)
- [Lab #7 JWT authentication bypass via algorithm confusion(13:28)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769777)
- [Lab #8 JWT authentication bypass via algorithm confusion with no exposed key(22:11)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/55769780)

HTTP Host Header Attacks
- [HTTP Host Header Attacks | Complete Guide(19:35)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022085)
- [Lab #1 Basic password reset poisoning(9:18)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022086)
- [Lab #2 Host header authentication bypass(6:48)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022087)
- [Lab #3 Web cache poisoning via ambiguous requests(19:34)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022088)
- [Lab #4 Routing-based SSRF(12:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022089)
- [Lab #5 SSRF via flawed request parsing(15:16)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022090)
- [Lab #6 Host validation bypass via connection state attack(8:48)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022091)
- [Lab #7 Password reset poisoning via dangling markup(17:23)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/60022092)

OAuth 2.0 Vulnerabilities
- [OAuth 2.0 Vulnerabilities | Complete Guide(47:09)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517970)
- [Lab #1 Authentication bypass via OAuth implicit flow(14:36)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517971)
- [Lab #2 SSRF via OpenID dynamic client registration(18:13)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517972)
- [Lab #3 Forced OAuth profile linking(13:04)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517973)
- [Lab #4 OAuth account hijacking via redirect_uri(13:25)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517974)
- [Lab #5 Stealing OAuth access tokens via an open redirect(24:42)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517975)
- [Lab #6 Stealing OAuth access tokens via a proxy page(21:26)Start](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/62517976)

What's Next?
- [Upcoming VideosPreview](https://academy.ranakhalil.com/courses/web-security-academy-video-series/lectures/34417771)