
## Username Enumeration

If you try entering the username **admin** and fill in the other form fields with fake information, you'll see we get the error **An account with this username already exists**. We can use the existence of this error message to produce a list of valid usernames already signed up on the system by using the ffuf tool below.

```shell-session
user@tryhackme$ ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.201.68.251/customers/signup -mr "username already exists"
```

In the above example, the `-w` argument selects the file's location on the computer that contains the list of usernames that we're going to check exists. The `-X` argument specifies the request method, this will be a GET request by default, but it is a POST request in our example. The `-d` argument specifies the data that we are going to send. In our example, we have the fields username, email, password and cpassword. We've set the value of the username to **FUZZ**. In the ffuf tool, the FUZZ keyword signifies where the contents from our wordlist will be inserted in the request. The `-H` argument is used for adding additional headers to the request. In this instance, we're setting the `Content-Type` so the web server knows we are sending form data. The `-u` argument specifies the URL we are making the request to, and finally, the `-mr` argument is the text on the page we are looking for to validate we've found a valid username.

## Brute Force

```shell-session
user@tryhackme$ ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.201.68.251/customers/login -fc 200
```

This ffuf command is a little different to the previous one in Task 2. Previously we used the **FUZZ** keyword to select where in the request the data from the wordlists would be inserted, but because we're using multiple wordlists, we have to specify our own FUZZ keyword. In this instance, we've chosen `W1` for our list of valid usernames and `W2` for the list of passwords we will try. The multiple wordlists are again specified with the `-w` argument but separated with a comma.  For a positive match, we're using the `-fc` argument to check for an HTTP status code other than 200.  

Running the above command will find a single working username and password combination that answers the question below.

## Logic Flaw

**Logic Flaw Example  

The below mock code example checks to see whether the start of the path the client is visiting begins with /admin and if so, then further checks are made to see whether the client is, in fact, an admin. If the page doesn't begin with /admin, the page is shown to the client.  

```php
if( url.substr(0,6) === '/admin') {
    # Code to check user is an admin
} else {
    # View Page
}
```

Because the above PHP code example uses three equals signs (===), it's looking for an exact match on the string, including the same letter casing. The code presents a logic flaw because an unauthenticated user requesting **/adMin** will not have their privileges checked and have the page displayed to them, totally bypassing the authentication checks.

### 🎯 **Goal of the Feature (What it’s supposed to do)**

The password reset page asks for:

1. The **email** (e.g., `robert@acmeitsupport.thm`)
    
2. The **username** (e.g., `robert`)  
    If both match, the **reset link is sent to Robert’s email**.
    

---

### 🐞 **What’s the Logic Flaw?**

The flaw lies in **how the server handles the `email` value** during the second step.

- The server uses a special PHP variable called `$_REQUEST`.
    
- `$_REQUEST` combines **GET** (from the URL) and **POST** (from form data).
    
- If the same key (e.g., `email`) is in both GET and POST, **POST wins**.
    

---

### 🧪 **How You Exploit It (Step-by-Step)**

#### ✅ Normal request:

bash

CopyEdit

`curl 'http://.../reset?email=robert@acmeitsupport.thm' \      -H 'Content-Type: application/x-www-form-urlencoded' \      -d 'username=robert'`

- URL contains email: `email=robert@acmeitsupport.thm` (GET)
    
- Form data has only `username=robert` (POST)
    
- Reset email goes to **Robert's real email**
    

---

#### 🔥 Malicious request:

bash

CopyEdit

`curl 'http://.../reset?email=robert@acmeitsupport.thm' \      -H 'Content-Type: application/x-www-form-urlencoded' \      -d 'username=robert&email=attacker@hacker.com'`

- URL still says `email=robert@acmeitsupport.thm` (GET) ✅ validation passes
    
- But POST **overrides** the email with `attacker@hacker.com`
    
- The reset link is **sent to attacker’s email** instead! 😈
    

---

### 🧵 Why it works?

PHP merges GET and POST into one array (`$_REQUEST`), and **POST data overrides GET**. So you trick the server:

- Use the correct email in the URL (GET) for validation
    
- But inject your own email in the form data (POST) to **steal the reset link**
    

---

### 🎁 Bonus:

If you control an email like `yourname@customer.acmeitsupport.thm`, the reset link ends up **in your own account**, and you can:

- Log in as **Robert**
    
- View his support tickets
    
- Find the **flag**
    

---

### ✅ In Short:

> **By sending two `email` values (GET + POST), you trick the server into sending a password reset email to yourself instead of the real user.**

This is a **logic flaw** — the app assumes only one source of truth, but it's using both GET and POST **insecurely**.


## Cookie Tampering

### Plain Text

The contents of some cookies can be in plain text, and it is obvious what they do. Take, for example, if these were the cookie set after a successful login:

**Set-Cookie: logged_in=true; Max-Age=3600; Path=/**  
****Set-Cookie: admin=false; Max-Age=3600; Path=/****

We see one cookie (logged_in), which appears to control whether the user is currently logged in or not, and another (admin), which controls whether the visitor has admin privileges. Using this logic, if we were to change the contents of the cookies and make a request we'll be able to change our privileges.

First, we'll start just by requesting the target page:  

```shell-session
user@tryhackme$ curl http://10.201.68.251/cookie-test
```

We can see we are returned a message of: **Not Logged In**

Now we'll send another request with the logged_in cookie set to true and the admin cookie set to false:  

```shell-session
user@tryhackme$ curl -H "Cookie: logged_in=true; admin=false" http://10.201.68.251/cookie-test
```

We are given the message: **Logged In As A User**

Finally, we'll send one last request setting both the logged_in and admin cookie to true:

```shell-session
user@tryhackme$ curl -H "Cookie: logged_in=true; admin=true" http://10.201.68.251/cookie-test
```

This returns the result: **Logged In As An Admin** as well as a flag which you can use to answer question one.  

### **Hashing**  

Sometimes cookie values can look like a long string of random characters; these are called hashes which are an irreversible representation of the original text. Here are some examples that you may come across:

|   |   |   |
|---|---|---|
|**Original String**|**Hash Method**|**Output**|
|1|md5|c4ca4238a0b923820dcc509a6f75849b|
|1|sha-256|6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b|
|1|sha-512|4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a|
|1|sha1|356a192b7913b04c54574d18c28d46e6395428ab|

You can see from the above table that the hash output from the same input string can significantly differ depending on the hash method in use. Even though the hash is irreversible, the same output is produced every time, which is helpful for us as services such as [https://crackstation.net/](https://crackstation.net/) keep databases of billions of hashes and their original strings.

### **Encoding**

Encoding is similar to hashing in that it creates what would seem to be a random string of text, but in fact, the encoding is reversible. So it begs the question, what is the point in encoding? Encoding allows us to convert binary data into human-readable text that can be easily and safely transmitted over mediums that only support plain text ASCII characters.  
  
Common encoding types are base32 which converts binary data to the characters A-Z and 2-7, and base64 which converts using the characters a-z, A-Z, 0-9,+, / and the equals sign for padding.

  
Take the below data as an example which is set by the web server upon logging in:

****Set-Cookie:** session=eyJpZCI6MSwiYWRtaW4iOmZhbHNlfQ==; Max-Age=3600; Path=/**

This string base64 decoded has the value of **{"id":1,"admin": false}** we can then encode this back to base64 encoded again but instead setting the admin value to true, which now gives us admin access.