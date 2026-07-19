## Telnet

The Telnet protocol is an application layer protocol used to connect to a virtual terminal of another computer.

When a user connects, they will be asked for a username and password. Upon correct authentication, the user will access the remote system’s terminal. Unfortunately, all this communication between the Telnet client and the Telnet server is not encrypted, making it an easy target for attackers.

A Telnet server uses the Telnet protocol to listen for incoming connections on port 23.

```
pentester@TryHackMe$ telnet 10.10.101.115
bento login: frank
Password: D2xc9CgD
frank@bento:~$
```

it is not a reliable protocol for remote administration as all the data are sent in cleartext.

## Hypertext Transfer Protocol (HTTP)

Hypertext Transfer Protocol (HTTP) is the protocol used to transfer web pages. Your web browser connects to the webserver and uses HTTP to request HTML pages and images among other files and submit forms and upload various files. Anytime you browse the World Wide Web (WWW), you are certainly using the HTTP protocol.

The image below shows a client requesting the HTML page `index.html`, which the webserver provides. Then the client requests an image, `logo.jpg`, and the web server sends it.

![Pasted image 20250725081113.png](attachments/Pasted%20image%2020250725081113.png)

HTTP sends and receives data as cleartext (not encrypted); therefore, you can use a simple tool, such as Telnet (or Netcat), to communicate with a web server and act as a “web browser”. The key difference is that you need to input the HTTP-related commands instead of the web browser doing that for you.

1. First, we connect to port 80 using `telnet MACHINE_IP 80`.
2. Next, we need to type `GET /index.html HTTP/1.1` to retrieve the page `index.html` or `GET / HTTP/1.1` to retrieve the default page.
3. Finally, you need to provide some value for the host like `host: telnet` and press the Enter/Return key **twice**.

In the console output below, we could recover the requested page along with a trove of information not usually displayed by the web browser. If the page we requested is not found, we get error 404.

```shell-session
pentester@TryHackMe$ telnet 10.10.20.242 80
Trying 10.10.20.242...
Connected to 10.10.20.242.
Escape character is '^]'.
GET /index.html HTTP/1.1
host: telnet

HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Wed, 15 Sep 2021 08:56:20 GMT
Content-Type: text/html
Content-Length: 234
Last-Modified: Wed, 15 Sep 2021 08:53:59 GMT
Connection: keep-alive
ETag: "6141b4a7-ea"
Accept-Ranges: bytes

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Welcome to my Web Server</title>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
</head>
<body>
  <h1>Coming Soon<h1>
</body>
</html>
```

Of particular interest in the output above is that the user needs only to type a couple of commands to get the page they need: `GET /index.html HTTP/1.1` followed by `host: telnet`.

## File Transfer Protocol (FTP)

File Transfer Protocol (FTP) was developed to make the transfer of files between different computers with different systems efficient.

FTP also sends and receives data as cleartext; therefore, we can use Telnet (or Netcat) to communicate with an FTP server and act as an FTP client. In the example below, we carried out the following steps:

1. We connected to an FTP server using a Telnet client. Since FTP servers listen on port 21 by default, we had to specify to our Telnet client to attempt connection to port 21 instead of the default Telnet port.
2. We needed to provide the username with the command `USER frank`.
3. Then, we provided the password with the command `PASS D2xc9CgD`.
4. Because we supplied the correct username and password, we got logged in.

A command like `STAT` can provide some added information. The `SYST` command shows the System Type of the target (UNIX in this case). `PASV` switches the mode to passive. It is worth noting that there are two modes for FTP:

- Active: In the active mode, the data is sent over a separate channel originating from the FTP server’s port 20.
- Passive: In the passive mode, the data is sent over a separate channel originating from an FTP client’s port above port number 1023.

The command `TYPE A` switches the file transfer mode to ASCII, while `TYPE I` switches the file transfer mode to binary. However, we cannot transfer a file using a simple client such as Telnet because FTP creates a separate connection for file transfer.

```shell-session
pentester@TryHackMe$ telnet 10.10.12.160 21
Trying 10.10.12.160...
Connected to 10.10.12.160.
Escape character is '^]'.
220 (vsFTPd 3.0.3)
USER frank
331 Please specify the password.
PASS D2xc9CgD
230 Login successful.
SYST
215 UNIX Type: L8
PASV
227 Entering Passive Mode (10,10,0,148,78,223).
TYPE A
200 Switching to ASCII mode.
STAT          
211-FTP server status:
     Connected to ::ffff:10.10.0.1
     Logged in as frank
     TYPE: ASCII
     No session bandwidth limit
     Session timeout in seconds is 300
     Control connection is plain text
     Data connections will be plain text
     At session startup, client count was 1
     vsFTPd 3.0.3 - secure, fast, stable
211 End of status
QUIT
221 Goodbye.
Connection closed by foreign host.
```

