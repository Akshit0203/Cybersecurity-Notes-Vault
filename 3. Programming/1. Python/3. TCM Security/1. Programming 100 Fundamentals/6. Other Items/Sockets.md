In Python, sockets are a fundamental networking concept used for communication between computers over a network. Sockets enable programs to establish connections, send data, and receive data over various network protocols, such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

A **socket** is like a **virtual communication endpoint** that allows two programs (usually on different computers) to **send and receive data** over a network.

Socket programming in Python allows you to create client-server applications, networked applications, and perform various networking tasks. It provides a powerful and flexible way to communicate over networks using different protocols.

## Socket Creation:

To use sockets in Python, you need to import the `socket` module
You can create a socket object using the `socket.socket()` function, which takes two parameters: 

the address family (e.g., `socket.AF_INET` for IPv4)
the socket type (e.g., `socket.SOCK_STREAM` for TCP or `socket.SOCK_DGRAM` for UDP).

```
import socket

# Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

AF → Address Family
INET → Internet (IPv4)

| Keyword       | Meaning            |
| ------------- | ------------------ |
| `AF_INET`     | Use IPv4 addresses |
| `AF_INET6`    | Use IPv6 addresses |
| `SOCK_STREAM` | TCP connection     |
| `SOCK_DGRAM`  | UDP connection     |

Once you have a socket object, you can use various methods to establish connections, send data, and receive data. Here are some commonly used methods:

- `socket.connect(address)`: Establishes a connection to a remote address.
- `socket.bind(address)`: Binds the socket to a specific address and port.
- `socket.listen(backlog)`: Listens for incoming connections on a TCP socket.
- `socket.accept()`: Accepts an incoming connection and returns a new socket object for communication.
- `socket.send(data)`: Sends data over the socket.
- `socket.recv(buffer_size)`: Receives data from the socket.


Here's an example of a basic TCP server that listens for incoming connections:

```
import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 1234)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5) # 5 means it can queue 5 pending clients before rejecting new ones

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    # Receive and send data
    data = client_socket.recv(1024) # receive up to 1024 bytes
    client_socket.send(b"Received: " + data) # b"..." means bytes data format is required in networking

    # Close the client socket
    client_socket.close()
```


## Example 

create a python script:
```
#!/bin/python

import socket

HOST = '127.0.0.1' #local address
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock stream is a port #This creates a new socket object.
s.connect((HOST,PORT)) #It expects a tuple: (IP, port) → in this case (HOST, PORT)
s.send(b"Hello from Python!")
```

```
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 7777      
listening on [any] 7777 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 51366
Hello from Python!    
```



