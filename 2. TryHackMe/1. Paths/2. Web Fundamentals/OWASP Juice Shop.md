## Inject the juice

### Question 1

Which user does the app pick?

The app usually:

1. Executes the query.
    
2. Calls something like `fetch_one()` or `fetch()` on the result.
    
3. Uses the first returned row’s `id` as the authenticated user.
    

If the first row in the users table is the administrator (very common in demos/labs or poorly initialized DBs), the app grabs that admin `id` and puts it in your session. You didn’t have to name “admin” — you just made the query return a row and the app blindly used the first row it found.

### Why Question #2 (`bender@juice-sh.op'--`) works

Nice — this is a classic SQL injection trick. I’ll walk through the exact mechanics so it’s obvious why `bender@juice-sh.op'--` logs you in without needing `1=1`.

### 1) The original SQL the app probably runs

A typical (vulnerable) login query looks like this (simplified):

`SELECT id FROM users WHERE email = '<EMAIL_FROM_FORM>'   AND password = '<PASSWORD_FROM_FORM>';`

If the app puts the literal form values into that query (no parameterization), an attacker can break out of the intended string.

---

### 2) What happens when you submit `bender@juice-sh.op'--` as the email

Plugging that email into the query gives:

`SELECT id FROM users WHERE email = 'bender@juice-sh.op'--'   AND password = 'whatever';`

Now interpret that:

- The single quote after `juice-sh.op` **closes** the string literal that started before the email.
    
- Everything after `--` is an SQL **comment**, so `--'` and the rest of the line (including the password check and the trailing quote) are ignored by the database.
    
- The resulting effective query the DB sees is:
    

`SELECT id FROM users WHERE email = 'bender@juice-sh.op' --  AND password = 'whatever';`

So the `AND password = ...` part is commented out and not evaluated at all.

## Who broke my lock?!

## AH! Don't look!

### What the Poison Null Byte does (plain explanation)

- `%00` is the URL-encoded representation of a **NULL** byte (a zero-valued byte, `\0`).
    
- Many low-level C-style string APIs treat `\0` as the _end of the string_. Anything after `\0` is ignored by those APIs.
    
- If the server or one of its libraries eventually hands a filename containing a `\0` to a C-style file API, that API will stop at the `\0`. So a request for:
    
    `package.json.bak\0.md`
    
    may be interpreted by the file-open function as just:
    
    `package.json.bak`
    
    which lets you fetch the `.bak` file even though the web-layer “saw” a `.md` extension.
    

So the high-level idea: append a null byte _in the request_ so the part the web app checks (or allows) looks safe (e.g., ends with `.md`) but the underlying file operation actually opens the truncated name (the real `.bak`).

---

### Why `%2500` instead of `%00`

- `%00` in a URL stands for the null byte.
    
- Many web servers and frameworks perform URL-decoding early in the request handling. If you send `%00` directly, the server may decode it immediately into a raw null byte (or reject it).
    
- Double-encoding (encode the `%` itself as `%25`) gives `%2500` in the browser/request. When the server decodes once, `%2500` → `%00` (a literal `%00` sequence). If the server (or an underlying layer) decodes again or interprets `%00` as a null byte when passed to a lower-level API, you get the actual `\0`.
    
- Practically: sending `package.json.bak%2500.md` often survives one round of decoding so that the null byte reaches the part of the stack that triggers the truncation behavior.
    

(Implementation details vary by stack — sometimes a single decode is enough, sometimes multiple layers cause the effect. `%2500` is a common technique to ensure the null byte appears where needed.)

---

### Typical flow for your example

Request:

`GET /ftp/package.json.bak%2500.md HTTP/1.1`

Server / framework decoding steps (one possible scenario):

1. Initial URL decode: `%2500` → `%00`
    
2. Later interpretation / additional decode or when passed to lower-level API: `%00` → `\0`
    
3. Low-level file open sees `package.json.bak\0.md` and treats string as `package.json.bak`.
    
4. The web-layer check that enforces allowed extensions might have happened earlier (or looked at the raw decoded string that appeared to end with `.md`), so the download is allowed; the low-level open fetches the `.bak` file.

### How to fix / mitigate (what server developers should do)

- **Don’t rely on filename extensions alone** for access control. Implement authorization checks based on the resource identity and user permissions.
    
- **Canonicalize and validate input** early and reject any filenames containing control characters (including `\0`) or percent-encoded `\00`.
    
- **Use safe APIs** / higher-level languages that properly treat strings and don’t expose C `\0` truncation behavior to user input.
    
- **Reject double-encoded sequences** or normalize decoding to a single, secure stage.
    
- **Whitelist allowed file types and handle them server-side** (don’t let client-supplied filenames directly map to filesystem paths).
    
- Run static/hardening checks and WAF rules that detect null-byte encodings.

## Who's flying this thing?
## Where did that come from?

**There are three major types of XSS attacks:**

| DOM (Special)            | DOM XSS _(Document Object Model-based Cross-site Scripting)_ uses the HTML environment to execute malicious javascript. This type of attack commonly uses the _<script></script>_ HTML tag.                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Persistent (Server-side) | Persistent XSS is javascript that is run when the server loads the page containing it. These can occur when the server does not sanitise the user data when it is **uploaded** to a page. These are commonly found on blog posts. |
| Reflected (Client-side)  | Reflected XSS is javascript that is run on the client-side end of the web application. These are most commonly found when the server doesn't sanitise **search** data.                                                            |

![](https://assets.tryhackme.com/additional/imgur/AMz9jps.png)

We will be using the iframe element with a javascript alert tag: 

_<iframe src="javascript:alert(`xss`)">_ 

Inputting this into the **search bar** will trigger the alert.

![](https://assets.tryhackme.com/additional/imgur/rKEx3aR.png)

Note that we are using **iframe** which is a common HTML element found in many web applications, there are others which also produce the same result. 

This type of XSS is also called XFS (Cross-Frame Scripting), is one of the most common forms of detecting XSS within web applications.

Websites that allow the user to modify the iframe or other DOM elements will most likely be vulnerable to XSS.





From there you will see a "Truck" icon, clicking on that will bring you to the track result page. You will also see that there is an id paired with the order.   ![](https://assets.tryhackme.com/additional/imgur/kQdIKyL.png)

We will use the iframe XSS, _<iframe src="javascript:alert(`xss`)">,_ in the place of the _5267-f73dcd000abcc353_

After submitting the URL, refresh the page and you will then get an alert saying XSS!

![](https://assets.tryhackme.com/additional/imgur/rKEx3aR.png)

**Why does this work?**

The server will have a lookup table or database (depending on the type of server) for each tracking ID. As the 'id' parameter is not sanitised before it is sent to the server, we are able to perform an XSS attack.