```
find / -name "flag"
```

Flag might be available in `/opt/apache/htdocs` , also check root dir always.



- look for flags in config folder, also search for all the files that has name flag, can be any case.
- Don't try single exploit. Even time consuming, try all the exploits.
- Whenever you got access to linux target machine, always check root directory, / directory as well as check the cronjobs.


`C:\Windows\system32>dir C:\Windows\System32\*.txt /s /b`
This cmd will find all files that end with 'flag'.


![[Pasted image 20250811052557.png]]


**File searching using keyword in meterpreter**:
`meterpreter> search -d /usr/bin -f *ckdo*` --> to search for file that has 'ckdo'.


