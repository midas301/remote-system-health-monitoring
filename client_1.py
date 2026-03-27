import socket
import time
import psutil  
from cryptography.fernet import Fernet

KEY = b'6_W8V_vR9-9X8S5_S-9v8S5_S-9v8S5_S-9v8S5_S-0='
cipher = Fernet(KEY)

SERVER_IP, SERVER_PORT = "127.0.0.1", 5005
NODE_NAME = "Research-Lab-PC"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Node {NODE_NAME} starting secure telemetry...")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        message = f"{NODE_NAME},{cpu},{ram}"
        
        encrypted_msg = cipher.encrypt(message.encode())
        
        sock.sendto(encrypted_msg, (SERVER_IP, SERVER_PORT))
        print(f"Encrypted metrics sent to aggregator.")
        
        time.sleep(5)
except KeyboardInterrupt:
    print("Shutting down node.")
finally:
    sock.close()