Considering the sophistication of the data transfer over FTP, let’s use an actual FTP client to download a text file. We only needed a small number of commands to retrieve the file. After logging in successfully, we get the FTP prompt, `ftp>`, to execute various FTP commands. We used `ls` to list the files and learn the file name; then, we switched to `ascii` since it is a text file (not binary). Finally, `get FILENAME` made the client and server establish another channel for file transfer.

```shell-session
pentester@TryHackMe$ ftp 10.10.12.160
Connected to 10.10.12.160.
220 (vsFTPd 3.0.3)
Name: frank
331 Please specify the password.
Password: D2xc9CgD
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
227 Entering Passive Mode (10,20,30,148,201,180).
150 Here comes the directory listing.
-rw-rw-r--    1 1001     1001         4006 Sep 15 10:27 README.txt
226 Directory send OK.
ftp> ascii
200 Switching to ASCII mode.
ftp> get README.txt
local: README.txt remote: README.txt
227 Entering Passive Mode (10,10,0,148,125,55).
150 Opening BINARY mode data connection for README.txt (4006 bytes).
WARNING! 9 bare linefeeds received in ASCII mode
File may not have transferred correctly.
226 Transfer complete.
4006 bytes received in 0.000269 secs (14892.19 Kbytes/sec)
ftp> exit
221 Goodbye.
```



## Simple Mail Transfer Protocol (SMTP)

Email delivery over the Internet requires the following components:

1. Mail Submission Agent (MSA)
2. Mail Transfer Agent (MTA)
3. Mail Delivery Agent (MDA)
4. Mail User Agent (MUA)

The above four terms may look cryptic, but they are more straightforward than they appear. We will explain these terms using the figure below.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/822a449fd569c16c875a13ca2487b714.png)

The figure shows the following five steps that an email needs to go through to reach the recipient’s inbox:
1. A Mail User Agent (MUA), or simply an email client, has an email message to be sent. The MUA connects to a Mail Submission Agent (MSA) to send its message.
2. The MSA receives the message, checks for any errors before transferring it to the Mail Transfer Agent (MTA) server, commonly hosted on the same server.
3. The MTA will send the email message to the MTA of the recipient. The MTA can also function as a Mail Submission Agent (MSA).
4. A typical setup would have the MTA server also functioning as a Mail Delivery Agent (MDA).
5. The recipient will collect its email from the MDA using their email client.

SMTP server listens on port 25 by default. To see basic communication with an SMTP server, we used Telnet to connect to it. Once connected, we issue `helo hostname` and then start typing our email.

```shell-session
pentester@TryHackMe$ telnet 10.10.34.35 25
```

## Post Office Protocol 3 (POP3)

Post Office Protocol version 3 (POP3) is a protocol used to download the email messages from a Mail Delivery Agent (MDA) server, as shown in the figure below. The mail client connects to the POP3 server, authenticates, downloads the new email messages before (optionally) deleting them.

![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5f04259cf9bf5b57aed2c476/room-content/ed910ad418376edc846846fc2a0dd3f6.png)

