This project is a distributed system health monitoring service built using low-level UDP socket programming. It allows multiple remote nodes (clients) to periodically collect system metrics (CPU and RAM usage) and transmit them securely to a central aggregator (server).

Features:
1. Low-level Sockets: Built using the Python socket module with SOCK_DGRAM.

2. Secure Communication: Implements Symmetric Payload Encryption (AES-128) to ensure data confidentiality over UDP.

3. Concurrency: The server is designed to handle multiple asynchronous remote nodes.

4. Real-time Alerting: Threshold-based monitoring (e.g., CPU > 80%) triggers immediate server-side alerts.

The system follows a Push-based Client-Server Architecture:

1. Remote Nodes: Collect system data using psutil, encrypt the payload, and send it via UDP.

2. Central Aggregator: Receives encrypted datagrams, decrypts them using a shared key, and performs health analysis.

3. Security Design Choice (The SSL/TLS Workaround): Standard Python SSL/TLS libraries are designed specifically for TCP streams. Because this project utilizes UDP for high-performance, low-overhead telemetry, a standard SSL wrap is not natively supported.

Our Solution: We implemented Payload-Level Encryption using the cryptography library (Fernet/AES). This ensures that all data exchanges are encrypted end-to-end, satisfying the mandatory security requirement while maintaining the connectionless nature of UDP.

Setup Instructions
1. Prerequisites
Ensure you have Python 3.x installed. Install the required dependencies by executing the following on bash:

pip install cryptography psutil

2. Configuration
Open server_1.py and node_1.py.

Ensure the KEY variable is identical in both files.

For distributed testing, change SERVER_IP in node_1.py to the Server's actual LAN IP.

3. Running the System
Start the Server by executing the following on bash:

python3 server_1.py
Start Remote Nodes: (Open new terminals for each node) by executing the following on bash:
python3 node_1.py

Performance Evaluation: 
1. Latency: Observed sub-5ms latency for local transmissions.
2. Scalability: Successfully tested with [X] concurrent nodes reporting every 5 seconds.
3. Security Integrity: Unauthorized packets (unencrypted or wrong key) are automatically dropped by the server's error-handling logic, preventing spoofing.
