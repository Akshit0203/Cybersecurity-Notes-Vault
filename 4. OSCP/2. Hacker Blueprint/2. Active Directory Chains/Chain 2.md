
KEEP MAKING REPORT OF ALL STEPS
AND KEEP TAKING AS MANY SCREENSHOTS AS YOU CAN

KEEP A MAIN NOTE OF ALL THE CREDENTIALS YOU KEEP GETTING 
Format :
```
ip1
ip2
ip3

domain name 

initial username
initial password

new user
new pass
```

----

add all the three ips to /etc/hosts
```
sudo nano /etc/hosts
```
paste :
```
ip1 <DOMAIN NAME>
ip2 <DOMAIN NAME>
ip3 <DOMAIN NAME>
```

-----

password spray initial creds for all 3 ips 
for both winrm and rdp login

----

collect data for bloodhound 
run bloodhound

mark initial access user as owned
queries : 
1. see all domain admins
2. all kerberoastable users
3. as-rep roastable users

----

do Authenticated LDAP enumeration to find out users

--------

do as-rep roasting
crack hash

---

password spray the new username and passwords for all 3 ips 
for both winrm and rdp login

----

login to user
run powerup

----

Look for services which have

ModifiableFilePermissions : Write attributes
start name : local system

if you have 
seshutdown privilege

you can replace the service binary with something malicious and restart the machine


start type = demand start
service_start_name = local system

```
sc.exe qc <service name>
```

try to start
```
sc.exe start <service name> 
```
see if you have permissions or not


see if we can replace the service binary with our reverse shell 

```
copy .\reverseshell.exe C:<binary path>\keep original.exe name only in last
```

enumerate the service more 

```
sc.exe qc "service name"
```

```
START_TYPE = autostart
```
that means the service will auto start on startup , so we restart the machine
in powershell : 
```
restart-computer
```

remeber to keep listener running to get reverse shell

-----

now we can dump hashes 


```
net localgroup administrators <USERNAME> /add
```

after you dump hashesh of one machine , 

then move on to other lcient id you have the login creds of 

then dump that mahcine hashes 

then next one 

THEN PASSWORD SPRAY ON EVERY IP using smb first