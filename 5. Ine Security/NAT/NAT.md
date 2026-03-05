![](attachments/INE-Essentials-of-Network-Address-Translation-NAT-Course-File%201.pdf)

Why NAT ?
1. save money by not needing to buy so many public ips
2. ipv4 total number is limited , so to save/reserve them
3. useful security mechanism, -> outside people cannot communicate with internal network

Types of NAT
1. Static NAT
internal ip address is static address and does not change
ex. server that never moves - map it to an inside global address
it will be mapped to a specific nat route , so that the ip doesnt change
2. Dynamic NAT
I have pool of public address which my internal ips can be translated to
ex. first come first serve
we cannot thus predict which public address will be given
3. NAT Overloading
ex. home router 
traffic appears to be coming from just 1 ip
but it is actually coming from different clients
