![image1](../../../attachments/b2dddc766ba94d4a99b71e8f79cd4799.png)

# Port Scanning Countermeasures 

▪ Configure firewall and intrusion detection system (IDS) rules to detect and block probes. ▪ The firewall should be capable of detecting the probes sent by attackers using port-scanning tools. It should not allow traffic to pass through after simply inspecting the TCP header. The firewall should be able to examine the data contained in each packet before allowing traffic to pass through it.
▪ Run the port scanning tools against hosts on the network to determine whether the firewall accurately detects the port scanning activity.
▪ Ensure that the router, IDS, and firewall firmware are updated with their latest releases/versions.
▪ Configure commercial firewalls to protect the network against fast port scans and SYN floods.
▪ Hackers use tools such as Nmap and perform OS detection to sniff the details of a remote OS. Thus, it is important to employ an IDS in such cases. Snort (<https://www.snort.org>) is a very useful intrusion detection and prevention technology, mainly because signatures are frequently available from public authors.
▪ Keep as few ports open as possible and filter the rest, as an intruder may attempt to enter through any open port. Use a custom rule set to lock down the network, block unwanted ports at the firewall, and filter the following ports: 135–159, 256–258, 389, 445, 1080, 1745, and 3268.
▪ Block unwanted services running on the ports and update the service versions. ▪ Ensure that the versions of services running on the ports are non-vulnerable. ▪ Block inbound ICMP message types and all outbound ICMP type-3 unreachable messages at border routers arranged in front of the company’s main firewall.
▪ Attackers attempt to perform source routing and send packets to the targets, which may not be reachable via the Internet, using an intermediate host that can interact with the target. Hence, it is necessary to ensure that the firewall and router can block such source-routing techniques.
▪ Ensure that the mechanisms used for routing and filtering at the routers and firewalls, respectively, cannot be bypassed using a particular source port or source routing methods.
![image2](../../../attachments/622ec277e51a4b80ae7132a3b551bdb3.png)

# Banner Grabbing Countermeasures 

![image3](../../../attachments/3f756b43d3f14aea8f4839ef2f87df15.png)

![image4](../../../attachments/e1cec97af15e48949f1085690595dfba.png)

![image5](../../../attachments/18ec7b6f11bb40f9a7c8892c9d81f793.png)

# IP Spoofing Countermeasures 

![image6](../../../attachments/c597524b06a84077b7e5c3a56187b838.png)

![image7](../../../attachments/9e9d220889194ef18b84b84125dadc77.png)

# Scanning Detection and Prevention Tools 

![image8](../../../attachments/c840645bc9574cd0875697b48d3bceb7.png)