The example below shows what a POP3 session would look like if conducted via a Telnet client. First, the user connects to the POP3 server at the POP3 default port 110. Authentication is required to access the email messages; the user authenticates by providing his username `USER frank` and password `PASS D2xc9CgD`. Using the command `STAT`, we get the reply `+OK 1 179`; based on [RFC 1939](https://datatracker.ietf.org/doc/html/rfc1939), a positive response to `STAT` has the format `+OK nn mm`, where _nn_ is the number of email messages in the inbox, and _mm_ is the size of the inbox in octets (byte). The command `LIST` provided a list of new messages on the server, and `RETR 1` retrieved the first message in the list. We don’t need to concern ourselves with memorizing these commands; however, it is helpful to strengthen our understanding of such protocol.

```shell-session
pentester@TryHackMe$ telnet 10.10.34.35 110
Trying 10.10.34.35...
Connected to 10.10.34.35.
Escape character is '^]'.
+OK 10.10.34.35 Mail Server POP3 Wed, 15 Sep 2021 11:05:34 +0300 
USER frank
+OK frank
PASS D2xc9CgD
+OK 1 messages (179) octets
STAT
+OK 1 179
LIST
+OK 1 messages (179) octets
1 179
.
RETR 1
+OK
From: Mail Server 
To: Frank 
subject: Sending email with Telnet
Hello Frank,
I am just writing to say hi!
.
QUIT
+OK 10.10.34.35 closing connection
Connection closed by foreign host.
```

The example above shows that the commands are sent in cleartext. Using Telnet was enough to authenticate and retrieve an email message. As the username and password are sent in cleartext, any third party watching the network traffic can steal the login credentials.

In general, your mail client (MUA) will connect to the POP3 server (MDA), authenticate, and download the messages. Although the communication using the POP3 protocol will be hidden behind a sleek interface, similar commands will be issued, as shown in the Telnet session above.

Based on the default settings, the mail client deletes the mail message after it downloads it. The default behaviour can be changed from the mail client settings if you wish to download the emails again from another mail client. Accessing the same mail account via multiple clients using POP3 is usually not very convenient as one would lose track of read and unread messages. To keep all mailboxes synchronized, we need to consider other protocols, such as IMAP.

## Internet Message Access Protocol (IMAP)

Internet Message Access Protocol (IMAP) is more sophisticated than POP3. IMAP makes it possible to keep your email synchronized across multiple devices (and mail clients). In other words, if you mark an email message as read when checking your email on your smartphone, the change will be saved on the IMAP server (MDA) and replicated on your laptop when you synchronize your inbox.

Let’s take a look at sample IMAP commands. In the console output below, we use Telnet to connect to the IMAP server’s default port, and then we authenticate using `LOGIN username password`. IMAP requires each command to be preceded by a random string to be able to track the reply. So we added `c1`, then `c2`, and so on. Then we listed our mail folders using `LIST "" "*"`, before checking if we have any new messages in the inbox using `EXAMINE INBOX`. We don’t need to memorize these commands; however, we are simply providing the example below to give a vivid image of what happens when the mail client communicates with an IMAP server.

```shell-session
pentester@TryHackMe$ telnet 10.10.34.35 143
Trying 10.10.34.35...
Connected to 10.10.34.35.
Escape character is '^]'.
* OK [CAPABILITY IMAP4rev1 UIDPLUS CHILDREN NAMESPACE THREAD=ORDEREDSUBJECT THREAD=REFERENCES SORT QUOTA IDLE ACL ACL2=UNION STARTTLS ENABLE UTF8=ACCEPT] Courier-IMAP ready. Copyright 1998-2018 Double Precision, Inc.  See COPYING for distribution information.
c1 LOGIN frank D2xc9CgD
* OK [ALERT] Filesystem notification initialization error -- contact your mail administrator (check for configuration errors with the FAM/Gamin library)
c1 OK LOGIN Ok.
c2 LIST "" "*"
* LIST (\HasNoChildren) "." "INBOX.Trash"
* LIST (\HasNoChildren) "." "INBOX.Drafts"
* LIST (\HasNoChildren) "." "INBOX.Templates"
* LIST (\HasNoChildren) "." "INBOX.Sent"
* LIST (\Unmarked \HasChildren) "." "INBOX"
c2 OK LIST completed
c3 EXAMINE INBOX
* FLAGS (\Draft \Answered \Flagged \Deleted \Seen \Recent)
* OK [PERMANENTFLAGS ()] No permanent flags permitted
* 0 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 631694851] Ok
* OK [MYRIGHTS "acdilrsw"] ACL
c3 OK [READ-ONLY] Ok
c4 LOGOUT
* BYE Courier-IMAP server shutting down
c4 OK LOGOUT completed
Connection closed by foreign host.
```

It is clear that IMAP sends the login credentials in cleartext, as we can see in the command `LOGIN frank D2xc9CgD`. Anyone watching the network traffic would be able to know Frank’s username and password.

## Summary 

| Protocol | TCP Port | Application(s) | Data Security |
| -------- | -------- | -------------- | ------------- |
| FTP      | 21       | File Transfer  | Cleartext     |
| HTTP     | 80       | Worldwide Web  | Cleartext     |
| IMAP     | 143      | Email (MDA)    | Cleartext     |
| POP3     | 110      | Email (MDA)    | Cleartext     |
| SMTP     | 25       | Email (MTA)    | Cleartext     |
| Telnet   | 23       | Remote Access  | Cleartext     |
