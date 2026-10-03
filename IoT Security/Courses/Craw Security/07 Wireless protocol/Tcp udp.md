## What does zoom use tcp or udp ?

Zoom uses both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) for its operations, depending on the type of data being transmitted and network conditions. Here's a breakdown:

When Zoom Uses TCP:
Control Signaling: For session establishment, signaling, and control commands, Zoom uses TCP to ensure reliable delivery.
Fallback Mechanism: If UDP is blocked (e.g., by firewalls or network policies), Zoom falls back to TCP for audio, video, and screen sharing, though this might result in higher latency.

When Zoom Uses UDP:
Real-time Media (Audio and Video): Zoom primarily uses UDP for audio and video data because it is faster and better suited for real-time communication. UDP allows data packets to be sent without waiting for acknowledgment, reducing latency.
Screen Sharing: For real-time screen sharing, Zoom may also prefer UDP for efficiency.

Preferred Protocol:
Zoom prefers UDP for its real-time communication features (like video and audio) to maintain low latency and smooth performance. However, it adapts to TCP if UDP is unavailable or unstable.

Protocol Adaptability:
Zoom uses an intelligent network optimization feature to automatically switch between protocols and data centers to maintain a stable and high-quality connection for users, even in challenging network environments.
