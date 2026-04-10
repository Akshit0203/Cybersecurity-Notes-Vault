![image1](../../../attachments/cb5b0eb20815411c9ed755d156eb4c97.png)

# Packet Fragmentation
Packet fragmentation refers to the splitting of a probe packet into several smaller packets (fragments) while sending it to a network. When these packets reach a host, the IDS and firewalls behind the host generally queue all of them and process them one by one. However, since this method of processing involves greater CPU and network resource consumption, the configuration of most IDS cause them to skip fragmented packets during port scans.

![image2](../../../attachments/b86a0917e107451183fb3d2208d41235.png)

# Source Routing 

![image3](../../../attachments/8957f6faff1f4629a10196c12f055d03.png)

![image4](../../../attachments/0b16995373d34a39854f081244758d92.png)

# IP Address Decoy 

The IP address decoy technique refers to generating or manually specifying IP addresses of the decoys to evade IDS/firewalls. It appears to the target that the decoys as well as the host(s) are scanning the network. This technique makes it difficult for the IDS/firewall to determine which IP address is actually scanning the network and which IP addresses are decoys

![image5](../../../attachments/d7bf9f3d37a648d596fbc0c101b175bd.png)

![image6](../../../attachments/e679308d897843f3bb6ddd321665e98e.png)

![image7](../../../attachments/df45d2afe2f94d72a6372f40a3c6c734.png)

![image8](../../../attachments/d8a268b6437f435c9a5613fdb2d33bb4.png)

![image9](../../../attachments/55c0a47333604dc7bb55293d2981d4d4.png)

# MAC Address Spoofing 

![image10](../../../attachments/ccc738f0bde3455eba347473633e7709.png)

![image11](../../../attachments/09c29b10b7b443218bc36d34baf84268.png)

![image12](../../../attachments/936755f051974c72b61a7129d0085e8a.png)

![image13](../../../attachments/a71c182f277e4f71ba4341a4fbed06ff.png)

# Creating Custom Packets 

Colasoft Packet Builder Source: <https://www.colasoft.com>

![image14](../../../attachments/cb48fa5dfbc3426f92db7946c32916cb.png)

There are three views in the Packet Builder: Packet List, Decode Editor, and Hex Editor. • Packet List displays all the constructed packets. When you select one or more packets in Packet List, the first highlighted packet is displayed in both Decode Editor and Hex Editor for editing.
• In Hex Editor, the data of the packet are represented as hexadecimal values and ASCII characters; nonprintable characters are represented by a dot (".") in the ASCII section. You can edit either the hexadecimal values or the ASCII characters.
• Decode Editor allows the attacker to edit packets without remembering the value length, byte order, and offsets. You can select a field and change the value in the edit box.

![image15](../../../attachments/41858344bb0847eda378dd0d0b8a1c12.png)

![image16](../../../attachments/31ecb8d414744bcfb0a2118bccb83869.png)

🧠 What Are Checksums?
A checksum is a small value that helps verify the integrity of data during transmission. It’s like a digital fingerprint for a packet.

Here’s how it works:

When a system sends a packet, it calculates a checksum based on the packet's contents (like a math summary).
The receiving system recalculates the checksum when it gets the packet.
If the checksums match, the packet is valid!
✅ Match: Packet is accepted.
❌ Mismatch: Packet is discarded (since it might be corrupted or tampered with).
In TCP/UDP, checksums help ensure that the data wasn’t corrupted during transmission.

🕵️ What Is "Sending Bad Checksums"?
Attackers sometimes intentionally send packets with invalid or incorrect checksums to see how a system responds.

🛡️ Properly configured firewalls/IDS: Drop the packet silently (no response).
🛑 Weakly configured systems or firewalls: Might still respond, leaking useful information!
🧩 Why Use Bad Checksums?
It’s a sneaky technique! Attackers can use it to:

Bypass Firewalls/IDS: Some firewalls only inspect packet headers but don’t validate checksums, accidentally leaking responses.
Fingerprint Firewalls: By analyzing whether a system responds or stays silent, attackers can guess if a firewall or IDS is present and how it’s configured.

![image17](../../../attachments/b43e7f3dc2004f1d9e2dfd8039f55fce.png)

# Proxy Servers 

A proxy server is an application that can serve as an intermediary for connecting with other computers.

How does a proxy server work?
Initially, when you use a proxy to request a particular web page on an actual server, the proxy server receives it. The proxy server then sends your request to the actual server on your behalf. It mediates between you and the actual server to transmit and respond to the request, as shown in the figure below.

![image18](../../../attachments/5b198f64e5c34440854b59f39d10d5b6.png)

When the attacker uses a proxy to connect to the target system, the server logs will record the proxy's source address rather than the attacker’s source address
![image19](../../../attachments/72eedf281d5942f29bc738fee08cef70.png)

