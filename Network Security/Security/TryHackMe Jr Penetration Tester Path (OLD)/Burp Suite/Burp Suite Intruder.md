
## What is Intruder

Burp Suite's Intruder module is a powerful tool that allows for automated and customisable attacks. It provides the ability to modify specific parts of a request and perform repetitive tests with variations of input data. Intruder is particularly useful for tasks like fuzzing and brute-forcing, where different values need to be tested against a target.

Intruder is Burp Suite's built-in fuzzing tool that allows for automated request modification and repetitive testing with variations in input values. By using a captured request (often from the Proxy module), Intruder can send multiple requests with slightly altered values based on user-defined configurations. It serves various purposes, such as brute-forcing login forms by substituting username and password fields with values from a wordlist or performing fuzzing attacks using wordlists to test subdirectories, endpoints, or virtual hosts. Intruder's functionality is comparable to command-line tools like **Wfuzz** or **ffuf**.

Let's explore the Intruder interface:

![Showing the intruder interface](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/2b2a10c651bee6531f8dbeb5e32733e8.png)

There are four sub-tabs within Intruder:

- **Positions**: This tab allows us to select an attack type (which we will cover in a future task) and configure where we want to insert our payloads in the request template.
- **Payloads**: Here we can select values to insert into the positions defined in the **Positions** tab. We have various payload options, such as loading items from a wordlist. The way these payloads are inserted into the template depends on the attack type chosen in the **Positions** tab. The **Payloads** tab also enables us to modify Intruder's behavior regarding payloads, such as defining pre-processing rules for each payload (e.g., adding a prefix or suffix, performing match and replace, or skipping payloads based on a defined regex).
- **Resource Pool**: This tab is not particularly useful in the Burp Community Edition. It allows for resource allocation among various automated tasks in Burp Professional. Without access to these automated tasks, this tab is of limited importance.
- **Settings**: This tab allows us to configure attack behavior. It primarily deals with how Burp handles results and the attack itself. For instance, we can flag requests containing specific text or define Burp's response to redirect (3xx) responses.

