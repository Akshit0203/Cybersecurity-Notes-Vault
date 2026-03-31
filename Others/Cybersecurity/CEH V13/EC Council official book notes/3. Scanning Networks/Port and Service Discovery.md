# TCP Connect/Full-Open Scan 

TCP Connect/Full Open Scan is one of the most reliable forms of TCP scanning. In TCP Connect scanning, the OS’s TCP connect() system call tries to open a connection to every port of interest on the target machine. If the port is listening, the connect() call will result in a successful connection with the host on that particular port; otherwise, it will return an error message stating that the port is not reachable.

TCP Connect scan completes a three-way handshake with the target machine. In the TCP three-way handshake, the client sends a SYN packet, which the recipient acknowledges with a SYN+ACK packet. Then, the client acknowledges the SYN+ACK packet with an ACK packet to complete the connection. Once the handshake is completed, the scanner sends an RST packet to end the connection.

![image1](../../../attachments/16b90bc76d58489999c2c7e386c61cde.png)

# Stealth Scan (Half-Open Scan) 

The stealth scan involves resetting the TCP connection between the client and the server abruptly before completion of the three-way handshake signals, hence making the connection half-open. A stealth scan sends a single frame to a TCP port without any TCP handshaking or additional packet transfers. This type of scan sends a single frame with the expectation of a single response. The half-open scan partially opens a connection but stops halfway through. The stealth scan is also called a “SYN scan,” because it only sends the SYN packet. This prevents the service from notifying the incoming connection. TCP SYN or half-open scanning is a stealth method of port scanning.

![image2](../../../attachments/6dc762aab4e14c789e2ea49c59dc486d.png)

![image3](../../../attachments/cc0f4819a447415db113cf9aad5cbd77.png)

# Xmas Scan 

Xmas scan is a type of inverse TCP scanning technique with the FIN, URG, and PUSH flags set to send a TCP frame to a remote device. If the target has opened the port, then you will receive no response from the remote system. If the target has closed the port, then you will receive a remote system reply with an RST.

![image4](../../../attachments/fa4937c516814cf69aeaf5a58a0360c8.png)

![image5](../../../attachments/a1a4b79925c742caa9f1d28c16049fa7.png)

# TCP Maimon Scan

the probe used here is FIN/ACK. In most cases, to determine if the port is open or closed, the RST packet should be generated as a response to a probe request. However, in many BSD systems, the port is open if the packet gets dropped in response to a probe.

![image6](../../../attachments/1a23d5539f8748858704ec99dbbad461.png)

# ACK Flag Probe Scan 

![image7](../../../attachments/6a00176ea49343a4a24518667c36a81a.png)

# IDLE/IPID Header Scan

The IDLE/IPID header scan is a TCP port scan method that can be used to send a spoofed source address to a computer to determine what services are available. It offers the complete blind scanning of a remote host.

IDLE Scan
▪ Step 1
Choose a “Zombie” and Probe Its Current IP Identification (IPID) Number
The first step in an idle scan is to determine an appropriate zombie.

In the first step, the SYN+ACK packet is sent to the zombie machine to probe its IPID number. Here, the SYN+ACK packet is sent to probe the IPID number and not to establish a TCP connection (three-way handshake).

![image8](../../../attachments/3b355e4eaa4a41f8b544ba5083593c11.png)

![image9](../../../attachments/2581a3a785864e9bbafb6ec9e3c397d1.png)

![image10](../../../attachments/0ca99c6b3cd9422ea5563891970f82d1.png)

![image11](../../../attachments/2162c491f281479d8cf37629cda906ed.png)

![image12](../../../attachments/2e2f08a1c8b346a68f7e5856597fbe36.png)

![image13](../../../attachments/5f7443c388eb4324ad16f8960aae03df.png)

![image14](../../../attachments/ba96d6312e2f45778f1237a00f6bb2ac.png)

![image15](../../../attachments/fbc9cf8a16c047a181c86ff3908194ce.png)

![image16](../../../attachments/a93b2909a3d545d78b078115e3e67ce5.png)

![image17](../../../attachments/46c2478a98fa434781215db0bf69db9b.png)

![image18](../../../attachments/08272e4279704dc0af368b68d3e0e12d.png)

# Port Scanning with AI 

![image19](../../../attachments/567eb085d53a41b68e452c4cd9c1f15a.png)

![image20](../../../attachments/3cc8043d27434e0c8e9863b07ec79459.png)

![image21](../../../attachments/2bea53966b534f79814b48cb1d7b7182.png)

![image22](../../../attachments/f773e8664bab4dc7b32f8e51873d78e2.png)

![image23](../../../attachments/e2ad714269354e2085a93d7b0bf2e8fa.png)

![image24](../../../attachments/221617b3e38146dbb558f64db4b70185.png)

![image25](../../../attachments/d78293c3f8c14e5ea823065ee77d3b50.png)

![image26](../../../attachments/8b59ed7602344af9a7c38a2d7eba5968.png)

# Service Version Discovery 

The version detection technique is nothing but examination of the TCP and UDP ports. The probes from the Nmap service-probes database are used for querying various services and matching expressions for recognizing and parsing responses. In Zenmap, the -sV option is used to detect service versions.

![image27](../../../attachments/be82774ade1c458188b5db10f62b7f5f.png)

# Service Version Discovery with AI 

![image28](../../../attachments/2cd910ff9176480a8122c8f558821a04.png)

![image29](../../../attachments/4708884ec6d64d2788b510b548be5dd9.png)

