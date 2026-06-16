# Upload Vulnerabilities — CTF Writeup

> [!info] Room Overview
> **Platform:** TryHackMe · Web Fundamentals Path
> **Techniques Used:** File Upload Bypass, Webshells, Reverse Shells, Client-Side Filter Bypass, Server-Side Filter Bypass (Extensions, Magic Numbers, MIME), Black-Box Enumeration

> [!abstract] Table of Contents
> 1. [[#Task 1 Getting Started|Getting Started (Hosts Setup)]]
> 2. [[#Task 2 Overwriting Existing Files|Overwriting Existing Files]]
> 3. [[#Task 3 Remote Code Execution|Remote Code Execution (Webshells & Reverse Shells)]]
> 4. [[#Task 4 Filtering|Filtering (Client-Side vs Server-Side)]]
> 5. [[#Task 5 Bypassing Client-Side Filtering|Bypassing Client-Side Filtering]]
> 6. [[#Task 6 Bypassing Server-Side Filtering — File Extensions|Bypassing Server-Side Filtering — File Extensions]]
> 7. [[#Task 7 Bypassing Server-Side Filtering — Magic Numbers|Bypassing Server-Side Filtering — Magic Numbers]]
> 8. [[#Task 8 Example Methodology|Example Methodology (Enumeration Checklist)]]
> 9. [[#Task 9 Challenge|Challenge]]
> 10. [[#Task 10 Conclusion|Conclusion (Cleanup)]]

---

# Task 1 Getting Started

## Hosts File Setup

The **hosts file** maps domain names to IP addresses locally, bypassing DNS.

- On **Linux / MacOS:** `/etc/hosts` (edit with `sudo nano /etc/hosts`)
- On **Windows:** `C:\Windows\System32\drivers\etc\hosts` (open with "Run as Administrator")

This is required because the TryHackMe machine's DNS isn't available; the hosts entry lets you use **name-based virtual hosting (vhosts)** so the webserver at a single IP can serve different sites based on the **Host** header in the HTTP request.

Add the following line at the end of the file:

```
10.48.179.246    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm
```

---

# Task 2 Overwriting Existing Files

## How It Works

Checks may be applied to see if the filename already exists on the server; if a file with the same name already exists then the server will return an error message asking the user to pick a different file name.

File permissions also come into play when protecting existing files from being overwritten. Web pages, for example, should not be writeable to the web user, thus preventing them from being overwritten with a malicious version uploaded by an attacker.

## Walkthrough

Here we have a web page with an upload form:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759494686706.png)

You may need to enumerate more than this for a real challenge; however, in this instance, let's just take a look at the source code of the page:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759494769552.png)

Inside the red box, we see the code that's responsible for displaying the image on the page. It's being sourced from a file called `spaniel.jpg`, inside a directory called `images`.

Now we know where the image is being pulled from — can we overwrite it? Let's download another image from the internet and call it `spaniel.jpg`. We'll then upload it to the site and see if we can overwrite the existing image:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759495388389.png)

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759495947155.png)

Attack successful — we managed to overwrite the original `images/spaniel.jpg` with our own copy.

---

# Task 3 Remote Code Execution

Remote Code Execution (RCE) allows us to execute code arbitrarily on the web server. RCE via an upload vulnerability is typically exploited by uploading a program written in the same language as the back-end of the website (or another language the server understands and will execute).

> [!note]
> In a _routed_ application (i.e. routes are defined programmatically rather than mapped to the file-system), this method of attack becomes much more complicated and less likely to occur. Most modern web frameworks are routed programmatically.

There are **two basic ways** to achieve RCE when exploiting a file upload vulnerability:

1. **Webshells** — simpler, sometimes the only option (e.g., file length limits or firewall rules prevent network-based shells)
2. **Reverse / Bind Shells** — the ideal goal for an attacker

**General methodology:** upload a shell of one kind or another, then activate it — either by navigating directly to the file (non-routed applications with inadequate restrictions), or by forcing the webapp to run the script.

---

## Webshell Attack

Let's assume we've found a webpage with an upload form:

![](https://assets.tryhackme.com/additional/imgur/GxMJAKH.png)

Start with a **Gobuster** scan to find directories:

![](https://assets.tryhackme.com/additional/imgur/OftwAIE.png)

We've got two directories — `uploads` and `assets`. Files we upload will likely be placed in `uploads`. Let's try uploading a legitimate image file first:

![](https://assets.tryhackme.com/additional/imgur/aAyIrod.png)

![](https://assets.tryhackme.com/additional/imgur/mIbGRIk.png)

Navigating to `http://demo.uploadvulns.thm/uploads` confirms the spaniel picture has been uploaded:

![](https://assets.tryhackme.com/additional/imgur/lVe2tjL.png)

![](https://assets.tryhackme.com/additional/imgur/N8vWlVO.png)

We can upload images. Now let's try a webshell. We know this webserver runs a PHP back-end.

A simple PHP webshell takes a parameter and executes it as a system command:

```php
<?php
    echo system($_GET["cmd"]);
?>
```

This code takes a GET parameter and executes it as a system command, then echoes the output to the screen.

Let's upload it to the site, then use it to show our current user and the contents of the current directory:

![](https://assets.tryhackme.com/additional/imgur/CU0Uyx5.png)

Success!

---

## Reverse Shell Attack

The process for uploading a reverse shell is almost identical to a webshell. We'll use the ubiquitous **Pentest Monkey reverse shell**, which comes by default on Kali Linux but can also be downloaded [here](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php).

### Steps

1. **Edit line 49** of the shell — change `$ip = '127.0.0.1';  // CHANGE THIS` to your TryHackMe `tun0` IP address (found on the [access page](https://tryhackme.com/access)). You can ignore the following line.

2. **Start a Netcat listener** to receive the connection:

```bash
nc -lvnp 1234
```

![](https://assets.tryhackme.com/additional/imgur/ysY306E.png)

3. **Upload the shell**, then activate it by navigating to `http://demo.uploadvulns.thm/uploads/shell.php` (the name will be whatever you called it — `php-reverse-shell.php` by default).

The website should hang and not load properly — however, if we switch back to the terminal, we have a hit:

![](https://assets.tryhackme.com/additional/imgur/he0hbiR.png)

Once again, we have obtained RCE on this webserver.

---

# Task 4 Filtering

## Client-Side vs Server-Side

**Client-side scripts** run in the user's browser (JavaScript). In the context of file-uploads, the filtering occurs **before** the file is even uploaded to the server. Because the filtering happens on _our_ computer, it is trivially easy to bypass. Client-side filtering by itself is a highly insecure method of verifying that an uploaded file is not malicious.

**Server-side scripts** run on the server (PHP, Node.js, Python, etc.). Server-side filtering is more difficult to bypass since you don't have the code in front of you. Instead we must form a payload that conforms to the filters in place but still allows code execution.

---

## Filter Types

### Extension Validation

File extensions are used (in theory) to identify the contents of a file. In practice they are very easy to change. Filters that check extensions work in one of two ways:

- **Blacklist** — a list of extensions that are **not** allowed
- **Whitelist** — a list of extensions that **are** allowed (reject everything else)

### MIME Type Validation

MIME (**M**ultipurpose **I**nternet **M**ail **E**xtension) types are identifiers for files, attached in the header of the request:

![](https://assets.tryhackme.com/additional/imgur/uptWRKW.png)

MIME types follow the format `<type>/<subtype>`. In the request above, the image `spaniel.jpg` was uploaded with MIME type `image/jpeg`. As MIME is based on the file extension, this is extremely easy to bypass.

### Magic Number Validation

Magic numbers are the more accurate way of determining file contents. The "magic number" is a string of bytes at the very beginning of the file content which identifies the content. For example, a PNG file would have these bytes at the top: `89 50 4E 47 0D 0A 1A 0A`.

![](https://assets.tryhackme.com/additional/imgur/vHQWOgi.png)

Unlike Windows, Unix systems use magic numbers for identifying files.

### File Length Filtering

File length filters prevent huge files from being uploaded (which could starve server resources). Our fully fledged PHP reverse shell is 5.4 KB — relatively tiny, but if the form expects a maximum of 2 KB then we'd need an alternative shell.

### File Content Filtering

More complicated filtering systems may scan the full contents of an uploaded file to ensure that it's not spoofing its extension, MIME type, and magic number.

> [!important]
> None of these filters are perfect by themselves — they will usually be used in conjunction, providing a **multi-layered filter**. Any of these can be applied client-side, server-side, or both.

---

# Task 5 Bypassing Client-Side Filtering

Client-side filtering is extremely easy to bypass since it occurs entirely on a machine you control.

## Four Bypass Techniques

1. **Turn off JavaScript in your browser** — works provided the site doesn't require JS for basic functionality.

2. **Intercept and modify the incoming page** — use BurpSuite to intercept the incoming web page and strip out the JavaScript filter before it runs.

3. **Intercept and modify the file upload** — let the page load normally, but intercept the file upload after it's already passed (and been accepted by) the filter.

4. **Send the file directly to the upload point** — post the data directly using `curl`, completely bypassing the client-side filter:

```bash
curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>
```

To use this method, first intercept a successful upload (using BurpSuite or the browser console) to see the parameters being used in the upload, which can then be slotted into the command above.

---

## Walkthrough — Method 1: Stripping JS Before Page Load

We find an upload page:

![](https://assets.tryhackme.com/additional/imgur/fI67jX0.png)

Looking at the source code, we see a basic JavaScript function checking for the MIME type of uploaded files:

![](https://assets.tryhackme.com/additional/imgur/TrI5jQD.png)

The filter is using a **whitelist** to exclude any MIME type that isn't `image/jpeg`.

Start BurpSuite and reload the page. We'll see our request to the site — right-click the intercepted data → **Do Intercept** → **Response to this request**:

![](https://assets.tryhackme.com/additional/imgur/T0RjAry.png)

Click **Forward** to see the server's response. Here we can delete, comment out, or otherwise break the JavaScript function before it loads:

![](https://assets.tryhackme.com/additional/imgur/ACgWLpH.png)

Having deleted the function, click **Forward** until the site finishes loading. We are now free to upload any kind of file to the website:

![](https://assets.tryhackme.com/additional/imgur/5cyqjqa.png)

> [!tip] Intercepting External JS Files
> BurpSuite will not, by default, intercept external JavaScript files. If you need to edit an external script, go to **Options** tab → **Intercept Client Requests** section → edit the first line's condition to remove `^js$|`:
>
> ![](https://assets.tryhackme.com/additional/imgur/95hi6pX.png)

---

## Walkthrough — Method 2: Intercepting the Upload Request

Reload the webpage to put the filter back in place. Take the reverse shell and rename it to `shell.jpg`. Since the MIME type (based on the file extension) checks out, the client-side filter lets our payload through:

![](https://assets.tryhackme.com/additional/imgur/WNpruFM.png)

Activate BurpSuite intercept, click **Upload**, and catch the request:

![](https://assets.tryhackme.com/additional/imgur/h2164Li.png)

The MIME type of our PHP shell is currently `image/jpeg`. Change this to `text/x-php`, and the file extension from `.jpg` to `.php`, then forward the request to the server:

![](https://assets.tryhackme.com/additional/imgur/sqmwssT.png)

Navigate to `http://demo.uploadvulns.thm/uploads/shell.php` with a Netcat listener running — we receive a connection from the shell:

![](https://assets.tryhackme.com/additional/imgur/cUqNO2L.png)

---

# Task 6 Bypassing Server-Side Filtering — File Extensions

## What Is Server-Side Filtering?

Unlike client-side filters (JavaScript) which run in your browser, **server-side filters run on the server** — you cannot see or edit them. You must:

- Upload files
- See what gets accepted or rejected
- Test different tricks until something bypasses the filter

This is called **black-box testing**.

---

## Example 1 — White-Box (Server Code Provided)

The server code is shown:

```php
$extension = pathinfo($_FILES["fileToUpload"]["name"])["extension"];
switch($extension){
    case "php":
    case "phtml":
    case NULL:
        $uploadFail = True;
        break;
    default:
        $uploadFail = False;
}
```

### Analysis

- Server **only blocks:** `.php`, `.phtml`
- Server **checks only the last extension** (after the last dot)

| Filename      | Result       |
| ------------- | ------------ |
| `shell.php`   | ❌ Blocked   |
| `shell.phtml` | ❌ Blocked   |
| `shell.php5`  | ✅ Allowed   |
| `shell.php7`  | ✅ Allowed   |
| `shell.phar`  | ✅ Allowed   |
| `shell.pht`   | ✅ Allowed   |

But some of these **may not execute** on the server.

### Result

`.phar` works — `payload.phar` is NOT blocked by the filter AND the server executes it as PHP. Shell obtained.

---

## Example 2 — Black-Box Testing (No Code Shown)

### Step 1 — Test a safe file

Upload `spaniel.jpg` → Works. So `.jpg` is allowed.

### Step 2 — Test a dangerous file

Upload `shell.php` → Blocked. So server blocks `.php`.

### Step 3 — Test alternative PHP extensions

Try `.php3`, `.php5`, `.phar`, `.pht`, etc. → None work here.

### Step 4 — Try double extensions

What if the filter is weak and only checks if `.jpg` appears anywhere in the filename? Try uploading:

```
shell.jpg.php
```

This filename **contains `.jpg`**, so it may pass the filter — and it does. This means the server code was something like:

```
IF filename contains ".jpg" → allow
```

### Step 5 — After upload

Go to `/uploads/shell.jpg.php`. The server interprets the **last extension** `.php` → PHP runs → shell obtained.

---

## Key Lesson — Extension Bypass Reference

> [!important] Server-side bypassing = test everything

| Trick                     | Example         | Why It Works                                       |
| ------------------------- | --------------- | -------------------------------------------------- |
| Alternative PHP extension | `shell.phar`    | Server blocks only `.php` and `.phtml`             |
| Double extension          | `shell.jpg.php` | Server only checks if filename _contains_ `.jpg`   |
| Last extension check      | `shell.php5`    | Server checks last dot only                        |

**Other techniques to try:**

- Uppercase extensions (`shell.PHP`)
- Extension with trailing dot (`shell.php.`)
- Null byte tricks (`shell.php%00.jpg`)
- MIME spoofing

Every filter works differently. Your bypass must match THAT filter.

---

# Task 7 Bypassing Server-Side Filtering — Magic Numbers

Magic numbers are used as a more accurate identifier of files. The magic number is a string of hex digits and is always the very first thing in a file. Knowing this, it's possible to validate file uploads by reading those first few bytes and comparing them against either a whitelist or a blacklist.

> [!note]
> This technique can be very effective against a PHP-based webserver; however, it can sometimes fail against other types of webserver.

## Walkthrough

We have an upload page:

![](https://assets.tryhackme.com/additional/imgur/yQnQGsn.png)

If we upload our standard `shell.php`, we get an error; however, if we upload a JPEG, the website is fine with it.

We know that JPEG files are accepted, so let's add the JPEG magic number to the top of our `shell.php` file. A quick look at the [list of file signatures on Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures) shows several possible JPEG magic numbers. Let's pick `FF D8 FF DB`.

### Step 1 — Check current file type

Use the Linux `file` command to check the file type of our shell:

![](https://assets.tryhackme.com/additional/imgur/2126EHS.png)

As expected, the command reports the filetype as PHP.

### Step 2 — Add placeholder bytes

The magic number we've chosen is four bytes long. Open the reverse shell script and add four random characters on the first line (we'll use four `A`s):

![](https://assets.tryhackme.com/additional/imgur/oe434wu.png)

### Step 3 — Edit hex values

Reopen the file in `hexeditor` (comes by default on Kali). The file looks like this:

![](https://assets.tryhackme.com/additional/imgur/otIyN96.png)

Note the four bytes in the red box: they are all `41`, which is the hex code for a capital `A` — exactly what we added at the top of the file.

Change this to the JPEG magic number: `FF D8 FF DB`

![](https://assets.tryhackme.com/additional/imgur/2OlGKdQ.png)

### Step 4 — Verify the spoof

Save and exit (Ctrl + X). Use `file` again to confirm we have successfully spoofed the filetype:

![](https://assets.tryhackme.com/additional/imgur/ldyt88v.png)

### Step 5 — Upload and get a shell

Upload the modified shell and see if it bypasses the filter:

![](https://assets.tryhackme.com/additional/imgur/Coat5LI.png)

We bypassed the server-side magic number filter and received a reverse shell.

---

# Task 8 Example Methodology

This task teaches you **how to approach ANY file upload challenge** — a checklist to follow every time.

## Step 1 — Recon the Whole Website

Before touching the upload page, check what technologies the site uses (PHP? ASP? Apache? Nginx?).

**Tools:**
- Browser DevTools → Network tab
- Wappalyzer extension
- BurpSuite (intercept page → check `Server:` and `X-Powered-By:` headers)

**Goal:** Know what environment you're attacking.

## Step 2 — Find the Upload Page & Check Client-Side Filters

On the upload page:
- View source
- Look for JavaScript blocking file types
- Try turning off JavaScript
- Intercept the page in Burp and remove JS restrictions

**Goal:** Understand what the browser checks — and bypass it easily.

## Step 3 — Upload a Harmless File

Upload something safe, like `image.jpg`.

Why? You want to see:
- Does the file upload?
- Where is it stored? (`/uploads/`? `/images/`?)
- Can you access it in your browser?

If you _can_ access it, you now know:
- The upload folder path
- The naming scheme (does server rename files?)
- The upload process behaviour

Use **Gobuster** if the folder is not obvious:

```bash
gobuster dir -u http://site -w wordlist.txt -x php,txt,html
```

## Step 4 — Upload a Malicious File

Example: `shell.php` — this will usually be blocked (good!).

The **error message** gives clues:

| Error Message                | Indicates            |
| ---------------------------- | -------------------- |
| "Extension not allowed"      | Extension filter     |
| "Invalid file type"          | MIME filter          |
| "File signature not allowed" | Magic bytes filter   |
| "File too large"             | File-size filter     |

## Step 5 — Identify the Server-Side Filter Type

### A) Test for Extension Blacklist / Whitelist

Upload `test.abcxyz`:
- If it **uploads** → server uses a **blacklist** (blocks only specific extensions)
- If it **fails** → server uses a **whitelist** (only allows certain extensions)

### B) Test Magic Number Filtering

1. Take a valid JPG (works normally)
2. Change its magic bytes to something else (like `GIF89a`)
3. Upload again

If upload fails → server checks magic numbers.

### C) Test MIME Type Filtering

Intercept upload request in BurpSuite, change:

```
Content-Type: image/jpeg
```

to:

```
Content-Type: application/x-php
```

If upload fails → server checks MIME type.

### D) Test File Size Filter

Upload small → works → upload bigger → works → upload even bigger → fails.
Now you know the max allowed size.

---

# Task 9 Challenge

*(Challenge task — work through it using the methodology above.)*

---

# Task 10 Conclusion

Now that you've finished the room, remember to **revert the changes** you made to your `hosts` file back in Task 1.

**On Linux or MacOS:**

```bash
sudo sed -i '$d' /etc/hosts
```

**On Windows:**

```powershell
(GC C:\Windows\System32\drivers\etc\hosts | select -Skiplast 1) | SC C:\Windows\System32\drivers\etc\hosts
```