**Note:** The term "fuzzing" refers to the process of testing functionality or existence by applying a set of data to a parameter. For example, fuzzing for endpoints in a web application involves taking each word in a wordlist and appending it to a request URL (e.g., http://10.201.52.210/WORD_GOES_HERE) to observe the server's response.

## Positions

When using Burp Suite Intruder to perform an attack, the first step is to examine the positions within the request where we want to insert our payloads. These positions inform Intruder about the locations where our payloads will be introduced (as we will explore in upcoming tasks).

Let's navigate to the Positions tab:

![Showing the positions tab](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/1372bbafab835e10806ee6beb6681f36.png)

Notice that Burp Suite automatically attempts to identify the most probable positions where payloads can be inserted. These positions are highlighted in green and enclosed by section marks (`§`).

On the right-hand side of the interface, we find the following buttons: `Add §`, `Clear §`, and `Auto §`:

- The `Add §` button allows us to define new positions manually by highlighting them within the request editor and then clicking the button.
- The `Clear §` button removes all defined positions, providing a blank canvas where we can define our own positions.
- The `Auto §` button automatically attempts to identify the most likely positions based on the request. This feature is helpful if we previously cleared the default positions and want them back.

The following GIF demonstrates the process of adding, clearing, and automatically reselecting positions:

![Process of adding, clearing, and automatically reselecting positions](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/504d75f7c90e1c985dae5e05038f50ac.gif)

## Payloads

In the **Payloads** tab of Burp Suite Intruder, we can create, assign, and configure payloads for our attack. This sub-tab is divided into four sections:

![Payloads sub-tab divided into four sections](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/f049dff9e1172b76c0f81ad4771b012d.png)

1. **Payload Sets**:
    - This section allows us to choose the position for which we want to configure a payload set and select the type of payload we want to use.
    - When using attack types that allow only a single payload set (Sniper or Battering Ram), the "Payload Set" dropdown will have only one option, regardless of the number of defined positions.
    - If we use attack types that require multiple payload sets (Pitchfork or Cluster Bomb), there will be one item in the dropdown for each position.
    - **Note:** When assigning numbers in the "Payload Set" dropdown for multiple positions, follow a top-to-bottom, left-to-right order. For example, with two positions (`username=§pentester§&password=§Expl01ted§`), the first item in the payload set dropdown would refer to the username field, and the second item would refer to the password field.
  
2. **Payload settings**:
    - This section provides options specific to the selected payload type for the current payload set.
    - For example, when using the "Simple list" payload type, we can manually add or remove payloads to/from the set using the **Add** text box, **Paste** lines, or **Load** payloads from a file. The **Remove** button removes the currently selected line, and the **Clear** button clears the entire list. Be cautious with loading huge lists, as it may cause Burp to crash.
    - Each payload type will have its own set of options and functionality. Explore the options available to understand the range of possibilities.  
        
        ![Available options](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/722a734ac5dd6437211504d3bc7bb6c2.png)
        
  
3. **Payload Processing**:
    - In this section, we can define rules to be applied to each payload in the set before it is sent to the target.
    - For example, we can capitalize every word, skip payloads that match a regex pattern, or apply other transformations or filtering.
    - While you may not use this section frequently, it can be highly valuable when specific payload processing is required for your attack.
  
4. **Payload Encoding**:
    - The section allows us to customize the encoding options for our payloads.
    - By default, Burp Suite applies URL encoding to ensure the safe transmission of payloads. However, there may be cases where we want to adjust the encoding behavior.
    - We can override the default URL encoding options by modifying the list of characters to be encoded or unchecking the "URL-encode these characters" checkbox.

## Introduction to Attack Types

### 🔹 1. Sniper

- **How it works:** Changes **one parameter at a time**.
    
- **Use case:** Good for testing single fields like username, password, or an input box.
    

👉 Example:  
You test a login form.

- Sniper puts `admin` in the username field while password stays the same.
    
- Next try, it puts `root`.
    
- Then `test`, and so on.  
    Only one thing changes each time.
    

---

### 🔹 2. Battering Ram

- **How it works:** Uses the **same payload in all positions at once**.
    
- **Use case:** When multiple fields expect the **same value**.
    

👉 Example:  
Form has two parameters: `username` and `email`.

- Payload = `test123` → goes into **both fields at once**.
    
- Payload = `admin` → goes into both fields again.
    

---

### 🔹 3. Pitchfork

- **How it works:** Uses **different payload lists** for each position, advancing them in parallel.
    
- **Use case:** When parameters are related and need testing together.
    

👉 Example:  
Login form with `username` and `password`.

- List 1: `admin, user, guest`
    
- List 2: `123, pass, test`  
    → Test combos:
    

1. `admin:123`
    
2. `user:pass`
    
3. `guest:test`
    

(Each position gets its own list.)

---

### 🔹 4. Cluster Bomb

- **How it works:** Tries **all possible combinations** of payloads across positions.
    
- **Use case:** When you want to brute-force all combinations.
    

👉 Example:  
Same login form with `username` and `password`.

- List 1: `admin, user`
    
- List 2: `123, pass`  
    → Test combos:
    

1. `admin:123`
    
2. `admin:pass`
    
3. `user:123`
    
4. `user:pass`
    

---

✅ **Quick analogy:**

- **Sniper** → one bullet at a time.
    
- **Battering Ram** → same hit on all doors together.
    
- **Pitchfork** → two prongs, moving forward together.
    
- **Cluster Bomb** → explodes everywhere, testing all combos.


The difference between **Pitchfork** and **Cluster Bomb** is subtle but important. Let’s keep it simple:

---

### 🔹 Pitchfork

- Uses **multiple payload sets** (one for each position).
    
- Moves **in sync** — payload 1 from list A pairs with payload 1 from list B, payload 2 with payload 2, and so on.
    
- Stops when the shortest list runs out.
    

👉 Example:

- Username list: `admin, user, guest`
    
- Password list: `123, pass, test`
    

**Tries:**

1. `admin:123`
    
2. `user:pass`
    
3. `guest:test`
    

---

### 🔹 Cluster Bomb

- Also uses **multiple payload sets**.
    
- But tries **all possible combinations** of them (Cartesian product).
    
- Much larger attack space.
    

👉 Example:

- Username list: `admin, user, guest`
    
- Password list: `123, pass`
    

**Tries:**

1. `admin:123`
    
2. `admin:pass`
    
3. `user:123`
    
4. `user:pass`
    
5. `guest:123`
    
6. `guest:pass`
    

---

✅ **Quick Difference in One Line:**

- **Pitchfork** = march forward together, one-to-one pairing.
    
- **Cluster Bomb** = try every possible combo, one-to-many pairing.


## Sniper

The **Sniper** attack type is the default and most commonly used attack type in Burp Suite Intruder. It is particularly effective for single-position attacks, such as password brute-force or fuzzing for API endpoints. In a Sniper attack, we provide a set of payloads, which can be a wordlist or a range of numbers, and Intruder inserts each payload into each defined position in the request.

Example Positions

```html
POST /support/login/ HTTP/1.1
Host: 10.201.65.233
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Origin: http://10.201.65.233
Connection: close
Referer: http://10.201.65.233/support/login/
Upgrade-Insecure-Requests: 1

username=§pentester§&password=§Expl01ted§
```

In this example, we have two positions defined for the `username` and `password` body parameters. In a Sniper attack, Intruder takes each payload from the payload set and substitutes it into each defined position in turn.

Assuming we have a wordlist with three words: `burp`, `suite`, and `intruder`, Intruder would generate six requests:

|Request Number|Request Body|
|---|---|
|1|`username=burp&password=Expl01ted`|
|2|`username=suite&password=Expl01ted`|
|3|`username=intruder&password=Expl01ted`|
|4|`username=pentester&password=burp`|
|5|`username=pentester&password=suite`|
|6|`username=pentester&password=intruder`|

Observe how Intruder starts with the first position (`username`) and substitutes each payload into it, then moves to the second position (`password`) and performs the same substitution with the payloads. The total number of requests made by Intruder Sniper can be calculated as `requests = numberOfWords * numberOfPositions`.

The Sniper attack type is beneficial when we want to perform tests with single-position attacks, utilizing different payloads for each position. It allows for precise testing and analysis of different payload variations.

## Battering Ram

The **Battering ram** attack type in Burp Suite Intruder differs from Sniper in that it places the same payload in every position simultaneously, rather than substituting each payload into each position in turn.

Example Positions

```
POST /support/login/ HTTP/1.1
    Host: MACHINE_IP
    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 37
    Origin: http://MACHINE_IP
    Connection: close
    Referer: http://MACHINE_IP/support/login/
    Upgrade-Insecure-Requests: 1
    
    username=§pentester§&password=§Expl01ted§
```

Using the Battering Ram attack type with the same wordlist from before (`burp`, `suite`, and `intruder`), Intruder would generate three requests:

|Request Number|Request Body|
|---|---|
|1|`username=burp&password=burp`|
|2|`username=suite&password=suite`|
|3|`username=intruder&password=intruder`|

## Pitchfork

The **Pitchfork** attack type in Burp Suite Intruder is similar to having multiple Sniper attacks running simultaneously. While Sniper uses one payload set to test all positions simultaneously, Pitchfork utilises one payload set per position <span style="color:rgb(0, 176, 240)">(up to a maximum of 20)</span> and iterates through them all simultaneously.

To better understand Pitchfork, let us revisit our brute-force example, but this time with two wordlists:

1. The first wordlist contains usernames: `joel`, `harriet`, and `alex`.
2. The second wordlist contains passwords: `J03l`, `Emma1815`, and `Sk1ll`.

We can use these two lists to perform a Pitchfork attack on the login form. Each request made during the attack would look like this:

|Request Number|Request Body|
|---|---|
|1|`username=joel&password=J03l`|
|2|`username=harriet&password=Emma1815`|
|3|`username=alex&password=Sk1ll`|

As shown in the table, Pitchfork takes the first item from each list and substitutes them into the request, one per position. It then repeats this process for the next request by taking the second item from each list and substituting it into the template. Intruder continues this iteration until one or all of the lists run out of items. It's important to note that Intruder stops testing as soon as one of the lists is complete. Therefore, in Pitchfork attacks, it is ideal for the payload sets to have the same length. If the lengths of the payload sets differ, Intruder will only make requests until the shorter list is exhausted, and the remaining items in the longer list will not be tested.

## Cluster Bomb

The **Cluster bomb** attack type in Burp Suite Intruder allows us to choose multiple payload sets, one per position (up to a maximum of 20). Unlike Pitchfork, where all payload sets are tested simultaneously, Cluster bomb iterates through each payload set individually, ensuring that every possible combination of payloads is tested.

To illustrate the Cluster bomb attack type, let's use the same wordlists as before:

- Usernames: `joel`, `harriet`, and `alex`.
- Passwords: `J03l`, `Emma1815`, and `Sk1ll`.

In this example, let's assume that we don't know which password belongs to which user. We have three users and three passwords, but the mappings are unknown. In this case, we can use a Cluster bomb attack to try every combination of values. The request table for our username and password positions would look like this:

|Request Number|Request Body|
|---|---|
|1|`username=joel&password=J03l`|
|2|`username=harriet&password=J03l`|
|3|`username=alex&password=J03l`|
|4|`username=joel&password=Emma1815`|
|5|`username=harriet&password=Emma1815`|
|6|`username=alex&password=Emma1815`|
|7|`username=joel&password=Sk1ll`|
|8|`username=harriet&password=Sk1ll`|
|9|`username=alex&password=Sk1ll`|

As shown in the table, the Cluster bomb attack type iterates through every combination of the provided payload sets. It tests every possibility by substituting each value from each payload set into the corresponding position in the request.

Cluster bomb attacks can generate a significant amount of traffic as it tests every combination. The number of requests made by a Cluster bomb attack can be calculated by multiplying the number of lines in each payload set together. It's important to be cautious when using this attack type, especially when dealing with large payload sets. Additionally, when using Burp Community and its Intruder rate-limiting, the execution of a Cluster bomb attack with a moderately sized payload set can take a significantly longer time.

The Cluster bomb attack type is particularly useful for credential brute-forcing scenarios where the mapping between usernames and passwords is unknown.

## Practical Example

To put our theoretical knowledge into practice, we will attempt to gain access to the support portal located at `http://10.201.16.65/support/login`. This portal follows a typical login structure, and upon inspecting its source code, we find that no protective measures have been implemented:

Support Login Form Source Code

```html
---
<form method="POST">
    <div class="form-floating mb-3">
        <input class="form-control" type="text" name=username  placeholder="Username" required>
        <label for="username">Username</label>
    </div>
    <div class="form-floating mb-3">
        <input class="form-control" type="password" name=password  placeholder="Password" required>
        <label for="password">Password</label>
    </div>
    <div class="d-grid"><button class="btn btn-primary btn-lg" type="submit">Login!</button></div>
</form>
---
```

Given the absence of protective measures, we have multiple options to exploit this form, including a cluster bomb attack for brute-forcing the credentials. However, we have an easier approach at our disposal.

Approximately three months ago, Bastion Hosting fell victim to a cyber attack, compromising employee usernames, email addresses, and plaintext passwords. While the affected employees were instructed to change their passwords promptly, there is a possibility that some disregarded this advice.

As we possess a list of known usernames, each accompanied by a corresponding password, we can leverage a credential-stuffing attack instead of a straightforward brute-force. This method proves advantageous and significantly quicker, especially when utilising the rate-limited version of Intruder. To access the leaked credentials, download the file from the target machine using the following command in the AttackBox: `wget http://10.201.16.65:9999/Credentials/BastionHostingCreds.zip`

#### Tutorial

To solve this example, follow these steps to conduct a credential-stuffing attack with Burp Macros:

1. Download and Prepare Wordlists:
    
    - Download and extract the BastionHostingCreds.zip file.
    - Within the extracted folder, find the following wordlists:
        - emails.txt
        - usernames.txt
        - passwords.txt
        - combined.txt
    
      
    
    These contain lists of leaked emails, usernames, and passwords, respectively. The last list contains the combined email and password lists. We will be using the `usernames.txt` and `passwords.txt` lists.
    
2. Navigate to `http://10.201.16.65/support/login` in your browser. Activate the Burp Proxy and attempt to log in, capturing the request in your proxy. Note that any credentials will suffice for this step.
    
3. Send the captured request from the Proxy to Intruder by right-clicking and selecting "Send to Intruder" or using `Ctrl + I`.
    
4. In the "Positions" sub-tab, ensure that only the username and password parameters are selected. Clear any additional selections, such as session cookies.
    
5. Set the Attack type to "Pitchfork."
    
    ![Set the attack type to pitchfork](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/ebd86a3904d8cce5659194499d31db1d.png)
    
6. Move to the "Payloads" sub-tab. You will find two payload sets available for the username and password fields.
    
    ![Configure the two payload sets](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/f9ca1e72d694d8d27f7318637321d2be.png)
    
7. In the first payload set (for usernames), go to "Payload Options," choose "Load," and select the `usernames.txt` list.

- Repeat the same process for the second payload set (for passwords) using the `passwords.txt` list.
- The entire process can be seen in the GIF image below:
    
    ![Showing the entire process](https://assets.muirlandoracle.co.uk/thm/modules/burp/settingPayloads.gif)
    

9. Click the **Start Attack** button to begin the credential-stuffing attack. A warning about rate-limiting may appear; click **OK** to proceed. The attack will take a few minutes to complete in Burp Community.
    
10. Once the attack starts, a new window will display the results of the requests. However, as Burp sent 100 requests, we need to identify which one(s) were successful.
    
    Since the response status codes are not differentiating successful and unsuccessful attempts (all are 302 redirects), we need to use the response length to distinguish them.
    
    ![Showing the result with the smallest response length](https://assets.muirlandoracle.co.uk/thm/modules/burp/2ed757b27276.png)
    
    Click on the header for the "Length" column to sort the results by byte length. Look for the request with a shorter response length, indicating a successful login attempt.
    
9. To confirm the successful login attempt, use the credentials from the request with the shorter response length to log in.

## Extra Mile Challenge

1. Navigate to `http://10.201.47.96/admin/login/`. Activate **Intercept** in the Proxy module and attempt to log in. Capture the request and send it to Intruder.
    
2. Configure the positions the same way as we did for brute-forcing the support login:
    
    - Set the attack type to "Pitchfork".
    - Clear all predefined positions and select only the username and password form fields. Our macro will handle the other two positions.
        
    
    ![Showing the predefined positions](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/cdade963a8004b0d9da03e075a60f3aa.png)
    
3. Now switch over to the Payloads tab and load in the same username and password wordlists we used for the support login attack.
    
    Up until this point, we have configured Intruder in almost the same way as our previous credential stuffing attack; this is where things start to get more complicated.
    
4. With the username and password parameters handled, we now need to find a way to grab the ever-changing loginToken and session cookie. Unfortunately, "recursive grep" won't work here due to the redirect response, so we can't do this entirely within Intruder – we will need to build a macro.
    
    Macros allow us to perform the same set of actions repeatedly. In this case, we simply want to send a GET request to `/admin/login/`.
    
    Fortunately, setting this up is a straightforward process.
    
    - Switch over to the main "Settings" tab at the top-right of Burp.
    - Click on the "Sessions" category.
    - Scroll down to the bottom of the category to the "Macros" section and click the **Add** button.
    - The menu that appears will show us our request history. If there isn't a GET request to `http://10.201.47.96/admin/login/` in the list already, navigate to this location in your browser, and you should see a suitable request appear in the list.
    - With the request selected, click **OK**.
    - Finally, give the macro a suitable name, then click **OK** again to finish the process.
    
    There are a lot of steps here, comparatively speaking, so the following GIF shows the entire process:
    
    ![Process showing the addition of the macro](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/3b370cfce8a050faf415c7d9a5a8227e.gif)
    
5. Now that we have a macro defined, we need to set Session Handling rules that define how the macro should be used.
    
    - Still in the "Sessions" category of the main settings, scroll up to the "Session Handling Rules" section and choose to **Add** a new rule.
    - A new window will pop up with two tabs in it: "Details" and "Scope". We are in the Details tab by default.
        
    
    ![Window showing the details and scope](https://assets.muirlandoracle.co.uk/thm/modules/burp/38ceffeebf99.png)
    
    - Fill in an appropriate description, then switch to the Scope tab.
    - In the "Tools Scope" section, deselect every checkbox other than Intruder – we do not need this rule to apply anywhere else.
    - In the "URL Scope" section, choose "Use suite scope"; this will set the macro to only operate on sites that have been added to the global scope (as was discussed in [Burp Basics](https://tryhackme.com/room/burpsuitebasics)). If you have not set a global scope, keep the "Use custom scope" option as default and add `http://10.201.47.96/` to the scope in this section.
        
        ![Change the URL scope](https://assets.muirlandoracle.co.uk/thm/modules/burp/4d3fc6d19a12.png)
        
6. Now we need to switch back over to the Details tab and look at the "Rule Actions" section.
    
    - Click the **Add** button – this will cause a dropdown menu to appear with a list of actions we can add.
    - Select "Run a Macro" from this list.
    - In the new window that appears, select the macro we created earlier.
        
    
    As it stands, this macro will now overwrite all of the parameters in our Intruder requests before we send them; this is great, as it means that we will get the loginTokens and session cookies added straight into our requests. That said, we should restrict which parameters and cookies are being updated before we start our attack:
    
    - Select "Update only the following parameters and headers", then click the **Edit** button next to the input box below the radio button.
    - In the "Enter a new item" text field, type "loginToken". Press **Add**, then **Close**.
    - Select "Update only the following cookies", then click the relevant **Edit** button.
    - Enter "session" in the "Enter a new item" text field. Press **Add**, then **Close**.
    - Finally, press **OK** to confirm our action.
        
    
    The following GIF demonstrates this final stage of the process:
    
    ![Showing the added macro](https://tryhackme-images.s3.amazonaws.com/user-uploads/645b19f5d5848d004ab9c9e2/room-content/250c140897e3b470093e7232c70c07cf.gif)
    
7. Click **OK**, and we're done!
    
8. You should now have a macro defined that will substitute in the CSRF token and session cookie. All that's left to do is switch back to Intruder and start the attack!
    
    **Note:** You should be getting 302 status code responses for every request in this attack. If you see 403 errors, then your macro is not working properly.
    
1. As with the support login credential stuffing attack we carried out, the response codes here are all the same (302 Redirects). Once again, order your responses by length to find the valid credentials. Your results won't be quite as clear-cut as last time – you will see quite a few different response lengths: however, the response that indicates a successful login should still stand out as being significantly shorter.


