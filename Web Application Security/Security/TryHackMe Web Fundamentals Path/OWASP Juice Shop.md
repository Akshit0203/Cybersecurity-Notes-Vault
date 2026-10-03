# OWASP Juice Shop — CTF Writeup

> [!info] Room Overview
> **Platform:** TryHackMe · Web Fundamentals Path
> **Target:** OWASP Juice Shop — an intentionally vulnerable web application
> **Techniques Used:** SQL Injection, Poison Null Byte, Cross-Site Scripting (DOM & Reflected XSS)

> [!abstract] Table of Contents
> 1. [[#Task 1 Inject the Juice — SQL Injection|SQL Injection (Login Bypass)]]
> 2. [[#Task 2 Who Broke My Lock?!|Who Broke My Lock?!]]
> 3. [[#Task 3 AH! Don't Look! — Poison Null Byte|Poison Null Byte (File Access Bypass)]]
> 4. [[#Task 4 Who's Flying This Thing?|Who's Flying This Thing?]]
> 5. [[#Task 5 Where Did That Come From? — XSS|Cross-Site Scripting (XSS)]]

---

# Task 1 Inject the Juice — SQL Injection

## Question 1 — Which User Does the App Pick?

When you inject `' OR 1=1--` into the login form, the app:

1. Executes the query.
2. Calls something like `fetch_one()` or `fetch()` on the result.
3. Uses the **first returned row's** `id` as the authenticated user.

If the first row in the users table is the **administrator** (very common in demos/labs or poorly initialised DBs), the app grabs that admin `id` and puts it in your session. You didn't have to name "admin" — you just made the query return a row and the app blindly used the first row it found.

## Question 2 — Why `bender@juice-sh.op'--` Works

This is a classic SQL injection trick. Here are the exact mechanics:

### Step 1 — The Original SQL the App Runs

A typical vulnerable login query looks like this:

```sql
SELECT id FROM users
WHERE email = '<EMAIL_FROM_FORM>'
  AND password = '<PASSWORD_FROM_FORM>';
```

If the app puts literal form values into that query (no parameterisation), an attacker can break out of the intended string.

---

### Step 2 — What Happens When You Submit `bender@juice-sh.op'--`

Plugging that email into the query gives:

```sql
SELECT id FROM users
WHERE email = 'bender@juice-sh.op'--'
  AND password = 'whatever';
```

Breaking this down:

- The single quote after `juice-sh.op` **closes** the string literal that started before the email.
- Everything after `--` is an SQL **comment**, so `--'` and the rest of the line (including the password check and the trailing quote) are ignored by the database.
- The resulting effective query the DB sees is:

```sql
SELECT id FROM users
WHERE email = 'bender@juice-sh.op' -- AND password = 'whatever';
```

The `AND password = ...` part is **commented out and never evaluated** — login bypassed.

---

# Task 2 Who Broke My Lock?!

*(Brute-force / authentication challenge — no additional notes captured.)*

---

# Task 3 AH! Don't Look! — Poison Null Byte

## What the Poison Null Byte Does

- `%00` is the URL-encoded representation of a **NULL byte** (a zero-valued byte, `\0`).
- Many low-level C-style string APIs treat `\0` as the _end of the string_. Anything after `\0` is ignored by those APIs.
- If the server or one of its libraries hands a filename containing a `\0` to a C-style file API, that API will stop at the `\0`. So a request for:

  ```
  package.json.bak\0.md
  ```

  may be interpreted by the file-open function as just:

  ```
  package.json.bak
  ```

  which lets you fetch the `.bak` file even though the web-layer "saw" a `.md` extension.

> [!tip] Core Idea
> Append a null byte _in the request_ so the part the web app checks (or allows) looks safe (e.g., ends with `.md`) but the underlying file operation actually opens the truncated name (the real `.bak`).

---

## Why `%2500` Instead of `%00`

- `%00` in a URL stands for the null byte.
- Many web servers and frameworks perform URL-decoding early in the request handling. If you send `%00` directly, the server may decode it immediately into a raw null byte (or reject it).
- **Double-encoding** (encode the `%` itself as `%25`) gives `%2500` in the browser/request. When the server decodes once, `%2500` → `%00` (a literal `%00` sequence). If the server (or an underlying layer) decodes again or interprets `%00` as a null byte when passed to a lower-level API, you get the actual `\0`.
- Practically: sending `package.json.bak%2500.md` often survives one round of decoding so that the null byte reaches the part of the stack that triggers the truncation behaviour.

> [!note]
> Implementation details vary by stack — sometimes a single decode is enough, sometimes multiple layers cause the effect. `%2500` is a common technique to ensure the null byte appears where needed.

---

## Attack Flow — Step by Step

**Request:**

```http
GET /ftp/package.json.bak%2500.md HTTP/1.1
```

**Server / framework decoding steps** (one possible scenario):

1. **Initial URL decode:** `%2500` → `%00`
2. **Later interpretation / additional decode** (or when passed to lower-level API): `%00` → `\0`
3. **Low-level file open** sees `package.json.bak\0.md` and treats string as `package.json.bak`.
4. The web-layer check that enforces allowed extensions might have happened earlier (or looked at the raw decoded string that appeared to end with `.md`), so the download is allowed; the low-level open fetches the `.bak` file.

---

## Mitigation Measures

- **Don't rely on filename extensions alone** for access control. Implement authorisation checks based on the resource identity and user permissions.
- **Canonicalise and validate input** early and reject any filenames containing control characters (including `\0`) or percent-encoded `\00`.
- **Use safe APIs** / higher-level languages that properly treat strings and don't expose C `\0` truncation behaviour to user input.
- **Reject double-encoded sequences** or normalise decoding to a single, secure stage.
- **Whitelist allowed file types and handle them server-side** (don't let client-supplied filenames directly map to filesystem paths).
- Run static/hardening checks and WAF rules that detect null-byte encodings.

---

# Task 4 Who's Flying This Thing?

*(Admin panel discovery challenge — no additional notes captured.)*

---

# Task 5 Where Did That Come From? — XSS

## XSS Types — Reference Table

| Type                       | Description                                                                                                                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DOM** (Special)          | DOM XSS _(Document Object Model-based Cross-site Scripting)_ uses the HTML environment to execute malicious JavaScript. This type of attack commonly uses the `<script></script>` HTML tag.            |
| **Persistent** (Server-side) | Persistent XSS is JavaScript that runs when the server loads the page containing it. Occurs when the server does not sanitise user data when it is **uploaded** to a page. Commonly found on blog posts. |
| **Reflected** (Client-side)  | Reflected XSS is JavaScript that runs on the client-side end of the web application. Most commonly found when the server doesn't sanitise **search** data.                                             |

---

## Challenge 1 — DOM XSS via the Search Bar

We use the `iframe` element with a JavaScript alert tag:

```html
<iframe src="javascript:alert(`xss`)">
```

Inputting this into the **search bar** triggers the alert:

![](https://assets.tryhackme.com/additional/imgur/AMz9jps.png)

![](https://assets.tryhackme.com/additional/imgur/rKEx3aR.png)

> [!note]
> We are using `iframe` which is a common HTML element found in many web applications; there are others which also produce the same result.
>
> This type of XSS is also called **XFS (Cross-Frame Scripting)** and is one of the most common forms of detecting XSS within web applications.
>
> Websites that allow the user to modify the iframe or other DOM elements will most likely be vulnerable to XSS.

---

## Challenge 2 — Reflected XSS via Order Tracking

1. Navigate to the order tracking page — you will see a **"Truck" icon**; clicking it brings you to the track result page.
2. You will also see that there is an `id` paired with the order:

![](https://assets.tryhackme.com/additional/imgur/kQdIKyL.png)

3. Use the iframe XSS payload `<iframe src="javascript:alert(`xss`)">` **in place of** the order ID `5267-f73dcd000abcc353`.
4. After submitting the URL, **refresh the page** and you will get an alert saying XSS!

![](https://assets.tryhackme.com/additional/imgur/rKEx3aR.png)

### Why Does This Work?

The server has a lookup table or database for each tracking ID. As the `id` parameter is **not sanitised** before it is sent to the server, we are able to perform an XSS attack.