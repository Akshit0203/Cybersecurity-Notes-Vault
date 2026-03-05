`ip a s` --> used to identify ip address

![[Pasted image 20250528120510.png]]


---

`curl -v <url>` --> to make a simple request to the url and verbose.

`curl -I <url>` --> will make request and return only the headers.

`curl -v -X OPTIONS <url>` --> used to specify a header.

If the web application has a upload endpoints url. Try to use OPTIONS in header and check what are the methods available. If it has post , delete etc. You can try to upload a webshell there.

`curl <url> --upload-file webshell.php` --> upload a file to the server.

To delete a file, the server must allow DELETE method in its "allow methods".
`DELETE /uploads/webshell.php` --> send a request a burp, to delete a file.




