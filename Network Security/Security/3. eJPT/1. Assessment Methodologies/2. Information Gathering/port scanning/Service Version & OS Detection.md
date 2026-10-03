```
nmap -T4 -sS -sV -p- demo.ine.local
```
"-sV" for version detection

```
nmap -T4 -sS -sV --version-intensity 8 -O --osscan-guess -p- demo.ine.local
```
"--version-intensity 8" for increasing the aggressiveness of service version detection , 8 being highest level

```
nmap -T4 -sS -sV -O -p- demo.ine.local
```
"-O" for operating system detection

```
nmap -T4 -sS -sV -O --osscan-guess -p- demo.ine.local
```
"-osscan-guess" for aggressive OS scan



