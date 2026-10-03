## Robots.txt

The robots.txt file is a document that tells search engines which pages they are and aren't allowed to show on their search engine results or ban specific search engines from crawling the website altogether. It can be common practice to restrict certain website areas so they aren't displayed in search engine results.

 http://10.10.134.30/robots.txt

## Favicon

The favicon is a small icon displayed in the browser's address bar or tab used for branding a website.

  

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/42a556740d021fc3e7111a689dcadb28.png)

  

Sometimes when frameworks are used to build a website, a favicon that is part of the installation gets leftover, and if the website developer doesn't replace this with a custom one, this can give us a clue on what framework is in use. OWASP host a database of common framework icons that you can use to check against the targets favicon [https://wiki.owasp.org/index.php/OWASP_favicon_database](https://wiki.owasp.org/index.php/OWASP_favicon_database).

Viewing the page source you'll see line six contains a link to the images/favicon.ico file. 

  

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5efe36fb68daf465530ca761/room-content/1f1217249bf0edf74c8e6d0ba58bbc58.png)  

  

If you run the following command on the AttackBox, it will download the favicon and get its md5 hash value which you can then lookup on the  
[https://wiki.owasp.org/index.php/OWASP_favicon_database](https://wiki.owasp.org/index.php/OWASP_favicon_database).

```shell-session
user@machine$ curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum
```


## Sitemap.xml (opposite of robots.txt)

sitemap.xml file gives a list of every file the website owner wishes to be listed on a search engine.

 http://10.10.134.30/sitemap.xml
## HTTP Headers

When we make requests to the web server, the server returns various HTTP headers.

```
curl http://10.10.134.30 -v
```

## Automated Discovery (important , All-in-one)

**Using ffuf:**

```shell-session
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.134.30/FUZZ
```

**Using dirb:**

```shell-session
dirb http://10.10.134.30/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```

**Using Gobuster:**

```shell-session
gobuster dir --url http://10.10.134.30/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```