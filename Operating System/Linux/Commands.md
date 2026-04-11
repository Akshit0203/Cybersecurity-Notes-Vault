## Where Am I?

 `pwd`

```shell-session
ubuntu@tryhackme:~$ pwd
/home/ubuntu
```

It stands for "print working directory", which basically means "show me the folder I'm currently in".

## What's Around Me?

 `ls`

```shell-session
ubuntu@tryhackme:~$ ls
Desktop    Downloads  Pictures  Templates  logsDocuments  Music      Public    Videos     projects
```

This lists the content of the current directory. If we need more details, we can try: `ls -l`

ls -l Command

```shell-session
ubuntu@tryhackme:~$ ls -l
total 44
drwxr-xr-x 2 ubuntu ubuntu 4096 Feb 27  2022 Desktop
drwxr-xr-x 6 ubuntu ubuntu 4096 Dec 11 12:45 Documents
drwxr-xr-x 2 ubuntu ubuntu 4096 Feb 16  2024 Downloads
```

The output displays important information about the files and directories like file sizes, permissions, dates, and more.

**Hidden Files**

In order to get the hidden files in the directory, we can append the command to `ls -al`, and it will display all the hidden files present in the directory, as shown below:

```shell-session
ubuntu@tryhackme:~$ ls -al
total 144
drwxr-xr-x 24 ubuntu ubuntu  4096 Feb 10 10:48 .
drwxr-xr-x  3 root   root    4096 Feb 10 10:36 ..
-rw-------  1 ubuntu ubuntu   439 Feb 10 06:47 .Xauthority
-rw-rw-r--  1 ubuntu ubuntu     0 Sep 12  2024 .Xresources
```

Hidden files aren't really `secret`; they start with a dot `.`, and Linux hides such files by default.

