**Resources/Tools Used:**

**[Task 1] Pickle Rick**

- gobuster
- [http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
- Netcat

This Ricky and Morty themed challenge requires you to exploit a webserver to find three ingredients that will help Rick make his potion to transform himself back into a human from a pickle.

**#1 This subtask requires you to find first ingredient.**

First ingredient was found by following these steps:

- Browsed to webpage.

![](https://stawm.design.blog/wp-content/uploads/2020/05/webpage-1.png?w=1024)

Webpage

- Reviewed the source of this page that gave a username “R1ckRul3s”.

![](https://stawm.design.blog/wp-content/uploads/2020/05/webpage-source-1.png?w=1024)

Username discovered

- Browsed to “robots.txt” file and found one interesting piece of information there.

![](https://stawm.design.blog/wp-content/uploads/2020/05/robots-txt-file-updated.png?w=475)

Robots file

- Used gobuster to brute force directories to discover directories and pages on this website. Gobuster discovered few interesting pages.

![](https://stawm.design.blog/wp-content/uploads/2020/05/gobuter-disvoerd-directories.png?w=1024)

gobuster output

- Browsed to “login.php” and found a login page asking for a username and password. Tried information gathered in previous steps to login to this portal.

![](https://stawm.design.blog/wp-content/uploads/2020/05/login-page.png?w=1024)

login.php

![](https://stawm.design.blog/wp-content/uploads/2020/05/login-page-creds.png?w=1024)

Credentials

![](https://stawm.design.blog/wp-content/uploads/2020/05/login-page-success.png?w=1024)

Login successful

- Tried listing the contents of directory.

![](https://stawm.design.blog/wp-content/uploads/2020/05/ls-al.png?w=623)

Directory listing

- Saw an interesting file “Sup3rS3cretPickl3Ingred.txt” but could not read contents of the file (using cat) as this functionality was disabled on the server.

![](https://stawm.design.blog/wp-content/uploads/2020/05/cat-1.png?w=631)

Tru to read file

![](https://stawm.design.blog/wp-content/uploads/2020/05/cat-command-diabled.png?w=663)

cat disabled

- As this was a very restrictive environment, tried getting a reverse shell from the server. First tried to identify if python (python2 was not available) is available on the server.

![](https://stawm.design.blog/wp-content/uploads/2020/05/00-which-pyhton3.png?w=1024)

python3 check

![](https://stawm.design.blog/wp-content/uploads/2020/05/which-pyhton3.png?w=1024)

python3 available

- We had python3 available on the server. Used pentestmonkey cheat sheet for python reverse shell. Started a netcat listener on port 4444 and copied the command and changed IP and port to reflect our attack machine IP and local port (running netcat).

![](https://stawm.design.blog/wp-content/uploads/2020/05/pentestmonkey.png?w=1024)

Python reverse shell from penestmonkey website

![](https://stawm.design.blog/wp-content/uploads/2020/05/reverse-shell-command.png?w=1024)

Python reverse shell command

![](https://stawm.design.blog/wp-content/uploads/2020/05/sarted-nc-listerner.png?w=349)

Netcat listener

- Upon executing the python reverse shell command immediately got the shell with user “www-data” authority from system.

![](https://stawm.design.blog/wp-content/uploads/2020/05/reverse-shell.png?w=1024)

Reverse shell

- From this folder got first ingredient.

![](https://stawm.design.blog/wp-content/uploads/2020/05/1-1-ingredient-1-updated.png?w=366)

First ingredient

- From this folder read the file “clue.txt” to see contents of the file for remaining ingredients.

![](https://stawm.design.blog/wp-content/uploads/2020/05/clue.txt_.png?w=533)

Clue.txt

**#2 This subtask requires you to find second ingredient.**

- Browsed to “/home/rick” folder to get the second ingredient.

![](https://stawm.design.blog/wp-content/uploads/2020/05/1-2-ingreient-2-updated.png?w=609)

Second ingredient

**#3 This subtask requires you to find third ingredient.**

- Tried accessing “/root” folder but access was denied to our current user (www-data).

![](https://stawm.design.blog/wp-content/uploads/2020/05/root-access-denied.png?w=375)

root folder inaccessible

- For privilege escalation tried to identify what commands are allowed to current user with root privileges and to our surprise all commands were allowed without any password.

![](https://stawm.design.blog/wp-content/uploads/2020/05/sudo-l-1.png?w=951)

sudo -l

- Ran “sudo bash -i” to get root access to system.

![](https://stawm.design.blog/wp-content/uploads/2020/05/root-access-1.png?w=792)

root access

- Browsed to “/root” folder to get the third and last ingredient.

![](https://stawm.design.blog/wp-content/uploads/2020/05/1-3-ingredient-3-updated.png?w=451)

Third and last ingredient